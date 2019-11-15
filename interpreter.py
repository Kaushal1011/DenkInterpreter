#!/usr/bin/env python3

from ast import *
from parser import NodeVisitor, Parser
from token import *

from lexer import Lexer


class Interpreter(NodeVisitor):
    GLOBAL_SCOPE = {}

    def __init__(self, parser: Parser):
        self.parser = parser

    def visit_BinOp(self, node: BinOp) -> int:
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)

        if node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)

        if node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)

        if node.op.type == DIV:
            return self.visit(node.left) // self.visit(node.right)

    def visit_Num(self, node: Num) -> int:
        return node.value

    def visit_UnaryOp(self, node: UnaryOp) -> int:
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

    def interpret(self) -> str:
        tree = self.parser.parse()
        if tree is None:
            return ''

        return str(self.visit(tree))
