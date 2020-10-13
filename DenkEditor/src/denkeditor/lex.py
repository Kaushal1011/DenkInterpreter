###############################################################################
#                                                                             #
#  Lexer                                                                      #
#                                                                             #
###############################################################################

from enum import Enum

from base import LexerError


class TokenType(Enum):
    PLUS = "+"
    MINUS = "-"
    MUL = "*"
    LPAREN = "("
    RPAREN = ")"
    SEMI = ";"
    DOT = "."
    COLON = ":"
    COMMA = ","
    FLOAT_DIV = "/"
    EQUALS = "="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    BWISEAND = "&"
    BWISEOR = "|"
    BWISEXOR = "^"
    BWISENOT = "~"
    BWISESHIFTLEFT = "<<"
    BWISESHIFTRIGHT = ">>"

    # block of reserved words
    PROGRAM = "PROGRAM"  # marks the beginning of the block
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    TRUE = "TRUE"
    FALSE = "FALSE"
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    FUNCTION = "FUNCTION"
    IF = "IF"
    THEN = "THEN"
    ELSE = "ELSE"
    WHILE = "WHILE"
    DO = "DO"
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"
    REAL = "REAL"
    INTEGER_DIV = "DIV"
    VAR = "VAR"
    PROCEDURE = "PROCEDURE"
    WRITELN = "WRITELN"
    READINT = "READINT"
    READFLOAT = "READFLOAT"
    READSTRING = "READSTRING"
    STRING = "STRING"
    BEGIN = "BEGIN"
    END = "END"  # marks the end of the block
    # misc
    ID = "ID"
    INTEGER_CONST = "INTEGER_CONST"
    REAL_CONST = "REAL_CONST"
    ASSIGN = ":="
    EOF = "EOF"
    NOT_EQUALS = "<>"
    GREATER_OR_EQUALS_THAN = ">="
    LESS_OR_EQUALS_THAN = "<="


class Token:
    def __init__(self, type, value, lineno=None, column=None):
        self.type = type
        self.value = value
        self.lineno = lineno
        self.column = column

    def __str__(self):
        return "Token({type}, {value}, position={lineno}:{column})".format(
            type=self.type,
            value=repr(self.value),
            lineno=self.lineno,
            column=self.column,
        )

    def __repr__(self):
        return self.__str__()


def _build_reserved_keywords():
    """Build a dictionary of reserved keywords.
    """
    # enumerations support iteration, in definition order
    tt_list = list(TokenType)
    start_index = tt_list.index(TokenType.PROGRAM)
    end_index = tt_list.index(TokenType.END)
    reserved_keywords = {
        token_type.value: token_type
        for token_type in tt_list[start_index : end_index + 1]
    }
    return reserved_keywords


RESERVED_KEYWORDS = _build_reserved_keywords()


class Lexer:
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]
        # token line number and column number
        self.lineno = 1
        self.column = 1

    def error(self):
        s = "Lexer error on '{lexeme}' line: {lineno} column: {column}".format(
            lexeme=self.current_char, lineno=self.lineno, column=self.column,
        )
        raise LexerError(message=s)

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        if self.current_char == "\n":
            self.lineno += 1
            self.column = 0

        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]
            self.column += 1

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char != "}":
            self.advance()
        self.advance()  # the closing curly brace

    def number(self):
        """Return a (multidigit) integer or float consumed from the input."""

        # Create a new token with current line and column number
        token = Token(type=None, value=None, lineno=self.lineno, column=self.column)

        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == ".":
            result += self.current_char
            self.advance()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()

            token.type = TokenType.REAL_CONST
            token.value = float(result)
        else:
            token.type = TokenType.INTEGER_CONST
            token.value = int(result)

        return token

    def integer(self):
        """Return a (multidigit) integer or float consumed from the input."""

        # Create a new token with current line and column number
        token = Token(type=None, value=None, lineno=self.lineno, column=self.column)

        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == ".":
            result += self.current_char
            self.advance()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()

            token.type = TokenType.REAL_CONST
            token.value = float(result)
        else:
            token.type = TokenType.INTEGER_CONST
            token.value = int(result)

        return token

    def _id(self):
        """Handle identifiers and reserved keywords"""
        # print("HI")
        # Create a new token with current line and column number
        token = Token(type=None, value=None, lineno=self.lineno, column=self.column)

        value = ""
        while self.current_char is not None and self.current_char.isalnum():
            value += self.current_char
            self.advance()

        token_type = RESERVED_KEYWORDS.get(value.upper())
        if token_type is None:
            token.type = TokenType.ID
            token.value = value
        else:
            # reserved keyword
            token.type = token_type
            token.value = value.upper()

        return token

    def string(self):
        """Handles String"""

        # Create a new token with current line and column number
        token = Token(type=None, value=None, lineno=self.lineno, column=self.column)

        value = ""
        # print(self.current_char!="\"")
        if self.current_char != "'":
            token = self._id()
            return token
        self.advance()

        while self.current_char != "'":

            # print(self.current_char)
            value += self.current_char
            if self.current_char == "'":
                break
            self.advance()

        # print (self.current_char)
        if self.current_char != "'":
            raise self.lexerError()

        self.advance()

        token.type = TokenType.STRING
        token.value = value

        return token

    def getProcessedString(self):
        return self.text[0 : self.pos]

    def latestWord(self):
        processedString = self.getProcessedString()
        latest10word = processedString[
            processedString.length - 20
            if len(processedString) >= 20
            else 0 : len(processedString)
        ]
        return latest10word

    def lexerError(self):
        return LexerError(
            None,
            None,
            "Lexer error on {} line : {} column : {}".format(
                self.current_char, self.lineno, self.column
            ),
        )

    def get_next_token(self):
        """

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == "{":
                self.advance()
                self.skip_comment()
                continue

            if self.current_char.isalpha():
                return self._id()

            if self.current_char == "'":
                return self.string()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == ":" and self.peek() == "=":
                token = Token(
                    type=TokenType.ASSIGN,
                    value=TokenType.ASSIGN.value,  # ':='
                    lineno=self.lineno,
                    column=self.column,
                )
                self.advance()
                self.advance()
                return token

            if self.current_char == ">" and self.peek() == "=":
                self.advance()
                self.advance()
                return Token(
                    TokenType.GREATER_OR_EQUALS_THAN,
                    TokenType.GREATER_OR_EQUALS_THAN,
                    self.lineno,
                    self.column,
                )

            if self.current_char == "<" and self.peek() == "=":
                self.advance()
                self.advance()
                return Token(
                    TokenType.LESS_OR_EQUALS_THAN,
                    TokenType.LESS_OR_EQUALS_THAN,
                    self.lineno,
                    self.column,
                )

            if self.current_char == "<" and self.peek() == ">":
                self.advance()
                self.advance()
                return Token(
                    TokenType.NOT_EQUALS, TokenType.NOT_EQUALS, self.lineno, self.column
                )
            if self.current_char == "<" and self.peek() == "<":
                self.advance()
                self.advance()
                return Token(
                    TokenType.BWISESHIFTLEFT,
                    TokenType.BWISESHIFTLEFT,
                    self.lineno,
                    self.column,
                )
            if self.current_char == ">" and self.peek() == ">":
                self.advance()
                self.advance()
                return Token(
                    TokenType.BWISESHIFTRIGHT,
                    TokenType.BWISESHIFTRIGHT,
                    self.lineno,
                    self.column,
                )

            try:

                token_type = TokenType(self.current_char)
            except ValueError:

                self.error()
            else:
                token = Token(
                    type=token_type,
                    value=token_type.value,
                    lineno=self.lineno,
                    column=self.column,
                )
                self.advance()
                return token

        return Token(type=TokenType.EOF, value=None)
