#!/usr/bin/env python3

from parser import Parser

from interpreter import Interpreter
from lexer import Lexer


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
