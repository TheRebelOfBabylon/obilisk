from parser.ast import BinOpNode, NumberNode, VariableNode
from parser.lexer import Token, VARIABLE, EXP, NUMBER, MUL, EQUAL, PLUS, MINUS

PLUS_MINUS = PLUS+MINUS


def create_num_node(var: str) -> NumberNode:
    return NumberNode(Token((var, NUMBER)))


some_var = VariableNode(Token(("x", VARIABLE)))

a = BinOpNode(create_num_node('a'), Token(("*", MUL)), BinOpNode(some_var, Token(("^", EXP)), NumberNode(Token(("2", NUMBER)))))
b = BinOpNode(create_num_node('b'), Token(("*", MUL)), some_var)
c = create_num_node('c')
d = create_num_node('d')

quadratic_left_full = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("=", EQUAL)), d), 'quadratic_left_full')
quadratic_left_no_b = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("=", EQUAL)), d), 'quadratic_left_no_b')
quadratic_left_no_c = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("=", EQUAL)), d), 'quadratic_left_no_c')
quadratic_left_no_bc = (BinOpNode(a, Token(("=", EQUAL)), d), 'quadratic_left_no_bc')

quadratic_right_full = (BinOpNode(d, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c)), 'quadratic_right_full')
quadratic_right_no_b = (BinOpNode(d, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), c)), 'quadratic_right_no_b')
quadratic_right_no_c = (BinOpNode(d, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), b)), 'quadratic_right_no_c')
quadratic_right_no_bc = (BinOpNode(d, Token(("=", EQUAL)), a), 'quadratic_right_no_bc')
