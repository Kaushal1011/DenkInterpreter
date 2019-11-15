#!/usr/bin/env python3

from token import *

from lexer import Lexer

from ast import *


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.curr_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type: str) -> None:
        if self.curr_token.type == token_type:
            self.curr_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self) -> Num:
        token = self.curr_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)

        if token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

    def term(self) -> BinOp:
        node = self.factor()

        while self.curr_token.type in (MUL, DIV):
            token = self.curr_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self) -> BinOp:
        node = self.term()

        while self.curr_token.type in (PLUS, MINUS):
            token = self.curr_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self) -> AST:
        return self.expr()


class NodeVisitor:
    def visit(self, node: BinOp):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, default=self.generic_visit)
        return visitor(node)

    def generic_visit(self, node: BinOp):
        raise Exception('No visit_{} method'.format(type(node).__name__))
