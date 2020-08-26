import sys
import re

RESERVED = 'RESERVED'
ADDOP = 'ADDOP'
SUBOP = 'SUBOP'
MULOP = 'MULOP'
POWEROP = 'POWEROP'
CALCOP = 'CALCOP'
TRIGOP = 'TRIGOP'
RECIPTRIGOP = 'RECIPTRIGOP'
ATRIGOP = 'ATRIGOP'
ARECIPTRIGOP = 'ARECIPTRIGOP'
HYPTRIGOP = 'HYPTRIGOP'
RECIPHYPTRIGOP = 'RECIPHYPTRIGOP'
AHYPTRIGOP = 'AHYPTRIGOP'
ARECIPHYPTRIGOP = 'ARECIPHYPTRIGOP'
LOGOP = 'LOGOP'
LNOP = 'LNOP'
BRACKET = 'BRACKET'
MATRIX_BR = 'MATRIX_BR'
MATRIX_ENDR = 'MATRIX_ENDR'
COMMA = 'COMMA'
CONSTANT = 'CONSTANT'
NUMBER = 'NUMBER'
VARIABLE = 'VARIABLE'

token_exprs = [
    (r'of',                                         None),
    (r'[ ]+',                                       None),
    (r'=',                                          RESERVED),
    (r'\+',                                         ADDOP),
    (r'\*|/',                                       MULOP),
    (r'-',                                          SUBOP),
    (r'\(|\)',                                      BRACKET),
    (r'\[|\]',                                      MATRIX_BR),
    (r'\;',                                         MATRIX_ENDR),
    (r'\^|(sqrt|SQRT)',                             POWEROP),
    (r'\,',                                         COMMA),
    (r'#(PI|pi|[Ee])',                              CONSTANT),
    (r'derivative|integral',                        CALCOP),
    (r'abs|ABS',                                    RESERVED),
    (r'(sin|cos|tan)|(SIN|COS|TAN)',                TRIGOP),
    (r'(sec|csc|cot)|(SEC|CSC|COT)',                RECIPTRIGOP),
    (r'(asin|acos|atan)|(ASIN|ACOS|ATAN)',          ATRIGOP),
    (r'(asec|acsc|acot)|(ASEC|ACSC|ACOT)',          ARECIPTRIGOP),
    (r'(sinh|cosh|tanh)|(SINH|COSH|TANH)',          HYPTRIGOP),
    (r'(sech|csch|coth)|(SECH|CSCH|COTH)',          RECIPHYPTRIGOP),
    (r'(asinh|acosh|atanh)|(ASINH|ACOSH|ATANH)',    AHYPTRIGOP),
    (r'(asech|acsch|acoth)|(ASECH|ACSCH|ACOTH)',    ARECIPHYPTRIGOP),
    (r'log|LOG',                                    LOGOP),
    (r'ln|LN',                                      LNOP),
    (r'[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?',      NUMBER),
    (r'[a-zA-Z_]',                                  VARIABLE),
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