from BEMDAS_algo_v3 import bracketify, foiling, grouping, stringify

eqn_one = "x^10+5.0x^8+10.0x^6+10.0x^4+5.0x^2+1.0"
eqn_two = "x^2+1"

eqn_one, var_one = bracketify(eqn_one)
eqn_two, var_two = bracketify(eqn_two)

ans = foiling(eqn_one, eqn_two, var_one[0])
ans.insert(0,"(1")
ans.append(")1")
ans = stringify(ans)
print(ans,"\n")


 