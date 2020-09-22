from Obilisk import Obilisk
from math_core.Algebra import Algebra, stringify_node
from parser.lexer import Lexer
from parser.combinator import TreeBuilder

obi = Obilisk("69*(((x-1)^8/(x+2)^8)-((x-1)^6/(x+2)^6))=(x-1)/(x+3)")
algebra = Algebra(stringify_node(obi.tree, obi.vars[0]), obi.tokens, obi.tree, obi.vars[0], obi.exprs)
algebra.remove_redundant_br()
algebra.find_divisor(algebra.tree)
for i in algebra.divisors:
    print(stringify_node(i, algebra.var))
print("\n")
algebra.multiply_div()
algebra.compute_low_hanging_fruit()
for i in algebra.solution:
    print(i)
print(stringify_node(algebra.tree, algebra.var), "\n")

obi = Obilisk("(((3x-5)*((x-1)/(x+2)))/(x+3))^8-(((x-1)/(x+2))/(x+3))^6 = 3")
algebra = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
algebra.remove_redundant_br()
algebra.find_divisor(algebra.tree)
for i in algebra.divisors:
    print(stringify_node(i, algebra.var))
print("\n")
algebra.multiply_div()
algebra.compute_low_hanging_fruit()
for i in algebra.solution:
    print(i)
print(stringify_node(algebra.tree, algebra.var), "\n")
# print("Dis da list")
# for i in algebra.exprs:
#     print(stringify_node(i, algebra.var))
# print("\n")
#
# obi = Obilisk("69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)=(x-1)/(x+2)")
# algebra = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
# algebra.check_for_substitution()
# for i in algebra.solution:
#     print(i)