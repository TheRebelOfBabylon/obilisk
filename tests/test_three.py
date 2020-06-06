from math_core.solve_functions import *
from math_core.BEMDAS_algo_v3 import bracketify, stringify, grouping

a = input("Enter the LHS of an eqn: ")
b = input("Enter the RHS of an eqn: ")

a, a_var = bracketify(a)
a, a_deg = grouping(a)

b, b_var = bracketify(b)
b, b_deg = grouping(b)

a = Solve_Func(a, a_var[0])
b = Solve_Func(b, b_var[0])
a_div = a.identify_div()
print(a_div)

a = a.redundant_br()
print(a.eqn)

#b_div = a_div[:]

#print(a_div)
a = a.multiply_br(a_div)
#print(a.eqn, a_div)

#print(b_div)
b = b.multiply_br(a_div)
#print(b.eqn, a_div)

a = a.redundant_div(a_div)
print(a.eqn)

a = a.bracket_remover()
#print(a.eqn)

b = b.bracket_remover()
#print(b.eqn)

a_string = stringify(a.eqn)
b_string = stringify(b.eqn)

print("\n"+a_string+" = "+b_string)

a.eqn, b.eqn, a_deg = rearrange(a.eqn, b.eqn, a.var)

a_string = stringify(a.eqn)
b_string = stringify(b.eqn)

print("\n"+a_string+" = "+b_string, a_deg)

ans = solver(a.eqn, b.eqn, a_deg, a.var)

#print(ans) 

a_asymptotes = find_asymptotes(a_div, a.var)
#print(a_asymptotes)

new_ans=[]
for i in ans:

	i = complex(i)
	if round(i.imag, 5) == 0:

		temp = round(i.real, 6)
		new_ans.append(temp)

	else:

		temp = round(i.real, 6)+round(i.imag, 6)*1j
		new_ans.append(temp)

#print(new_ans)
for i in a_asymptotes:

	asy = complex(i)
	k=0
	while k != len(new_ans):

		if round(new_ans[k].real,1)+round(new_ans[k].imag,1)*1j == asy:

			del new_ans[k]
			k=-1

		k+=1

for i in new_ans:

	print(a.var+" = "+str(i))

	