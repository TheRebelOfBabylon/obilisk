from BEMDAS_algo_v3 import is_number, stringify, grouping, combining, bracketify, is_even, foiling, oper_dict, bracket_add, calculate
import jenkins_traub
from algebra import Poly_Func

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

def solving(l_prime, r, var, highest_deg):

	l = l_prime[:]

	print("Beginning of solving: ", l, r, var, highest_deg)

	global oper_dict_two
	asymptote=[]

	ans=0
	#First we put equation in standard polynomial form
	#1. remove any brackets divided by brackets ()/()
	#2. remove any exponents on brackets
	#3. foil out any bracket multiplication ()*()
	#4. foil out any bracket's multiplied by constants c*()
	#5. Solve Bracket Addition or Subtraction.
	#6. Put in Standard form
	#7. Solve
 
	p=0
	p_open=0
	p_close=0

	#1. remove any brackets divided by brackets ()/()
	s=0
	div_check_l = 0
	while s != len(l):
	
		#print("we're looping infinitely in here",l,l_copy,r,r_copy,"\n",s, len(l))


		#What do we do if COS(()/())? or (()/())^7. Maybe it would be wise to make a marker that indicates a bracket is preceded by a special op like COS 
		if ("(" in l[s]) and (l[s-1] == "/") and (")" in l[s-2]) and (s != 0):

			div_check_l += 1
			print("s is currently "+str(s),l[s])
			br_string = "("
			k = s+1
			var_check = False
			while ")" not in l[k]:

				if var in l[k]:

					var_check = True

				br_string+=l[k]
				k+=1

			k+=1
			br_string+=")"
			
			exp_check = False
			if l[k] == "^":

				exp_check == True
				br_string+="^"+l[k+1]
				
			if var_check == True:

				temp, temp_var = bracketify(br_string)
				temp, temp_deg = grouping(temp)
				temp_string = stringify(temp)

				print("AN ASYMPTOTE HAS BEEN FOUND", temp_string)
				asy_temp = solving(temp, ["(1","0",")1"], temp_var[0], temp_deg[0])

				if not asymptote:

					asymptote.append(asy_temp)

				if asy_temp not in asymptote:
	
					asymptote.append(asy_temp)

				print("FOUND AN ASYMPTOTE: ", asymptote)

			k = 0
			b = 0
			while k != s:

				if "(" in l[k]:

					b+=1

				elif ")" in l[k]:

					b-=1

				k+=1
 
			x = 1
			c = b
			while k != len(l):

				if "(" in l[k]:

					b+=1

				elif ")" in l[k]:

					b-=1

				if (is_number(l[k]) == True) and (l[k-1] == "^") and (l[k-2] == ")"+str(c)):

					x*=float(l[k])
					c-=1

				elif (l[k-1] != "^") and (l[k-2] == ")"+str(c)):

					c-=1

				k+=1

			if (x > 1) and (exp_check == False):

				br_string = br_string+"^"+str(x)

			elif (x > 1) and (exp_check == True):

				x_temp = float(br_string[len(br_string)-1])
				x*=x_temp
				new_br_string = ""
				i=0
				while br_string[i] != "^":

					new_br_string+=br_string[i]

				new_br_string += "^"+str(x)
				br_string = new_br_string
				
			print("The divisor is: "+br_string)
			
			br, br_var = bracketify(br_string)
			br, br_deg = grouping(br)
			del br[0]
			del br[len(br)-1]

			print(br)

			k=1
			b=1
			while l[k] != ")1":

				if "(" in l[k]:

					b+=1

				elif ")" in l[k]:

					b-=1

				if ((is_number(l[k]) == True) or (var in l[k])) and (b == 1):

					#pass
					k+=1
					l.insert(k,"*")
					k+=1
					for i in range(len(br)-1,-1,-1):

						l.insert(k,br[i])

					#print(l, k)

					if k < s:

						s+=len(br)+1

					while l[k] != ")1":

						if "(" in l[k]:

							b+=1

						elif ")" in l[k]:

							b-=1

						if (l[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(l)-1:

						k-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				elif (l[k] == "(2"):

					l.insert(k,"*")
					for i in range(len(br)-1,-1,-1):

						l.insert(k,br[i])

					#print(l, k)

					if k < s:

						s+=len(br)+1

					#print("s is now "+str(s), l[s])
					k+=len(br)+1

					while l[k] != ")1":

						if "(" in l[k]:

							b+=1

						elif ")" in l[k]:

							b-=1

						if (l[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(l)-1:

						k-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				k+=1

			k=1
			b=1
			while r[k] != ")1":

				if "(" in r[k]:

					b+=1

				elif ")" in r[k]:

					b-=1

				if ((is_number(r[k]) == True) or (var in r[k])) and (b == 1):

					#pass
					k+=1
					r.insert(k,"*")
					k+=1
					for i in range(len(br)-1,-1,-1):

						r.insert(k,br[i])

					#print(r, k)

					while r[k] != ")1":

						if "(" in r[k]:

							b+=1

						elif ")" in r[k]:

							b-=1

						if (r[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(r)-1:

						k-=1

					#print("k = "+str(k), "len(r)-1 = "+str(len(r)-1))

				elif (r[k] == "(2"):

					r.insert(k,"*")
					for i in range(len(br)-1,-1,-1):

						r.insert(k,br[i])

					k+=len(br)+1
					#print(r, k)

					while r[k] != ")1":

						if "(" in r[k]:

							b+=1

						elif ")" in r[k]:

							b-=1

						if (r[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(r)-1:

						k-=1

					#print("k = "+str(k), "len(r)-1 = "+str(len(r)-1))

				k+=1

			print(l,r)

		elif ((is_number(l[s]) == True) or (var in l[s])) and (l[s-1] == "/") and (s != 0):

			#print("l[s] = /"+str(l[s]))
			div_check_l += 1
			br_string = l[s]

			if var in l[s]:

				temp=[]
				temp.append(l[s])
				temp.insert(0,"(1")
				temp.append(")1")
				temp_string = stringify(temp)
				temp, temp_var = bracketify(temp_string)
				temp, temp_deg = grouping(temp)

				print("AN ASYMPTOTE HAS BEEN FOUND", temp_string)
				asy_temp = solving(temp, ["(1","0",")1"], temp_var[0], temp_deg[0])
				if not asymptote:

					asymptote.append(asy_temp)

				if asy_temp not in asymptote:
	
					asymptote.append(asy_temp)

				print("FOUND AN ASYMPTOTE: ", asymptote)

			k = 0
			b = 0
			b_open = 0
			b_close = 0
			while k != s:

				if "(" in l[k]:

					b_open+=1
					b+=1

				elif ")" in l[k]:

					b_close+=1
					b-=1

				k+=1
 
			x = 1
			c = b
			while k != len(l):

				if "(" in l[k]:

					b_open+=1
					b+=1

				elif ")" in l[k]:

					b_close+=1
					b-=1

				if (is_number(l[k]) == True) and (l[k-1] == "^") and (l[k-2] == ")"+str(c)):

					x*=float(l[k])
					c-=1

				elif (l[k-1] != "^") and (l[k-2] == ")"+str(c)):

					c-=1

				k+=1

			if x > 1:

				br_string = "("+br_string+")^"+str(x)
				
			#print("The divisor is: "+br_string)
			
			br, br_var = bracketify(br_string)
			br, br_deg = grouping(br)
			del br[0]
			del br[len(br)-1]

			#print(br)

			k=1
			b=1
			while l[k] != ")1":

				if "(" in l[k]:

					b+=1

				elif ")" in l[k]:

					b-=1

				if ((is_number(l[k]) == True) or (var in l[k])) and (b == 1):

					#pass
					k+=1
					l.insert(k,"*")
					k+=1
					for i in range(len(br)-1,-1,-1):

						l.insert(k,br[i])

					#print(l, k)

					if k < s:

						s+=len(br)+1

					while l[k] != ")1":

						if "(" in l[k]:

							b+=1

						elif ")" in l[k]:

							b-=1

						if (l[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(l)-1:

						k-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				elif (l[k] == "(2"):

					l.insert(k,"*")
					for i in range(len(br)-1,-1,-1):

						l.insert(k,br[i])
					
					#print(l, k)

					if k < s:

						s+=len(br)+1

					k+=len(br)+1

					while l[k] != ")1":

						if "(" in l[k]:

							b+=1

						elif ")" in l[k]:

							b-=1

						if (l[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(l)-1:

						k-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				k+=1

			k=1
			b=1
			while r[k] != ")1":

				if "(" in r[k]:

					b+=1

				elif ")" in r[k]:

					b-=1

				if ((is_number(r[k]) == True) or (var in r[k])) and (b == 1):

					#pass
					k+=1
					r.insert(k,"*")
					k+=1
					for i in range(len(br)-1,-1,-1):

						r.insert(k,br[i])

					#print(r, k)

					while r[k] != ")1":

						if "(" in r[k]:

							b+=1

						elif ")" in r[k]:

							b-=1

						if (r[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(r)-1:

						k-=1

					#print("k = "+str(k), "len(r)-1 = "+str(len(r)-1))

				elif (r[k] == "(2"):

					r.insert(k,"*")
					for i in range(len(br)-1,-1,-1):

						r.insert(k,br[i])

					k+=len(br)+1
					#print(r, k)

					while r[k] != ")1":

						if "(" in r[k]:

							b+=1

						elif ")" in r[k]:

							b-=1

						if (r[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(r)-1:

						k-=1

					#print("k = "+str(k), "len(r)-1 = "+str(len(r)-1))

				k+=1

			print(l,r)
			
		s+=1

	print("AHHHHHHHHHHHHHHH")
	
	l_string = stringify(l)
	r_string = stringify(r)
	print(l_string+"="+r_string)

	s=0
	div_check_r = 0
	while s != len(r):
	
		#print("we're looping infinitely in here",l,l_copy,r,r_copy,"\n",s, len(r))

		#What do we do if COS(()/())? or (()/())^7. Maybe it would be wise to make a marker that indicates a bracket is preceded by a special op like COS 
		if ("(" in r[s]) and (r[s-1] == "/") and (")" in r[s-2]) and (s != 0):

			div_check_r += 1
			#print("s is currently "+str(s),r[s])
			br_string = "("
			k = s+1
			var_check = False
			while ")" not in r[k]:

				if var in r[k]:

					var_check = True

				br_string+=r[k]
				k+=1

			k+=1
			br_string+=")"
			
			exp_check = False
			if r[k] == "^":

				exp_check == True
				br_string+="^"+r[k+1]
				
			if var_check == True:

				temp, temp_var = bracketify(br_string)
				temp, temp_deg = grouping(temp)
				temp_string = stringify(temp)

				print("AN ASYMPTOTE HAS BEEN FOUND", temp_string)
				asy_temp = solving(temp, ["(1","0",")1"], temp_var[0], temp_deg[0])

				if not asymptote:

					asymptote.append(asy_temp)

				if asy_temp not in asymptote:
	
					asymptote.append(asy_temp)

				print("FOUND AN ASYMPTOTE: ", asymptote)

			k = 0
			b = 0
			while k != s:

				if "(" in r[k]:

					b+=1

				elif ")" in r[k]:

					b-=1

				k+=1
 
			x = 1
			c = b
			while k != len(r):

				if "(" in r[k]:

					b+=1

				elif ")" in r[k]:

					b-=1

				if (is_number(r[k]) == True) and (r[k-1] == "^") and (r[k-2] == ")"+str(c)):

					x*=float(r[k])
					c-=1

				elif (r[k-1] != "^") and (r[k-2] == ")"+str(c)):

					c-=1

				k+=1

			if (x > 1) and (exp_check == False):

				br_string = br_string+"^"+str(x)

			elif (x > 1) and (exp_check == True):

				x_temp = float(br_string[len(br_string)-1])
				x*=x_temp
				new_br_string = ""
				i=0
				while br_string[i] != "^":

					new_br_string+=br_string[i]

				new_br_string += "^"+str(x)
				br_string = new_br_string
				
			#print("The divisor is: "+br_string)
			
			br, br_var = bracketify(br_string)
			br, br_deg = grouping(br)
			del br[0]
			del br[len(br)-1]

			print(br)

			k=1
			b=1
			while r[k] != ")1":

				if "(" in r[k]:

					b+=1

				elif ")" in r[k]:

					b-=1

				if ((is_number(r[k]) == True) or (var in r[k])) and (b == 1):

					#pass
					k+=1
					r.insert(k,"*")
					k+=1
					for i in range(len(br)-1,-1,-1):

						r.insert(k,br[i])

					#print(r, k)

					if k < s:

						s+=len(br)+1

					while r[k] != ")1":

						if "(" in r[k]:

							b+=1

						elif ")" in r[k]:

							b-=1

						if (r[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(r)-1:

						k-=1

					#print("k = "+str(k), "len(r)-1 = "+str(len(r)-1))

				elif (r[k] == "(2"):

					r.insert(k,"*")
					for i in range(len(br)-1,-1,-1):

						r.insert(k,br[i])

					#print(r, k)

					if k < s:

						s+=len(br)+1

					#print("s is now "+str(s), r[s])
					k+=len(br)+1

					while r[k] != ")1":

						if "(" in r[k]:

							b+=1

						elif ")" in r[k]:

							b-=1

						if (r[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(r)-1:

						k-=1

					#print("k = "+str(k), "len(r)-1 = "+str(len(r)-1))

				k+=1

			k=1
			b=1
			while l[k] != ")1":

				if "(" in l[k]:

					b+=1

				elif ")" in l[k]:

					b-=1

				if ((is_number(l[k]) == True) or (var in l[k])) and (b == 1):

					#pass
					k+=1
					l.insert(k,"*")
					k+=1
					for i in range(len(br)-1,-1,-1):

						l.insert(k,br[i])

					#print(l, k)

					while l[k] != ")1":

						if "(" in l[k]:

							b+=1

						elif ")" in l[k]:

							b-=1

						if (l[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(l)-1:

						k-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				elif (l[k] == "(2"):

					l.insert(k,"*")
					for i in range(len(br)-1,-1,-1):

						l.insert(k,br[i])

					k+=len(br)+1
					#print(l, k)

					while l[k] != ")1":

						if "(" in l[k]:

							b+=1

						elif ")" in l[k]:

							b-=1

						if (l[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(l)-1:

						k-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				k+=1

			print(l,r)

		elif ((is_number(r[s]) == True) or (var in r[s])) and (r[s-1] == "/") and (s != 0):

			#print("r[s] = /"+str(l[s]))
			div_check_r += 1
			br_string = r[s]

			if var in r[s]:

				temp=[]
				temp.append(r[s])
				temp.insert(0,"(1")
				temp.append(")1")
				temp_string = stringify(temp)
				temp, temp_var = bracketify(temp_string)
				temp, temp_deg = grouping(temp)

				print("AN ASYMPTOTE HAS BEEN FOUND", temp_string)
				asy_temp = solving(temp, ["(1","0",")1"], temp_var[0], temp_deg[0])
				if not asymptote:

					asymptote.append(asy_temp)

				if asy_temp not in asymptote:
	
					asymptote.append(asy_temp)

				print("FOUND AN ASYMPTOTE: ", asymptote)

			k = 0
			b = 0
			b_open = 0
			b_close = 0
			while k != s:

				if "(" in r[k]:

					b_open+=1
					b+=1

				elif ")" in r[k]:

					b_close+=1
					b-=1

				k+=1
 
			x = 1
			c = b
			while k != len(r):

				if "(" in r[k]:

					b_open+=1
					b+=1

				elif ")" in r[k]:

					b_close+=1
					b-=1

				if (is_number(r[k]) == True) and (r[k-1] == "^") and (r[k-2] == ")"+str(c)):

					x*=float(r[k])
					c-=1

				elif (r[k-1] != "^") and (r[k-2] == ")"+str(c)):

					c-=1

				k+=1

			if x > 1:

				br_string = "("+br_string+")^"+str(x)
				
			#print("The divisor is: "+br_string)
			
			br, br_var = bracketify(br_string)
			br, br_deg = grouping(br)
			del br[0]
			del br[len(br)-1]

			#print(br)

			k=1
			b=1
			while r[k] != ")1":

				if "(" in r[k]:

					b+=1

				elif ")" in r[k]:

					b-=1

				if ((is_number(r[k]) == True) or (var in r[k])) and (b == 1):

					#pass
					k+=1
					r.insert(k,"*")
					k+=1
					for i in range(len(br)-1,-1,-1):

						r.insert(k,br[i])

					#print(r, k)

					if k < s:

						s+=len(br)+1

					while r[k] != ")1":

						if "(" in r[k]:

							b+=1

						elif ")" in r[k]:

							b-=1

						if (r[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(r)-1:

						k-=1

					#print("k = "+str(k), "len(r)-1 = "+str(len(r)-1))

				elif (r[k] == "(2"):

					r.insert(k,"*")
					for i in range(len(br)-1,-1,-1):

						r.insert(k,br[i])
					
					#print(r, k)

					if k < s:

						s+=len(br)+1

					k+=len(br)+1

					while r[k] != ")1":

						if "(" in r[k]:

							b+=1

						elif ")" in r[k]:

							b-=1

						if (r[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(r)-1:

						k-=1

					#print("k = "+str(k), "len(r)-1 = "+str(len(r)-1))

				k+=1

			k=1
			b=1
			while l[k] != ")1":

				if "(" in l[k]:

					b+=1

				elif ")" in l[k]:

					b-=1

				if ((is_number(l[k]) == True) or (var in l[k])) and (b == 1):

					#pass
					k+=1
					l.insert(k,"*")
					k+=1
					for i in range(len(br)-1,-1,-1):

						l.insert(k,br[i])

					#print(l, k)

					while l[k] != ")1":

						if "(" in l[k]:

							b+=1

						elif ")" in l[k]:

							b-=1

						if (l[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(l)-1:

						k-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				elif (l[k] == "(2"):

					l.insert(k,"*")
					for i in range(len(br)-1,-1,-1):

						l.insert(k,br[i])

					k+=len(br)+1
					#print(l, k)

					while l[k] != ")1":

						if "(" in l[k]:

							b+=1

						elif ")" in l[k]:

							b-=1

						if (l[k] in "+-") and (b == 1):

							break

						k+=1

					if k == len(l)-1:

						k-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				k+=1

			print(l,r)
			
		s+=1

	l_string = stringify(l)
	r_string = stringify(r)
	print(l_string+"="+r_string)

	#2.0.1 Remove unnecessary brackets
	s=0
	while s != len(l):

		if (is_number(l[s]) == True) and (l[s-1] == "^") and (")" in l[s-2]) and (s != 0):

			br = []
			b = l[s-2]
			b = b.replace(")","")
			b = int(b)
			j = s-3
			k = j
			x = float(l[s])

			br_cnt=0
			while l[j] != "("+str(b):

				if ")" in l[j]:

					br_cnt+=1

				br.insert(0,l[j])
				j-=1

			br_string = br[:]
			br_string.insert(0,"(1")
			br_string.append(")1")
			br_string = stringify(br_string)
			if (br_string[0] == "(") and (br_string[len(br)-1] == ")") and (br_cnt == 1):
				
				br = br_string
				n = 1
				new_br=""
				while n != len(br)-1:

					new_br += br[n]
					n+=1

				br = new_br
				#print("br = "+br)
				j+=2
				del l[j-1:k+1]
				j-=1
				n=0
				while n != len(br):

					l.insert(j,br[n])
					n+=1
					j+=1

				l_string = stringify(l)
				print(l_string+"="+r_string)

			elif (br_cnt != 1) and (br_cnt > 0):

				print("br",br)
				n=0
				while n!= len(br):

					if br[n] == ")"+str(b+1):

						br.insert(n+1,"^")
						br.insert(n+2,str(x))
						print("br",br)

					n+=1

				del l[s-1:s+1]
				print("now l looks like", l)
				del l[j:k+2]
				print("now l looks like", l)
				
				#j+=1
				n=0
				while n != len(br):

					if "(" in br[n]:

						l.insert(j,"("+str(b))
						b+=1

					elif ")" in br[n]:

						b-=1
						l.insert(j,")"+str(b))
						

					else:

						l.insert(j,br[n])

					n+=1
					j+=1

				l_string = stringify(l)
				print(l_string+"="+r_string, l)

				
								
		s+=1

	s=0
	while s != len(r):

		if (is_number(r[s]) == True) and (r[s-1] == "^") and (")" in r[s-2]) and (s != 0):

			br = []
			b = r[s-2]
			b = b.replace(")","")
			b = int(b)
			j = s-3
			k = j
			x = float(r[s])

			br_cnt=0
			while r[j] != "("+str(b):

				if ")" in r[j]:

					br_cnt+=1

				br.insert(0,r[j])
				j-=1

			br_string = br[:]
			br_string.insert(0,"(1")
			br_string.append(")1")
			br_string = stringify(br_string)
			if (br_string[0] == "(") and (br_string[len(br)-1] == ")") and (br_cnt == 1):
				
				br = br_string
				n = 1
				new_br=""
				while n != len(br)-1:

					new_br += br[n]
					n+=1

				br = new_br
				#print("br = "+br)
				j+=2
				del r[j-1:k+1]
				j-=1
				n=0
				while n != len(br):

					r.insert(j,br[n])
					n+=1
					j+=1

				r_string = stringify(r)
				print(l_string+"="+r_string)

			elif (br_cnt != 1) and (br_cnt > 0):

				print("br",br)
				n=0
				while n!= len(br):

					if br[n] == ")"+str(b+1):

						br.insert(n+1,"^")
						br.insert(n+2,str(x))
						print("br",br)

					n+=1

				del r[s-1:s+1]
				print("now r looks like", r)
				del r[j:k+2]
				print("now r looks like", r)
				
				#j+=1
				n=0
				while n != len(br):

					if "(" in br[n]:

						r.insert(j,"("+str(b))
						b+=1

					elif ")" in br[n]:

						b-=1
						r.insert(j,")"+str(b))
						

					else:

						r.insert(j,br[n])

					n+=1
					j+=1

				r_string = stringify(r)
				print(l_string+"="+r_string, r)

				
								
		s+=1

	b=0
	for s in l:

		if "(" in s:

			temp = s
			temp = temp.replace("(","")
			temp = int(temp)

			if temp > b:

				b = temp

	l_string = stringify(l)
	r_string = stringify(r)
	print(l_string+" = "+r_string)
	#2.0.2 If b > 2, then we have to foil out
	if (b >= 2) and ("/" in l_string):

		#now to remove any ()/()=1

		c = b
		l_copy = l[:]

		while c != 1:

			s=0
			while s != len(l):

				#is it ()*() or is it ()^3*()
				if ((l[s] == "("+str(c-1)) and (l[s-1] == "*") and (l[s-2] == ")"+str(c-1))):

					#we need to figure out if there are other brackets inside and if the second bracket has an exponent at the end
					br_cnt=0
					j=s+1
					br_two=[]
					while l[j] != ")"+str(c-1):

						if l[j] == "("+str(c):

							br_cnt+=1

						br_two.append(l[j])

						j+=1
			
					if br_cnt > 1:

						br_one=[]
						k=s-2
						while l[k] != "("+str(c-1):

							br_one.insert(0,l[k])
							k-=1

						br_one.insert(0,l[k])
						if l[j+1] == "^":

							x = float(l[j+2])

						else:

							x = 1

						del l[k:s]
						#IF x > 1, need to multiply the br_two exponent by x
						print("BRACKET_TWO", br_two, "BRACKET_ONE", br_one, "L", l)

						k=s-len(br_one)
						print(s)
						while l[k] != ")"+str(c-1):


							if l[k] == "("+str(c):

								b_open = 1

								l.insert(k,"*")

								for q in range(len(br_one)-1,-1,-1):

									if "(" in br_one[q]:

										l.insert(k,"("+str(c))
									
									elif ")" in br_one[q]:

										l.insert(k,")"+str(c))

									else:

										l.insert(k,br_one[q])

								print("L",l,l[k],k)

								k+=1
								while k!= len(l)-1:

									if l[k] == ")"+str(c):

										b_open = 0

									elif l[k] == "("+str(c):

										b_open = 1

									elif (l[k] in "+-") and (b_open == 0):

										break

									elif l[k] == ")"+str(c-1):

										break

									k+=1

								k-=1
								s=0

							k+=1

						j+=1
				
				elif ((l[s] == "("+str(c-1)) and (l[s-1] == "*") and (is_number(l[s-2]) == True) and (l[s-3] == "^") and (l[s-4] == ")"+str(c-1))):

					#we need to figure out if there are other brackets inside and if the second bracket has an exponent at the end
					br_cnt=0
					j=s+1
					br_two=[]
					while l[j] != ")"+str(c-1):

						if l[j] == "("+str(c):

							br_cnt+=1

						br_two.append(l[j])

						j+=1
			
					if br_cnt > 1:

						br_one=[]
						k=s-2
						while l[k] != "("+str(c-1):

							br_one.insert(0,l[k])
							k-=1

						br_one.insert(0,l[k])
						if l[j+1] == "^":

							x = float(l[j+2])

						else:

							x = 1

						del l[k:s]
						#IF x > 1, need to multiply the br_two exponent by x
						print("BRACKET_TWO", br_two, "BRACKET_ONE", br_one, "L", l)

						k=s-len(br_one)
						print(s)
						while l[k] != ")"+str(c-1):


							if l[k] == "("+str(c):

								b_open = 1

								l.insert(k,"*")

								for q in range(len(br_one)-1,-1,-1):

									if "(" in br_one[q]:

										l.insert(k,"("+str(c))
									
									elif ")" in br_one[q]:

										l.insert(k,")"+str(c))

									else:

										l.insert(k,br_one[q])

								print("L",l,l[k],k)

								k+=1
								while k!= len(l)-1:

									if l[k] == ")"+str(c):

										b_open = 0

									elif l[k] == "("+str(c):

										b_open = 1

									elif (l[k] in "+-") and (b_open == 0):

										break

									elif l[k] == ")"+str(c-1):

										break

									k+=1

								k-=1
								s=0

							k+=1

						j+=1

				s+=1

			c-=1

		l_string = stringify(l)
		l_copy = l[:]
		print("before we remove divisions",l_string)
		c = b
		while c != 1:

			print("JESUS C = "+str(c), "div_check_l = "+str(div_check_l))
			s=0
			while s != len(l):

				if l[s] == "("+str(c):

					br=[]
					b_open = 1
					j = s
					while j != len(l)-1:

						if l[j] == ")"+str(c):

							b_open = 0

						elif l[j] == "("+str(c):

							b_open = 1

						elif (l[j] in "+-") and (b_open == 0):

							br.insert(0,"(1")
							br.append(")1")
							br_string = stringify(br)
							print("!!!BR_string", br_string)

							z=0
							while z != len(br_string):

								if "(" in br_string[z]:

									k=z
									temp=""
									while br_string[k] != ")":
								
										temp+=br_string[k]
										k+=1
					
									temp+=br_string[k]
									k+=1
									if br_string[k] == "^":

										while br_string[k] not in "*/+-":

											temp+=br_string[k]
											k+=1

									print("TEMP",temp)

									if (temp+"*" in br_string) and ("/"+temp in br_string):

										new_br_string = br_string
										br_string = br_string.replace(temp+"*","")
										br_string = br_string.replace("/"+temp,"")
										print(br_string, new_br_string)
										l_string = stringify(l)
										l_string = l_string.replace(new_br_string,br_string)
										l_copy, useless = bracketify(l_string)
										div_check_l-=1
										print(l_string,div_check_l)
										br=[]
										s=len(l)-2
										break

									else:

										z=k-1
										print("ZED = "+str(z))

								z+=1

						elif l[j] == ")"+str(c-1):
	
							br.insert(0,"(1")
							br.append(")1")
							br_string = stringify(br)
							print("!!!BR_string", br_string)

							z=0
							while z != len(br_string):

								if "(" in br_string[z]:

									k=z
									temp=""
									while br_string[k] != ")":
								
										temp+=br_string[k]
										k+=1
					
									temp+=br_string[k]
									k+=1
									if br_string[k] == "^":

										while br_string[k] not in "*/+-":

											temp+=br_string[k]
											k+=1

									print("TEMP",temp)

									if (temp+"*" in br_string) and ("/"+temp in br_string):

										new_br_string = br_string
										br_string = br_string.replace(temp+"*","")
										br_string = br_string.replace("/"+temp,"")
										print(br_string, new_br_string)
										l_string = stringify(l_copy)
										l_string = l_string.replace(new_br_string,br_string)
										l_copy, useless = bracketify(l_string)
										div_check_l-=1
										print(l_string,div_check_l)
										br=[]
										s=len(l)-2
										break

									else:

										z=k-1
										print("ZED = "+str(z))

								z+=1

						br.append(l[j])
						print(br)
						j+=1

				s+=1

			print("div_check_l = "+str(div_check_l))
			#if there's only one term, it won't get rid of bracket division so this piece of code will hopefully counter that
			if div_check_l != 0:

				l_string = stringify(l)
				find = l_string.find('/(')
				j = find + 1
				temp=""
				while l_string[j] != ")":
					
					temp += l_string[j]
					j += 1

				temp += ")"

				l_string = l_string.replace("/"+temp,'')
				l_string = l_string.replace(temp+"*",'')
				print(temp,l_string)
				l, useless = bracketify(l_string)
				l, useless = grouping(l)
				div_check_l = 0
				print(l)

			else:

				l = l_copy[:]

			c-=1

	b=0
	for s in r:

		if "(" in s:

			temp = s
			temp = temp.replace("(","")
			temp = int(temp)

			if temp > b:

				b = temp

	l_string = stringify(l)
	r_string = stringify(r)
	print("SUKAAAA",l_string+" = "+r_string)
	if (b >= 2) and ("/" in r_string):

		c = b
		while c != 1:

			s=0
			while s != len(r):

				#is it ()*() or is it ()^3*()
				if ((r[s] == "("+str(c-1)) and (r[s-1] == "*") and (r[s-2] == ")"+str(c-1))):

					#we need to figure out if there are other brackets inside and if the second bracket has an exponent at the end
					br_cnt=0
					j=s+1
					br_two=[]
					while r[j] != ")"+str(c-1):

						if r[j] == "("+str(c):

							br_cnt+=1

						br_two.append(r[j])

						j+=1
			
					if br_cnt > 1:

						br_one=[]
						k=s-2
						while r[k] != "("+str(c-1):

							br_one.insert(0,r[k])
							k-=1

						br_one.insert(0,r[k])
						if r[j+1] == "^":

							x = float(r[j+2])

						else:

							x = 1

						del r[k:s]
						#IF x > 1, need to multiply the br_two exponent by x
						print("BRACKET_TWO", br_two, "BRACKET_ONE", br_one, "L", r)

						k=s-len(br_one)
						print(s)
						while r[k] != ")"+str(c-1):


							if r[k] == "("+str(c):

								b_open = 1

								r.insert(k,"*")

								for q in range(len(br_one)-1,-1,-1):

									if "(" in br_one[q]:

										r.insert(k,"("+str(c))
									
									elif ")" in br_one[q]:

										r.insert(k,")"+str(c))

									else:

										r.insert(k,br_one[q])

								print("R",r,r[k],k)

								k+=1
								while k!= len(r)-1:

									if r[k] == ")"+str(c):

										b_open = 0

									elif r[k] == "("+str(c):

										b_open = 1

									elif (r[k] in "+-") and (b_open == 0):

										break

									elif r[k] == ")"+str(c-1):

										break

									k+=1

								k-=1
								s=0

							k+=1

						j+=1

				elif ((r[s] == "("+str(c-1)) and (r[s-1] == "*") and (is_number(r[s-2]) == True) and (r[s-3] == "^") and (r[s-4] == ")"+str(c-1))):

					#we need to figure out if there are other brackets inside and if the second bracket has an exponent at the end
					br_cnt=0
					j=s+1
					br_two=[]
					while r[j] != ")"+str(c-1):

						if r[j] == "("+str(c):

							br_cnt+=1

						br_two.append(r[j])

						j+=1
			
					if br_cnt > 1:

						br_one=[]
						k=s-2
						while r[k] != "("+str(c-1):

							br_one.insert(0,r[k])
							k-=1

						br_one.insert(0,r[k])
						if r[j+1] == "^":

							x = float(r[j+2])

						else:

							x = 1

						del r[k:s]
						#IF x > 1, need to multiply the br_two exponent by x
						print("BRACKET_TWO", br_two, "BRACKET_ONE", br_one, "L", r)

						k=s-len(br_one)
						print(s)
						while r[k] != ")"+str(c-1):


							if r[k] == "("+str(c):

								b_open = 1

								r.insert(k,"*")

								for q in range(len(br_one)-1,-1,-1):

									if "(" in br_one[q]:

										r.insert(k,"("+str(c))
									
									elif ")" in br_one[q]:

										r.insert(k,")"+str(c))

									else:

										r.insert(k,br_one[q])

								print("R",r,r[k],k)

								k+=1
								while k!= len(r)-1:

									if r[k] == ")"+str(c):

										b_open = 0

									elif r[k] == "("+str(c):

										b_open = 1

									elif (r[k] in "+-") and (b_open == 0):

										break

									elif r[k] == ")"+str(c-1):

										break

									k+=1

								k-=1
								s=0

							k+=1

						j+=1		

				s+=1

			c-=1

		#now to remove any ()/()=1

		c = b
		r_copy = r[:]
		while c != 1:

			print("C = "+str(c))
			s=0
			while s != len(r):

				if r[s] == "("+str(c):

					br=[]
					b_open = 1
					j = s
					while j != len(r):

						if r[j] == ")"+str(c):

							b_open = 0

						elif r[j] == "("+str(c):

							b_open = 1

						elif (r[j] in "+-") and (b_open == 0):

							br.insert(0,"(1")
							br.append(")1")
							br_string = stringify(br)
							print("!!!BR_string", br_string)

							z=0
							while z != len(br_string):

								if "(" in br_string[z]:

									k=z
									temp=""
									while br_string[k] != ")":
								
										temp+=br_string[k]
										k+=1
					
									temp+=br_string[k]
									k+=1
									if br_string[k] == "^":

										while br_string[k] not in "*/+-":

											temp+=br_string[k]
											k+=1

									print("TEMP",temp)

									if (temp+"*" in br_string) and ("/"+temp in br_string):

										new_br_string = br_string
										br_string = br_string.replace(temp+"*","")
										br_string = br_string.replace("/"+temp,"")
										print(br_string, new_br_string)
										r_string = stringify(r_copy)
										r_string = r_string.replace(new_br_string,br_string)
										r_copy, useless = bracketify(r_string)
										div_check_r-=1
										print(r_string,r_copy)
										br=[]
										s=len(r)-2
										break

									else:

										z=k-1
										print("ZED = "+str(z))

								z+=1

						elif r[j] == ")"+str(c-1):
	
							br.insert(0,"(1")
							br.append(")1")
							br_string = stringify(br)
							print("!!!BR_string", br_string)

							z=0
							while z != len(br_string):

								if "(" in br_string[z]:

									k=z
									temp=""
									while br_string[k] != ")":
								
										temp+=br_string[k]
										k+=1
					
									temp+=br_string[k]
									
									if len(br_string)-1 > k:

										k+=1
										if br_string[k] == "^":

											while br_string[k] not in "*/+-":

												temp+=br_string[k]
												k+=1

									print("TEMP",temp)

									if (temp+"*" in br_string) and ("/"+temp in br_string):

										new_br_string = br_string
										br_string = br_string.replace(temp+"*","")
										br_string = br_string.replace("/"+temp,"")
										print(br_string, new_br_string)
										r_string = stringify(r_copy)
										r_string = r_string.replace(new_br_string,br_string)
										r_copy, useless = bracketify(r_string)
										div_check_r-=1
										print(r_string,r_copy)
										br=[]
										s=len(r)-2
										break

									else:

										z=k-1
										print("ZED = "+str(z))

								z+=1

						br.append(r[j])
						print(br)
						j+=1

				s+=1

			if div_check_r != 0:

				r_string = stringify(r)
				find = r_string.find('/(')
				j = find + 1
				temp=""
				while r_string[j] != ")":
					
					temp += r_string[j]
					j += 1

				temp += ")"

				r_string = r_string.replace("/"+temp,'')
				r_string = r_string.replace(temp+"*",'')
				print(temp,r_string)
				r, useless = bracketify(r_string)
				r, useless = grouping(r)
				div_check_r = 0
				print(r)

			else:

				r = r_copy[:]

			c-=1 	

	#2.1 remove any exponents on brackets

	b=0
	for s in l:

		if "(" in s:

			temp = s
			temp = temp.replace("(","")
			temp = int(temp)

			if temp > b:

				b = temp

	l_string = stringify(l)
	r_string = stringify(r)
	print("NOW WE GET RID OF EXPONENTS",l_string+"="+r_string,"b = "+str(b))
	while b != 1:

		s=0
		while s != len(l):

			#1. remove any exponents on brackets
			if (is_number(l[s]) == True) and (l[s-1] == "^") and (")"+str(b) in l[s-2]) and (s != 0):

				x = float(l[s])
				if x >= 1:

					j=s-2
					br = []
					while l[j] != "("+str(b):

						br.insert(0,l[j])
						j-=1

					br.insert(0,l[j])

					check = False
					for op in oper_dict.values():

						if op == l[j-1]:

							check = True

					if check == False:
				
						br_one = br[:]
						br_two = br[:]
						br_og = br[:]
						br_og.append("^")
						br_og.append(str(x))
						br_og.insert(0,"(1")
						br_og.append(")1")
						br_og = stringify(br_og)
					
						#if number is not a multiple of 2 like 28, dividing by two yields an odd number eventually causing this to crash
						if is_even(x):


							#print("x is even and is "+str(x))
							while x != 1:

								if is_even(x):

									br = foiling(br_one, br_two, var)
									#print(br)
									br.insert(0,"("+str(b))
									br.append(")"+str(b))
									br_one = br[:]
									br_two = br[:]
									x/=2

								else:
									
									br = foiling(br_one, br_two, var)
									#print(br)
									br.insert(0,"("+str(b))
									br.append(")"+str(b))
									br_one = br[:]
									x-=2

									while x != 0:

										#print(br_one, br_two)
										br = foiling(br_one, br_two, var)
										#print(br)
										br.insert(0,"("+str(b))
										br.append(")"+str(b))
										br_one = br[:]
										x-=1

									break
	
							result = br
							result, var_res = grouping(result)
							res_string = stringify(result)
							print(res_string)

						else:
					
							print("x is odd and is "+str(x))
					
							#print(br_one, br_two)
							br = foiling(br_one, br_two, var)
							br.insert(0,"("+str(b))
							br.append(")"+str(b))
							br_one = br
							x-=2

							while x != 0:

								#print(br_one, br_two)
								br = foiling(br_one, br_two, var)
								br.insert(0,"("+str(b))
								br.append(")"+str(b))
								br_one = br
								x-=1

							result = br
							result, var_res = grouping(result)
							res_string = stringify(result)
							print(res_string)

						del l[j:s+1]
						#print("after deleting", l)
						if b > 2:

							l.insert(j,"("+str(b))
							j+=1
							for k in range(1,len(result)-1):

								l.insert(j,result[k])
								j+=1
								#print(l)

							l.insert(j,")"+str(b))

						else:

							for k in range(0,len(result)):

								l.insert(j,result[k])
								j+=1
								#print(l)

							l_string = stringify(l)
							#print("br_og = "+br_og, l_string)
							result.insert(0,"(1")
							result.append(")1")
							result = stringify(result)
							if br_og in l_string:

								#print("result = "+result)
								l_string = l_string.replace(br_og,result)
								#print("after subbing br_og...", l_string)
								l, var_l = bracketify(l_string)
								l, deg_l = grouping(l)
							
							r_string = stringify(r)
							if br_og in r_string:
		
								
								r_string = r_string.replace(br_og,result)
								r, var_r = bracketify(r_string)
								r, deg_r = grouping(r)
					
						s=-1
	
			s+=1

		#()*()
		s=0
		while s != len(l):
		
			#print("PRIVET!")
			if (l[s] == "("+str(b)) and (l[s-1] == "*") and (l[s-2] == ")"+str(b)):

				ini_two = s
				end_one = s-2
				k = s
				j = s-2
				br_one = []
				br_two = []

				while l[k] != ")"+str(b):

					br_two.append(l[k])
					k+=1

				br_two.append(l[k])

				while l[j] != "("+str(b):

					br_one.insert(0,l[j])
					j-=1

				br_one.insert(0,l[j])
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(b))
				br.append(")"+str(b))

				del l[j:k+1]
				k = j
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((var in l[s]) and (l[s-1] == "*") and (l[s-2] == ")"+str(b))) or ((is_number(l[s]) == True) and (l[s-1] == "*") and (l[s-2] == ")"+str(b))):

				end_one = s-2
				j = s-2
				br_one = []
				br_two = []

				while l[j] != "("+str(b):

					br_one.insert(0,l[j])
					j-=1

				br_one.insert(0,l[j])

				br_two.append("("+str(b))
				br_two.append(l[s])
				br_two.append(")"+str(b))
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(b))
				br.append(")"+str(b))

				k = j
				del l[j:s+1]
				print(l)
				for x in br:

					l.insert(k,x)
					k+=1

				print(l)
				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((l[s] == "("+str(b)) and (l[s-1] == "*") and (var in l[s-2])) or ((l[s] == "("+str(b)) and (l[s-1] == "*") and (is_number(l[s-2]) == True)):

				#print("ZDRAVSTVUITYA!")
				ini_two = s
				k = s
				br_one = []
				br_two = []

				while l[k] != ")"+str(b):

					br_two.append(l[k])
					k+=1

				br_two.append(l[k])

				br_one.append("("+str(b))
				br_one.append(l[s-2])
				br_one.append(")"+str(b))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(b))
				br.append(")"+str(b))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1


			elif (var in l[s]) and (l[s-1] == "*") and (var in l[s-2]):

				br_one = []
				br_two = []

				br_one.append("("+str(b))
				br_one.append(l[s-2])
				br_one.append(")"+str(b))

				br_two.append("("+str(b))
				br_two.append(l[s])
				br_two.append(")"+str(b))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(b))
				br.append(")"+str(b))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			s+=1

		#()+-()
		s=0
		while s != len(l):

			if (l[s] == "("+str(b)) and (l[s-1] in "+-") and (l[s-2] == ")"+str(b)):

				ini_two = s
				end_one = s-2
				op = l[s-1]
				k = s
				j = s-2
				br_one = []
				br_two = []

				while l[k] != ")"+str(b):

					br_two.append(l[k])
					k+=1

				br_two.append(l[k])

				while l[j] != "("+str(b):

					br_one.insert(0,l[j])
					j-=1

				br_one.insert(0,l[j])
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(b))
				br.append(")"+str(b))

				del l[j:k+1]
				k = j
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((var in l[s]) and (l[s-1] in "+-") and (l[s-2] == ")"+str(b))) or ((is_number(l[s]) == True) and (l[s-1] in "+-") and (l[s-2] == ")"+str(b))):

				end_one = s-2
				j = s-2
				op = l[s-1]
				br_one = []
				br_two = []

				while l[j] != "("+str(b):

					br_one.insert(0,l[j])
					j-=1

				br_one.insert(0,l[j])

				br_two.append("("+str(b))
				br_two.append(l[s])
				br_two.append(")"+str(b))
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(b))
				br.append(")"+str(b))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((l[s] == "("+str(b)) and (l[s-1] in "+-") and (var in l[s-2])) or ((l[s] == "("+str(b)) and (l[s-1] in "+-") and (is_number(l[s-2]) == True)):

				ini_two = s
				k = s
				op = l[s-1]
				br_one = []
				br_two = []

				while l[k] != ")"+str(b):

					br_two.append(l[k])
					k+=1

				br_two.append(l[k])

				br_one.append("("+str(b))
				br_one.append(l[s-2])
				br_one.append(")"+str(b))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(b))
				br.append(")"+str(b))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			s+=1

		b-=1

	l_string = stringify(l)
	print(l_string)

	s=0
	while s != len(r):

		if (is_number(r[s]) == True) and (r[s-1] == "^") and (")" in r[s-2]) and (s != 0):

			br = []
			b = r[s-2]
			b = b.replace(")","")
			j = s-3
			k = j

			while r[j] != "("+b:

				br.insert(0,r[j])
				j-=1

			br.insert(0,"(1")
			br.append(")1")
			br = stringify(br)
			if (br[0] == "(") and (br[len(br)-1] == ")"):
				print("br = "+br)
				n = 1
				new_br=""
				while n != len(br)-1:

					new_br += br[n]
					n+=1

				br = new_br
				print("br = "+br)
				j+=2
				del r[j-1:k+1]
				j-=1
				n=0
				while n != len(br):

					r.insert(j,br[n])
					n+=1
					j+=1

				r_string = stringify(r)
				print(l_string+"="+r_string)
								
		s+=1

	b=0
	for s in r:

		if "(" in s:

			temp = s
			temp = temp.replace("(","")
			temp = int(temp)

			if temp > b:

				b = temp

	l_string = stringify(l)
	r_string = stringify(r)
	print("\n"+l_string+"\n=\n"+r_string)
	

	#RHS now
	s=0
	while b != 1:

		s=0
		while s != len(r):

			#1. remove any exponents on brackets
			if (is_number(r[s]) == True) and (r[s-1] == "^") and (")"+str(b) in r[s-2]) and (s != 0):

				x = float(r[s])
				if x >= 1:

					j=s-2
					br = []
					while r[j] != "("+str(b):

						br.insert(0,r[j])
						j-=1

					br.insert(0,r[j])

					check = False
					for op in oper_dict.values():

						if op == r[j-1]:

							check = True

					if check == False:
				
						br_one = br[:]
						br_two = br[:]
						br_og = br[:]
						br_og.append("^")
						br_og.append(str(x))
						br_og.insert(0,"(1")
						br_og.append(")1")
						br_og = stringify(br_og)
					
						#if number is not a multiple of 2 like 28, dividing by two yields an odd number eventually causing this to crash
						if is_even(x):


							print("x is even and is "+str(x))
							while x != 1:

								if is_even(x):

									br = foiling(br_one, br_two, var)
									#print(br)
									br.insert(0,"("+str(b))
									br.append(")"+str(b))
									br_one = br[:]
									br_two = br[:]
									x/=2

								else:
									
									br = foiling(br_one, br_two, var)
									#print(br)
									br.insert(0,"("+str(b))
									br.append(")"+str(b))
									br_one = br[:]
									x-=2

									while x != 0:

										#print(br_one, br_two)
										br = foiling(br_one, br_two, var)
										#print(br)
										br.insert(0,"("+str(b))
										br.append(")"+str(b))
										br_one = br[:]
										x-=1

									break
	
							result = br
							result, var_res = grouping(result)
							res_string = stringify(result)
							print(res_string)

						else:
					
							print("x is odd and is "+str(x))
					
							#print(br_one, br_two)
							br = foiling(br_one, br_two, var)
							br.insert(0,"("+str(b))
							br.append(")"+str(b))
							br_one = br
							x-=2

							while x != 0:

								#print(br_one, br_two)
								br = foiling(br_one, br_two, var)
								br.insert(0,"("+str(b))
								br.append(")"+str(b))
								br_one = br
								x-=1

							result = br
							result, var_res = grouping(result)
							res_string = stringify(result)
							print(res_string)

						del r[j:s+1]
						#print("after deleting", l)
						if b > 2:

							for k in range(1,len(result)-1):

								r.insert(j,result[k])
								j+=1
								#print(l)

						else:

							for k in range(0,len(result)):

								r.insert(j,result[k])
								j+=1
								#print(l)

							l_string = stringify(l)
							#print("br_og = "+br_og, l_string)
							result.insert(0,"(1")
							result.append(")1")
							result = stringify(result)
							if br_og in l_string:

								#print("result = "+result)
								l_string = l_string.replace(br_og,result)
								#print("after subbing br_og...", l_string)
								l, var_l = bracketify(l_string)
								l, deg_l = grouping(l)
							
							r_string = stringify(r)
							if br_og in r_string:
		
								r_string = r_string.replace(br_og,result)
								r, var_r = bracketify(r_string)
								r, deg_r = grouping(r)
					
						s=-1
	
			s+=1

		b-=1

	#3. foil out any bracket multiplication ()*()
	#4. foil out any bracket's multiplied by constants c*()
	"""	
	b=0
	for s in l:

		if "(" in s:

			temp = s
			temp = temp.replace("(","")
			temp = int(temp)

			if temp > b:

				b = temp

	for c in range(b,1,-1):
		print(c)

		s=0
		while s != len(l):

			if (l[s] == "("+str(c)) and (l[s-1] == "*") and (l[s-2] == ")"+str(c)):

				ini_two = s
				end_one = s-2
				k = s
				j = s-2
				br_one = []
				br_two = []

				while l[k] != ")"+str(c):

					br_two.append(l[k])
					k+=1

				br_two.append(l[k])

				while l[j] != "("+str(c):

					br_one.insert(0,l[j])
					j-=1

				br_one.insert(0,l[j])
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del l[j:k+1]
				k = j
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((var in l[s]) and (l[s-1] == "*") and (l[s-2] == ")"+str(c))) or ((is_number(l[s]) == True) and (l[s-1] == "*") and (l[s-2] == ")"+str(c))):

				end_one = s-2
				j = s-2
				br_one = []
				br_two = []

				while l[j] != "("+str(c):

					br_one.insert(0,l[j])
					j-=1

				br_one.insert(0,l[j])

				br_two.append("("+str(c))
				br_two.append(l[s])
				br_two.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((l[s] == "("+str(c)) and (l[s-1] == "*") and (var in l[s-2])) or ((l[s] == "("+str(c)) and (l[s-1] == "*") and (is_number(l[s-2]) == True)):

				ini_two = s
				k = s
				br_one = []
				br_two = []

				while l[k] != ")"+str(c):

					br_two.append(l[k])
					k+=1

				br_two.append(l[k])

				br_one.append("("+str(c))
				br_one.append(l[s-2])
				br_one.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1


			elif (var in l[s]) and (l[s-1] == "*") and (var in l[s-2]):

				br_one = []
				br_two = []

				br_one.append("("+str(c))
				br_one.append(l[s-2])
				br_one.append(")"+str(c))

				br_two.append("("+str(c))
				br_two.append(l[s])
				br_two.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			s+=1 
	"""
	b=0
	for s in r:

		if "(" in s:

			temp = s
			temp = temp.replace("(","")
			temp = int(temp)

			if temp > b:

				b = temp

	for c in range(b,1,-1):
		print(c)

		s=0
		while s != len(r):

			if (r[s] == "("+str(c)) and (r[s-1] == "*") and (r[s-2] == ")"+str(c)):

				ini_two = s
				end_one = s-2
				k = s
				j = s-2
				br_one = []
				br_two = []

				while r[k] != ")"+str(c):

					br_two.append(r[k])
					k+=1

				br_two.append(r[k])

				while r[j] != "("+str(c):

					br_one.insert(0,r[j])
					j-=1

				br_one.insert(0,r[j])
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del r[j:k+1]
				k = j
				for x in br:

					r.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((var in r[s]) and (r[s-1] == "*") and (r[s-2] == ")"+str(c))) or ((is_number(r[s]) == True) and (r[s-1] == "*") and (r[s-2] == ")"+str(c))):

				end_one = s-2
				j = s-2
				br_one = []
				br_two = []

				while r[j] != "("+str(c):

					br_one.insert(0,r[j])
					j-=1

				br_one.insert(0,r[j])

				br_two.append("("+str(c))
				br_two.append(r[s])
				br_two.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del r[s-2:k+1]
				k = s-2
				for x in br:

					r.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((r[s] == "("+str(c)) and (r[s-1] == "*") and (var in r[s-2])) or ((r[s] == "("+str(c)) and (r[s-1] == "*") and (is_number(r[s-2]) == True)):

				print("ASKINAMARINKINYDINK")
				ini_two = s
				k = s
				br_one = []
				br_two = []

				while r[k] != ")"+str(c):

					br_two.append(r[k])
					k+=1

				br_two.append(r[k])

				br_one.append("("+str(c))
				br_one.append(r[s-2])
				br_one.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del r[s-2:k+1]
				k = s-2
				for x in br:

					r.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)

				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1


			elif (var in r[s]) and (r[s-1] == "*") and (var in r[s-2]):

				br_one = []
				br_two = []

				br_one.append("("+str(c))
				br_one.append(r[s-2])
				br_one.append(")"+str(c))

				br_two.append("("+str(c))
				br_two.append(r[s])
				br_two.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+"*"+br_two_str
				print("br_og = "+br_og)

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del r[s-2:k+1]
				k = s-2
				for x in br:

					r.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			s+=1

	l_string = stringify(l)
	r_string = stringify(r)
	print("Here we are"+"\n"+l_string+"\n=\n"+r_string)
	
	#5. Solve Bracket Addition or Subtraction.
	
	b=0
	for s in l:

		if ("(" in s) and ("j" not in s):

			temp = s
			temp = temp.replace("(","")
			temp = int(temp)

			if temp > b:

				b = temp
	"""
	for c in range(b,1,-1):

		s=0
		while s != len(l):

			if (l[s] == "("+str(c)) and (l[s-1] in "+-") and (l[s-2] == ")"+str(c)):

				ini_two = s
				end_one = s-2
				op = l[s-1]
				k = s
				j = s-2
				br_one = []
				br_two = []

				while l[k] != ")"+str(c):

					br_two.append(l[k])
					k+=1

				br_two.append(l[k])

				while l[j] != "("+str(c):

					br_one.insert(0,l[j])
					j-=1

				br_one.insert(0,l[j])
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del l[j:k+1]
				k = j
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((var in l[s]) and (l[s-1] in "+-") and (l[s-2] == ")"+str(c))) or ((is_number(l[s]) == True) and (l[s-1] in "+-") and (l[s-2] == ")"+str(c))):

				end_one = s-2
				j = s-2
				op = l[s-1]
				br_one = []
				br_two = []

				while l[j] != "("+str(c):

					br_one.insert(0,l[j])
					j-=1

				br_one.insert(0,l[j])

				br_two.append("("+str(c))
				br_two.append(l[s])
				br_two.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((l[s] == "("+str(c)) and (l[s-1] in "+-") and (var in l[s-2])) or ((l[s] == "("+str(c)) and (l[s-1] in "+-") and (is_number(l[s-2]) == True)):

				ini_two = s
				k = s
				op = l[s-1]
				br_one = []
				br_two = []

				while l[k] != ")"+str(c):

					br_two.append(l[k])
					k+=1

				br_two.append(l[k])

				br_one.append("("+str(c))
				br_one.append(l[s-2])
				br_one.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del l[s-2:k+1]
				k = s-2
				for x in br:

					l.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			s+=1
	"""
	b=0
	for s in r:

		if ("(" in s) and ("j" not in s):

			temp = s
			temp = temp.replace("(","")
			temp = int(temp)

			if temp > b:

				b = temp

	for c in range(b,1,-1):

		s=0
		while s != len(r):

			if (r[s] == "("+str(c)) and (r[s-1] in "+-") and (r[s-2] == ")"+str(c)):

				ini_two = s
				end_one = s-2
				op = r[s-1]
				k = s
				j = s-2
				br_one = []
				br_two = []

				while r[k] != ")"+str(c):

					br_two.append(r[k])
					k+=1

				br_two.append(r[k])

				while r[j] != "("+str(c):

					br_one.insert(0,r[j])
					j-=1

				br_one.insert(0,r[j])
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del r[j:k+1]
				k = j
				for x in br:

					r.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((var in r[s]) and (r[s-1] in "+-") and (r[s-2] == ")"+str(c))) or ((is_number(r[s]) == True) and (r[s-1] in "+-") and (r[s-2] == ")"+str(c))):

				end_one = s-2
				j = s-2
				op = r[s-1]
				br_one = []
				br_two = []

				while r[j] != "("+str(c):

					br_one.insert(0,r[j])
					j-=1

				br_one.insert(0,r[j])

				br_two.append("("+str(c))
				br_two.append(r[s])
				br_two.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp.insert(0,"(1")
				br_one_temp.append(")1")
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp[0] = "(1"
				br_two_temp[len(br_two_temp)-1] = ")1"
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del r[s-2:k+1]
				k = s-2
				for x in br:

					r.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			elif ((r[s] == "("+str(c)) and (r[s-1] in "+-") and (var in r[s-2])) or ((r[s] == "("+str(c)) and (r[s-1] in "+-") and (is_number(r[s-2]) == True)):

				ini_two = s
				k = s
				op = r[s-1]
				br_one = []
				br_two = []

				while r[k] != ")"+str(c):

					br_two.append(r[k])
					k+=1

				br_two.append(r[k])

				br_one.append("("+str(c))
				br_one.append(r[s-2])
				br_one.append(")"+str(c))
				
				br_one_temp = br_one[:]
				br_one_temp[0] = "(1"
				br_one_temp[len(br_one_temp)-1] = ")1"
				br_one_str = stringify(br_one_temp)
				br_two_temp = br_two[:]
				br_two_temp.insert(0,"(1")
				br_two_temp.append(")1")
				br_two_str = stringify(br_two_temp)
				
				br_og = br_one_str+op+br_two_str
				print("br_og = "+br_og)

				br = bracket_add(br_one, op, br_two, var)
				#print(br)
				br.insert(0,"("+str(c))
				br.append(")"+str(c))

				del r[s-2:k+1]
				k = s-2
				for x in br:

					r.insert(k,x)
					k+=1

				l_string = stringify(l)
				print("\n\n"+l_string)

				if br_og in l_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					l_string = l_string.replace(br_og, br)
					print("\n\n"+l_string)


				r_string = stringify(r)
				if br_og in r_string:

					br.insert(0,"(1")
					br.append(")1")
					br = stringify(br)
					r_string = r_string.replace(br_og, br)
					print("\n\n"+r_string)

				s=-1

			s+=1

	l_string = stringify(l)
	r_string = stringify(r)
	print("\n"+l_string+"\n=\n"+r_string)

	#6. Put in Standard form

	if (l[1] == "(2") and (l[len(l)-2] == ")2"):

		del l[1]
		del l[len(l)-2]
		
	if (r[1] == "(2") and (r[len(r)-2] == ")2"):

		del r[1]
		del r[len(r)-2]

	l_string = stringify(l)
	r_string = stringify(r)
	print("\n"+l_string+"\n=\n"+r_string)

	l, l_deg = grouping(l)
	r, r_deg = grouping(r)
	print(l,r)

	#If there are nth order terms on RHS, move to LHS
	v=0
	while v != len(r)-1:

		if var in r[v]:

			if r[v-1] == "-":

				if "-" in r[v]:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+r[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					l.insert(len(l)-1,"-")
					r[v]=r[v].replace('-','')
					l.insert(len(l)-1,r[v])
					del r[v]
				
					if (r[v-1] == "+") or (r[v-1] == "-"):

						del r[v-1]

					elif (r[v] == "+") or (r[v] == "-"):

						del r[v]						

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

				else:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+r[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					l.insert(len(l)-1,"+")
					l.insert(len(l)-1,r[v])
					del r[v]

					if (r[v-1] == "+") or (r[v-1] == "-"):

						del r[v-1]

					elif (r[v] == "+") or (r[v] == "-"):

						del r[v]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

			elif r[v-1] == "+":

				if "-" in r[v]:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+r[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					l.insert(len(l)-1,"+")
					r[v]=r[v].replace('-','')
					l.insert(len(l)-1,r[v])
					del r[v]

					if (r[v-1] == "+") or (r[v-1] == "-"):

						del r[v-1]

					elif (r[v] == "+") or (r[v] == "-"):

						del r[v]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

				else:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+r[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					l.insert(len(l)-1,"-")
					l.insert(len(l)-1,r[v])
					del r[v]

					if (r[v-1] == "+") or (r[v-1] == "-"):

						del r[v-1]

					elif (r[v] == "+") or (r[v] == "-"):

						del r[v]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

			else:

				if "-" in r[v]:

					#this may be a complex number, need to determine this
					temp = r[v]
					exp_loc = temp.find("^")

					if exp_loc != -1:

						print("Yoootteee")
						temp = temp[0:exp_loc-1]
						temp = complex(temp)

					else:

						print("yosemite")
						temp = temp.replace(var,'')
						temp = complex(temp)
				
					if round(temp.imag,6) == 0:

						#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+r[v])
						#print(solution[sol_cnt])
						#sol_cnt=sol_cnt+1

						l.insert(len(l)-1,"+")
						r[v]=r[v].replace('-','')
						l.insert(len(l)-1,r[v])
						del r[v]
	
						if r[v] == "+":

							del r[v]

						else:

							r[v]=r[v]+r[v+1]
							del r[v+1]

						v=0
						#print(l,r)
						string = stringify(l)
						string += "="+stringify(r)
						print(string,"\n")
						#solution.insert(sol_cnt,string)
						#sol_cnt += 1

					else:

						l.insert(len(l)-1,"-")
						l.insert(len(l)-1,r[v])
						del r[v]
	
						if r[v] == "+":

							del r[v]

						else:

							r[v]=r[v]+r[v+1]
							del r[v+1]

						v=0
						#print(l,r)
						string = stringify(l)
						string += "="+stringify(r)
						print(string,"\n")
						#solution.insert(sol_cnt,string)
						#sol_cnt += 1

				else:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+r[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					l.insert(len(l)-1,"-")
					l.insert(len(l)-1,r[v])
					del r[v]

					if r[v] == "+":

						del r[v]

					elif r[v] == "-":

						del r[v]

						if "-" in r[v]:

							r[v] = r[v].replace('-','')

						else:

							r[v] = "-"+r[v]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

		v=v+1

	#move constants from LHS to RHS

	#print(l,r)
	b=0
	v=0
	while v != len(l)-1:

		if "(" in l[v]:

			b=b+1

		if ")" in l[v]:

			b=b-1

		if (var not in l[v]) & (is_number(l[v]) == True) & (l[v-1] not in oper_dict_two.values()) & (l[v+1] not in oper_dict_two.values()): #& you're not within variable bracket range
	
			if l[v-1] == "-":

				if "-" in l[v]:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+l[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					r.insert(len(r)-1,"-")
					l[v]=l[v].replace('-','')
					r.insert(len(r)-1,l[v])
					del l[v]

					if (l[v-1] == "+") or (l[v-1] == "-"):

						del l[v-1]

					elif (l[v] == "+") or (l[v] == "-"):

						del l[v]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

				else:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+l[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					if len(r) == 2:

						r.insert(len(r)-1,l[v])
						del l[v]

					else:

						r.insert(len(r)-1,"+")
						r.insert(len(r)-1,l[v])
						del l[v]

					if (l[v-1] == "+") or (l[v-1] == "-"):

						del l[v-1]

					elif (l[v] == "+") or (l[v] == "-"):

						del l[v]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

			elif l[v-1] == "+":

				if "-" in l[v]:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+l[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					r.insert(len(r)-1,"+")
					l[v]=l[v].replace('-','')
					r.insert(len(r)-1,l[v])
					del l[v]

					if (l[v-1] == "+") or (l[v-1] == "-"):

						del l[v-1]

					elif (l[v] == "+") or (l[v] == "-"):

						del l[v]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

				else:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+l[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					if len(r) == 2:

						r.insert(len(r)-1,"-"+str(l[v]))
						del l[v]

					else:

						r.insert(len(r)-1,"-")
						r.insert(len(r)-1,l[v])
						del l[v]

					if (l[v-1] == "+") or (l[v-1] == "-"):

						del l[v-1]

					elif (l[v] == "+") or (l[v] == "-"):

						del l[v]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

			else:
						
				if "-" in l[v]:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+l[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					r.insert(len(r)-1,"+")
					l[v]=l[v].replace('-','')
					r.insert(len(r)-1,l[v])
					del l[v]

					if l[v] == "+":

						del l[v]

					else:

						l[v]=l[v]+l[v+1]
						del l[v+1]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

				else:

					#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+l[v])
					#print(solution[sol_cnt])
					#sol_cnt=sol_cnt+1

					r.insert(len(r)-1,"-")
					r.insert(len(r)-1,l[v])
					del l[v]

					if l[v] == "+":

						del l[v]

					else:

						l[v]=l[v]+l[v+1]
						del l[v+1]

					v=0
					#print(l,r)
					string = stringify(l)
					string += "="+stringify(r)
					print(string,"\n")
					#solution.insert(sol_cnt,string)
					#sol_cnt += 1

		v=v+1				
	
	#list all nth order terms for LHS

	lhs_n_order=[]
	n=0

	for s in range(0,len(l)-1):

		if var in l[s]:

			if "^" in l[s]:

				temp=str(l[s])
				t=0
				temp_two=""
				while temp[t] != "^":
					
					t=t+1

				t+=1
				while t != len(temp):

					temp_two+=temp[t]

					t+=1

				if str(temp_two) not in lhs_n_order:

					lhs_n_order.insert(n,str(temp_two))
					n=n+1

			else:

				if "1.0" not in lhs_n_order:

					lhs_n_order.insert(n,"1.0")
					n=n+1

	if len(lhs_n_order) > 1:

		#Reorder lhs_n_order to numerical order

		#print(lhs_n_order)
		new_n_order=[]
		n=0
		s=0
		while s != len(lhs_n_order):

			j=float(lhs_n_order[s])
			k=0
			t=0
			while t != len(lhs_n_order):

				if j < float(lhs_n_order[t]):

					k=1

				t=t+1

			if k!=1:

				new_n_order.insert(n,lhs_n_order[s])
				n=n+1
				del lhs_n_order[s]
				s=-1

			s=s+1

		#print("\n\n\n#!#!#!#new_n_order#!#!#!#!#",new_n_order,"\n\n\n")
		#return ans		

		#Reorder terms on LHS from largest exponent to smallest
		rear_l=[]
		n=0	
		for s in range(0,len(new_n_order)):		

			for t in range(0,len(l)):

				if float(new_n_order[s]) > 1:

					if (var in l[t]) & ("^"+str(new_n_order[s]) in l[t]):

						#print(l[t])

						temp = l[t]
						v=0
						while temp[v] != var:

							v+=1

						v += 2
						b=""
						while v != len(temp):

							b = b+str(temp[v])
							v+=1

						#print(b,new_n_order[s])
						if float(b) == float(new_n_order[s]):

							if l[t-1] == "-":
						
								if "-" in l[t]:

									if n == 0:

										rear_l.insert(n,l[t])
										n=n+1

									else:

										rear_l.insert(n,"+")
										n=n+1
										rear_l.insert(n,l[t])
										n=n+1

								else:

									rear_l.insert(n,"-")

									if n == 0:		

										rear_l[n]=rear_l[n]+l[t]
										n=n+1

									else:
			
										n=n+1
										rear_l.insert(n,l[t])
										n=n+1

							elif l[t-1] == "+":

								if "-" in l[t]:

									if n == 0:		

										rear_l.insert(n,l[t])
										n=n+1

									else:
			
										rear_l.insert(n,"-")
										n=n+1
										rear_l.insert(n,l[t])
										rear_l[n] = rear_l[n].replace('-','')
										n=n+1

								else:
							
									if n == 0:

										rear_l.insert(n,l[t])
										n=n+1

									else:

										rear_l.insert(n,"+")
										n=n+1
										rear_l.insert(n,l[t])
										n=n+1

							else:

								if "-" in l[t]:

									if n == 0:		

										rear_l.insert(n,l[t])
										n=n+1

									else:
			
										rear_l.insert(n,l[t])
										n=n+1

								else:
							
									if n == 0:

										rear_l.insert(n,l[t])
										n=n+1

									else:

										rear_l.insert(n,"+")
										n=n+1
										rear_l.insert(n,l[t])
										n=n+1

				if float(new_n_order[s]) == 1:

					if (var in l[t]) & ("^" not in l[t]):

						#print(l[t])

						if l[t-1] == "-":
						
							if "-" in l[t]:

								if n == 0:

									rear_l.insert(n,l[t])
									n=n+1

								else:

									rear_l.insert(n,"+")
									n=n+1
									rear_l.insert(n,l[t])
									n=n+1

							else:

								rear_l.insert(n,"-")

								if n == 0:		

									rear_l[n]=rear_l[n]+l[t]
									n=n+1

								else:
			
									n=n+1
									rear_l.insert(n,l[t])
									n=n+1

						elif l[t-1] == "+":

							if "-" in l[t]:

								rear_l.insert(n,"-")

								if n == 0:		

									rear_l[n]=rear_l[n]+l[t]
									n=n+1

								else:
			
									n=n+1
									rear_l.insert(n,l[t])
									n=n+1

							else:
							
								if n == 0:

									rear_l.insert(n,l[t])
									n=n+1

								else:

									rear_l.insert(n,"+")
									n=n+1
									rear_l.insert(n,l[t])
									n=n+1

						else:

							if "-" in l[t]:

								rear_l.insert(n,"-")

								if n == 0:		

									rear_l[n]=rear_l[n]+l[t]
									n=n+1

								else:
			
									n=n+1
									rear_l.insert(n,l[t])
									n=n+1

							else:
							
								if n == 0:

									rear_l.insert(n,l[t])
									n=n+1

								else:

									rear_l.insert(n,"+")
									n=n+1
									rear_l.insert(n,l[t])
									n=n+1

		rear_l.insert(0,"(1")
		rear_l.insert(len(rear_l),")1")

		#print(rear_l)

	else:

		new_n_order = lhs_n_order
		rear_l = l

	l_string = stringify(rear_l)
	print(l_string)

	for s in range(0,len(new_n_order)):		

		t=0
		while t!=len(rear_l):

			if float(new_n_order[s]) > 1:

				if rear_l[t] == "+":

					if ("^"+str(new_n_order[s]) in rear_l[t-1]) & ("^"+str(new_n_order[s]) in rear_l[t+1]):

						exp_one=""
						exp_two=""

						temp_one=str(rear_l[t-1])
						temp_two=str(rear_l[t+1])
						v=0
						x=""
						while temp_one[v] != var:

							x=x+str(temp_one[v])
							v=v+1
			
						v+=2

						while v != len(temp_one):

							exp_one+=temp_one[v]
							v+=1
						
						if x == "":

							x = "1"

						elif x == "-":

							x = "-1"

						if rear_l[t-2] == "-":

							if "-" in x:

								x = x.replace('-','')

							else:

								x = "-"+x

						x=complex(x)

						if round(x.imag,6) == 0:

							x = x.real

						v=0
						y=""
						while temp_two[v] != var:

							y=y+str(temp_two[v])
							v=v+1

						v+=2

						while v != len(temp_two):

							exp_two+=temp_two[v]
							v+=1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=complex(y)

						if round(y.imag,6) == 0:

							y = y.real

						if (float(exp_one) == float(exp_two)) and (float(exp_one) == float(new_n_order[s])) and (float(exp_two) == float(new_n_order[s])):

							z=x+y

							#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+var+"^"+str(new_n_order[s])+" + "+str(y)+var+"^"+str(new_n_order[s])+" = "+str(z)+var+"^"+str(new_n_order[s]))
							#print(solution[sol_cnt])
							#sol_cnt=sol_cnt+1

							if z.imag == 0:
	
								if z == 0.0:

									del rear_l[t-1:t+2]
									#print(rear_l,rear_l[t])
									if (rear_l[t-1] == "-") or (rear_l[t-1] == "+"):

										del rear_l[t-1]
										t=0

									elif rear_l[t] == "+":

										del rear_l[t]
										t=0

								else:
	
									rear_l[t-1]=str(z)+var+"^"+str(new_n_order[s])
									del rear_l[t:t+2]

									if (rear_l[t-2] == "-") & ("-" in rear_l[t-1]):

										rear_l[t-1] = rear_l[t-1].replace('-','')

									if (rear_l[t-2] == "-") & (z > 0):

										rear_l[t-2] = "+"

									t=0

							else:

								rear_l[t-1]=str(z)+var+"^"+str(new_n_order[s])
								del rear_l[t:t+2]
								rear_l[t-2] = "+"
								t=0

							string = stringify(rear_l)
							string += "="+stringify(r)
							print(string,"\n")

				if rear_l[t] == "-":

					if ("^"+str(new_n_order[s]) in rear_l[t-1]) & ("^"+str(new_n_order[s]) in rear_l[t+1]):

						exp_one=""
						exp_two=""

						temp_one=str(rear_l[t-1])
						temp_two=str(rear_l[t+1])
						v=0
						x=""
						while temp_one[v] != var:

							x=x+str(temp_one[v])
							v=v+1

						v+=2

						while v != len(temp_one):

							exp_one+=temp_one[v]
							v+=1

						if x == "":

							x = "1"

						elif x == "-":

							x = "-1"

						if rear_l[t-2] == "-":

							if "-" in x:

								x = x.replace('-','')

							else:

								x = "-"+x

						x=complex(x)

						if round(x.imag,6) == 0:

							x = x.real

						v=0
						y=""
						while temp_two[v] != var:

							y=y+str(temp_two[v])
							v=v+1

						v+=2

						while v != len(temp_two):

							exp_two+=temp_two[v]
							v+=1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=complex(y)

						if round(y.imag,6) == 0:

							y = y.real

						if (float(exp_one) == float(exp_two)) and (float(exp_one) == float(new_n_order[s])) and (float(exp_two) == float(new_n_order[s])):
						
							z=x-y

							#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+var+"^"+str(new_n_order[s])+" + "+str(y)+var+"^"+str(new_n_order[s])+" = "+str(z)+var+"^"+str(new_n_order[s]))
							#print(solution[sol_cnt])
							#sol_cnt=sol_cnt+1

							if z.imag == 0:

								if z == 0.0:

									del rear_l[t-1:t+2]
									if (rear_l[t-1] == "-") or (rear_l[t-1] == "+"):

										del rear_l[t-1]
										t=0

									elif rear_l[t] == "-":

										del rear_l[t]
										t=0

								else:
	
									rear_l[t-1]=str(z)+var+"^"+str(new_n_order[s])
									del rear_l[t:t+2]

									if (rear_l[t-2] == "-") & ("-" in rear_l[t-1]):

										rear_l[t-1] = rear_l[t-1].replace('-','')

									t=0

							else:

								rear_l[t-1]=str(z)+var+"^"+str(new_n_order[s])
								del rear_l[t:t+2]
								t=0

							string = stringify(rear_l)
							string += "="+stringify(r)
							print(string,"\n")

			if float(new_n_order[s]) == 1:

				if rear_l[t] == "+":

					if (var in rear_l[t-1]) & (var in rear_l[t+1]) & ("^" not in rear_l[t-1]) & ("^" not in rear_l[t+1]):

						temp_one=str(rear_l[t-1])
						temp_two=str(rear_l[t+1])
						v=0
						x=""
						while temp_one[v] != var:

							x=x+str(temp_one[v])
							v=v+1

						if x == "":

							x = "1"

						elif x == "-":

							x = "-1"

						if rear_l[t-2] == "-":

							if "-" in x:

								x = x.replace('-','')

							else:

								x = "-"+x

						x=complex(x)

						if round(x.imag,6) == 0:

							x = x.real

						v=0
						y=""
						while temp_two[v] != var:

							y=y+str(temp_two[v])
							v=v+1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"
						print("y = "+y)
						y=complex(y)

						if round(y.imag,6) == 0:

							y = y.real

						z=x+y						

						#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+var+" + "+str(y)+var+" = "+str(z)+var)
						#print(solution[sol_cnt])
						#sol_cnt=sol_cnt+1

						if z.imag == 0:
	
							if z == 0.0:

								del rear_l[t-1:t+2]
								if (rear_l[t-1] == "-") or (rear_l[t-1] == "+"):

									del rear_l[t-1]
									t=0

								elif rear_l[t] == "+":

									del rear_l[t]
									t=0

							else:
	
								rear_l[t-1]=str(z)+var
								del rear_l[t:t+2]

								if (rear_l[t-2] == "-") & ("-" in rear_l[t-1]):

									rear_l[t-1] = rear_l[t-1].replace('-','')

								t=0

						else:

							rear_l[t-1]=str(z)+var
							del rear_l[t:t+2]
							t=0

						string = stringify(rear_l)
						string += "="+stringify(r)
						print(string,"\n")

				if rear_l[t] == "-":

					if (var in rear_l[t-1]) & (var in rear_l[t+1]) & ("^" not in rear_l[t-1]) & ("^" not in rear_l[t+1]):

						temp_one=str(rear_l[t-1])
						temp_two=str(rear_l[t+1])
						v=0
						x=""
						while temp_one[v] != var:

							x=x+str(temp_one[v])
							v=v+1

						if x == "":

							x = "1"

						elif x == "-":

							x = "-1"

						if rear_l[t-2] == "-":

							if "-" in x:

								x = x.replace('-','')

							else:

								x = "-"+x

						x=complex(x)

						if round(x.imag,6) == 0:

							x = x.real

						v=0
						y=""
						while temp_two[v] != var:

							y=y+str(temp_two[v])
							v=v+1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=complex(y)

						if round(y.imag,6) == 0:

							y = y.real

						z=x-y

						#solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+var+" + "+str(y)+var+" = "+str(z)+var)
						#print(solution[sol_cnt])
						#sol_cnt=sol_cnt+1

						if z.imag == 0:

							if z == 0.0:

								del rear_l[t-1:t+2]
								if (rear_l[t-1] == "-") or (rear_l[t-1] == "+"):

									del rear_l[t-1]
									t=0

								elif (rear_l[t-2] == "-") or (rear_l[t-2] == "+"):

									del rear_l[t-2]
									t=0

								elif rear_l[t] == "-":

									del rear_l[t]
									t=0

							else:
	
								rear_l[t-1]=str(z)+var
								del rear_l[t:t+2]
							
								if (rear_l[t-2] == "-") & ("-" in rear_l[t-1]):

									rear_l[t-1] = rear_l[t-1].replace('-','')

								t=0

						else:

							rear_l[t-1]=str(z)+var
							del rear_l[t:t+2]
							t=0

						string = stringify(rear_l)
						string += "="+stringify(r)
						print(string,"\n")

			t=t+1

	r, useless = grouping(r)
	print(r)
	right_side=calculate(r,0)

	r.clear()
	r.insert(0,"(1")
	r.insert(1,str(right_side))
	r.insert(2,")1")

	l_string = stringify(rear_l)
	r_string = stringify(r)

	print("\n\n"+l_string+"="+r_string)	

	#7. Solve

	solution=[]
	sol_cnt=0

	if float(new_n_order[0]) == 1:

		n=0
		while n != len(rear_l):

			if var in rear_l[n]:

				value = rear_l[n]
				value = value.replace(var,'')
				if value == '':

					value = 1+0j

				else:

					value = complex(value)
				

				if round(value.imag,6) == 0:

					value = value.real

				other_value = complex(r[1])

				if round(other_value.imag,6) == 0:

					other_value = other_value.real

				r[1] = other_value/value
				r[1] = str(r[1])
				rear_l[n] = var
				l_string = stringify(rear_l)
				r_string = stringify(r)
				print(l_string+" = "+r_string)
				
			n+=1

		if (len(rear_l) == 3) and (rear_l[1] == var):

			ans = []
			temp = complex(r[1])

			if round(temp.imag,6) == 0:

				temp = temp.real

			ans.append(temp)

	elif float(new_n_order[0]) == 2:

		if "-" in r[1]:

			r[1] = r[1].replace('-','')
			rear_l.insert(len(rear_l)-1,"+")
			rear_l.insert(len(rear_l)-1,r[1])
			r[1] = "0"

		else:

			rear_l.insert(len(rear_l)-1,"-")
			rear_l.insert(len(rear_l)-1,r[1])
			r[1] = "0"

		#Quadratic Formula

		rear_l = Poly_Func(rear_l)
		coeff = rear_l.get_coeff(int(new_n_order[0]),var)
		ans, solution, sol_cnt = coeff.quadratic(solution, sol_cnt)

		for s in range(0,len(ans)):

			#ans[s] = round(ans[s].real,6)+(round(ans[s].imag,6))*1j

			if round(ans[s].imag,6) == 0:

				ans[s] = ans[s].real	

		#return ans

	#3rd or polynomial

	elif float(new_n_order[0]) == 3:

		if "-" in r[1]:

			r[1] = r[1].replace('-','')
			rear_l.insert(len(rear_l)-1,"+")
			rear_l.insert(len(rear_l)-1,r[1])
			r[1] = "0"

		else:

			rear_l.insert(len(rear_l)-1,"-")
			rear_l.insert(len(rear_l)-1,r[1])
			r[1] = "0"

		#Cubic Function Formula

		rear_l = Poly_Func(rear_l)
		coeff = rear_l.get_coeff(int(new_n_order[0]),var)
		ans, solution, sol_cnt = coeff.cardano(solution, sol_cnt)

		for s in range(0,len(ans)):

			#ans[s] = round(ans[s].real,6)+(round(ans[s].imag,6))*1j

			if round(ans[s].imag,6) == 0:

				ans[s] = ans[s].real

		#return ans		

	#Ferrari's Method
	elif float(new_n_order[0]) == 4:

		if "-" in r[1]:

			r[1] = r[1].replace('-','')
			rear_l.insert(len(rear_l)-1,"+")
			rear_l.insert(len(rear_l)-1,r[1])
			r[1] = "0"

		else:

			rear_l.insert(len(rear_l)-1,"-")
			rear_l.insert(len(rear_l)-1,r[1])
			r[1] = "0"

		rear_l = Poly_Func(rear_l)
		coeff = rear_l.get_coeff(int(new_n_order[0]),var)
		#print(coeff.eqn)
		ans, solution, sol_cnt = coeff.ferrari(solution, sol_cnt)

		for s in range(0,len(ans)):

			#ans[s] = round(ans[s].real,6)+(round(ans[s].imag,6))*1j

			if round(ans[s].imag,6) == 0:

				ans[s] = ans[s].real
		
		#return ans		

	#For any polynomial of nth degree where n>=5
	else:

		if "-" in r[1]:

			r[1] = r[1].replace('-','')
			rear_l.insert(len(rear_l)-1,"+")
			rear_l.insert(len(rear_l)-1,r[1])
			r[1] = "0"

		else:

			rear_l.insert(len(rear_l)-1,"-")
			rear_l.insert(len(rear_l)-1,r[1])
			r[1] = "0"

		#print(new_n_order[0])

		rear_l = Poly_Func(rear_l)
		coeff=rear_l.get_coeff(int(float(new_n_order[0])),var)
		test=rear_l.get_coeff(int(float(new_n_order[0])),var)
		test_two=rear_l.get_coeff(int(float(new_n_order[0])),var)
		coeff=coeff.eqn
		
		#print("coeff before JT",coeff)
		print("Checking if 0 is a root via synthetic division...\n")
		solution.insert(sol_cnt,"Checking if 0 is a root via synthetic division...")
		sol_cnt+=1
		solution.insert(sol_cnt,"")
		sol_cnt+=1
		solution.insert(sol_cnt,"")
		sol_cnt+=1

		test = test.lin_divide([1,0])
		test_two = test_two.lin_divide([1,0])
		remainder = test.eqn[len(test.eqn)-1]

		del test_two.eqn[len(test_two.eqn)-1]

		test_temp = test_two.stringify(var)

		if remainder < 0:

			test_temp += str(remainder)+"/"+var

		else:

			test_temp += "+"+str(remainder)+"/"+var

		string = stringify(rear_l.eqn)
		string += "="+stringify(r)
		string = string.replace('=0','')
		print("("+string+")/"+var+" = "+test_temp+"\n")
		solution.insert(sol_cnt,"("+string+")/"+var+" = "+test_temp)
		sol_cnt+=1
		solution.insert(sol_cnt,"")
		sol_cnt+=1
		solution.insert(sol_cnt,"")
		sol_cnt+=1

		if test.eqn[len(test.eqn)-1] == 0:

			success_attempt = False
			ans=[]
			i = 1
			while success_attempt == False:

				if len(test.eqn)-2 >= 5:

					try:
						del test.eqn[len(test.eqn)-1]
						coeff=test.eqn
						#print(coeff)
						ans = jenkins_traub.real_poly(coeff,int(float(new_n_order[0]))-i)

					except ZeroDivisionError:

						string = test.stringify(var)

						test = test.lin_divide([1,0])
						
						print("0 might be a repeated root, trying again...\n")
						solution.insert(sol_cnt,"0 might be a repeated root, trying again...")
						sol_cnt+=1
						solution.insert(sol_cnt,"")
						sol_cnt+=1
						solution.insert(sol_cnt,"")
						sol_cnt+=1

						test_two = test_two.lin_divide([1,0])
						remainder = test.eqn[len(test.eqn)-1]

						del test_two.eqn[len(test_two.eqn)-1]

						test_temp = test_two.stringify(var)

						if remainder < 0:

							test_temp += str(remainder)+"/"+var

						else:

							test_temp += "+"+str(remainder)+"/"+var

						print("("+string+")/"+var+" = "+test_temp+"\n")
						solution.insert(sol_cnt,"("+string+")/"+var+" = "+test_temp)
						sol_cnt+=1
						solution.insert(sol_cnt,"")
						sol_cnt+=1
						solution.insert(sol_cnt,"")
						sol_cnt+=1

						i += 1

					else:

						success_attempt = True
						print("Success! 0 is a root\n")
						solution.insert(sol_cnt,"Success! 0 is a root")
						sol_cnt+=1
						solution.insert(sol_cnt,"")
						sol_cnt+=1
						solution.insert(sol_cnt,"")
						sol_cnt+=1

				elif len(test.eqn)-2 == 4:

					del test.eqn[len(test.eqn)-1]
					ans, solution, sol_cnt = test.ferrari(solution,sol_cnt)
					success_attempt = True

				else:

					break

			for s in range(1,i+1):

				ans.insert(0,0)
					

		else:

			print("0 is not a root\n")
			solution.insert(sol_cnt,"0 is not a root")
			sol_cnt+=1

			ans = jenkins_traub.real_poly(coeff,int(float(new_n_order[0])))

		print(ans)

		for i in range(0,len(ans)):

			#ans[i] = round(ans[i].real,6)+(round(ans[i].imag,6))*1j

			if round(ans[i].imag,5) == 0:
			
				ans[i] = ans[i].real
	
	#Last thing is removing asymptotes from the answers

	print(asymptote)
	for i in asymptote:

		asy = complex(i[0])
		print(asy)
		k=0
		while k != len(ans):

			#print(round(ans[k].real,2)+round(ans[k].imag,2)*1j, asy, round(ans[k].real,2)+round(ans[k].imag,2)*1j == asy)
			if round(ans[k].real,1)+round(ans[k].imag,1)*1j == asy:

				#print("Deleting "+str(ans[k]))
				del ans[k]
				k=-1

			k+=1

	print("Ans leaving solving", ans)
	return ans
	 					

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

				l_new_string = stringify(l_new)
				r_new_string = stringify(r_new)

				l_new, work_var = bracketify(l_new_string)
				r_new, work_var = bracketify(r_new_string)

				l_new, l_deg = grouping(l_new)
				r_new, r_deg = grouping(r_new)

				if l_deg[0] > r_deg[0]:

					work_deg = l_deg[0]

				elif l_deg[0] < r_deg[0]:

					work_deg = r_deg[0]

				else:

					work_deg = l_deg[0]

				ans = solving(l_new, r_new, work_var[0], work_deg)

			else:

				#solve and keep resubbing
				while work_var != var_type[0]:

					if any(isinstance(sub, list) for sub in r_new) == True:

						l_new_string = stringify(l_new)
						l_new, work_var = bracketify(l_new_string)
						l_new, work_deg = grouping(l_new)

						ans=[]
						for i in r_new:

							temp_string = stringify(i)
							temp, temp_var = bracketify(temp_string)
							temp, temp_deg = grouping(temp)

							ans_temp = solving(l_new, temp, work_var[0], work_deg[0])
							ans.append(ans_temp)

					else:

						l_new_string = stringify(l_new)
						r_new_string = stringify(r_new)
	
						l_new, work_var = bracketify(l_new_string)
						r_new, work_var = bracketify(r_new_string)

						l_new, l_deg = grouping(l_new)
						r_new, r_deg = grouping(r_new)

						if l_deg[0] > r_deg[0]:

							work_deg = l_deg[0]

						elif l_deg[0] < r_deg[0]:

							work_deg = r_deg[0]

						else:

							work_deg = l_deg[0]

						ans = solving(l_new, r_new, work_var[0], work_deg)

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

							ans_temp = solving(l_new, temp, work_var[0], work_deg[0])
							ans.append(ans_temp)
						
					else:

						l_new_string = stringify(l_new)
						r_new_string = stringify(r_new)

						l_new, work_var = bracketify(l_new_string)
						r_new, work_var = bracketify(r_new_string)

						l_new, l_deg = grouping(l_new)
						r_new, r_deg = grouping(r_new)

						if l_deg[0] > r_deg[0]:

							work_deg = l_deg[0]

						elif l_deg[0] < r_deg[0]:

							work_deg = r_deg[0]

						else:

							work_deg = l_deg[0]

						ans = solving(l_new, r_new, work_var[0], work_deg)

					l_new_string = work_var[0]
					print("bottle caps", l_new_string)
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
				
				l_og_string = stringify(l_og)
				l_og, l_var = bracketify(l_og_string)
				l_og, l_deg = grouping(l_og)
	
				r_og_string = stringify(r_og)
				r_og, r_var = bracketify(r_og_string)
				r_og, r_deg = grouping(r_og)

				if l_deg[0] > r_deg[0]:

					work_deg = l_deg[0]

				elif r_deg[0] > l_deg[0]:

					work_deg = r_deg[0]

				else:

					work_deg = l_deg[0]
	 
				ans = solving(l_og, r_og, var_type[0], work_deg)

				l_new, l_var = bracketify(var_type[0])

				r_new=[]
				for i in ans:

					temp, temp_var = bracketify(str(i))
					temp, temp_deg = grouping(temp)
					r_new.append(temp)

	else:

		l_og_string = stringify(l_og)
		l_og, l_var = bracketify(l_og_string)
		l_og, l_deg = grouping(l_og)
	
		r_og_string = stringify(r_og)
		r_og, r_var = bracketify(r_og_string)
		r_og, r_deg = grouping(r_og)

		if l_deg[0] > r_deg[0]:

			work_deg = l_deg[0]

		elif r_deg[0] > l_deg[0]:

			work_deg = r_deg[0]

		else:

			work_deg = l_deg[0]
	 
		ans = solving(l_og, r_og, var_type[0], work_deg)

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


		


					








