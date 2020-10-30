from math_core.Algebra import Algebra, stringify_node
from Obilisk import Obilisk

obi = Obilisk("69*(((x-1)^8/(x+2)^8)-((x-1)^6/(x+2)^6))=(x-1)/(x+3)")
print(stringify_node(obi.tree, obi.vars[0]))