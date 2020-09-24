from parser.ast import BinOpNode, NumberNode, VariableNode
from parser.lexer import Token, VARIABLE, EXP, NUMBER, MUL, EQUAL, PLUS, MINUS

PLUS_MINUS = PLUS+MINUS


def create_num_node(var: str) -> NumberNode:
    return NumberNode(Token((var, NUMBER)))


some_var = VariableNode(Token(("x", VARIABLE)))

monomial_x = (BinOpNode(create_num_node('a'), Token(("*", MUL)), some_var), "monomial_x")
monomial_x_power = (BinOpNode(create_num_node('a'), Token(("*", MUL)), BinOpNode(some_var, Token(("^", EXP)), create_num_node('2'))), "monomial_x_power")

poly_regex = r'(\(?[-\+]?([0-9]+(\.[0-9]*)?)?[a-zA-Z_](\^[0-9]+)?(\)(\^[0-9]+)?)?){0,}(\(?[-\+]?[0-9]+(\.[0-9]*)?(\)(\^[0-9]+)?)?){0,}'

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

a = BinOpNode(create_num_node('a'), Token(("*", MUL)), BinOpNode(some_var, Token(("^", EXP)), NumberNode(Token(("3", NUMBER)))))
b = BinOpNode(create_num_node('b'), Token(("*", MUL)), BinOpNode(some_var, Token(("^", EXP)), NumberNode(Token(("2", NUMBER)))))
c = BinOpNode(create_num_node('c'), Token(("*", MUL)), some_var)
d = create_num_node('d')
e = create_num_node('e')

cubic_left_full = (BinOpNode(BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d), Token(("=", EQUAL)), e), 'cubic_left_full')
cubic_left_no_b = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d), Token(("=", EQUAL)), e), 'cubic_left_no_b')
cubic_left_no_c = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), d), Token(("=", EQUAL)), e), 'cubic_left_no_c')
cubic_left_no_d = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("=", EQUAL)), e), 'cubic_left_no_d')
cubic_left_no_bc = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), d), Token(("=", EQUAL)), e), 'cubic_left_no_bc')
cubic_left_no_bd = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("=", EQUAL)), e), 'cubic_left_no_bd')
cubic_left_no_cd = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("=", EQUAL)), e), 'cubic_left_no_cd')
cubic_left_no_bcd = (BinOpNode(a, Token(("=", EQUAL)), e), 'cubic_left_no_bcd')

cubic_right_full = (BinOpNode(e, Token(("=", EQUAL)), BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d)), 'cubic_right_full')
cubic_right_no_b = (BinOpNode(e, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d)), 'cubic_right_no_b')
cubic_right_no_c = (BinOpNode(e, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), d)), 'cubic_right_no_c')
cubic_right_no_d = (BinOpNode(e, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c)), 'cubic_right_no_d')
cubic_right_no_bc = (BinOpNode(e, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), d)), 'cubic_right_no_bc')
cubic_right_no_bd = (BinOpNode(e, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), c)), 'cubic_right_no_bd')
cubic_right_no_cd = (BinOpNode(e, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), b)), 'cubic_right_no_cd')
cubic_right_no_bcd = (BinOpNode(e, Token(("=", EQUAL)), a), 'cubic_right_no_bcd')

a = BinOpNode(create_num_node('a'), Token(("*", MUL)), BinOpNode(some_var, Token(("^", EXP)), NumberNode(Token(("4", NUMBER)))))
b = BinOpNode(create_num_node('b'), Token(("*", MUL)), BinOpNode(some_var, Token(("^", EXP)), NumberNode(Token(("3", NUMBER)))))
c = BinOpNode(create_num_node('c'), Token(("*", MUL)), BinOpNode(some_var, Token(("^", EXP)), NumberNode(Token(("2", NUMBER)))))
d = BinOpNode(create_num_node('d'), Token(("*", MUL)), some_var)
e = create_num_node('e')
f = create_num_node('f')

quartic_left_full = (BinOpNode(BinOpNode(BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d), Token(("+", PLUS_MINUS)), e), Token(("=", EQUAL)), f), 'quartic_left_full')
quartic_left_no_b = (BinOpNode(BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d), Token(("+", PLUS_MINUS)), e), Token(("=", EQUAL)), f), 'quartic_left_no_b')
quartic_left_no_c = (BinOpNode(BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), d), Token(("+", PLUS_MINUS)), e), Token(("=", EQUAL)), f), 'quartic_left_no_c')
quartic_left_no_d = (BinOpNode(BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), e), Token(("=", EQUAL)), f), 'quartic_left_no_d')
quartic_left_no_e = (BinOpNode(BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d), Token(("=", EQUAL)), f), 'quartic_left_no_e')
quartic_left_no_bc = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), d), Token(("+", PLUS_MINUS)), e), Token(("=", EQUAL)), f), 'quartic_left_no_bc')
quartic_left_no_bd = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), e), Token(("=", EQUAL)), f), 'quartic_left_no_bd')
quartic_left_no_be = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d), Token(("=", EQUAL)), f), 'quartic_left_no_be')
quartic_left_no_cd = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), e), Token(("=", EQUAL)), f), 'quartic_left_no_cd')
quartic_left_no_ce = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), d), Token(("=", EQUAL)), f), 'quartic_left_no_ce')
quartic_left_no_de = (BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("=", EQUAL)), f), 'quartic_left_no_de')
quartic_left_no_bcd = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), e), Token(("=", EQUAL)), f), 'quartic_left_no_bcd')
quartic_left_no_bce = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), d), Token(("=", EQUAL)), f), 'quartic_left_no_bce')
quartic_left_no_bde = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("=", EQUAL)), f), 'quartic_left_no_bde')
quartic_left_no_cde = (BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("=", EQUAL)), f), 'quartic_left_no_cde')
quartic_left_no_bcde = (BinOpNode(a, Token(("=", EQUAL)), f), 'quartic_left_no_bcde')

quartic_right_full = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d), Token(("+", PLUS_MINUS)), e)), 'quartic_right_full')
quartic_right_no_b = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d), Token(("+", PLUS_MINUS)), e)), 'quartic_right_no_b')
quartic_right_no_c = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), d), Token(("+", PLUS_MINUS)), e)), 'quartic_right_no_c')
quartic_right_no_d = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), e)), 'quartic_right_no_d')
quartic_right_no_e = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d)), 'quartic_right_no_e')
quartic_right_no_bc = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), d), Token(("+", PLUS_MINUS)), e)), 'quartic_right_no_bc')
quartic_right_no_bd = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), e)), 'quartic_right_no_bd')
quartic_right_no_be = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), c), Token(("+", PLUS_MINUS)), d)), 'quartic_right_no_be')
quartic_right_no_cd = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), e)), 'quartic_right_no_cd')
quartic_right_no_ce = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), d)), 'quartic_right_no_ce')
quartic_right_no_de = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c)), 'quartic_right_no_de')
quartic_right_no_bcd = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), e)), 'quartic_right_no_bcd')
quartic_right_no_bce = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), d)), 'quartic_right_no_bce')
quartic_right_no_bde = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), c)), 'quartic_right_no_bde')
quartic_right_no_cde = (BinOpNode(f, Token(("=", EQUAL)), BinOpNode(a, Token(("+", PLUS_MINUS)), b)), 'quartic_right_no_cde')
quartic_right_no_bcde = (BinOpNode(f, Token(("=", EQUAL)), a), 'quartic_right_no_bcde')
