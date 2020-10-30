from Obilisk import Obilisk
from math_core.Calculus import Calculus, stringify_node

obi = Obilisk("derivative of |x^2|-2x^4+1+ln(x^2)+x*#e^(2x)+-cos(x)+2^x")
obi.identify_type_of_eqn()
calc = Calculus(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs, obi.type)
calc.derive()
for i in calc.solution:
    print(i)

# TODO - Fix These

obi = Obilisk("derivative of 1/2*((2x)*asin(2x))+sqrt(1-4x^2))")
obi.identify_type_of_eqn()
calc = Calculus(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs, obi.type)
calc.derive()
for i in calc.solution:
    print(i)

obi = Obilisk("derivative of (x)*asin(2x)+1/2*sqrt(1-4x^2)")
obi.identify_type_of_eqn()
calc = Calculus(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs, obi.type)
calc.derive()
for i in calc.solution:
    print(i)

