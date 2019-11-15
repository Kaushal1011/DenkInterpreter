#!/usr/bin/env python3

from token import *

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

    def skip_whitespace(self) -> None:
        while self.curr_char is not None and self.curr_char.isspace():
            self.advance()

    def integer(self) -> int:
        result = ''
        while self.curr_char is not None and self.curr_char.isdigit():
            result += self.curr_char
            self.advance()

        return int(result)

    def get_next_token(self) -> Token:
        while self.curr_char is not None:
            if self.curr_char.isspace():
                self.skip_whitespace()
                continue

            if self.curr_char.isdigit():
                return Token(INTEGER, self.integer())

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
                return Token(DIV, '/')

            if self.curr_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.curr_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)
