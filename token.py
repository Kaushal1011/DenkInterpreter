#!/usr/bin/env python3

from typing import Dict, Union

__all__ = [
    'INTEGER',
    'REAL',
    'PLUS',
    'COMMA',
    'COLON',
    'MINUS',
    'VAR',
    'PROGRAM',
    'INTEGER_CONST',
    'REAL_CONST',
    'MUL',
    'INTEGER_DIV',
    'FLOAT_DIV',
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
REAL = 'REAL'
INTEGER_CONST = 'INTEGER_CONST'
REAL_CONST = 'REAL_CONST'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
INTEGER_DIV = 'INTEGER_DIV'
FLOAT_DIV = 'FLOAT_DIV'
LPAREN = '('
RPAREN = ')'
ID = 'ID'
ASSIGN = 'ASSIGN'
BEGIN = 'BEGIN'
END = 'END'
SEMI = 'SEMI'
DOT = 'DOT'
PROGRAM = 'PROGRAM'
VAR = 'VAR'
COLON = 'COLON'
COMMA = 'COMMA'
EOF = 'EOF'


class Token:
    def __init__(self, dtype: str, value: Union[str, int, None]):
        self.type = dtype
        self.value = value

    def __str__(self):
        return 'Token({},{})'.format(self.type, repr(self.value))

    def __repr__(self):
        return self.__str__()


RESERVED_KEYWORDS: Dict[str, Token] = {
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END'),
    'DIV': Token('INTEGER_DIV', 'DIV'),
    'INTEGER': Token('INTEGER', 'INTEGER'),
    'REAL': Token('REAL', 'REAL'),
    'PROGRAM': Token('PROGRAM', 'PROGRAM'),
    'VAR': Token('VAR', 'VAR')
}
