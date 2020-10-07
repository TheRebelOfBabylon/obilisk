from Obilisk import Obilisk
from math_core.Calculus import Calculus, stringify_node

obi = Obilisk("derivative of x^2-2x+1+ln(x^2)+x*#e^(2x)+sqrt(x)+2^x")
obi.identify_type_of_eqn()
calc = Calculus(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs, obi.type)
calc.derive()
for i in calc.solution:
    print(i)