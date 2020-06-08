from tests.test import solve
from math_core.BEMDAS_algo_v3 import bracketify, grouping, stringify

l = input("Please enter the LHS of an equation: ")
r = input("Please enter the RHS of an equation: ")
a, a_var = bracketify(l)
#print(a)
a, a_deg = grouping(a)
#print(a)

b, b_var = bracketify(r)
b, b_deg = grouping(b)
print(b)

answer = solve(a, b, a_var)

#!!! RESOLVED
#Bug found in case 69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)=x+3
#There are 6 repeating roots of -2, -1.999999, -1.999988, -1.99998+2.4E-5, etc.)
#-2 is an asymptote. Program must recognize -2 as an asymptote and remove it from answers

#!!! RESOLVED
#New bug
#69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)=x/(x+3) (fixed, but answers are different from wolfram alpha

#!!! RESOLVED
#69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)^2=x/(x+3) 
# when we multiply over (x+3), it becomes (x+3)^0.5 which can't be foiled out. 
# the equation needs to remain 69*(x+3)*((x+2)^6*(x-1)^8-(x-1)^6*(x+2)^8)^2=x*(x+2)^16*(x+2)^12
# Changes to multiply_br are needed to prevent deleting brackets in the (1 layer if putting them into the next layer (i.e. "(2") means adding a power that is less than 1.
#*** It seems Jenkins-Traub cannot solve this problem. Might have to tweak some variables

#New Bug
#((3x-5)*((x-1)/(x+2))/(x+3))^8-(((x-1)/(x+2))/(x+3))^6 = 3
#Need to rewrite redundant_br: ((3x-5)*((x-1)/(x+2))/(x+3))^8 -> ((3x-5)*((x-1)/(x+2))^8/(x+3)^8) and (3x-5) is forgotten


