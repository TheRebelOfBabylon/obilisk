from BEMDAS_algo_v3 import bracketify, grouping, stringify
from bracketing_test import solving, isolate

#LHS_4 = ["(1","69","*","(2","(3","(4","x","-","1",")4","/","(4","x","+","2",")4",")3","^","8","-","(3","(4","x","-","1",")4","/","(4","x","+","2",")4",")3","^","6",")2",")1"]
#RHS_4 = ["(1","(2","x","-","1",")2","/","(2","x","+","2",")2",")1"]

def solve(LHS, RHS, var):

	ans_l, ans_r = isolate(LHS, RHS, var)
	#print(ans_l)
	#print(ans_r)

	l_string = stringify(ans_l)

	if any(isinstance(sub, list) for sub in ans_r) == True:

		ans=[]
		for i in ans_r:

			temp = i
			temp[1] = complex(temp[1])

			if temp[1].imag == 0:

				temp[1] = temp[1].real
				temp[1] = round(temp[1].real,6)

			else:

				temp[1] = round(temp[1].real,6)+round(temp[1].imag,6)*1j

			ans.append(temp[1])

		print("Final answer:")
		for i in ans:

			print(l_string+" = "+str(i))

	else:

		ans = complex(ans_r[1])

		if ans.imag == 0:

			ans = ans.real
			ans = round(ans.real,6)

		else:

			ans = round(ans.real,6)+round(ans.imag,6)*1j

		print("Final answer: "+l_string+" = "+str(ans))

	return True	

#I think rounding of complex number should happen at the end. Not getting same results as wolfram alpha atm. 
