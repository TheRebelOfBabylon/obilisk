from Obilisk import Obilisk
from math_core.Algebra import Algebra, stringify_node, round_complex

obi = Obilisk("x^5-2x^4+3x^3-4x^2+5x-6=0")
alg = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
ans = alg.isolate()
for a in ans:
    print(round_complex(a))

obi = Obilisk("x^5+3x^3-4x^2+5x-6=0")
alg = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
ans = alg.isolate()
for a in ans:
    print(round_complex(a))

obi = Obilisk("69*(((x-1)^8/(x+2)^8)-((x-1)^6/(x+2)^6))=(x-1)/(x+3)")
alg = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
ans = alg.isolate()
for a in ans:
    print(round_complex(a))