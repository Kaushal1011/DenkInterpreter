###############################################################################
#  AST visualizer - generates a DOT file for Graphviz.                        #
#                                                                             #
#  To generate an image from the DOT file run $ dot -Tpng -o ast.png ast.dot  #
#                                                                             #
###############################################################################
import argparse
import textwrap

from lex import Lexer
from parse import Parser
from astvisitor import NodeVisitor


class ASTVisualizer(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser
        self.ncount = 1
        self.dot_header = [textwrap.dedent("""\
        digraph astgraph {
          node [shape=circle, fontsize=12, fontname="Courier", height=.1];
          ranksep=.3;
          edge [arrowsize=.5]

        """)]
        self.dot_body = []
        self.dot_footer = ['}']

    def visit_Program(self, node):
        s = '  node{} [label="Program"]\n'.format(self.ncount)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        self.visit(node.block)

        s = '  node{} -> node{}\n'.format(node._num, node.block._num)
        self.dot_body.append(s)

    def visit_Block(self, node):
        s = '  node{} [label="Block"]\n'.format(self.ncount)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

        for decl_node in node.declarations:
            s = '  node{} -> node{}\n'.format(node._num, decl_node._num)
            self.dot_body.append(s)

        s = '  node{} -> node{}\n'.format(
            node._num,
            node.compound_statement._num
        )
        self.dot_body.append(s)

    def visit_VarDecl(self, node):
        s = '  node{} [label="VarDecl"]\n'.format(self.ncount)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        self.visit(node.var_node)
        s = '  node{} -> node{}\n'.format(node._num, node.var_node._num)
        self.dot_body.append(s)

        self.visit(node.type_node)
        s = '  node{} -> node{}\n'.format(node._num, node.type_node._num)
        self.dot_body.append(s)



    def visit_ProcedureDecl(self, node):
        s = '  node{} [label="ProcDecl:{}"]\n'.format(
            self.ncount,
            node.procName
        )
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        for param_node in node.params:
            self.visit(param_node)
            s = '  node{} -> node{}\n'.format(node._num, param_node._num)
            self.dot_body.append(s)

        self.visit(node.blockNode)
        s = '  node{} -> node{}\n'.format(node._num, node.blockNode._num)
        self.dot_body.append(s)

    def visit_FunctionDecl(self, node):
        s = '  node{} [label="ProcDecl:{}"]\n'.format(
            self.ncount,
            node.funcName
        )
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        for param_node in node.params:
            self.visit(param_node)
            s = '  node{} -> node{}\n'.format(node._num, param_node._num)
            self.dot_body.append(s)

        self.visit(node.blockNode)
        s = '  node{} -> node{}\n'.format(node._num, node.blockNode._num)
        self.dot_body.append(s)

    def visit_Param(self, node):
        s = '  node{} [label="Param"]\n'.format(self.ncount)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        self.visit(node.var_node)
        s = '  node{} -> node{}\n'.format(node._num, node.var_node._num)
        self.dot_body.append(s)

        self.visit(node.type_node)
        s = '  node{} -> node{}\n'.format(node._num, node.type_node._num)
        self.dot_body.append(s)

    def visit_WritelnCall(self, node):
        s = '  node{} [label="write CAll:{}"]\n'.format(
            self.ncount,
            node.proc_name
        )
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        for param_node in node.actual_params:
            self.visit(param_node)
            s = '  node{} -> node{}\n'.format(node._num, param_node._num)
            self.dot_body.append(s)

    def visit_Type(self, node):
        s = '  node{} [label="{}"]\n'.format(self.ncount, node.token.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

    def visit_Readint(self, node):
        s = '  node{} [label="Read int , {}"]\n'.format(self.ncount, node.token.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

    def visit_Readfloat(self, node):
        s = '  node{} [label="Read float ,{}"]\n'.format(self.ncount, node.token.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

    def visit_Readstring(self, node):
        s = '  node{} [label="Read string ,{}"]\n'.format(self.ncount, node.token.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1


    def visit_Num(self, node):
        s = '  node{} [label="{}"]\n'.format(self.ncount, node.token.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

    def visit_MyBoolean(self, node):
        s = '  node{} [label="{}"]\n'.format(self.ncount, node)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

    def visit_String(self, node):
        s = '  node{} [label="{}"]\n'.format(self.ncount, node.token.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

    def visit_BinOp(self, node):
        s = '  node{} [label="{}"]\n'.format(self.ncount, node.op.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        self.visit(node.left)
        self.visit(node.right)

        for child_node in (node.left, node.right):
            s = '  node{} -> node{}\n'.format(node._num, child_node._num)
            self.dot_body.append(s)

    def visit_UnaryOp(self, node):
        s = '  node{} [label="unary {}"]\n'.format(self.ncount, node.op.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        self.visit(node.right)
        s = '  node{} -> node{}\n'.format(node._num, node.right._num)
        self.dot_body.append(s)

    def visit_Compound(self, node):
        s = '  node{} [label="Compound"]\n'.format(self.ncount)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        for child in node.children:
            self.visit(child)
            s = '  node{} -> node{}\n'.format(node._num, child._num)
            self.dot_body.append(s)

    def visit_Assign(self, node):
        s = '  node{} [label="{}"]\n'.format(self.ncount, node.op.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        self.visit(node.left)
        self.visit(node.right)

        for child_node in (node.left, node.right):
            s = '  node{} -> node{}\n'.format(node._num, child_node._num)
            self.dot_body.append(s)

    def visit_Var(self, node):
        s = '  node{} [label="{}"]\n'.format(self.ncount, node.value)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

    def visit_NoOp(self, node):
        s = '  node{} [label="NoOp"]\n'.format(self.ncount)
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

    def visit_Call(self, node):
        s = '  node{} [label="Call:{}"]\n'.format(
            self.ncount,
            node.name
        )
        self.dot_body.append(s)
        node._num = self.ncount
        self.ncount += 1

        for param_node in node.actualParams:
            self.visit(param_node)
            s = '  node{} -> node{}\n'.format(node._num, param_node._num)
            self.dot_body.append(s)

    def visit_Condition(self,node):
        s='node[label="Condition:{}"]\n'.format(node.condition)
        if self.visit(node.condition) == True:
            self.visit(node.then)
        else:
            if node.myElse:
                self.visit(node.myElse)
        self.ncount+=1
        self.dot_body.append(s)
        node._num=self.ncount

    def visit_Then(self,node):
        s='node[label="Then{}"]\n'.format(node)
        self.ncount+=1
        self.dot_body.append(s)
        node._num=self.ncount
        self.visit(node.child)
    def visit_MyElse(self,node):
        s='node[label="Else{}"]\n'.format(node)
        self.ncount+=1
        self.dot_body.append(s)
        node._num=self.ncount
        self.visit(node.child)
    def visit_MyDo(self,node):
        s='node[label="Do{}"]\n'.format(node)
        self.ncount+=1
        self.dot_body.append(s)
        node._num=self.ncount
        self.visit(node.child)

    def visit_While(self,node):
        s='node[label="While{}"]\n'.format(node)
        self.ncount+=1
        self.dot_body.append(s)
        node._num=self.ncount
        # self.visit(node.child)
        while(self.visit(node.condition) == True):
            try:
                if self.visit(node.myDo) == True:
                    break
            except Exception:
                raise Exception

    def visit_Continue(self,node):
        s='node[label="Conitnue{}"]\n'.format(node)
        self.ncount+=1
        self.dot_body.append(s)
        node._num=self.ncount
    def visit_Break(self,node):
        s='node[label="Break{}"]\n'.format(node)
        self.ncount+=1
        self.dot_body.append(s)
        node._num=self.ncount


    def gendot(self):
        tree = self.parser.parse()
        self.visit(tree)
        return ''.join(self.dot_header + self.dot_body + self.dot_footer)


def main():
    argparser = argparse.ArgumentParser(
        description='Generate an AST DOT file.'
    )
    argparser.add_argument(
        'fname',
        help='Pascal source file'
    )
    args = argparser.parse_args()
    fname = args.fname
    text = open(fname, 'r').read()

    lexer = Lexer(text)
    parser = Parser(lexer)
    viz = ASTVisualizer(parser)
    content = viz.gendot()
    print(content)


if __name__ == '__main__':
    main()
