"""
Obilisk Token Class and Lexer code
"""

import re
from typing import Tuple, List

PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
EXP = 'EXP'
FUNC = 'FUNC'
EQUAL = 'EQUAL'
L_BRACKET = 'L_BRACKET'
R_BRACKET = 'R_BRACKET'
L_MATRIX_BR = 'L_MATRIX_BR'
R_MATRIX_BR = 'R_MATRIX_BR'
ENDL = 'ENDL'
COMMA = 'COMMA'
CONSTANT = 'CONSTANT'
NUMBER = 'NUMBER'
VARIABLE = 'VARIABLE'
EOF = 'EOF'

token_exprs = [
    (r'of', None),
    (r'[\s]+', None),
    (r'=', EQUAL),
    (r'\+', PLUS),
    (r'-',  MINUS),
    (r'\*', MUL),
    (r'/', DIV),
    (r'\^', EXP),
    (r'\(', L_BRACKET),
    (r'\)', R_BRACKET),
    (r'\[', L_MATRIX_BR),
    (r'\]', R_MATRIX_BR),
    (r'\;', ENDL),
    (r'(sqrt|SQRT)', FUNC),
    (r'\,', COMMA),
    (r'\#(pi|PI|e|E)', CONSTANT),
    (r'derivative|integral', FUNC),
    (r'solve|isolate|roots', FUNC),
    (r'd/d[a-zA-Z_]', FUNC),
    (r'abs|ABS', FUNC),
    (r'(sin|cos|tan)|(SIN|COS|TAN)', FUNC),
    (r'(sec|csc|cot)|(SEC|CSC|COT)', FUNC),
    (r'(asin|acos|atan)|(ASIN|ACOS|ATAN)', FUNC),
    (r'(asec|acsc|acot)|(ASEC|ACSC|ACOT)', FUNC),
    (r'(sinh|cosh|tanh)|(SINH|COSH|TANH)', FUNC),
    (r'(sech|csch|coth)|(SECH|CSCH|COTH)', FUNC),
    (r'(asinh|acosh|atanh)|(ASINH|ACOSH|ATANH)', FUNC),
    (r'(asech|acsch|acoth)|(ASECH|ACSCH|ACOTH)', FUNC),
    (r'log|LOG', FUNC),
    (r'ln|LN', FUNC),
    (r'[0-9]+(\.[0-9]*)?[ij]', NUMBER),
    (r'[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?([\+\-][0-9]+(\.[0-9]*)?[ij])?', NUMBER),
    (r'(d?[a-zA-Z_](\')*){1,}?', VARIABLE),
]


class Token:
    def __init__(self, token: Tuple[str, str]):
        self.value = token[0]
        self.tag = token[1]

    def __repr__(self):
        return 'Token(%s, %s)' % (self.value, self.tag)

class Lexer():
    def __init__(self, eqn: str):
        self.eqn = eqn
        self.vars = []

    def lex(self, token_exprs):
        """Method takes an eqn in string format and returns a list of tokens"""
        pos = 0
        tokens = []
        while pos < len(self.eqn):
            match = None
            for token_expr in token_exprs:
                pattern, tag = token_expr
                regex = re.compile(pattern)
                match = regex.match(self.eqn, pos)
                if match:
                    text = match.group(0)
                    if tag:
                        token = Token((text, tag))
                        tokens.append(token)
                    break
            if not match:
                raise SyntaxError('Illegal character: {}\n'.format(self.eqn[pos]))
            else:
                pos = match.end(0)
        tokens.append(Token((None, EOF)))
        tokens = self.inference(tokens)
        self.check_for_vars(tokens)
        return tokens

    @staticmethod
    def inference(tokens: List[Token]) -> List[Token]:
        """Function adds MUL tokens between variables and numbers, constants, brackets or functions"""
        mul_token = Token(("*", MUL))
        one_token = Token(("1", NUMBER))
        l_brack_token = Token(("(", L_BRACKET))
        r_brack_token = Token((")", R_BRACKET))
        i = 0
        if tokens[0].tag == VARIABLE:
            tokens.insert(0, mul_token)
            tokens.insert(0, one_token)
        while i != len(tokens):
            if tokens[i-1].tag in (NUMBER, R_BRACKET, CONSTANT) and tokens[i].tag in (VARIABLE, CONSTANT, L_BRACKET, FUNC):
                tokens.insert(i, mul_token)
            elif tokens[i-1].tag in (PLUS, MINUS, EQUAL, DIV, EXP, L_BRACKET) and tokens[i].tag == VARIABLE:
                tokens.insert(i + 1, r_brack_token)
                tokens.insert(i, mul_token)
                tokens.insert(i, one_token)
                tokens.insert(i, l_brack_token)
            elif tokens[i-2].tag != NUMBER and tokens[i-1].tag == MUL and tokens[i].tag == VARIABLE:
                tokens.insert(i + 1, r_brack_token)
                tokens.insert(i, mul_token)
                tokens.insert(i, one_token)
                tokens.insert(i, l_brack_token)
            i += 1
        return tokens

    def obilisk_lex(self):
        return self.lex(token_exprs)

    def check_for_vars(self, tokens: List[Token]):
        """Function checks for variable tokens and stores the values in a list"""
        for token in tokens:
            if token.tag == VARIABLE:
                if token.value not in self.vars:
                    self.vars.append(token.value)


def parse(eqn):
    lexer = Lexer(eqn)
    tokens = lexer.obilisk_lex()
    print("\n", eqn)
    for tok in tokens:
        print(tok)
    print(lexer.vars)
    return tokens
