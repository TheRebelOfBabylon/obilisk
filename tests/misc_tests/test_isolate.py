from Obilisk import Obilisk
from math_core.Algebra import Algebra, stringify_node

obi = Obilisk("x^5-2x^4+3x^3-4x^2+5x-6=0")
alg = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
ans = alg.isolate()
print(ans)