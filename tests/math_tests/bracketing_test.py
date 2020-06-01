from BEMDAS_algo_v3 import is_number, stringify, grouping, combining, bracketify, is_even, foiling, oper_dict, bracket_add, calculate
import jenkins_traub
from algebra import Poly_Func
from solve_functions import *

#LHS_1 = ["(1","x","^","2","+","x","^","3","/","x",")1"]
#RHS_1 = ["(1","0",")1"]

# 69*(((x-1)/(x+2))^8 - ((x-1)/(x+2))^6) = x+3

#LHS_2 = ["(1","69","*","(2","(3","(4","x","-","1",")4","/","(4","x","+","2",")4",")3","^","8","-","(3","(4","x","-","1",")4","/","(4","x","+","2",")4",")3","^","6",")2",")1"]
#RHS_2 = ["(1","x","+","3",")1"]

#LHS_3 = ["(1","x","^","2","+","x","+","1",")1"]
#RHS_3 = ["(1","x","^","x",")1"]

# 69*(((x-1)/(x+2))^8 - ((x-1)/(x+2))^6) = (x-1)/(x+2)

oper_list = [

	"SIN",
	"COS",
	"TAN",
	"SEC",
	"CSC",
	"COT",
	"ASIN",
	"ACOS",
	"ATAN",
	"ASEC",
	"ACSC",
	"ACOT",
	"SINH",
	"COSH",
	"TANH",
	"SECH",
	"CSCH",
	"COTH",
	"ASINH",
	"ACOSH",
	"ATANH",
	"ASECH",
	"ACSCH",
	"ACOTH",
	"LN",
	"LOG",
	"SQRT"
]

anti_dict = {

	"SIN":"ASIN",
	"COS":"ACOS",
	"TAN":"ATAN",
	"SEC":"ASEC",
	"CSC":"ACSC",
	"COT":"ACOT",
	"ASIN":"SIN",
	"ACOS":"COS",
	"ATAN":"TAN",
	"ASEC":"SEC",
	"ACSC":"CSC",
	"ACOT":"COT",
	"SINH":"ASINH",
	"COSH":"ACOSH",
	"TANH":"ATANH",
	"SECH":"ASECH",
	"CSCH":"ACSCH",
	"COTH":"ACOTH",
	"ASINH":"SINH",
	"ACOSH":"COSH",
	"ATANH":"TANH",
	"ASECH":"SECH",
	"ACSCH":"CSCH",
	"ACOTH":"COTH",
	"LN":"e^",
	"e^":"LN",

}

var_dict = {

	"a":"b",
	"b":"c",
	"c":"d",
	"d":"e",
	"e":"f",
	"f":"g",
	"g":"h",
	"h":"i",
	"i":"j",
	"j":"k",
	"k":"l",
	"l":"m",
	"m":"n",
	"n":"o",
	"o":"p",
	"p":"q",
	"q":"r",
	"r":"s",
	"s":"t",
	"t":"u",
	"u":"v",
	"v":"w",
	"w":"x",
	"x":"y",
	"y":"z",
	"z":"a"

}

oper_dict_two = {
	
	0 : "SIN",
	1 : "COS",
	2 : "TAN",
	3 : "SEC",
	4 : "CSC",
	5 : "COT",
	6 : "ASIN",
	7 : "ACOS",
	8 : "ATAN",
	9 : "ASEC",
	10 : "ACSC",
	11 : "ACOT",
	12 : "SINH",
	13 : "COSH",
	14 : "TANH",
	15 : "SECH",
	16 : "CSCH",
	17 : "COTH",
	18 : "ASINH",
	19 : "ACOSH",
	20 : "ATANH",
	21 : "ASECH",
	22 : "ACSCH",
	23 : "ACOTH",
	24 : "LN",
	25 : "LOG",
	26 : "SQRT",
	27 : "^",
	28 : "*",
	29 : "/"

}

def bracketing(bracket, var_type, lvl, bracket_dict):

	global var_dict

	sub_br=[]
	s=1
	br=""
	b=lvl
	b_open=1
	b_close=0
	while s != len(bracket):

		if "(" in bracket[s]:

			sub_br.append(bracket[s])
			br="("
			b+=1
			b_open+=1
			t=s+1
			while bracket[t] != ")"+str(b):

				sub_br.append(bracket[t])
				t+=1

			sub_br.append(bracket[t])
			print("sub_br",sub_br, b)
			br = stringify(sub_br)

			del bracket[s+1:t+1]
			print("bracket",bracket,"bracket_dict",bracket_dict)
			if br in bracket_dict:

				bracket[s] = bracket_dict[br]
				b=lvl
				b_open=1
				s=0
				print("bracket is now:",bracket,"bracket_dict",bracket_dict)
				sub_br.clear()

			else:

				print("here we go, bracket-ception")
				new_br, bracket_dict = bracketing(sub_br, var_type, b, bracket_dict)
				print("new bracket",new_br,"bracket_dict",bracket_dict)

				if (len(new_br) == 3) and (is_number(new_br[1]) == True):

					bracket[s] = new_br[1]
					b=lvl
					b_open=1
					s=0
					sub_br.clear()

				else:

					new_br_string = stringify(new_br)

					if new_br_string in bracket_dict:

						bracket[s] = bracket_dict[new_br_string]
						b=lvl
						b_open=1
						s=0
						print("bracket is now:",bracket,"bracket_dict",bracket_dict)
						sub_br.clear()

					else:

						#set current index to equal a new variable, and store bracket in a dictionary where key is variable and value is contents of bracket.
						if len(bracket_dict) != 0:

							for var in bracket_dict.values():

								new_var = var_dict[var]

						else:

							new_var = var_dict[var_type[0]]

					
						print(new_br_string)
						bracket_dict[new_br_string] = new_var
						bracket[s] = new_var
						print("bracket after brackception:",bracket,"bracket_dict",bracket_dict)
						b=lvl
						b_open=1
						s=0
						sub_br.clear()

		s+=1

	print("made it through")
	for var in bracket_dict.values():
		
		if var not in var_type:

			var_type.append(var)

	bracket, br_deg = grouping(bracket)
	print("bracket after grouping",bracket)
	bracket = combining(bracket, var_type, br_deg[0])
	print("bracket after combining",bracket)
	
	return bracket, bracket_dict

def solving(l, r, var):

	print(l, r)

	l = Solve_Func(l, var)
	r = Solve_Func(r, var)
	
	l_div = l.identify_div()
	r_div = r.identify_div()

	print("What",l_div, r_div)

	#l_div = []
	if not l_div:

		#l_div = [] = r_div
		if not r_div:

			l = l.redundant_br()
			r = r.redundant_br()

			l = l.bracket_remover()
			r = r.bracket_remover()

			l.eqn, r.eqn, l_deg = rearrange(l.eqn, r.eqn, l.var)

			ans = solver(l.eqn, r.eqn, l_deg, l.var)

			asy = []

		#l_div = [] != r_div
		else:

			l = l.redundant_br()
			r = r.redundant_br()

			l = l.multiply_br(r_div)
			r = r.multiply_br(r_div)

			l = l.redundant_div(r_div)
			r = r.redundant_div(r_div)

			l = l.bracket_remover()
			r = r.bracket_remover()

			l.eqn, r.eqn, l_deg = rearrange(l.eqn, r.eqn, l.var)

			ans = solver(l.eqn, r.eqn, l_deg, l.var)

			asy = find_asymptotes(r_div, l.var)

	#l_div != []
	else:

		#l_div != [] = r_div
		if not r_div:

			l = l.redundant_br()
			r = r.redundant_br()

			l = l.multiply_br(l_div)
			r = r.multiply_br(l_div)

			l = l.redundant_div(l_div)
			r = r.redundant_div(l_div)

			print(l.eqn, r.eqn)

			l = l.bracket_remover()
			r = r.bracket_remover()

			l.eqn, r.eqn, l_deg = rearrange(l.eqn, r.eqn, l.var)

			ans = solver(l.eqn, r.eqn, l_deg, l.var)

			asy = find_asymptotes(l_div, l.var)

		#l_div != [] != r_div
		else:

			print("we should be here", l_div, r_div)

			l = l.redundant_br()
			r = r.redundant_br()

			l = l.multiply_br(l_div)
			r = r.multiply_br(l_div)

			l = l.redundant_div(l_div)
			r = r.redundant_div(l_div)

			l = l.multiply_br(r_div)
			r = r.multiply_br(r_div)

			l = l.redundant_div(r_div)
			r = r.redundant_div(r_div)


			print("AYO",stringify(l.eqn)+" = "+stringify(r.eqn))

			l = l.bracket_remover()
			r = r.bracket_remover()

			l.eqn, r.eqn, l_deg = rearrange(l.eqn, r.eqn, l.var)

			ans = solver(l.eqn, r.eqn, l_deg, l.var)

			l_asy = find_asymptotes(l_div, l.var)
			r_asy = find_asymptotes(r_div, l.var)

			asy = []
			for i in l_asy:

				if i not in asy:

					asy.append(i)

			for i in r_asy:

				if i not in asy:

					asy.append(i)

	new_ans=[]
	for i in ans:

		i = complex(i)
		if round(i.imag, 4) == 0:

			temp = round(i.real, 6)
			new_ans.append(temp)

		else:

			temp = round(i.real, 6)+round(i.imag, 6)*1j
			new_ans.append(temp)

	if asy:

		for i in asy:

			asy_temp = complex(i)
			k=0
			while k != len(new_ans):

				if round(new_ans[k].real,1)+round(new_ans[k].imag,1)*1j == asy_temp:

					del new_ans[k]
					k=-1

				k+=1

	return new_ans	 					

def isolate(l, r, var_type):

	bracket_dict={}

	global var_dict

	#as a first step, check if there’s a variable to the power of the variable. If so, end and return an error. Else continue
	b=0
	j=0
	s=0
	b_open=0
	b_close=0
	#LHS first
	for i in range(0,len(l)):

		print("l[i]",l[i])

		if "(" in l[i]:

			b+=1
			j=i
			b_open+=1

		if ")" in l[i]:

			b-=1
			b_close+=1

		if l[i] == "^":

			s = i

		if (l[i] == var_type[0]):

			#print("There's a variable")

			#is it x^x?
			print("Test 1: x^x?", l[i-1] == "^", l[i-2] == var_type[0])
			if (l[i-1] == "^") and (l[i-2] == var_type[0]):

				ans = "Cannot calculate x^x or any other variation"
				return ans, 0

			#is it x^(19+x) or something like that?
			print("Test 2: x^(...x)?", b_open != b_close, s < j, l[s-1] == var_type[0], "(" in l[s+1]) 
			if (b_open != b_close) and (s < j) and (l[s-1] == var_type[0]) and ("(" in l[s+1]): 

				k=i
				b_temp=0
				while k != s:

					if "(" in l[k]:

						b_temp-=1

					if ")" in l[k]:

						b_temp+=1

					k-=1

				if b_temp != 0:

					ans = "Cannot calculate x^x or any other variation"
					return ans, 0

			#is it (x^2-5x+6)^x or something like that?
			print("Test 3: (...x...)^x?", l[i-1] == "^", ")" in l[i-2]) 
			if (l[i-1] == "^") and (")" in l[i-2]):

				k=i-2
				while l[k] != "("+str(b+1):

					if l[k] == var_type[0]:
						
						ans = "Cannot calculate x^x or any other variation"
						return ans, 0

					k-=1 

			#is it (x^2-5x+6)^(19+x)
			print("Test 4: (...x...)^(...x...)?", b_open != b_close, s < j, ")" in l[s-1], "(" in l[s+1])
			if (b_open != b_close) and (s < j) and (")" in l[s-1]) and ("(" in l[s+1]) and (s != 0):

				k=i
				b_temp=0
				while k != s:

					if "(" in l[k]:

						b_temp-=1

					if ")" in l[k]:

						b_temp+=1

					k-=1

				if b_temp != 0:

					#we know the variable is in the exponent now is it also in the base
					k=s-1
					b_temp = l[k]
					b_temp = b_temp.replace(")","")
					while l[k] != "("+b_temp:

						if l[k] == var_type[0]:
						
							ans = "Cannot calculate x^x or any other variation"
							return ans, 0

						k-=1

	#RHS Next
	b=0
	j=0
	s=0
	b_open=0
	b_close=0
	for i in range(0,len(r)):

		print("r[i]",r[i])

		if "(" in r[i]:

			b+=1
			j=i
			b_open+=1

		if ")" in r[i]:

			b-=1
			b_close+=1

		if r[i] == "^":

			s = i

		if (r[i] == var_type[0]):

			#is it x^x?
			print("Test 1: x^x?", r[i-1] == "^", r[i-2] == var_type[0])
			if (r[i-1] == "^") and (r[i-2] == var_type[0]):

				ans = "Cannot calculate x^x or any other variation"
				return ans, 0

			#is it x^(19+x) or something like that? 
			print("Test 2: x^(...x)?", b_open != b_close, s < j, r[s-1] == var_type[0], "(" in r[s+1])
			if (b_open != b_close) and (s < j) and (r[s-1] == var_type[0]) and ("(" in r[s+1]): 

				k=i
				b_temp=0
				while k != s:

					if "(" in r[k]:

						b_temp-=1

					if ")" in r[k]:

						b_temp+=1

					k-=1

				if b_temp != 0:

					ans = "Cannot calculate x^x or any other variation"
					return ans, 0

			#is it (x^2-5x+6)^x or something like that?
			print("Test 3: (...x...)^x?", r[i-1] == "^", ")" in r[i-2]) 
			if (r[i-1] == "^") and (")" in r[i-2]):

				k=i-2
				while r[k] != "("+str(b+1):

					if r[k] == var_type[0]:
						
						ans = "Cannot calculate x^x or any other variation"
						return ans, 0

					k-=1 

			#is it (x^2-5x+6)^(19+x)
			print("Test 4: (...x...)^(...x...)?", b_open != b_close, s < j, ")" in r[s-1], "(" in r[s+1])
			if (b_open != b_close) and (s < j) and (")" in r[s-1]) and ("(" in r[s+1]) and (s != 0):

				k=i
				b_temp=0
				while k != s:

					if "(" in r[k]:

						b_temp-=1

					if ")" in r[k]:

						b_temp+=1

					k-=1

				if b_temp != 0:

					#we know the variable is in the exponent now is it also in the base
					k=s-1
					b_temp = r[k]
					b_temp = b_temp.replace(")","")
					while r[k] != "("+b_temp:

						if r[k] == var_type[0]:
						
							ans = "Cannot calculate x^x or any other variation"
							return ans, 0

						k-=1

	#make a copy of LHS and RHS. Store as global variables
	l_og = l[:]
	l_new, bracket_dict = bracketing(l, var_type, 1, bracket_dict)

	s=0
	while s == 0:

		br = stringify(l_new)
		length = len(br)
		if br in bracket_dict:

			del l_new[1:length+1]
			l_new.insert(1,bracket_dict[br])

		else:

			s = 1

	r_og = r[:]
	r_new, bracket_dict = bracketing(r, var_type, 1, bracket_dict)

	s=0
	while s == 0:

		br = stringify(r_new)
		length = len(br)
		if br in bracket_dict:

			del r_new[1:length+1]
			r_new.insert(1,bracket_dict[br])

		else:

			s = 1

	#Lets take note of the variables in l and r now
	work_var_l=[]
	work_var_r=[]
	for var in bracket_dict.values():

		for i in range(0,len(l_new)):

			if var in l_new[i]:

				work_var_l.append(var)

		for i in range(0,len(r_new)):

			if var in r_new[i]:

				work_var_r.append(var)

	for i in range(0,len(l_new)):

		if (var_type[0] in l_new[i]) and (var_type[0] not in work_var_l):

			work_var_l.append(var_type[0])

	for i in range(0,len(r_new)):

		if (var_type[0] in r_new[i]) and (var_type[0] not in work_var_r):

			work_var_r.append(var_type[0]) 

	print("YOOOOOOOOOOO", work_var_l, work_var_r, bracket_dict)

	if (len(work_var_l) == 1) and (len(work_var_r) == 1):

		if (work_var_l[0] == work_var_r[0]):

			work_var = work_var_l
			if work_var == var_type[0]:

				ans = solving(l_new, r_new, work_var[0])

			else:

				#solve and keep resubbing
				while work_var != var_type[0]:

					if any(isinstance(sub, list) for sub in r_new) == True:

						ans=[]
						for i in r_new:

							temp_string = stringify(i)
							temp, temp_var = bracketify(temp_string)
							temp, temp_deg = grouping(temp)

							ans_temp = solving(l_new, temp, work_var[0])
							ans.append(ans_temp)

					else:

						ans = solving(l_new, r_new, work_var[0])

					for i in ans:

						print(work_var[0]+" = "+str(i))

					for i in bracket_dict:

						if bracket_dict[i] == work_var[0]:

							print(work_var[0]+" = "+i)
							l_new_string = i

					#is the new resubstitution a single variable or does more resubbing need to be done?
					work_var_l=[]
					for var in bracket_dict.values():

						for i in range(0,len(l_new_string)):

							if var in l_new_string[i]:

								work_var_l.append(var)

					if len(work_var_l) > 1:

						while len(work_var_l) != 1:

							for i in work_var_l:

								for k in bracket_dict:

									if bracket_dict[k] == i:

										print(i+" = "+k)
										l_new_string = l_new_string.replace(i,k)

							work_var_l=[]
							for var in bracket_dict.values():

								for i in range(0,len(l_new_string)):

									if var in l_new_string[i]:

										work_var_l.append(var)

					r_new=[]
					for i in ans:

						print(l_new_string+" = "+str(i))
						temp, temp_var = bracketify(str(i))
						temp, temp_deg = grouping(temp)
						r_new.append(temp)

					l_new, work_var = bracketify(l_new_string)
					l_new, l_deg = grouping(l_new)

		else:

			#Now we should check if the variables are one character apart. Ex: z and a or a and b
			if (work_var_l[0] == var_dict[work_var_r[0]]):

				print(work_var_l[0], var_dict[work_var_r[0]])
				for x in bracket_dict:

					if bracket_dict[x] == work_var_l[0]:

						sub = x

				print("we here one", sub)
				br = stringify(l_new)
				br = br.replace(work_var_l[0],"("+sub+")")
				print(br)
				l_new, work_var = bracketify(br)
				l_new, l_deg = grouping(l_new)
				print(l_new)

				#solve and keep resubbing
				while (l_new[1] != var_type[0]) and (len(l_new) != 3):

					if any(isinstance(sub, list) for sub in r_new) == True:

						l_new_string = stringify(l_new)
						l_new, work_var = bracketify(l_new_string)
						l_new, work_deg = grouping(l_new)

						ans=[]
						for i in r_new:

							temp_string = stringify(i)
							temp, temp_var = bracketify(temp_string)
							temp, temp_deg = grouping(temp)

							ans_temp = solving(l_new, temp, work_var[0])
							ans.append(ans_temp)
						
					else:

						ans = solving(l_new, r_new, work_var[0])

					l_new_string = work_var[0]
					print("bottle caps", l_new_string, ans)
					r_new=[]

					if any(isinstance(sub, list) for sub in ans) == True:

						for i in ans:

							print(work_var[0]+" = "+str(i[0]))
							r_temp, r_var = bracketify(str(i[0]))
							r_temp, r_deg = grouping(r_temp)
							r_new.append(r_temp)

					else:

						for i in ans:

							print(work_var[0]+" = "+str(i))
							r_temp, r_var = bracketify(str(i))
							r_temp, r_deg = grouping(r_temp)
							r_new.append(r_temp)

					resub = False
					for i in bracket_dict:

						if bracket_dict[i] == work_var[0]:

							print(work_var[0]+" = "+i)
							l_new_string = i
							resub = True

					#Is there a resub?is the new resubstitution a single variable or does more resubbing need to be done?

					if resub == True:

						work_var_l=[]
						for var in bracket_dict.values():

							for i in range(0,len(l_new_string)):

								if var in l_new_string[i]:

									work_var_l.append(var)

						if len(work_var_l) > 1:

							while len(work_var_l) != 1:

								for i in work_var_l:

									for k in bracket_dict:

										if bracket_dict[k] == i:

											print(i+" = "+k)
											l_new_string = l_new_string.replace(i,"("+k+")")
											print(l_new_string)

								work_var_l=[]
								for var in bracket_dict.values():
									
									for i in range(0,len(l_new_string)):

										if var in l_new_string[i]:

											work_var_l.append(var)

								if not work_var_l:

									for i in range(0,len(l_new_string)):

										if (var_type[0] in l_new_string[i]) and (var_type[0] not in work_var_l):

											work_var_l.append(var_type[0])
					
						for i in ans:

							print(l_new_string+" = "+str(i))

					l_new, work_var = bracketify(l_new_string)
					l_new, l_deg = grouping(l_new)

			elif (work_var_r[0] == var_dict[work_var_l[0]]):

				for x in bracket_dict:

					if bracket_dict[x] == work_var_r[0]:

						sub = x

				print("we here one", sub)
				br = stringify(r_new)
				br = br.replace(work_var_r[0],"("+sub+")")
				print(br)
				#r_new = bracketify(br)
				#r_new, r_deg = grouping(r_new)
				#r_new = combining(r_new, work_var_r[0], r_deg[0])
				#print(r_new)
				#try:

					#solving l_new + r_new	

				#except:

					#foil, then solve

			else:
				
				ans = solving(l_og, r_og, var_type[0])

				l_new, l_var = bracketify(var_type[0])

				r_new=[]
				for i in ans:

					temp, temp_var = bracketify(str(i))
					temp, temp_deg = grouping(temp)
					r_new.append(temp)

	else:

		#print(l_og_string+" = "+r_og_string)
	 
		ans = solving(l_og, r_og, var_type[0])

		l_new, l_var = bracketify(var_type[0])

		r_new=[]
		for i in ans:

			temp, temp_var = bracketify(str(i))
			temp, temp_deg = grouping(temp)
			r_new.append(temp)

	print("Made it to the end","l", "r")

	return l_new,r_new

#print("LHS:", LHS_1)
#print("RHS:", RHS_1)
#ans_l, ans_r = isolate(LHS_1,RHS_1,["x"])
#print(ans_l,ans_r)

#print("LHS:", LHS_2)
#print("RHS:", RHS_2)
#ans_l, ans_r = isolate(LHS_2,RHS_2,["x"])
#print(ans_l,ans_r)

#print("LHS:", LHS_3)
#print("RHS:", RHS_3)
#ans_l, ans_r = isolate(LHS_3,RHS_3,["x"])
#print(ans_l, ans_r)

#print("LHS:", LHS_4)
#print("RHS:", RHS_4)
#ans_l, ans_r = isolate(LHS_4,RHS_4,["x"])
#ans_l, l_deg = grouping(ans_l)
#ans_r, r_deg = grouping(ans_r)

#if l_deg[0] >= r_deg[0]:

	#ans = solving(ans_l, ans_r, "a", l_deg[0])
	#print(ans)

#else:

	#ans = solving(ans_l, ans_r, "x", r_deg[0])
	#print(ans)


		


					








