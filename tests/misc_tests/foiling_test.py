from math_core.Algebra import Algebra
from Obilisk import Obilisk

# obi_l = Obilisk("x^4+x^3+1")
# alg_l = Algebra(obi_l.eqn_string, obi_l.tokens, obi_l.tree, obi_l.vars[0], obi_l.exprs)
# obi_r = Obilisk("x+2")
# alg_r = Algebra(obi_r.eqn_string, obi_r.tokens, obi_r.tree, obi_r.vars[0], obi_r.exprs)
# alg_l.foiling(alg_l.tree, alg_r.tree)

obi = Obilisk("(x+2)^8")
alg = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
alg.compute_monomial_ops(alg.tree)
for i in alg.solution:
    print(i)

# obi = Obilisk("(x+2)^7")
# alg = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
# alg.compute_monomial_ops(alg.tree)
# for i in alg.solution:
#     print(i)

obi = Obilisk("((x-1)^8*(x+2)^6)-((x-1)^6*(x+2)^8)")
algebra = Algebra(stringify_node(obi.tree, obi.vars[0]), obi.tokens, obi.tree, obi.vars[0], obi.exprs)
#print(stringify_node(algebra.tree.left, algebra.var)+"-"+stringify_node(algebra.tree.right, algebra.var))
algebra.foil_monomials()
for i in algebra.solution:
    print(i)