"""
Obilisk Token Class and Lexer code
"""

import re
from typing import Tuple

BINOP = 'BINOP'
UNIFUNC = 'UNIFUNC'
BINFUNC = 'BINFUNC'
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

token_exprs = [
    (r'of', None),
    (r'[\s]+', None),
    (r'=', EQUAL),
    (r'\+|-|\*|/|\^', BINOP),
    (r'\(', L_BRACKET),
    (r'\)', R_BRACKET),
    (r'\[', L_MATRIX_BR),
    (r'\]', R_MATRIX_BR),
    (r'\;', ENDL),
    (r'(sqrt|SQRT)', UNIFUNC),
    (r'\,', COMMA),
    (r'#[a-zA-Z_]', CONSTANT),
    (r'derivative|integral', UNIFUNC),
    (r'd/d[a-zA-Z_]', UNIFUNC),
    (r'abs|ABS', UNIFUNC),
    (r'(sin|cos|tan)|(SIN|COS|TAN)', UNIFUNC),
    (r'(sec|csc|cot)|(SEC|CSC|COT)', UNIFUNC),
    (r'(asin|acos|atan)|(ASIN|ACOS|ATAN)', UNIFUNC),
    (r'(asec|acsc|acot)|(ASEC|ACSC|ACOT)', UNIFUNC),
    (r'(sinh|cosh|tanh)|(SINH|COSH|TANH)', UNIFUNC),
    (r'(sech|csch|coth)|(SECH|CSCH|COTH)', UNIFUNC),
    (r'(asinh|acosh|atanh)|(ASINH|ACOSH|ATANH)', UNIFUNC),
    (r'(asech|acsch|acoth)|(ASECH|ACSCH|ACOTH)', UNIFUNC),
    (r'log|LOG', BINFUNC),
    (r'ln|LN', UNIFUNC),
    (r'[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?([\+\-][0-9]+(\.[0-9]*)?[ij])?', NUMBER),
    (r'(d?[a-zA-Z_](\')*){1,}?', VARIABLE),
]


class Token:
    def __init__(self, token: Tuple[str, str]):
        self.value = token[0]
        self.tag = token[1]

    def __repr__(self):
        return 'Token(%s, %s)' % (self.value, self.tag)


def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = Token((text, tag))
                    tokens.append(token)
                break
        if not match:
            raise SyntaxError('Illegal character: {}\n'.format(characters[pos]))
        else:
            pos = match.end(0)
    return tokens


def obilisk_lex(characters):
    return lex(characters, token_exprs)


def parse(eqn):
    tokens = obilisk_lex(eqn)
    print("\n", eqn)
    for tok in tokens:
        print(tok)
