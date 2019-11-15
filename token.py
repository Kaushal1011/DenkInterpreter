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
    'ID',
    'ASSIGN',
    'BEGIN',
    'END',
    'SEMI',
    'DOT',
    'EOF',
    'Token',
    'RESERVED_KEYWORDS',
]

INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = '('
RPAREN = ')'
ID = 'ID'
ASSIGN = 'ASSIGN'
BEGIN = 'BEGIN'
END = 'END'
SEMI = 'SEMI'
DOT = 'DOT'
EOF = 'EOF'


class Token:
    def __init__(self, dtype: str, value: Union[str, int, None]):
        self.type = dtype
        self.value = value

    def __str__(self):
        return 'Token({},{})'.format(self.type, repr(self.value))

    def __repr__(self):
        return self.__str__()


RESERVED_KEYWORDS = {
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END')
}
