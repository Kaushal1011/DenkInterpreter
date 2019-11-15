#!/usr/bin/env python3

from token import *
from typing import Union

__all__ = ['Lexer']


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.curr_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self) -> None:
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.curr_char = None
        else:
            self.curr_char = self.text[self.pos]

    def peek(self) -> Union[str, None]:
        curr_pos = self.pos + 1
        if curr_pos > len(self.text) - 1:
            return None

        return self.text[curr_pos]

    def skip_whitespace(self) -> None:
        while self.curr_char is not None and self.curr_char.isspace():
            self.advance()

    def skip_comment(self) -> None:
        while self.curr_char != '}':
            self.advance()

        self.advance()

    def number(self) -> Token:
        result = ''
        while self.curr_char is not None and self.curr_char.isdigit():
            result += self.curr_char
            self.advance()

        if self.curr_char == '.':
            result += self.curr_char
            self.advance()

            while self.curr_char is not None and self.curr_char.isdigit():
                result += self.curr_char
                self.advance()

            return Token('REAL_CONST', float(result))

        return Token('INTEGER_CONST', int(result))

    def _id(self) -> Token:
        result = ''
        while self.curr_char is not None and self.curr_char.isalnum():
            result += self.curr_char
            self.advance()

        return RESERVED_KEYWORDS.get(result, Token(ID, result))

    def get_next_token(self) -> Token:
        while self.curr_char is not None:
            if self.curr_char.isspace():
                self.skip_whitespace()
                continue

            if self.curr_char == '{':
                self.advance()
                self.skip_comment()
                continue

            if self.curr_char.isalpha():
                return self._id()

            if self.curr_char.isdigit():
                return self.number()

            if self.curr_char == ':' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(ASSIGN, ':=')

            if self.curr_char == ';':
                self.advance()
                return Token(SEMI, ';')

            if self.curr_char == ':':
                self.advance()
                return Token(COLON, ':')

            if self.curr_char == ',':
                self.advance()
                return Token(COMMA, ',')

            if self.curr_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.curr_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.curr_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.curr_char == '/':
                self.advance()
                return Token(FLOAT_DIV, '/')

            if self.curr_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.curr_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            if self.curr_char == '.':
                self.advance()
                return Token(DOT, '.')

            self.error()

        return Token(EOF, None)
