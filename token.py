#!/usr/bin/env python3

from typing import Union

__all__ = [
    'INTEGER',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'LPAREN',
    'RPAREN',
    'EOF',
    'Token',
]

INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = '('
RPAREN = ')'
EOF = 'EOF'


class Token:
    def __init__(self, dtype: str, value: Union[str, int, None]):
        self.type = dtype
        self.value = value

    def __str__(self):
        return 'Token({},{})'.format(self.type, repr(self.value))

    def __repr__(self):
        return self.__str__()
