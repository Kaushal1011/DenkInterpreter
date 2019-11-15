#!/usr/bin/env python3

from ast import *
from parser import NodeVisitor, Parser
from token import *

from lexer import Lexer


class Interpreter(NodeVisitor):
    def __init__(self, parser: Parser):
        self.parser = parser

    def visit_BinOp(self, node: BinOp):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)

        if node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)

        if node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)

        if node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Num(self, node: Num):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)


def main() -> None:
    while True:
        try:
            text = input('>>> ')
        except EOFError:
            break

        if not text:
            continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
