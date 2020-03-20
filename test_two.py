from test import solve
from BEMDAS_algo_v3 import bracketify, grouping, stringify

l = input("Please enter the LHS of an equation: ")
r = input("Please enter the RHS of an equation: ")
a, a_var = bracketify(l)
a, a_deg = grouping(a)

b, b_var = bracketify(r)
b, b_deg = grouping(b)

answer = solve(a, b, a_var)

#Bug found in case 69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)=x+3
#There are 6 repeating roots of -2, -1.999999, -1.999988, -1.99998+2.4E-5, etc.)
#-2 is an asymptote. Program must recognize -2 as an asymptote and remove it from answers

