#!/usr/bin/env python3

from ast import *
from token import *
from typing import List, Union

from lexer import Lexer


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.curr_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type: str) -> None:
        if self.curr_token.type == token_type:
            self.curr_token = self.lexer.get_next_token()
        else:
            self.error()

    def empty(self) -> NoOp:
        return NoOp()

    def variable(self) -> Var:
        node = Var(self.curr_token)
        self.eat(ID)
        return node

    def assignment_statement(self) -> Assign:
        left = self.variable()
        token = self.curr_token
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def statement(self) -> Union[Compound, Assign, NoOp]:
        if self.curr_token.type == BEGIN:
            node = self.compound_statement()
        elif self.curr_token.type == ID:
            node = self.assignment_statement()
        else:
            node = self.empty()

        return node

    def statement_list(self) -> List[Union[Compound, Assign, NoOp]]:
        node = self.statement()
        results = [node]

        while self.curr_token.type == SEMI:
            self.eat(SEMI)
            results.append(self.statement())

        if self.curr_token.type == ID:
            self.error()

        return results

    def compound_statement(self) -> Compound:
        self.eat(BEGIN)
        nodes = self.statement_list()
        self.eat(END)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root

    def program(self) -> Compound:
        node = self.compound_statement()
        self.eat(DOT)
        return node

    def factor(self) -> Union[Num, UnaryOp]:
        token = self.curr_token
        if token.type == PLUS:
            self.eat(PLUS)
            return UnaryOp(token, self.factor())

        if token.type == MINUS:
            self.eat(MINUS)
            return UnaryOp(token, self.factor())

        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)

        if token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

        return self.variable()

    def term(self) -> BinOp:
        node = self.factor()

        while self.curr_token.type in (MUL, DIV):
            token = self.curr_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self) -> BinOp:
        node = self.term()

        while self.curr_token.type in (PLUS, MINUS):
            token = self.curr_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self) -> Compound:
        '''
        program : compound_statement DOT
        compound_statement : BEGIN statement_list END
        statement_list : statement
                       | statement SEMI statement_list
        statement : compound_statement
                  | assignment_statement
                  | empty
        assignment_statement : variable ASSIGN expr
        empty :
        expr: term ((PLUS | MINUS) term)*
        term: factor ((MUL | DIV) factor)*
        factor : PLUS factor
               | MINUS factor
               | INTEGER
               | LPAREN expr RPAREN
               | variable
        variable: ID
        '''

        node = self.program()
        if self.curr_token.type != EOF:
            self.error()

        return node


class NodeVisitor:
    def visit(self,
              node: Union[UnaryOp, BinOp, Compound, Assign, NoOp]) -> int:
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))
