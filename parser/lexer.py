import sys
import re

OPERATOR = 'OPERATOR'
EQUAL = 'EQUAL'
BRACKET = 'BRACKET'
MATRIX_BR = 'MATRIX_BR'
ENDL = 'ENDL'
COMMA = 'COMMA'
CONSTANT = 'CONSTANT'
NUMBER = 'NUMBER'
VARIABLE = 'VARIABLE'

token_exprs = [
    (r'of',                                         None),
    (r'[\s]+',                                      None),
    (r'=',                                          EQUAL),
    (r'\+|-|\*|/',                                  OPERATOR),
    (r'\(|\)',                                      BRACKET),
    (r'\[|\]',                                      MATRIX_BR),
    (r'\;',                                         ENDL),
    (r'\^|(sqrt|SQRT)',                             OPERATOR),
    (r'\,',                                         COMMA),
    (r'#[a-zA-Z_]',                                 CONSTANT),
    (r'derivative|integral',                        OPERATOR),
    (r'd/d[a-zA-Z_]',                               OPERATOR),
    (r'abs|ABS',                                    OPERATOR),
    (r'(sin|cos|tan)|(SIN|COS|TAN)',                OPERATOR),
    (r'(sec|csc|cot)|(SEC|CSC|COT)',                OPERATOR),
    (r'(asin|acos|atan)|(ASIN|ACOS|ATAN)',          OPERATOR),
    (r'(asec|acsc|acot)|(ASEC|ACSC|ACOT)',          OPERATOR),
    (r'(sinh|cosh|tanh)|(SINH|COSH|TANH)',          OPERATOR),
    (r'(sech|csch|coth)|(SECH|CSCH|COTH)',          OPERATOR),
    (r'(asinh|acosh|atanh)|(ASINH|ACOSH|ATANH)',    OPERATOR),
    (r'(asech|acsch|acoth)|(ASECH|ACSCH|ACOTH)',    OPERATOR),
    (r'log|LOG',                                    OPERATOR),
    (r'ln|LN',                                      OPERATOR),
    (r'[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?([\+\-][0-9]+(\.[0-9]*)?[ij])?',      NUMBER),
    (r'(d?[a-zA-Z_](\')*){1,}?',                    VARIABLE),
]

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
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens


def imp_lex(characters):
    return lex(characters, token_exprs)

def parse(eqn):
    tokens = imp_lex(eqn)
    print("\n", eqn)
    for tok in tokens:
        print(tok)