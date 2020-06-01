from BEMDAS_algo_v3 import bracketify, grouping
from bracketing_test import solving

#LHS_1 = "69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)"
#RHS_1 = "x+3"
#print(LHS_1+"="+RHS_1)
#LHS_1, var_type_l = bracketify(LHS_1)
#RHS_1, var_type_r = bracketify(RHS_1)

#print(LHS_1, RHS_1)

#LHS = "(x^2+1)^7"
#RHS = "0"
#LHS, var_type = bracketify(LHS)
#RHS, var_type_r = bracketify(RHS)
#LHS, LHS_deg = grouping(LHS)

#ans = solving(LHS, RHS, var_type[0], LHS_deg[0])

LHS = "69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)"
RHS = "((x-1)/(x+2))^4"
LHS, var_type = bracketify(LHS)
RHS, var_type_r = bracketify(RHS)
LHS, LHS_deg = grouping(LHS)

ans = solving(LHS, RHS, var_type[0], LHS_deg[0])

print(ans, len(ans))