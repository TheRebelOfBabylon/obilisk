import math
import cmath
import os
import psutil
import calculus
from algebra import *
import jenkins_traub

process = psutil.Process(os.getpid())
beginning = process.memory_info().rss

solution=[]
sol_cnt=0
var_type=[]

oper_dict = {
	
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
	26 : "SQRT"

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

#To detect divisions by zero
def div_check(x,y):

	try:
		x/y

	except ZeroDivisionError:

		return True

	else:

		return False

def operation(num_one,oper,num_two):

	operation_ans = 0

	if oper == "^":

		operation_ans = num_one**num_two

	elif oper == "/":

		#Check if division by zero
		if div_check(num_one,num_two) == True:

			operation_ans = math.inf

		else:

			operation_ans = num_one/num_two

	elif oper == "*":

		operation_ans = num_one*num_two

	elif oper == "+":
				
		operation_ans = num_one+num_two

	elif oper == "-":

		operation_ans = num_one-num_two

	elif oper == "SIN":
		
		num_two = math.radians(num_two)
		operation_ans = round(math.sin(num_two),7)

	elif oper == "COS":
		
		num_two = math.radians(num_two)
		operation_ans = round(math.cos(num_two),7)

	elif oper == "TAN":
		
		num_two = math.radians(num_two)
		operation_ans = round(math.tan(num_two),7)

	elif oper == "SEC":
		
		num_two = math.radians(num_two)
		if div_check(1,round(math.cos(num_two),7)) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(1/math.cos(num_two),7)

	elif oper == "CSC":
		
		num_two = math.radians(num_two)
		if div_check(1,round(math.sin(num_two),7)) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(1/math.sin(num_two),7)

	elif oper == "COT":
		
		num_two = math.radians(num_two)
		if div_check(1,round(math.tan(num_two),7)) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(1/math.tan(num_two),7)

	elif oper == "ASIN":
		
		operation_ans = math.asin(num_two)
		operation_ans = round(math.degrees(operation_ans),7)

	elif oper == "ACOS":
		
		operation_ans = math.acos(num_two)
		operation_ans = round(math.degrees(operation_ans),7)

	elif oper == "ATAN":
		
		operation_ans = math.atan(num_two)
		operation_ans = round(math.degrees(operation_ans),7)

	elif oper == "ASEC":
		
		if div_check(1,num_two) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(math.degrees(math.acos(1/num_two)),7)

	elif oper == "ACSC":
		
		if div_check(1,num_two) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(math.degrees(math.asin(1/num_two)),7)

	elif oper == "ACOT":
		
		if div_check(1,num_two) == True:

			operation_ans = round(math.degrees(math.atan(math.inf)),7)

		else:

			operation_ans = round(math.degrees(math.atan(1/num_two)),7)

	elif oper == "SINH":
		
		operation_ans = round(math.sinh(num_two),7)

	elif oper == "COSH":
		
		operation_ans = round(math.cosh(num_two),7)

	elif oper == "TANH":
		
		operation_ans = round(math.tanh(num_two),7)

	elif oper == "SECH":
		
		if div_check(1,round(math.cosh(num_two),7)) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(1/math.cosh(num_two),7)

	elif oper == "CSCH":
		
		if div_check(1,round(math.sinh(num_two),7)) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(1/math.sinh(num_two),7)

	elif oper == "COTH":
		
		if div_check(1,round(math.tanh(num_two),7)) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(1/math.tanh(num_two),7)

	elif oper == "ASINH":
		
		operation_ans = round(math.asinh(num_two),7)

	elif oper == "ACOSH":
		
		operation_ans = round(math.acosh(num_two),7)

	elif oper == "ATANH":
		
		operation_ans = round(math.atanh(num_two),7)

	elif oper == "ASECH":
		
		if div_check(1,num_two) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(math.acosh(1/num_two),7)

	elif oper == "ACSCH":
		
		if div_check(1,num_two) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(math.asinh(1/num_two),7)

	elif oper == "ACOTH":
		
		if div_check(1,num_two) == True:

			operation_ans = math.inf

		else:

			operation_ans = round(math.atanh(1/num_two),7)

	elif oper == "LN":

		operation_ans = math.log(num_two)

	elif oper == "LOG":

		operation_ans = math.log(num_two,num_one)

	elif oper == "SQRT":

		operation_ans = cmath.sqrt(num_two)
	
	return operation_ans

def calculate(n,b):
	
	op="0"
	oper="x"
	y=0
	z=0
	t=0
	bracket=[]
	calc=0.0
	brack_num=0
	length=len(n)
	global sol_cnt, solution, oper_dict

	while t <= (length-1):

			#print(t,n[t],length)
			
			if "(" in n[t]:
				
				b=b+1
				brack_num=")"+str(b)
				y=t+1
				while brack_num not in n[y]:

					bracket.insert(z,n[y])
					z=z+1
					y=y+1

				del n[(t+1):(t+len(bracket)+2)]
				length=len(n)
				#print(n,bracket,length)
				n[t]=str(calculate(bracket,b))
				#print(n)
				b=b-1
				bracket.clear()

			t=t+1
	
	#for loop to walk list of operations
	for s in oper_dict.values():

		op=s
		
		#while loop to walk the inputted array
		t=0
		while t <= (length-1):
			#print(s,t,n[t],length)

			if length == 1:

				calc=n[t]

			if n[t] == op:

				if (n[t] == "SIN") or (n[t] == "COS") or (n[t] == "TAN") or (n[t] == "ASIN") or (n[t] == "ACOS") or (n[t] == "ATAN") or (n[t] == "SINH") or (n[t] == "COSH") or (n[t] == "TANH") or (n[t] == "SECH") or (n[t] == "CSCH") or (n[t] == "COTH") or (n[t] == "ASINH") or (n[t] == "ACOSH") or (n[t] == "ATANH") or (n[t] == "LN") or (n[t] == "SQRT"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "SEC"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = 1/COS("+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "CSC"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = 1/SIN("+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "COT"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = 1/TAN("+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ASEC"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ACOS(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACSC"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ASIN(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACOT"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ATAN(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ASECH"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ACOSH(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACSCH"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ASINH(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACOTH"):

					calc = operation(0,op,float(n[t+1]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ATANH(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "LOG"):

					calc = operation(float(n[t+1]),op,float(n[t+2]))
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ Log of "+n[t+2]+" to the base of "+n[t+1]+" = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1:t+3]
					#print(n)
					length=len(n)

			t=t+1

	#After resolving complex calculations, now to resolve ^*/+-
	for s in range (0,3):

		if s == 0:

			op = "^"
			op1 = ""

		elif s == 1:

			op = "*"
			op1 = "/"

		elif s == 2:

			op = "+"
			op1 = "-"

		t=0
		while t <= length-1:
			
			if n[t] == op:
				
				calc = operation(float(n[t-1]),op,float(n[t+1]))
				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+n[t-1]+op+n[t+1]+" = "+str(calc))
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1
				n[t-1] = str(calc)
				del n[t:t+2]
				t=t-1 #line added to make sure all ops are performed
				length=len(n)
				#print(n, calc)

			elif n[t] == op1:

				calc = operation(float(n[t-1]),op1,float(n[t+1]))
				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+n[t-1]+op1+n[t+1]+" = "+str(calc))
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1
				n[t-1] = str(calc)
				del n[t:t+2]
				t=t-1 #line added to make sure all ops are performed
				length=len(n)
				#print(n, calc)

			t = t+1

	return calc

def simplify(eqn):

	s=0
	b=1
	k=0
	temp=[]
	while s != len(eqn):

		#add logic for dealing with trig operations, log, ln

		if ("(" in eqn[s]) & (str(b) not in eqn[s]):
	
			#we are inside a bracket
			b=b+1
			t=s+1
			var_check = 0

			#while we aren't at the close bracket
			while (")"+str(b)) not in eqn[t]:
			
				if var_check != 1:
					
					temp.insert(k,str(eqn[t]))
					k=k+1

				#if the variable is within the brackets
				if (eqn[t].isalpha() == True) & (len(eqn[t]) == 1):

					var_check = 1
					temp.clear()

				t=t+1
			
			if var_check == 0:

				if len(temp) > 1:
					
					eqn[s]=str(calculate(temp, b))
					del eqn[s+1:t+1]
					b=b-1

			else:
				
				s=t	
				b=b-1

		s=s+1

	return eqn

def is_number(s):

	try:
			
		float(s)
		return True

	except ValueError:
		
		return False

def has_numbers(s):

	return any(char.isdigit() for char in s)

def is_even(s):

	if s % 2 == 0:

		return True

	else:

		return False

def cube_root(x):

	print(x)

	if isinstance(x, complex):

		return x**(1/3)
	
	else:

		if x >= 0.0:

			return x**(1/3)

		else:

			return -(-x)**(1/3)

def stringify(l,r):

	temp=""
	for s in range(1,len(l)-1):

		if "(" in str(l[s]):
		
			temp += "("

		elif ")" in str(l[s]):
	
			temp += ")"

		else:

			temp=temp+str(l[s])

	temp = temp + "="

	for s in range(1,len(r)-1):

		if "(" in str(r[s]):
		
			temp += "("

		elif ")" in str(r[s]):
	
			temp += ")"

		else:

			temp=temp+str(r[s])

	return temp

def isolate(l, r, lvl):

	global var_index_l, var_index_r, var_type, oper_dict_two, solution, sol_cnt
	
	op=""
	op1=""

	#print(l,r)

	#Simplify both sides of equation
	
	simp_l = simplify(l)
	simp_r = simplify(r)	

	#Grouping
	#LHS
	bracket=["0"]
	bracket_temp=""
	b=0
	b_open = 0
	b_close = 0
	s=0
	simp_l.insert(len(simp_l),"0")
	simp_l.insert(len(simp_l)+1,"0")
	while s != len(simp_l)-2:

		if "(" in simp_l[s]:

			b += 1
			i = s
			b_open += 1

		if ")" in simp_l[s]:

			b -= 1
			b_close += 1


		if var_type[0] in simp_l[s]:

			#We have a variable inside a bracket expression
			if (b > 1) & (b_open != b_close):

				if bracket[0] == "0":
	
					bracket[0] = "("+str(b)
					bracket_temp="("
					z = i+1
					while ")" not in simp_l[z]:

						#print(simp_l[z])
						if "(" in simp_l[z]:

							bracket_temp += "("

						if ")" in simp_l[z]:

							bracket_temp += ")"

						else:

							bracket_temp += simp_l[z] 
							bracket.append(str(simp_l[z]))
							z += 1

					bracket.append(")"+str(b))
					bracket_temp += ")"
					#print("bracket",bracket)
					simp_l[i] = var_type[0]
					del simp_l[i+1:z+1]
					s=-1
					b=0
					b_open = 0
					b_close = 0
					#print("4",simp_l)
	
				else:

					b_temp=["("+str(b)]
					z = i+1
					while ")" not in simp_l[z]:

						#print(simp_l[z])
						b_temp.append(str(simp_l[z]))
						z += 1

					b_temp.append(")"+str(b))
					#print(b_temp)
					simp_l[i] = var_type[0]
					del simp_l[i+1:z+1]

					for j in range(0,len(b_temp)):

						if var_type[0] in b_temp[j]:

							del b_temp[j]
							#print(b_temp)
							for l in range(len(bracket)-1,0,-1):

								b_temp.insert(j,bracket[l])
								#print(b_temp)
							
							b_temp.insert(j,bracket[0])
							break

					bracket = b_temp
					bracket_temp = ""
					for s in range(0,len(bracket)):

						if "(1" in bracket[s]:

							pass

						elif ")1" in bracket[s]:

							pass

						elif "(" in bracket[s]:

							bracket_temp += "("

						elif ")" in bracket[s]:

							bracket_temp += ")"

						else:

							bracket_temp += bracket[s]

					#print("bracket",bracket)
					s=-1
					b=0
					b_open = 0
					b_close = 0
					#print("5",simp_l)

			#combining x with ^ and exponents
			if (simp_l[s+1] == "^") & (is_number(simp_l[s+2]) == True):

				simp_l[s] = str(simp_l[s])+str(simp_l[s+1])+str(simp_l[s+2])
				del simp_l[s+1:s+3]
				#print("1",simp_l)
				s=-1
				b=0
				b_open = 0
				b_close = 0
			
				# combining x^# with constant in front of it
			if (s != -1) & (is_number(simp_l[s-1]) == True):

				simp_l[s-1] = str(simp_l[s-1])+str(simp_l[s])
				del simp_l[s]
				#print("2",simp_l)
				s=-1
				b=0
				b_open = 0
				b_close = 0

				# combining x^# with constant in front of it
			if (s != -1) & (simp_l[s-1] == "*") & (is_number(simp_l[s-2]) == True):

				simp_l[s-2] = str(simp_l[s-2])+str(simp_l[s])
				del simp_l[s-1:s+1]
				#print("3",simp_l)
				s=-1
				b=0
				b_open = 0
				b_close = 0

		s=s+1

	#print(simp_l)
	del simp_l[len(simp_l)-2:len(simp_l)]
	#print(simp_l)

	if bracket_temp != "":

		solution.insert(sol_cnt,"-- Substituting "+bracket_temp+" for "+var_type[0]+" --")
		print("")
		print(solution[sol_cnt])
		sol_cnt=sol_cnt+1
		solution.insert(sol_cnt,"")
		sol_cnt+=1

		temp=""
		for s in range(0,len(simp_l)):

			if "(1" in simp_l[s]:

				pass

			elif ")1" in simp_l[s]:

				pass

			elif "(" in simp_l[s]:

				temp += "("

			elif ")" in simp_l[s]:

				temp += ")"

			else:

				temp += simp_l[s]

		temp += "="
		for s in range(0,len(simp_r)):

			if "(1" in simp_r[s]:

				pass

			elif ")1" in simp_r[s]:

				pass

			elif "(" in simp_r[s]:

				temp += "("

			elif ")" in simp_r[s]:

				temp += ")"

			else:

				temp += simp_r[s]

		solution.insert(sol_cnt,temp)
		print(solution[sol_cnt],"\n")
		sol_cnt=sol_cnt+1

	#RHS
	bracket_r=[]
	bracket_temp_r=""
	b=0
	b_open = 0
	b_close = 0
	s=0
	simp_r.insert(len(simp_r),"0")
	simp_r.insert(len(simp_r)+1,"0")
	while s != len(simp_r)-2:

		if "(" in simp_r[s]:

			b += 1
			i = s
			b_open += 1

		if ")" in simp_r[s]:

			b -= 1
			b_close += 1

		if var_type[0] in simp_r[s]:

			#We have a variable inside a bracket expression
			if (b > 1) & (b_open != b_close):

				if bracket_r[0] == "0":
	
					bracket_r[0] = "("+str(b)
					bracket_temp_r="("
					z = i+1
					while ")" not in simp_r[z]:

						#print(simp_r[z])
						if "(" in simp_r[z]:

							bracket_temp_r += "("

						if ")" in simp_r[z]:

							bracket_temp_r += ")"

						else:

							bracket_temp_r += simp_r[z] 
							bracket_r.append(str(simp_r[z]))
							z += 1

					bracket_r.append(")"+str(b))
					bracket_temp_r += ")"
					#print("bracket",bracket)
					simp_r[i] = var_type[0]
					del simp_r[i+1:z+1]
					s=-1
					b=0
					b_open = 0
					b_close = 0
					#print("4",simp_l)
	
				else:

					b_temp=["("+str(b)]
					z = i+1
					while ")" not in simp_r[z]:

						#print(simp_r[z])
						b_temp.append(str(simp_r[z]))
						z += 1

					b_temp.append(")"+str(b))
					#print(b_temp)
					simp_r[i] = var_type[0]
					del simp_r[i+1:z+1]

					for j in range(0,len(b_temp)):

						if var_type[0] in b_temp[j]:

							del b_temp[j]
							#print(b_temp)
							for l in range(len(bracket_r)-1,0,-1):

								b_temp.insert(j,bracket_r[l])
								#print(b_temp)
							
							b_temp.insert(j,bracket_r[0])
							break

					bracket_r = b_temp
					bracket_temp_r = ""
					for s in range(0,len(bracket_r)):

						if "(1" in bracket_r[s]:

							pass

						elif ")1" in bracket_r[s]:

							pass

						elif "(" in bracket_r[s]:

							bracket_temp_r += "("

						elif ")" in bracket_r[s]:

							bracket_temp_r += ")"

						else:

							bracket_temp_r += bracket_r[s]

					#print("bracket",bracket_r)
					s=-1
					b=0
					b_open = 0
					b_close = 0
					#print("5",simp_l)

			if (simp_r[s+1] == "^") & (is_number(simp_r[s+2]) == True):

				simp_r[s] = str(simp_r[s])+str(simp_r[s+1])+str(simp_r[s+2])
				del simp_r[s+1:s+3]
				s=0
			
			if is_number(simp_r[s-1]) == True:

				simp_r[s-1] = str(simp_r[s-1])+str(simp_r[s])
				del simp_r[s]
				s=0

			
			if (simp_r[s-1] == "*") & (is_number(simp_r[s-2]) == True):

				simp_r[s-2] = str(simp_r[s-2])+str(simp_r[s])
				del simp_r[s-1:s+1]
				s=0

		s=s+1

	del simp_r[len(simp_r)-2:len(simp_r)]

	if bracket_temp_r != "":

		solution.insert(sol_cnt,"-- Substituting "+bracket_temp_r+" for "+var_type[0]+" --")
		print("")
		print(solution[sol_cnt])
		sol_cnt=sol_cnt+1

		temp=""
		for s in range(0,len(simp_l)):

			if "(1" in simp_l[s]:

				pass

			elif ")1" in simp_l[s]:

				pass

			elif "(" in simp_l[s]:

				temp += "("

			elif ")" in simp_l[s]:

				temp += ")"

			else:

				temp += simp_l[s]

		temp += "="
		for s in range(0,len(simp_r)):

			if "(1" in simp_r[s]:

				pass

			elif ")1" in simp_r[s]:

				pass

			elif "(" in simp_r[s]:

				temp += "("

			elif ")" in simp_r[s]:

				temp += ")"

			else:

				temp += simp_r[s]

		solution.insert(sol_cnt,temp)
		print(solution[sol_cnt],"\n")
		sol_cnt=sol_cnt+1

	#print(simp_l,simp_r)
	
	#If there are nth order terms on RHS, move to LHS
	v=0
	while v != len(simp_r)-1:

		if var_type[0] in simp_r[v]:

			if simp_r[v-1] == "-":

				if "-" in simp_r[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+simp_r[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_l.insert(len(simp_l)-1,"-")
					simp_r[v]=simp_r[v].replace('-','')
					simp_l.insert(len(simp_l)-1,simp_r[v])
					del simp_r[v]
				
					if (simp_r[v-1] == "+") or (simp_r[v-1] == "-"):

						del simp_r[v-1]

					elif (simp_r[v] == "+") or (simp_r[v] == "-"):

						del simp_r[v]						

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+simp_r[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_l.insert(len(simp_l)-1,"+")
					simp_l.insert(len(simp_l)-1,simp_r[v])
					del simp_r[v]

					if (simp_r[v-1] == "+") or (simp_r[v-1] == "-"):

						del simp_r[v-1]

					elif (simp_r[v] == "+") or (simp_r[v] == "-"):

						del simp_r[v]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

			elif simp_r[v-1] == "+":

				if "-" in simp_r[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_r[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_l.insert(len(simp_l)-1,"+")
					simp_r[v]=simp_r[v].replace('-','')
					simp_l.insert(len(simp_l)-1,simp_r[v])
					del simp_r[v]

					if (simp_r[v-1] == "+") or (simp_r[v-1] == "-"):

						del simp_r[v-1]

					elif (simp_r[v] == "+") or (simp_r[v] == "-"):

						del simp_r[v]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_r[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_l.insert(len(simp_l)-1,"-")
					simp_l.insert(len(simp_l)-1,simp_r[v])
					del simp_r[v]

					if (simp_r[v-1] == "+") or (simp_r[v-1] == "-"):

						del simp_r[v-1]

					elif (simp_r[v] == "+") or (simp_r[v] == "-"):

						del simp_r[v]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

			else:
				
				if "-" in simp_r[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_r[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_l.insert(len(simp_l)-1,"+")
					simp_r[v]=simp_r[v].replace('-','')
					simp_l.insert(len(simp_l)-1,simp_r[v])
					del simp_r[v]
	
					if simp_r[v] == "+":

						del simp_r[v]

					else:

						simp_r[v]=simp_r[v]+simp_r[v+1]
						del simp_r[v+1]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_r[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_l.insert(len(simp_l)-1,"-")
					simp_l.insert(len(simp_l)-1,simp_r[v])
					del simp_r[v]

					if simp_r[v] == "+":

						del simp_r[v]

					elif simp_r[v] == "-":

						del simp_r[v]

						if "-" in simp_r[v]:

							simp_r[v] = simp_r[v].replace('-','')

						else:

							simp_r[v] = "-"+simp_r[v]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

		v=v+1

	#move constants from LHS to RHS

	#print(simp_l,simp_r)
	b=0
	v=0
	while v != len(simp_l)-1:

		if "(" in simp_l[v]:

			b=b+1

		if ")" in simp_l[v]:

			b=b-1

		if (var_type[0] not in simp_l[v]) & (is_number(simp_l[v]) == True) & (simp_l[v-1] not in oper_dict_two.values()) & (simp_l[v+1] not in oper_dict_two.values()) & (b==lvl): #& you're not within variable bracket range
	
			if simp_l[v-1] == "-":

				if "-" in simp_l[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+simp_l[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_r.insert(len(simp_r)-1,"-")
					simp_l[v]=simp_l[v].replace('-','')
					simp_r.insert(len(simp_r)-1,simp_l[v])
					del simp_l[v]

					if (simp_l[v-1] == "+") or (simp_l[v-1] == "-"):

						del simp_l[v-1]

					elif (simp_l[v] == "+") or (simp_l[v] == "-"):

						del simp_l[v]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+simp_l[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					if len(simp_r) == 2:

						simp_r.insert(len(simp_r)-1,simp_l[v])
						del simp_l[v]

					else:

						simp_r.insert(len(simp_r)-1,"+")
						simp_r.insert(len(simp_r)-1,simp_l[v])
						del simp_l[v]

					if (simp_l[v-1] == "+") or (simp_l[v-1] == "-"):

						del simp_l[v-1]

					elif (simp_l[v] == "+") or (simp_l[v] == "-"):

						del simp_l[v]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

			elif simp_l[v-1] == "+":

				if "-" in simp_l[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_l[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_r.insert(len(simp_r)-1,"+")
					simp_l[v]=simp_l[v].replace('-','')
					simp_r.insert(len(simp_r)-1,simp_l[v])
					del simp_l[v]

					if (simp_l[v-1] == "+") or (simp_l[v-1] == "-"):

						del simp_l[v-1]

					elif (simp_l[v] == "+") or (simp_l[v] == "-"):

						del simp_l[v]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_l[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					if len(simp_r) == 2:

						simp_r.insert(len(simp_r)-1,"-"+str(simp_l[v]))
						del simp_l[v]

					else:

						simp_r.insert(len(simp_r)-1,"-")
						simp_r.insert(len(simp_r)-1,simp_l[v])
						del simp_l[v]

					if (simp_l[v-1] == "+") or (simp_l[v-1] == "-"):

						del simp_l[v-1]

					elif (simp_l[v] == "+") or (simp_l[v] == "-"):

						del simp_l[v]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

			else:
						
				if "-" in simp_l[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_l[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_r.insert(len(simp_r)-1,"+")
					simp_l[v]=simp_l[v].replace('-','')
					simp_r.insert(len(simp_r)-1,simp_l[v])
					del simp_l[v]

					if simp_l[v] == "+":

						del simp_l[v]

					else:

						simp_l[v]=simp_l[v]+simp_l[v+1]
						del simp_l[v+1]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_l[v])
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1

					simp_r.insert(len(simp_r)-1,"-")
					simp_r.insert(len(simp_r)-1,simp_l[v])
					del simp_l[v]

					if simp_l[v] == "+":

						del simp_l[v]

					else:

						simp_l[v]=simp_l[v]+simp_l[v+1]
						del simp_l[v+1]

					v=0
					#print(simp_l,simp_r)
					string = stringify(simp_l,simp_r)
					print(string,"\n")
					solution.insert(sol_cnt,string)
					sol_cnt += 1

		v=v+1				
	
	#list all nth order terms for LHS

	lhs_n_order=[]
	n=0

	for s in range(0,len(simp_l)-1):

		if var_type[0] in simp_l[s]:

			if "^" in simp_l[s]:

				temp=str(simp_l[s])
				t=0
				hat_check=0
				temp_two=""
				while t != len(temp):

					if temp[t] == "^":
		
						hat_check=1
						t=t+1

					if hat_check == 1:

						temp_two=temp_two+str(temp[t])
					
					t=t+1

				if str(temp_two) not in lhs_n_order:

					lhs_n_order.insert(n,str(temp_two))
					n=n+1

			else:

				if "1" not in lhs_n_order:

					lhs_n_order.insert(n,"1")
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

		#print(new_n_order)


		#Reorder terms on LHS from largest exponent to smallest
		rear_l=[]
		n=0	
		for s in range(0,len(new_n_order)):		

			for t in range(0,len(simp_l)):

				if int(new_n_order[s]) > 1:

					if (var_type[0] in simp_l[t]) & ("^"+str(new_n_order[s]) in simp_l[t]):

						#print(simp_l[t])

						temp = simp_l[t]
						v=0
						while temp[v] != var_type[0]:

							v+=1

						v += 2
						b=""
						while v != len(temp):

							b = b+str(temp[v])
							v+=1

						#print(b,new_n_order[s])
						if int(b) == int(new_n_order[s]):

							if simp_l[t-1] == "-":
						
								if "-" in simp_l[t]:

									if n == 0:

										rear_l.insert(n,simp_l[t])
										n=n+1

									else:

										rear_l.insert(n,"+")
										n=n+1
										rear_l.insert(n,simp_l[t])
										n=n+1

								else:

									rear_l.insert(n,"-")

									if n == 0:		

										rear_l[n]=rear_l[n]+simp_l[t]
										n=n+1

									else:
			
										n=n+1
										rear_l.insert(n,simp_l[t])
										n=n+1

							elif simp_l[t-1] == "+":

								if "-" in simp_l[t]:

									if n == 0:		

										rear_l.insert(n,simp_l[t])
										n=n+1

									else:
			
										rear_l.insert(n,"-")
										n=n+1
										rear_l.insert(n,simp_l[t])
										rear_l[n] = rear_l[n].replace('-','')
										n=n+1

								else:
							
									if n == 0:

										rear_l.insert(n,simp_l[t])
										n=n+1

									else:

										rear_l.insert(n,"+")
										n=n+1
										rear_l.insert(n,simp_l[t])
										n=n+1

							else:

								if "-" in simp_l[t]:

									if n == 0:		

										rear_l.insert(n,simp_l[t])
										n=n+1

									else:
			
										rear_l.insert(n,simp_l[t])
										n=n+1

								else:
							
									if n == 0:

										rear_l.insert(n,simp_l[t])
										n=n+1

									else:

										rear_l.insert(n,"+")
										n=n+1
										rear_l.insert(n,simp_l[t])
										n=n+1

				if int(new_n_order[s]) == 1:

					if (var_type[0] in simp_l[t]) & ("^" not in simp_l[t]):

						#print(simp_l[t])

						if simp_l[t-1] == "-":
						
							if "-" in simp_l[t]:

								if n == 0:

									rear_l.insert(n,simp_l[t])
									n=n+1

								else:

									rear_l.insert(n,"+")
									n=n+1
									rear_l.insert(n,simp_l[t])
									n=n+1

							else:

								rear_l.insert(n,"-")

								if n == 0:		

									rear_l[n]=rear_l[n]+simp_l[t]
									n=n+1

								else:
			
									n=n+1
									rear_l.insert(n,simp_l[t])
									n=n+1

						elif simp_l[t-1] == "+":

							if "-" in simp_l[t]:

								rear_l.insert(n,"-")

								if n == 0:		

									rear_l[n]=rear_l[n]+simp_l[t]
									n=n+1

								else:
			
									n=n+1
									rear_l.insert(n,simp_l[t])
									n=n+1

							else:
							
								if n == 0:

									rear_l.insert(n,simp_l[t])
									n=n+1

								else:

									rear_l.insert(n,"+")
									n=n+1
									rear_l.insert(n,simp_l[t])
									n=n+1

						else:

							if "-" in simp_l[t]:

								rear_l.insert(n,"-")

								if n == 0:		

									rear_l[n]=rear_l[n]+simp_l[t]
									n=n+1

								else:
			
									n=n+1
									rear_l.insert(n,simp_l[t])
									n=n+1

							else:
							
								if n == 0:

									rear_l.insert(n,simp_l[t])
									n=n+1

								else:

									rear_l.insert(n,"+")
									n=n+1
									rear_l.insert(n,simp_l[t])
									n=n+1

		rear_l.insert(0,"(1")
		rear_l.insert(len(rear_l),")1")

		#print(rear_l)

	else:

		new_n_order = lhs_n_order
		rear_l = simp_l

	for s in range(0,len(new_n_order)):		

		t=0
		while t!=len(rear_l):

			if int(new_n_order[s]) > 1:

				if rear_l[t] == "+":

					if ("^"+str(new_n_order[s]) in rear_l[t-1]) & ("^"+str(new_n_order[s]) in rear_l[t+1]):

						temp_one=str(rear_l[t-1])
						temp_two=str(rear_l[t+1])
						v=0
						x=""
						while temp_one[v] != var_type[0]:

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

						x=float(x)

						v=0
						y=""
						while temp_two[v] != var_type[0]:

							y=y+str(temp_two[v])
							v=v+1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=float(y)

						z=x+y

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+var_type[0]+"^"+str(new_n_order[s])+" + "+str(y)+var_type[0]+"^"+str(new_n_order[s])+" = "+str(z)+var_type[0]+"^"+str(new_n_order[s]))
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1
				
						z=str(z)
	
						if float(z) == 0.0:

							del rear_l[t-1:t+2]
							#print(rear_l,rear_l[t])
							if (rear_l[t-1] == "-") or (rear_l[t-1] == "+"):

								del rear_l[t-1]
								t=0

							elif rear_l[t] == "+":

								del rear_l[t]
								t=0

						else:
	
							rear_l[t-1]=z+var_type[0]+"^"+str(new_n_order[s])
							del rear_l[t:t+2]

							if (rear_l[t-2] == "-") & ("-" in rear_l[t-1]):

								rear_l[t-1] = rear_l[t-1].replace('-','')

							if (rear_l[t-2] == "-") & (float(z) > 0):

								rear_l[t-2] = "+"

							t=0

						string = stringify(rear_l,simp_r)
						print(string,"\n")

				if rear_l[t] == "-":

					if ("^"+str(new_n_order[s]) in rear_l[t-1]) & ("^"+str(new_n_order[s]) in rear_l[t+1]):

						temp_one=str(rear_l[t-1])
						temp_two=str(rear_l[t+1])
						v=0
						x=""
						while temp_one[v] != var_type[0]:

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

						x=float(x)

						v=0
						y=""
						while temp_two[v] != var_type[0]:

							y=y+str(temp_two[v])
							v=v+1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=float(y)
						z=x-y

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+var_type[0]+"^"+str(new_n_order[s])+" + "+str(y)+var_type[0]+"^"+str(new_n_order[s])+" = "+str(z)+var_type[0]+"^"+str(new_n_order[s]))
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1

						z=str(z)

						if float(z) == 0.0:

							del rear_l[t-1:t+2]
							if (rear_l[t-1] == "-") or (rear_l[t-1] == "+"):

								del rear_l[t-1]
								t=0

							elif rear_l[t] == "-":

								del rear_l[t]
								t=0

						else:
	
							rear_l[t-1]=z+var_type[0]+"^"+str(new_n_order[s])
							del rear_l[t:t+2]

							if (rear_l[t-2] == "-") & ("-" in rear_l[t-1]):

								rear_l[t-1] = rear_l[t-1].replace('-','')

							t=0

						string = stringify(rear_l,simp_r)
						print(string,"\n")

			if int(new_n_order[s]) == 1:

				if rear_l[t] == "+":

					if (var_type[0] in rear_l[t-1]) & (var_type[0] in rear_l[t+1]) & ("^" not in rear_l[t-1]) & ("^" not in rear_l[t+1]):

						temp_one=str(rear_l[t-1])
						temp_two=str(rear_l[t+1])
						v=0
						x=""
						while temp_one[v] != var_type[0]:

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

						x=float(x)

						v=0
						y=""
						while temp_two[v] != var_type[0]:

							y=y+str(temp_two[v])
							v=v+1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=float(y)
						z=x+y						

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+var_type[0]+" + "+str(y)+var_type[0]+" = "+str(z)+var_type[0])
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1

						z=str(z)
	
						if float(z) == 0.0:

							del rear_l[t-1:t+2]
							if (rear_l[t-1] == "-") or (rear_l[t-1] == "+"):

								del rear_l[t-1]
								t=0

							elif rear_l[t] == "+":

								del rear_l[t]
								t=0

						else:
	
							rear_l[t-1]=z+var_type[0]
							del rear_l[t:t+2]

							if (rear_l[t-2] == "-") & ("-" in rear_l[t-1]):

								rear_l[t-1] = rear_l[t-1].replace('-','')

							t=0

						string = stringify(rear_l,simp_r)
						print(string,"\n")

				if rear_l[t] == "-":

					if (var_type[0] in rear_l[t-1]) & (var_type[0] in rear_l[t+1]) & ("^" not in rear_l[t-1]) & ("^" not in rear_l[t+1]):

						temp_one=str(rear_l[t-1])
						temp_two=str(rear_l[t+1])
						v=0
						x=""
						while temp_one[v] != var_type[0]:

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

						x=float(x)

						v=0
						y=""
						while temp_two[v] != var_type[0]:

							y=y+str(temp_two[v])
							v=v+1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=float(y)
						z=x-y

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+var_type[0]+" + "+str(y)+var_type[0]+" = "+str(z)+var_type[0])
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1

						z=str(z)

						if float(z) == 0.0:

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
	
							rear_l[t-1]=z+var_type[0]
							del rear_l[t:t+2]
							
							if (rear_l[t-2] == "-") & ("-" in rear_l[t-1]):

								rear_l[t-1] = rear_l[t-1].replace('-','')

							t=0

						string = stringify(rear_l,simp_r)
						print(string,"\n")

			t=t+1

	right_side=calculate(simp_r,0)

	simp_r.clear()
	simp_r.insert(0,"(1")
	simp_r.insert(1,str(right_side))
	simp_r.insert(2,")1")

	#print(rear_l,simp_r)

	temp=""
	for s in range(0,len(rear_l)):

		if "(1" in rear_l[s]:

			pass

		elif ")1" in rear_l[s]:

			pass

		elif "(" in rear_l[s]:

			temp += "("

		elif ")" in rear_l[s]:

			temp += ")"

		else:

			temp += rear_l[s]

	temp += "="
	for s in range(0,len(simp_r)):

		if "(1" in simp_r[s]:

			pass

		elif ")1" in simp_r[s]:

			pass

		elif "(" in simp_r[s]:

			temp += "("

		elif ")" in simp_r[s]:

			temp += ")"

		else:

			temp += simp_r[s]

	solution.insert(sol_cnt,"")
	sol_cnt+=1
	solution.insert(sol_cnt,"-- After combining all similar terms... --")
	print(solution[sol_cnt]+"\n"+temp+"\n")
	sol_cnt=sol_cnt+1
	solution.insert(sol_cnt,temp)
	sol_cnt += 1

	if len(new_n_order) == 1:

		solution.insert(sol_cnt,"")
		sol_cnt+=1
		print("-- Isolating "+var_type[0]+"... --")
		solution.insert(sol_cnt,"-- Isolating "+var_type[0]+"... --")
		sol_cnt += 1
		t=0
		while t != len(rear_l):

			#* first
			if (var_type[0] in rear_l[t]) & (len(rear_l[t]) > 1):

				temp=rear_l[t]
				x=""
				y=""
				v=0
				while temp[v] != var_type[0]:

					x=x+str(temp[v])
					v=v+1

				if x == "":

					x = "1"

				elif x == "-":

					x = "-1"

				while v != len(temp):

					y=y+str(temp[v])
					v=v+1

				rear_l[t] = y
				#print(simp_r[1])

				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ / "+str(x))
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1

				simp_r[1] = operation(float(simp_r[1]),"/",float(x))

				string = stringify(rear_l,simp_r)
				print(string,"\n")
				solution.insert(sol_cnt,string)
				sol_cnt += 1

			if (rear_l[t] == "*") & (var_type[0] in rear_l[t-1]):

				x = float(rear_l[t+1])
				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ / "+str(x))
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1
				simp_r[1] = operation(float(simp_r[1]),"/",x)
				del rear_l[t:t+2]

				string = stringify(rear_l,simp_r)
				print(string,"\n")
				solution.insert(sol_cnt,string)
				sol_cnt += 1

			if (rear_l[t-1] == "*") & (var_type[0] in rear_l[t]):

				x = float(rear_l[t-2])
				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ / "+str(x))
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1
				simp_r[1] = operation(float(simp_r[1]),"/",x)
				del rear_l[t-2:t]
				t=0
				#print(rear_l,simp_r)

				string = stringify(rear_l,simp_r)
				print(string,"\n")
				solution.insert(sol_cnt,string)
				sol_cnt += 1

			#/ second
			if (rear_l[t] == "/") & (var_type[0] in rear_l[t-1]):			

				x = float(rear_l[t+1])
				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ * "+str(x))
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1
				simp_r[1] = operation(float(simp_r[1]),"*",x)
				del rear_l[t+1:t+2]

				string = stringify(rear_l,simp_r)
				print(string,"\n")
				solution.insert(sol_cnt,string)
				sol_cnt += 1

			if (rear_l[t-1] == "/") & (var_type[0] in rear_l[t]):

				x = float(rear_l[t-2])
				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ * "+var_type[0])
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1
				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ / "+simp_r[1])
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1
				simp_r[1] = operation(x,"/",float(simp_r[1]))
				del rear_l[t-2:t]
				t=0
				#print(rear_l,simp_r)

				string = stringify(rear_l,simp_r)
				print(string,"\n")
				solution.insert(sol_cnt,string)
				sol_cnt += 1

			#^ third
			if (var_type[0] in rear_l[t]) & ("^" in rear_l[t]):

				temp=rear_l[t]
				x=""
				y=""
				v=0
				while temp[v] != "^":

					x=x+str(temp[v])
					v=v+1

				v=v+1
				while v != len(temp):

					y=y+str(temp[v])
					v=v+1

				if x == "":

					x = "1"

				elif x == "-":

					x = "-1"

				rear_l[t] = x

				#If the required operation is square root
				if float(y) == 2:
					
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ SQRT")
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					simp_r[1] = operation(0,"SQRT",float(simp_r[1]))
					
					if "0j" in str(simp_r[1]):
	
						simp_r[1] = str(simp_r[1]).replace('+0j','')
						simp_r[1] = str(simp_r[1]).replace('(','')
						simp_r[1] = str(simp_r[1]).replace(')','')
					
					#check_var = simp_r[1]

				else:
				
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ ^ (1/"+str(y)+")")
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					simp_r[1] = operation(float(simp_r[1]),"^",1/float(y))

					if "0j" in str(simp_r[1]):
	
						simp_r[1] = str(simp_r[1]).replace('+0j','')
						simp_r[1] = str(simp_r[1]).replace('(','')
						simp_r[1] = str(simp_r[1]).replace(')','')

				#if is_even(float(y)) == True:

					#simp_r[1] = "+/- "+str(simp_r[1])

				string = stringify(rear_l,simp_r)
				print(string,"\n")
				solution.insert(sol_cnt,string)
				sol_cnt += 1
			
			t=t+1

		#print(rear_l,simp_r)

		if bracket[0] == "0":

			ans=[]
			ans.insert(0,simp_r[1])
			return ans

		else:

			solution.insert(sol_cnt,"-- Reintroducing "+bracket_temp+" --")
			print(solution[sol_cnt],"\n")
			sol_cnt=sol_cnt+1
			string = stringify(bracket,simp_r)
			print(string)
			solution.insert(sol_cnt,string)
			sol_cnt += 1
			simp_r[1] = str(simp_r[1])
			ans = isolate(bracket,simp_r,1)
			return ans
			

	#What if the final equation is a 2nd order polynomial
	elif int(new_n_order[0]) == 2:

		if "-" in simp_r[1]:

			simp_r[1] = simp_r[1].replace('-','')
			rear_l.insert(len(rear_l)-1,"+")
			rear_l.insert(len(rear_l)-1,simp_r[1])
			simp_r[1] = "0"

		else:

			rear_l.insert(len(rear_l)-1,"-")
			rear_l.insert(len(rear_l)-1,simp_r[1])
			simp_r[1] = "0"

		#Quadratic Formula

		rear_l = Poly_Func(rear_l)
		coeff = rear_l.get_coeff(int(new_n_order[0]),var_type[0])
		ans, solution, sol_cnt = coeff.quadratic(solution, sol_cnt)

		for s in range(0,len(ans)):

			if "(" in str(ans[s]):

				ans[s] = str(ans[s]).replace('(','')

			if ")" in str(ans[s]):

				ans[s] = str(ans[s]).replace(')','')		

		return ans

	#3rd or polynomial

	elif int(new_n_order[0]) == 3:

		if "-" in simp_r[1]:

			simp_r[1] = simp_r[1].replace('-','')
			rear_l.insert(len(rear_l)-1,"+")
			rear_l.insert(len(rear_l)-1,simp_r[1])
			simp_r[1] = "0"

		else:

			rear_l.insert(len(rear_l)-1,"-")
			rear_l.insert(len(rear_l)-1,simp_r[1])
			simp_r[1] = "0"

		#Cubic Function Formula

		rear_l = Poly_Func(rear_l)
		coeff = rear_l.get_coeff(int(new_n_order[0]),var_type[0])
		ans, solution, sol_cnt = coeff.cardano(solution, sol_cnt)

		for s in range(0,len(ans)):

			ans[s] = round(ans[s].real,6)+(round(ans[s].imag,6))*1j

			if ans[s].imag == 0:

				ans[s] = ans[s].real

			if "(" in str(ans[s]):

				ans[s] = str(ans[s]).replace('(','')

			if ")" in str(ans[s]):

				ans[s] = str(ans[s]).replace(')','')
		

		return ans		

	#Ferrari's Method
	elif int(new_n_order[0]) == 4:

		if "-" in simp_r[1]:

			simp_r[1] = simp_r[1].replace('-','')
			rear_l.insert(len(rear_l)-1,"+")
			rear_l.insert(len(rear_l)-1,simp_r[1])
			simp_r[1] = "0"

		else:

			rear_l.insert(len(rear_l)-1,"-")
			rear_l.insert(len(rear_l)-1,simp_r[1])
			simp_r[1] = "0"

		rear_l = Poly_Func(rear_l)
		coeff = rear_l.get_coeff(int(new_n_order[0]),var_type[0])
		#print(coeff.eqn)
		ans, solution, sol_cnt = coeff.ferrari(solution, sol_cnt)

		for s in range(0,len(ans)):

			ans[s] = round(ans[s].real,6)+(round(ans[s].imag,6))*1j

			if ans[s].imag == 0:

				ans[s] = ans[s].real

			if "(" in str(ans[s]):

				ans[s] = str(ans[s]).replace('(','')

			if ")" in str(ans[s]):

				ans[s] = str(ans[s]).replace(')','')
		
		return ans		

	#For any polynomial of nth degree where n>=5
	else:

		if "-" in simp_r[1]:

			simp_r[1] = simp_r[1].replace('-','')
			rear_l.insert(len(rear_l)-1,"+")
			rear_l.insert(len(rear_l)-1,simp_r[1])
			simp_r[1] = "0"

		else:

			rear_l.insert(len(rear_l)-1,"-")
			rear_l.insert(len(rear_l)-1,simp_r[1])
			simp_r[1] = "0"

		#print(new_n_order[0])

		rear_l = Poly_Func(rear_l)
		coeff=rear_l.get_coeff(int(new_n_order[0]),var_type[0])
		test=rear_l.get_coeff(int(new_n_order[0]),var_type[0])
		test_two=rear_l.get_coeff(int(new_n_order[0]),var_type[0])
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

		test_temp = test_two.stringify(var_type[0])

		if remainder < 0:

			test_temp += str(remainder)+"/"+var_type[0]

		else:

			test_temp += "+"+str(remainder)+"/"+var_type[0]

		string = stringify(rear_l.eqn,simp_r)
		string = string.replace('=0','')
		print("("+string+")/"+var_type[0]+" = "+test_temp+"\n")
		solution.insert(sol_cnt,"("+string+")/"+var_type[0]+" = "+test_temp)
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
						ans = jenkins_traub.real_poly(coeff,int(new_n_order[0])-i)

					except ZeroDivisionError:

						string = test.stringify(var_type[0])

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

						test_temp = test_two.stringify(var_type[0])

						if remainder < 0:

							test_temp += str(remainder)+"/"+var_type[0]

						else:

							test_temp += "+"+str(remainder)+"/"+var_type[0]

						print("("+string+")/"+var_type[0]+" = "+test_temp+"\n")
						solution.insert(sol_cnt,"("+string+")/"+var_type[0]+" = "+test_temp)
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

			ans = jenkins_traub.real_poly(coeff,int(new_n_order[0]))

		for i in range(0,len(ans)):

			ans[i] = round(ans[i].real,5)+(round(ans[i].imag,5))*1j

			if round(ans[i].imag,4) == 0:
			
				ans[i] = ans[i].real

			if "(" in str(ans[i]):

				ans[i] = str(ans[i]).replace('(','')

			if ")" in str(ans[i]):

				ans[i] = str(ans[i]).replace(')','') 

		return ans

def main(a):

	master=[]
	numtemp=[]
	bracket=[]
	i=0
	j=0#walk the master array
	b=0
	k=0
	temp=""
	ans=0
	global sol_cnt, solution
	sol_cnt=0
	solution=[]
	var_num=0
	var_index=0

	solution.insert(sol_cnt,"The inputted equation is "+str(a))
	print(solution[sol_cnt])
	sol_cnt=sol_cnt+1

	a = "(" + a + ")00000"
	s=0
	#Transform input string array into code-readable format
	while s != len(a)-5:

		if a[s] == "(":
		
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		elif a[s] == "^":

			master.insert(j,"^")
			j=j+1

		elif a[s] == "/":

			master.insert(j,"/")
			j=j+1

		elif a[s] == "*":

			master.insert(j,"*")
			j=j+1

		elif a[s] == "+":

			master.insert(j,"+")
			j=j+1

		#checks if previous digit is a number so that it doesn't mistake a negative number for an operation
		elif (a[s] == "-") & ((a[s-1] == ")") or (a[s-1].isdigit() == True) or (a[s-1].isalpha() == True)):
	
			master.insert(j,"-")
			j=j+1

		#Sine
		elif (a[s] == "s") & (a[s+1] == "i") & (a[s+3] != "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"SIN")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Cosine
		elif (a[s] == "c") & (a[s+1] == "o") & (a[s+2] == "s") & (a[s+3] != "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"COS")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Tangent
		elif (a[s] == "t") & (a[s+1] == "a") & (a[s+3] != "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"TAN")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Secant
		elif (a[s] == "s") & (a[s+1] == "e") & (a[s+3] != "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"SEC")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Cosecant
		elif (a[s] == "c") & (a[s+1] == "s") & (a[s+3] != "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"CSC")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Cotangent
		elif (a[s] == "c") & (a[s+1] == "o") & (a[s+2] == "t") & (a[s+3] != "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"COT")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Arc Sine
		elif (a[s] == "a") & (a[s+1] == "s") & (a[s+2] == "i") & (a[s+4] != "h"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ASIN")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Arc Cosine
		elif (a[s] == "a") & (a[s+1] == "c") & (a[s+2] == "o") & (a[s+3] == "s") & (a[s+4] != "h"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ACOS")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Arc Tangent
		elif (a[s] == "a") & (a[s+1] == "t") & (a[s+4] != "h"):
		
			while a[s] != "(":

				s=s+1
			
			master.insert(j,"ATAN")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Arc Secant
		elif (a[s] == "a") & (a[s+1] == "s") & (a[s+2] == "e") & (a[s+4] != "h"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ASEC")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Arc Cosecant
		elif (a[s] == "a") & (a[s+1] == "c") & (a[s+2] == "s") & (a[s+4] != "h"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ACSC")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Arc Cotangent
		elif (a[s] == "a") & (a[s+1] == "c") & (a[s+2] == "o") & (a[s+3] == "t") & (a[s+4] != "h"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ACOT")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Sine
		elif (a[s] == "s") & (a[s+1] == "i") & (a[s+3] == "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"SINH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1
	
		#Hyperbolic Cosine
		elif (a[s] == "c") & (a[s+1] == "o") & (a[s+2] == "s") & (a[s+3] == "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"COSH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Tangent
		elif (a[s] == "t") & (a[s+1] == "a") & (a[s+3] == "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"TANH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Secant
		elif (a[s] == "s") & (a[s+1] == "e") & (a[s+3] == "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
			
			master.insert(j,"SECH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Cosecant
		elif (a[s] == "c") & (a[s+1] == "s") & (a[s+3] == "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"CSCH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Cotangent
		elif (a[s] == "c") & (a[s+1] == "o") & (a[s+2] == "t") & (a[s+3] == "h") & (a[s-1] != "a"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"COTH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Arc Sine
		elif (a[s] == "a") & (a[s+1] == "s") & (a[s+2] == "i") & (a[s+4] == "h") :
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ASINH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Arc Cosine
		elif (a[s] == "a") & (a[s+1] == "c") & (a[s+2] == "o") & (a[s+3] == "s") & (a[s+4] == "h") :
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ACOSH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1
	
		#Hyperbolic Arc Tangent
		elif (a[s] == "a") & (a[s+1] == "t") & (a[s+2] == "a") & (a[s+4] == "h") :
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ATANH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Arc Secant
		elif (a[s] == "a") & (a[s+1] == "s") & (a[s+2] == "e") & (a[s+4] == "h") :
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ASECH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Arc Cosecant
		elif (a[s] == "a") & (a[s+1] == "c") & (a[s+2] == "s") & (a[s+4] == "h") :
		
			while a[s] != "(":

				s=s+1
			
			master.insert(j,"ACSCH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Hyperbolic Arc Cotangent
		elif (a[s] == "a") & (a[s+1] == "c") & (a[s+2] == "o") & (a[s+3] == "t") & (a[s+4] == "h") :
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"ACOTH")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Natural Logarithm
		elif (a[s] == "l") & (a[s+1] == "n"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"LN")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#Logarithm
		elif (a[s] == "l") & (a[s+1] == "o"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"LOG")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		elif a[s] == ",":

			master.insert(j,")" + str(b))
			b=b-1
			j=j+1
			b=b+1
			master.insert(j,"(" + str(b))
			j=j+1

		#Square Root
		elif (a[s] == "s") & (a[s+1] == "q"):
		
			while a[s] != "(":

				s=s+1
		
			master.insert(j,"SQRT")
			j=j+1
			b=b+1 #system has knowledge of current amount of open brackets
			master.insert(j,"(" + str(b)) 
			j=j+1

		#PI
		elif (a[s] == "P") & (a[s+1] == "I"):
		
			master.insert(j,str(math.pi))
			s=s+1
			j=j+1

		#Euler's number
		elif a[s] == "e":

			master.insert(j,str(math.e))
			j=j+1

		elif a[s] == ")":

			master.insert(j,")" + str(b))
			b=b-1
			j=j+1

		elif a[s] == "=":

			master.insert(j,"=")
			j=j+1

		#The following code is for single character variables
		elif (a[s].isalpha() == True) & (a[s-1].isalpha() == False) & (a[s+1].isalpha() == False) & (a[s] != "d"):

			master.insert(j,str(a[s]))
			if str(a[s]) not in var_type:

				var_type.insert(var_num,str(a[s]))
				var_num=var_num+1

			j=j+1

		#the following code is for handling large numbers and decimals
		else:

		
			numtemp.insert(i,a[s])

			if (a[s+1].isdigit() == True) or (a[s+1] == "."): #if the next index is a number or a period

				i=i+1

			elif (a[s] == "-") & (a[s-1].isdigit() == False):

				master.insert(j,"-1")
				j=j+1
				master.insert(j,"*")
				j=j+1
				numtemp.clear()
		
			else:

				for k in range(0,i+1):

					temp=str(temp)+str(numtemp[k])

				master.insert(j,temp)
				j=j+1
				i=0
				numtemp.clear()
				temp = "" #clear up temp

		s=s+1
	print(master,var_num,var_type)
	if (var_num != 0) or (len(var_type) != 0):

		if len(var_type) > 1:

			solution.insert(sol_cnt, "Multivariable problems are not yet supported")
			print(solution)

		else:

			equal_cnt=0
			LHS=[]
			i=0
			RHS=[]
			j=0
			b=0
			b_open=0
			b_open_index=0
			b_close=0
			var_num_l=0
			var_num_r=0
			var_ranges_l=[]
			var_ranges_r=[]
			m=0
			master.insert(len(master),"0")
			master.insert(len(master)+1,"0")
			c=len(master)
			s=0
			while s != c-2:

				if master[s] == "=":

					equal_cnt=1
					LHS.insert(i,")1")
					RHS.insert(j,"(1")
					j=j+1

				else:			

					if equal_cnt == 0:

						LHS.insert(i,str(master[s]))
					
						if "(" in master[s]:

							b_open=b_open+1
							b=b+1
							b_open_index=s

						if ")" in master[s]:

							b_close=b_close+1
							b=b-1
					
						if (master[s].isalpha() == True) & (len(master[s]) == 1):

							if (master[s+1] == "^") & ("(" not in master[s+2]):

								LHS[i] = str(LHS[i])+str(master[s+1])+str(master[s+2])
								del master[s+1:s+3]
								c=len(master)

							if LHS[i-1].isdigit() == True:

								LHS[i-1] = str(LHS[i-1])+str(LHS[i])
								del LHS[i]
								i=i-1

							var_num_l=var_num_l+1

							if b_open != b_close:

								t=s
								while (")" not in master[t]) & (str(b) not in master[t]):

									t=t+1
	
								var_ranges_l.insert(m,str(b_open_index)+":"+str(t))
								m=m+1

							else:

								var_ranges_l.insert(m,str(i))			
	
						i=i+1

					else:

						RHS.insert(j,str(master[s]))
					
						if "(" in master[s]:

							b_open=b_open+1
							b=b+1
							b_open_index=s

						if ")" in master[s]:

							b_close=b_close+1
							b=b-1

						if (master[s].isalpha() == True) & (len(master[s]) == 1):
		
							if (master[s+1] == "^") & ("(" not in master[s+2]):

								RHS[j] = str(RHS[j])+str(master[s+1])+str(master[s+2])
								del master[s+1:s+3]
								c=len(master)
							
							if RHS[j-1].isdigit() == True:

								RHS[j-1] = str(RHS[j-1])+str(RHS[j])
								del RHS[j]
								j=j-1

							var_num_r=var_num_r+1

							if b_open != b_close:

								t=s
								while (")" not in master[t]) & (str(b) not in master[t]):

									t=t+1
	
								var_ranges_r.insert(m,str(b_open_index)+":"+str(t))
								m=m+1

							else:

								var_ranges_r.insert(m,str(j))

						j=j+1

				s=s+1

			#if var_index_l != 0:

				#then the variable is on the LHS of the equation

			#elif var_index_r != 0:

				#then the variable is on the RHS of the equation			

			#print(LHS,RHS)
			ans=isolate(LHS,RHS,1)

			if len(ans) == 1:
		
				solution.insert(sol_cnt,"The value of "+str(var_type[0])+" is "+str(ans[0]))
				print(solution[sol_cnt])
				the_end = process.memory_info().rss
				mem_tot = abs(the_end - beginning)
				solution.insert(sol_cnt+1,mem_tot)

			if len(ans) > 1:

				solution.insert(sol_cnt,"The values of "+str(var_type[0])+" are")
				print(solution[sol_cnt])
				for s in range(0,len(ans)):

					solution.insert(sol_cnt+1+s,str(ans[s]))
					print(solution[sol_cnt+1+s])

				print("")
				the_end = process.memory_info().rss
				mem_tot = abs(the_end - beginning)
				solution.insert(sol_cnt+2+s,mem_tot)

			return solution

	else:
 
		ans=calculate(master,0)
		print(ans)
		solution.insert(sol_cnt,"The final answer is "+str(ans))
		print(solution[sol_cnt])
		#print(solution)
		the_end = process.memory_info().rss
		mem_tot = abs(the_end - beginning)
		solution.insert(sol_cnt+1,mem_tot)
		#print(mem_tot, "bytes", beginning, "bytes", the_end, "bytes")

		return solution


