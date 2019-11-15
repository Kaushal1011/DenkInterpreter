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

    def type_spec(self) -> Type:
        token = self.curr_token
        if self.curr_token.type == INTEGER:
            self.eat(INTEGER)
        else:
            self.eat(REAL)

        return Type(token)

    def variable_declaration(self) -> List[VarDecl]:
        var_nodes = [Var(self.curr_token)]
        self.eat(ID)

        while self.curr_token.type == COMMA:
            self.eat(COMMA)
            var_nodes.append(Var(self.curr_token))
            self.eat(ID)

        self.eat(COLON)

        type_node = self.type_spec()
        return [VarDecl(var_node, type_node) for var_node in var_nodes]

    def declarations(self) -> List[VarDecl]:
        decs: List[VarDecl] = []
        if self.curr_token.type == VAR:
            self.eat(VAR)
            while self.curr_token.type == ID:
                var_decl = self.variable_declaration()
                decs.extend(var_decl)
                self.eat(SEMI)

        return decs

    def block(self) -> Block:
        dec_nodes = self.declarations()
        comp_stmt_node = self.compound_statement()
        return Block(dec_nodes, comp_stmt_node)

    def program(self) -> Program:
        self.eat(PROGRAM)
        var_node = self.variable()
        prog_name = var_node.value
        self.eat(SEMI)
        block_node = self.block()
        program_node = Program(prog_name, block_node)
        self.eat(DOT)
        return program_node

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

        return results

    def compound_statement(self) -> Compound:
        self.eat(BEGIN)
        nodes = self.statement_list()
        self.eat(END)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root

    def factor(self) -> Union[Num, UnaryOp]:
        token = self.curr_token
        if token.type == PLUS:
            self.eat(PLUS)
            return UnaryOp(token, self.factor())

        if token.type == MINUS:
            self.eat(MINUS)
            return UnaryOp(token, self.factor())

        if token.type == INTEGER_CONST:
            self.eat(INTEGER_CONST)
            return Num(token)

        if token.type == REAL_CONST:
            self.eat(REAL_CONST)
            return Num(token)

        if token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

        return self.variable()

    def term(self) -> BinOp:
        node = self.factor()

        while self.curr_token.type in (MUL, INTEGER_DIV, FLOAT_DIV):
            token = self.curr_token
            self.eat(token.type)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self) -> BinOp:
        node = self.term()

        while self.curr_token.type in (PLUS, MINUS):
            token = self.curr_token
            self.eat(token.type)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self) -> Compound:
        '''
        program : PROGRAM variable SEMI block DOT
        block : declarations compound_statement
        declarations : VAR (variable_declaration SEMI)+
                     | empty
        variable_declaration : ID (COMMA ID)* COLON type_spec
        type_spec : INTEGER | REAL
        compound_statement : BEGIN statement_list END
        statement_list : statement
                       | statement SEMI statement_list
        statement : compound_statement
                  | assignment_statement
                  | empty
        assignment_statement : variable ASSIGN expr
        empty :
        expr : term ((PLUS | MINUS) term)*
        term : factor ((MUL | INTEGER_DIV | FLOAT_DIV) factor)*
        factor : PLUS factor
               | MINUS factor
               | INTEGER_CONST
               | REAL_CONST
               | LPAREN expr RPAREN
               | variable
        variable: ID
        '''

        node = self.program()
        if self.curr_token.type != EOF:
            self.error()

        return node
