from Obilisk import Obilisk
from math_core.Calculus import Calculus, stringify_node

obi = Obilisk("integral of 3x^2+4x+1/x-x+7+csc(2x)")
obi.identify_type_of_eqn()
calc = Calculus(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs, obi.type)
print(calc.tree)
calc.derive()
for i in calc.solution:
    print(i)