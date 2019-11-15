#!/usr/bin/env python3

from parser import Parser

from interpreter import Interpreter
from lexer import Lexer


def main() -> None:
    import sys
    with open(sys.argv[1]) as f:
        text = f.read()

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(interpreter.GLOBAL_SCOPE)


if __name__ == '__main__':
    main()
