#!/usr/bin/env python3

from token import Token

__all__ = [
    'AST',
    'BinOp',
    'Num',
    'UnaryOp',
    'Var',
    'Assign',
    'Compound',
    'NoOp',
]


class AST:
    pass


class Num(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value


class BinOp(AST):
    def __init__(self, left: Num, op: Token, right: Num):
        self.left = left
        self.token = self.op = op
        self.right = right


class UnaryOp(AST):
    def __init__(self, op: Token, expr: Num):
        self.token = self.op = op
        self.expr = expr


class Compound(AST):
    '''Represent 'BEGIN ... END' block'''
    def __init__(self):
        self.children = []


class Var(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value


class Assign(AST):
    def __init__(self, left: Var, op: Token, right: Token):
        self.left = left
        self.token = self.op = op
        self.right = right


class NoOp(AST):
    pass
