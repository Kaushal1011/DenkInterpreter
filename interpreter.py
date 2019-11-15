#!/usr/bin/env python3

from ast import *
from parser import NodeVisitor, Parser
from token import *

from lexer import Lexer


class Interpreter(NodeVisitor):
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

    def interpret(self) -> str:
        tree = self.parser.parse()
        if tree is None:
            return ''

        return str(self.visit(tree))


def main() -> None:
    while True:
        try:
            text = input('>>> ')
        except EOFError:
            print()
            break

        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        print(interpreter.interpret())


if __name__ == '__main__':
    main()
