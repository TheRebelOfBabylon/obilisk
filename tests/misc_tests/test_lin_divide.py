from Obilisk import Obilisk
from math_core.Algebra import Algebra

obi = Obilisk("x^3-2x^2+3x-4=0")
alg_num = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
obi2 = Obilisk("x-1")
alg2 = Algebra(obi2.eqn_string, obi2.tokens, obi2.tree, obi2.vars[0], obi2.exprs)
num = alg_num.get_coeff(alg_num.tree)
denom = alg2.get_coeff(alg2.tree)
print(f"num: {num}")
print(f"denom: {denom}")
alg_num.lin_divide(num, denom)

obi = Obilisk("x^3-6x^2+11x-6=0")
alg_num = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
obi2 = Obilisk("x^3-6x^2+11x-6")
alg2 = Algebra(obi2.eqn_string, obi2.tokens, obi2.tree, obi2.vars[0], obi2.exprs)
num = alg_num.get_coeff(alg_num.tree)
denom = alg2.get_coeff(alg2.tree)
print(f"num: {num}")
print(f"denom: {denom}")
alg_num.lin_divide(num, denom)

obi = Obilisk("x^3 - 5 x^2 + 12 x - 8=0")
alg_num = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
obi2 = Obilisk("x^2 - 4 x + 8")
alg2 = Algebra(obi2.eqn_string, obi2.tokens, obi2.tree, obi2.vars[0], obi2.exprs)
num = alg_num.get_coeff(alg_num.tree)
denom = alg2.get_coeff(alg2.tree)
print(f"num: {num}")
print(f"denom: {denom}")
alg_num.lin_divide(num, denom)

obi = Obilisk("x^3-6x^2+11x-6=0")
alg_num = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
der = alg_num.poly_coeff_derivative(alg_num.get_coeff(alg_num.tree))
print(f"derivative of {alg_num.eqn_string} is {der}")
value = 4
print(f"the value of the eqn at {value} is {alg_num.evaluate(alg_num.get_coeff(alg_num.tree), value)}")