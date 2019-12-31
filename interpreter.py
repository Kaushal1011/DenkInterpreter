

import argparse
import sys
from enum import Enum
from base import LexerError
from base import ParserError
from base import SemanticError
from base import Error
from base import ErrorCode
from lex import Lexer
from parse import Parser
from sts import SemanticAnalyzer
from lex import TokenType
from astvisitor import NodeVisitor
from base import _SHOULD_LOG_STACK
from base import _SHOULD_LOG_SCOPE
from parse import ProcedureDecl
from parse import FunctionDecl


###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################


class ARType(Enum):
    PROGRAM = 'PROGRAM'


class CallStack:
    def __init__(self):
        self._records = []

    def push(self, ar):
        arNow = self.peek()
        if arNow != None:
            ar.enclosingActivationRecord = arNow
            ar.nestingLevel = arNow.nestingLevel+1

        self._records.append(ar)

    def pop(self):
        return self._records.pop()

    def peek(self):
        if self._records != []:
            return self._records[-1]
        else:
            return None
        # return

    def __str__(self):
        s = '\n'.join(repr(ar) for ar in reversed(self._records))
        s = f'CALL STACK\n{s}\n'
        return s

    def __repr__(self):
        return self.__str__()


class ActivationRecord:
    def __init__(self, name, type, nesting_level=1, enclosingActivationRecord=None):
        self.name = name
        self.type = type
        self.nestingLevel = nesting_level
        self.members = {}
        self.enclosingActivationRecord = enclosingActivationRecord

    # def __setitem__(self, key, value):
    #     self.members[key] = value

    # def __getitem__(self, key):
    #     return self.members[key]

    # def get(self, key):
    #     return self.members.get(key)

    def declareItem(self, key):
        self.members[key] = None

    def setItem(self, key, value):
        if key in self.members.keys():
            self.members[key] = value
        elif self.enclosingActivationRecord != None:
            self.enclosingActivationRecord.setItem(key, value)
        else:
            raise RuntimeError(ErrorCode.ID_NOT_FOUND, None, "ID_NOT_FOUND")

    def getItem(self, key):
        if key in self.members.keys():
            return self.members[key]
        elif self.enclosingActivationRecord != None:
            return self.enclosingActivationRecord.getItem(key)
        else:
            raise RuntimeError(ErrorCode.ID_NOT_FOUND, None, "ID_NOT_FOUND")

    def hasItem(self, key):
        if key in self.members.keys():
            return True
        elif self.enclosingActivationRecord != None:
            return self.enclosingActivationRecord.hasItem(key)
        else:
            return False

    def setReturn(self, value):
        self.returnValue = value

    def __str__(self):
        lines = [
            '{level}: {type} {name}'.format(
                level=self.nestingLevel,
                type=self.type.value,
                name=self.name,
            )
        ]
        for name, val in self.members.items():
            lines.append(f'   {name:<20}: {val}')

        s = '\n'.join(lines)
        return s

    def __repr__(self):
        return self.__str__()


class BreakError(Error):
    name = "BreakError"

    def __init__(self, token=None):
        pass


class ContinueError(Error):
    name = "ContinueError"

    def __init__(self, token=None):
        pass


class Interpreter(NodeVisitor):
    def __init__(self):
        # self.tree = tree
        self.call_stack = CallStack()
        self.programActivationRecord = None

    def log(self, msg):
        if _SHOULD_LOG_STACK:
            print(msg)

    def visit_Program(self, node):
        program_name = node.name
        self.log(f'ENTER: PROGRAM {program_name}')

        ar = ActivationRecord(
            name=program_name,
            type=ARType.PROGRAM,
            nesting_level=1,
        )
        self.call_stack.push(ar)

        self.log(str(self.call_stack))

        self.visit(node.block)

        self.log(f'LEAVE: PROGRAM {program_name}')
        self.log(str(self.call_stack))

        self.call_stack.pop()

    def visit_Block(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    def visit_VarDecl(self, node):
        varName = node.var_node.value
        ar = self.call_stack.peek()
        ar.declareItem(varName)

    def visit_Type(self, node):
        # Do nothing

        pass

    def visit_BinOp(self, node):
        leftVal = self.visit(node.left)
        rightVal = self.visit(node.right)

        if node.op.type == TokenType.PLUS:
            return leftVal+rightVal
        elif node.op.type == TokenType.MINUS:
            return leftVal - rightVal
        elif node.op.type == TokenType.MUL:
            return leftVal * rightVal
        elif node.op.type == TokenType.INTEGER_DIV:
            return leftVal // rightVal
        elif node.op.type == TokenType.FLOAT_DIV:
            return float(leftVal) / float(rightVal)
        elif node.op.type == TokenType.BWISESHIFTLEFT:
            return leftVal << rightVal
        elif node.op.type == TokenType.BWISESHIFTRIGHT:
            return leftVal >> rightVal
        elif node.op.type == TokenType.BWISEOR:
            return leftVal | rightVal
        elif node.op.type == TokenType.BWISEAND:
            return leftVal & rightVal
        elif node.op.type == TokenType.BWISEXOR:
            return leftVal ^ rightVal
        elif node.op.type == TokenType.AND:
            return leftVal and rightVal
        elif node.op.type == TokenType.OR:
            return leftVal or rightVal
        elif node.op.type == TokenType.EQUALS:
            return leftVal == rightVal
        elif node.op.type == TokenType.NOT_EQUALS:
            return leftVal != rightVal
        elif node.op.type == TokenType.GREATER_THAN:
            return leftVal > rightVal
        elif node.op.type == TokenType.GREATER_OR_EQUALS_THAN:
            return leftVal >= rightVal
        elif node.op.type == TokenType.LESS_THAN:
            return leftVal < rightVal
        elif node.op.type == TokenType.LESS_OR_EQUALS_THAN:
            return leftVal <= rightVal
        else:
            raise self.runtimeError(
                ErrorCode.UNEXPECTED_TOKEN,
                node.token
            )

    def visit_Num(self, node):
        return node.value

    def visit_String(self, node):
        return node.value

    def visit_MyBoolean(self, node):
        return node.value

    def visit_UnaryOp(self, node):
        op = node.op.type
        if self.visit(node.right) == None:
            raise self.runtimeError(
                ErrorCode.ID_NOT_FOUND,
                node.token
            )
        if op == TokenType.PLUS:
            return +self.visit(node.right)
        elif op == TokenType.MINUS:
            return -self.visit(node.right)
        elif op == TokenType.NOT:
            return not self.visit(node.right)
        elif op == TokenType.BWISENOT:
            return ~self.visit(node.right)
        else:
            raise self.runtimeError(
                ErrorCode.UNEXPECTED_TOKEN,
                node.token
            )

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        var_value = self.visit(node.right)

        ar = self.call_stack.peek()
        if ar.type == TokenType.FUNCTION and var_name == ar.name:
            ar.setReturn(var_value)
        else:
            # print(var_name,var_value)
            ar.setItem(var_name, var_value)

    def visit_Var(self, node):
        varName = node.value
        ar = self.call_stack.peek()
        if ar.hasItem(varName):
            val = ar.getItem(varName)
            if val == None:
                raise self.runtimeError(
                    ErrorCode.VARIABLE_NOT_INITIALISER,
                    node.token
                )
            return val
        raise self.runtimeError(
            ErrorCode.ID_NOT_FOUND,
            node.token
        )

    def visit_NoOp(self, node):
        pass

    def visit_ProcedureDecl(self, node):
        procName = node.procName
        ar = self.call_stack.peek()
        ar.declareItem(procName)
        ar.setItem(procName, node)

    def visit_FunctionDecl(self, node):
        funcName = node.funcName
        ar = self.call_stack.peek()
        ar.declareItem(funcName)
        ar.setItem(funcName, node)

    def visit_ProcedureCall(self, node):
        pass

    def visit_WritelnCall(self, node):
        for param in node.actual_params:
            print(self.visit(param))

    def visit_Readint(self, node):
        return int(input())

    def visit_Readfloat(self, node):
        return float(input())

    def visit_Readstring(self, node):
        return str(input())

    def visit_Call(self, node):
        name = node.name
        ar = self.call_stack.peek()
        proc = ar.getItem(name)
        if isinstance(proc, ProcedureDecl):
            self.log('ENTER : PROCEDURE {}'.format(name))
            actualParamValues = []
            for actualParam in node.actualParams:
                actualParamValues.append(self.visit(actualParam))
            newAr = ActivationRecord(name, TokenType.PROCEDURE)
            self.call_stack.push(newAr)
            ar = self.call_stack.peek()
            for i in range(0, len(proc.params)):
                ar.declareItem(proc.params[i].var_node.value)
                ar.setItem(proc.params[i].var_node.value, actualParamValues[i])
            self.visit(proc.blockNode)
            self.log('{}'.format(self.call_stack))
            self.log('LEAVE: PROCEDURE {}'.format(name))
        elif isinstance(proc, FunctionDecl):
            self.log('ENTER: FUNCTION {}'.format(name))
            actualParamValues = []
            for actualParam in node.actualParams:
                actualParamValues.append(self.visit(actualParam))
            newAr = ActivationRecord(name, TokenType.FUNCTION)
            self.call_stack.push(newAr)
            ar = self.call_stack.peek()
            for i in range(0, len(proc.params)):
                ar.declareItem(proc.params[i].var_node.value)
                ar.setItem(proc.params[i].var_node.value, actualParamValues[i])
            self.visit(proc.blockNode)
            self.log('{}'.format(self.call_stack))
            self.call_stack.pop()
            self.log('LEAVE: FUNCTION {}'.format(name))
            if ar.returnValue == None:
                raise self.runtimeError(
                    ErrorCode.MISSING_RETURN,
                    proc.token
                )
            return ar.returnValue

    def visit_Condition(self, node):
        if self.visit(node.condition) == True:
            self.visit(node.then)
        else:
            if node.myElse:
                self.visit(node.myElse)

    def visit_Then(self, node):
        self.visit(node.child)

    def visit_MyElse(self, node):
        self.visit(node.child)

    def visit_While(self, node):
        while(self.visit(node.condition) == True):
            try:
                if self.visit(node.myDo) == True:
                    break
            except BreakError:
                break
            except ContinueError:
                continue
            except Exception:
                raise Exception

    def visit_MyDo(self, node):
        self.visit(node.child)

    def visit_Continue(self, node):
        raise ContinueError(node.token)

    def visit_Break(self, node):
        raise BreakError(node.token)

    def interpret(self, tree):
        self.visit(tree)
        if self.programActivationRecord:
            return self.programActivationRecord.members

    def runtimeError(self, errorCode, token):
        return RuntimeError(
            errorCode,
            token,
            '{} -> {}'.format(errorCode, token)
        )


def main():
    parser = argparse.ArgumentParser(
        description='SPI - Simple Pascal Interpreter'
    )
    parser.add_argument('inputfile', help='Pascal source file')
    parser.add_argument(
        '--scope',
        help='Print scope information',
        action='store_true',
    )
    parser.add_argument(
        '--stack',
        help='Print call stack',
        action='store_true',
    )
    args = parser.parse_args()

    global _SHOULD_LOG_SCOPE, _SHOULD_LOG_STACK
    _SHOULD_LOG_SCOPE, _SHOULD_LOG_STACK = args.scope, args.stack

    text = open(args.inputfile, 'r').read()
    # print(text)

    lexer = Lexer(text)

    try:
        parser = Parser(lexer)
        tree = parser.parse()
    except (LexerError, ParserError) as e:
        print(e.message)
        sys.exit(1)

    semantic_analyzer = SemanticAnalyzer(_SHOULD_LOG_SCOPE)
    try:
        semantic_analyzer.visit(tree)
    except SemanticError as e:
        print(e.message)
        sys.exit(1)

    interpreter = Interpreter()
    interpreter.interpret(tree)


if __name__ == '__main__':
    main()
