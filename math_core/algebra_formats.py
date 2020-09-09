from parser.ast import BinOpNode, FuncNode, NumberNode, VariableNode, ConstantNode, UniOpNode, NUMNode, CONSTNode
from parser.lexer import Token, VARIABLE, EXP, NUMBER, MUL, EQUAL, PLUS, MINUS

#TODO - Add support for certain terms to not exist at all

NUM_OR_CONST = NUMNode + CONSTNode #Some number can be a variable or a constant
PLUS_MINUS = PLUS+MINUS

some_number = NumberNode(Token(("1", NUMBER)), NUM_OR_CONST)
some_var = VariableNode(Token(("x", VARIABLE)))

a = BinOpNode(some_number, Token(("*", MUL)), BinOpNode(some_var, Token(("^", EXP)), NumberNode(Token(("2", NUMBER)), NUMNode)))
b = BinOpNode(some_number, Token(("*", MUL)), some_var)
c = some_number
d = some_number

quadratic = BinOpNode(BinOpNode(BinOpNode(a, Token(("+", PLUS_MINUS)), b), Token(("+", PLUS_MINUS)), c), Token(("=", EQUAL)), d)

