"""
Obilisk Token Class and Lexer code
"""

import re
from typing import Tuple

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
    (r'#[a-zA-Z_]', CONSTANT),
    (r'derivative|integral', FUNC),
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
    tokens.append(Token((None, EOF)))
    return tokens


def obilisk_lex(characters):
    return lex(characters, token_exprs)


def parse(eqn):
    tokens = obilisk_lex(eqn)
    print("\n", eqn)
    for tok in tokens:
        print(tok)
    return tokens
