from Obilisk import Obilisk
from math_core.Algebra import Algebra, stringify_node
from parser.lexer import Lexer
from parser.combinator import TreeBuilder

# obi = Obilisk("69*(((x-1)^8/(x+2)^8)-((x-1)^6/(x+2)^6))=(x-1)/(x+3)")
# algebra = Algebra(stringify_node(obi.tree, obi.vars[0]), obi.tokens, obi.tree, obi.vars[0], obi.exprs)
# algebra.remove_redundant_br()
# algebra.find_divisors()
# algebra.multiply_div()
# #print(stringify_node(algebra.tree, algebra.var), "\n")
# algebra.foil_monomials()
# for i in algebra.solution:
#     print(i)
# print(stringify_node(algebra.tree, algebra.var), "\n")
#
# print("\n", "Begin")
# obi = Obilisk("(((3x-5)*((x-1)/(x+2)))/(x+3))^8-(((x-1)/(x+2))/(x+3))^6 = 3")
# algebra = Algebra(stringify_node(obi.tree, obi.vars[0]), obi.tokens, obi.tree, obi.vars[0], obi.exprs)
# algebra.remove_redundant_br()
# algebra.find_divisors()
# algebra.multiply_div()
# #print(stringify_node(algebra.tree, algebra.var), "\n")
# algebra.foil_monomials()
# for i in algebra.solution:
#     print(i)
# print(stringify_node(algebra.tree, algebra.var), "\n")
#
# print("\n", "Begin")
# obi = Obilisk("69*(((x-1)^8/(x+2)^8)-((x-1)^6/(x+2)^6))^2=(x-1)")
# algebra = Algebra(stringify_node(obi.tree, obi.vars[0]), obi.tokens, obi.tree, obi.vars[0], obi.exprs)
# algebra.remove_redundant_br()
# algebra.find_divisors()
# algebra.multiply_div()
# #print(stringify_node(algebra.tree, algebra.var), "\n")
# algebra.foil_monomials()
# for i in algebra.solution:
#     print(i)
# print(stringify_node(algebra.tree, algebra.var), "\n")

print("\n", "Begin")
obi = Obilisk("x^5-8x^18+4=6x+x^5-8x^18-6x")
algebra = Algebra(stringify_node(obi.tree, obi.vars[0]), obi.tokens, obi.tree, obi.vars[0], obi.exprs)
algebra.remove_redundant_br()
algebra.find_divisors()
if algebra.divisors is not None:
    algebra.multiply_div()
#print(stringify_node(algebra.tree, algebra.var), "\n")
algebra.foil_monomials()
for i in algebra.solution:
    print(i)
print(stringify_node(algebra.tree, algebra.var), "\n")

# print("\n", "Begin")
# obi = Obilisk("(((3x-5)*((x-1)/(x+2)))/(x+3))^8-(((x-1)/(x+2))/(x+3))^6 = 3")
# algebra = Algebra(stringify_node(obi.tree, obi.vars[0]), obi.tokens, obi.tree, obi.vars[0], obi.exprs)
# algebra.remove_redundant_br()
# algebra.find_divisors()
# algebra.multiply_div()
# for i in algebra.solution:
#     print(i)
# print("\n")
# for i in algebra.divisors:
#     print(stringify_node(i, algebra.var))
# print("\n", stringify_node(algebra.tree, algebra.var))
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