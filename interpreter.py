#!/usr/bin/env python3

from ast import *
from parser import Parser
from token import *
from typing import Union

from lexer import Lexer


class NodeVisitor:
    def visit(self, node: Union[UnaryOp, BinOp, Compound, Assign, NoOp,
                                Program, Block, VarDecl, Type, Var]):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser: Parser):
        self.parser = parser
        self.GLOBAL_SCOPE = {}

    def visit_Program(self, node: Program):
        self.visit(node.block)

    def visit_Block(self, node: Block):
        for decls in node.declarations:
            self.visit(decls)
        self.visit(node.compound_statement)

    def visit_VarDecl(self, node: VarDecl):
        pass

    def visit_Type(self, node: Type):
        pass

    def visit_BinOp(self, node: BinOp):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)

        if node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)

        if node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)

        if node.op.type == INTEGER_DIV:
            return self.visit(node.left) // self.visit(node.right)

        if node.op.type == FLOAT_DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Num(self, node: Num):
        return node.value

    def visit_UnaryOp(self, node: UnaryOp):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)

        if op == MINUS:
            return -self.visit(node.expr)

    def visit_Compound(self, node: Compound):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node: Assign):
        var = node.left.value
        self.GLOBAL_SCOPE[var] = self.visit(node.right)

    def visit_Var(self, node: Token):
        var = node.value
        val = self.GLOBAL_SCOPE.get(var)
        if val is None:
            raise NameError(repr(var))

        return val

    def visit_NoOp(self, node: Token):
        # Do nothing on empty statements
        pass

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''

        return self.visit(tree)
