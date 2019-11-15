#!/usr/bin/env python3

from token import Token
from typing import List

__all__ = [
    'AST',
    'BinOp',
    'Num',
    'UnaryOp',
    'Var',
    'Assign',
    'Compound',
    'NoOp',
    'VarDecl',
    'Program',
    'Block',
    'Type',
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


class Type(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value


class VarDecl(AST):
    def __init__(self, var_node: Var, type_node: Type):
        self.var_node = var_node
        self.type_node = type_node


class Block(AST):
    def __init__(self, declarations: List[VarDecl], compound_stmt: Compound):
        self.declarations = declarations
        self.compound_statement = compound_stmt


class Program(AST):
    def __init__(self, name: str, block: Block):
        self.name = name
        self.block = block
