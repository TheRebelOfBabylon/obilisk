import math
import cmath
import os
import time
import codecs
import calculus
import jenkins_traub

start = time.time()

print('\nEnter an equation: ')

a = input()
memo = a

a = "(" + a + ")00000"

solution=[]
sol_cnt=0
master=[]
numtemp=[]
bracket=[]
i=0
j=0#walk the master array
b=0
k=0
temp=""
ans=0
var_num=0
var_index=0
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

	#Loop for brackets
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
	
	#print(n)
	#for loop to walk list of operations except for ^*/+-
	for s in oper_dict.values():

		op=s
		
		#while loop to walk the inputted array
		t=0
		while t <= (length-1):
			#print(s,t,n[t],length)

			if length == 1:

				calc=n[t]

			elif (n[t] == op):

				if (n[t] == "SIN") or (n[t] == "COS") or (n[t] == "TAN") or (n[t] == "ASIN") or (n[t] == "ACOS") or (n[t] == "ATAN") or (n[t] == "SINH") or (n[t] == "COSH") or (n[t] == "TANH") or (n[t] == "SECH") or (n[t] == "CSCH") or (n[t] == "COTH") or (n[t] == "ASINH") or (n[t] == "ACOSH") or (n[t] == "ATANH") or (n[t] == "LN") or (n[t] == "SQRT"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "SEC"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","1/COS("+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "CSC"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","1/SIN("+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "COT"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","1/TAN("+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ASEC"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","ACOS(1/"+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACSC"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","ASIN(1/"+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACOT"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","ATAN(1/"+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ASECH"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","ACOSH(1/"+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACSCH"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","ASINH(1/"+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACOTH"):

					solution.insert(sol_cnt,op+"("+n[t+1]+")")
					calc = operation(0,op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=","ATANH(1/"+n[t+1]+") =",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "LOG"):

					solution.insert(sol_cnt,op+"("+n[t+1]+","+n[t+2]+")")
					calc = operation(float(n[t+1]),op,float(n[t+2]))
					print("OP"+str(sol_cnt+1)+"___","Log of",n[t+2],"to the base",n[t+1],"=",calc)
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1:t+3]
					#print(n)
					length=len(n)

									
			t=t+1
	
	op1 = ""
	#After resolving complex calculations, now to resolve ^*/+-
	for s in range (0,3):

		if s == 0:

			op = "^"

		elif s == 1:

			op = "*"
			op1 = "/"

		elif s == 2:

			op = "+"
			op1 = "-"

		t=0
		while t <= length-1:
			#print(op,op1,t,n[t],length)
			if n[t] == op:
				
				solution.insert(sol_cnt,n[t-1]+op+n[t+1])
				calc = operation(float(n[t-1]),op,float(n[t+1]))
				print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=",calc)
				sol_cnt=sol_cnt+1
				n[t-1] = str(calc)
				del n[t:t+2]
				t=t-1 #line added to make sure all ops are performed
				length=len(n)
				#print(n, calc)

			elif n[t] == op1:

				solution.insert(sol_cnt,n[t-1]+op1+n[t+1])
				calc = operation(float(n[t-1]),op1,float(n[t+1]))
				print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=",calc)
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

def quadratic(rear_l,var):

	#a
	temp=rear_l[1]
	a=""
	v=0
	while temp[v] != var:

		a=a+str(temp[v])
		v=v+1

	if a == "":

		a = "1"

	if a == "-":

		a = "-1"

	if var_type[0] in rear_l[3]:

		temp=rear_l[3]

		if rear_l[2] == "-":

			b = "-"

		else:

			b=""

		v=0
		while temp[v] != var:

			b=b+str(temp[v])
			v=v+1

		if b == "":

			b = "1"

		if b == "-":

			b = "-1"

		if rear_l[4] == "-":

			c = "-"
			c = c+rear_l[5]

		else:

			c=rear_l[5]

	else:

		b = 0

		if rear_l[2] == "-":

			c = "-"
			c = c+rear_l[3]

		else:

			c=rear_l[3]

	print(a,b,c)

	a=float(a)
	b=float(b)
	c=float(c)

	ans_one = ((-1*b)+((b**2)-(4*a*c))**0.5)/(2*a)
	ans_two = ((-1*b)-((b**2)-(4*a*c))**0.5)/(2*a)

	ans=[]
	ans.insert(0,ans_one)
	ans.insert(1,ans_two)
		
	#print(rear_l,simp_r)
	return ans

def cube_root(x):

	print(x)

	if isinstance(x, complex):

		return x**(1/3)
	
	else:

		if x >= 0.0:

			return x**(1/3)

		else:

			return -(-x)**(1/3)

def isolate(l, r, lvl):

	global var_index_l, var_index_r, var_type, oper_dict_two, solution, sol_cnt
	
	op=""
	op1=""

	#Simplify both sides of equation
	
	simp_l = simplify(l)
	simp_r = simplify(r)	

	#Grouping
	#LHS
	s=0
	simp_l.insert(len(simp_l),"0")
	simp_l.insert(len(simp_l)+1,"0")
	while s != len(simp_l)-2:

		if var_type[0] in simp_l[s]:
		

			#combining x with ^ and exponents
			if (simp_l[s+1] == "^") & (is_number(simp_l[s+2]) == True):

				simp_l[s] = str(simp_l[s])+str(simp_l[s+1])+str(simp_l[s+2])
				del simp_l[s+1:s+3]
				s=0
			
			# combining x^# with constant in front of it
			if is_number(simp_l[s-1]) == True:

				simp_l[s-1] = str(simp_l[s-1])+str(simp_l[s])
				del simp_l[s]
				s=0

			# combining x^# with constant in front of it
			if (simp_l[s-1] == "*") & (is_number(simp_l[s-2]) == True):

				simp_l[s-2] = str(simp_l[s-2])+str(simp_l[s])
				del simp_l[s-1:s+1]
				s=0

		s=s+1

	del simp_l[len(simp_l)-2:len(simp_l)]

	#RHS
	s=0
	simp_r.insert(len(simp_r),"0")
	simp_r.insert(len(simp_r)+1,"0")
	while s != len(simp_r)-2:

		if var_type[0] in simp_r[s]:

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

	print(simp_l,simp_r)
	
	#If there are nth order terms on RHS, move to LHS
	v=0
	while v != len(simp_r)-1:

		if var_type[0] in simp_r[v]:

			if simp_r[v-1] == "-":

				if "-" in simp_r[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+simp_r[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+simp_r[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

			elif simp_r[v-1] == "+":

				if "-" in simp_r[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_r[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_r[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

			else:
				
				if "-" in simp_r[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_r[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_r[v])
					print(solution[sol_cnt],"\n")
					sol_cnt=sol_cnt+1

					simp_l.insert(len(simp_l)-1,"-")
					simp_l.insert(len(simp_l)-1,simp_r[v])
					del simp_r[v]

					if simp_r[v] == "+":

						del simp_r[v]

					else:

						if "-" in simp_r[v+1]:

							del simp_r[v]
							simp_r[v] = simp_r[v].replace('-','')

						else:

							del simp_r[v]
							simp_r[v] = "-"+simp_r[v]

					v=0
					#print(simp_l,simp_r)
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

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
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ + "+simp_l[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

			elif simp_l[v-1] == "+":

				if "-" in simp_l[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_l[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_l[v])
					print(solution[sol_cnt],"\n")
					sol_cnt=sol_cnt+1

					simp_r.insert(len(simp_r)-1,"-")
					simp_r.insert(len(simp_r)-1,simp_l[v])
					del simp_l[v]

					if (simp_l[v-1] == "+") or (simp_l[v-1] == "-"):

						del simp_l[v-1]

					elif (simp_l[v] == "+") or (simp_l[v] == "-"):

						del simp_l[v]

					v=0
					#print(simp_l,simp_r)
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

			else:
						
				if "-" in simp_l[v]:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_l[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

				else:

					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ - "+simp_l[v])
					print(solution[sol_cnt],"\n")
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
					temp=""
					for s in range(1,len(simp_l)-1):

						temp=temp+simp_l[s]

					temp = temp + "="

					for s in range(1,len(simp_r)-1):

						temp=temp+simp_r[s]

					print(temp)

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

	#Reorder lhs_n_order to numerical order

	print(lhs_n_order)
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

	print(new_n_order)


	#Reorder terms on LHS from largest exponent to smallest
	rear_l=[]
	n=0	
	for s in range(0,len(new_n_order)):		

		for t in range(0,len(simp_l)):

			if int(new_n_order[s]) > 1:

				if (var_type[0] in simp_l[t]) & ("^"+str(new_n_order[s]) in simp_l[t]):

					print(simp_l[t])

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

					print(simp_l[t])

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

	print(rear_l)

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
						z=str(z)
	
						if float(z) == 0.0:

							del rear_l[t-1:t+2]
							print(rear_l,rear_l[t])
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

							t=0

				if rear_l[t] == "-":

					if ("^"+str(new_n_order[s]) in rear_l[t-1]) & ("^"+str(new_n_order[s]) in rear_l[t+1]):

						#print(rear_l,rear_l[t])

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

			t=t+1

	right_side=calculate(simp_r,0)

	simp_r.clear()
	simp_r.insert(0,"(1")
	simp_r.insert(1,str(right_side))
	simp_r.insert(2,")1")

	print(rear_l,simp_r)

	if len(new_n_order) == 1:

		t=0
		while t != len(rear_l):

			#* first
			if (var_type[0] in rear_l[t]) & (len(rear_l[t]) > 3):

				temp=rear_l[t]
				x=""
				y=""
				v=0
				while temp[v] != var_type[0]:

					x=x+str(temp[v])
					v=v+1

				while v != len(temp):

					y=y+str(temp[v])
					v=v+1

				rear_l[t] = y

				simp_r[1] = operation(float(simp_r[1]),"/",float(x))

			#/ second

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

				rear_l[t] = x

				#If the required operation is square root
				if float(y) == 2:

					simp_r[1] = operation(0,"SQRT",float(simp_r[1]))
					
					if "0j" in str(simp_r[1]):
	
						simp_r[1] = str(simp_r[1]).replace('+0j','')
						simp_r[1] = str(simp_r[1]).replace('(','')
						simp_r[1] = str(simp_r[1]).replace(')','')
					
					#check_var = simp_r[1]

				else:
				
					simp_r[1] = operation(float(simp_r[1]),"^",1/float(y))

					if "0j" in str(simp_r[1]):
	
						simp_r[1] = str(simp_r[1]).replace('+0j','')
						simp_r[1] = str(simp_r[1]).replace('(','')
						simp_r[1] = str(simp_r[1]).replace(')','')

				if is_even(float(y)) == True:

					simp_r[1] = "+/- "+str(simp_r[1])
			
			t=t+1

		print(rear_l,simp_r)
		ans=[]
		ans.insert(0,simp_r[1])
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

		ans = quadratic(rear_l,var_type[0])

		for s in range(0,len(ans)):

			if "(" in str(ans[s]):

				ans[s] = str(ans[s]).replace('(','')

			if ")" in str(ans[s]):

				ans[s] = str(ans[s]).replace('(','')		

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

		#a
		temp=rear_l[1]
		a=""
		v=0
		while temp[v] != var_type[0]:

			a=a+str(temp[v])
			v=v+1

		if a == "":

			a = "1"

		if a == "-":

			a = "-1"

		if "^2" in rear_l[3]:

			temp=rear_l[3]

			if rear_l[2] == "-":

				b = "-"

			else:

				b=""

			v=0
			while temp[v] != var_type[0]:

				b=b+str(temp[v])
				v=v+1

			if b == "":

				b = "1"

			if b == "-":

				b = "-1"

			if var_type[0] in rear_l[5]:

				temp=rear_l[5]

				if rear_l[4] == "-":

					c = "-"

				else:

					c = ""

				v=0
				while temp[v] != var_type[0]:

					c=c+str(temp[v])
					v=v+1

				if c == "":

					c = "1"

				if c == "-":

					c= "-1"

				if rear_l[6] == "-":

					d = "-"
					d = d+rear_l[7]

				else:

					d=rear_l[7]

			#c = 0
			else:

				c = 0
		
				if rear_l[4] == "-":

					d = "-"
					d = d+rear_l[5]

				else:

					d=rear_l[5]

		#b = 0
		else:

			b = 0

			if var_type[0] in rear_l[3]:

				temp=rear_l[3]

				if rear_l[2] == "-":

					c = "-"

				else:

					c = ""

				v=0
				while temp[v] != var_type[0]:

					c=c+str(temp[v])
					v=v+1

				if c == "":

					c = "1"

				if c == "-":

					c= "-1"

				if rear_l[4] == "-":

					d = "-"
					d = d+rear_l[5]

				else:

					d=rear_l[5]

			# c = 0
			else:

				c = 0

				if rear_l[2] == "-":

					d = "-"
					d = d+rear_l[3]

				else:

					d=rear_l[3] 

		print(a,b,c,d)

		a=float(a)
		b=float(b)
		c=float(c)
		d=float(d)

		print("a",a,"b",b,"c",c,"d",d)

		#depressed cubic
		p = ((3*a*c)-(b**2))/(9*(a**2))
		q = ((9*a*b*c)-(27*(a**2)*d)-(2*(b**3)))/(54*(a**3))

		print(p,q)

		s = cube_root((q)+(((p)**3)+((q)**2))**(1/2))
		t = cube_root((q)-(((p)**3)+((q)**2))**(1/2))

		print("s",s,"t",t)

		print(1j*1j)

		ans_one = s+t-(b/(3*a))
		ans_two = (-1*((s+t)/2))-(b/(3*a))+(((1j*(3**0.5))/2)*(s-t))
		ans_three = (-1*((s+t)/2))-(b/(3*a))-(((1j*(3**0.5))/2)*(s-t))

		ans_one = str(ans_one)
		ans_two = str(ans_two)
		ans_three = str(ans_three)

		if "(" in ans_one:

			ans_one = ans_one.replace('(','')

		if ")" in ans_one:

			ans_one = ans_one.replace(')','')

		if "(" in ans_two:

			ans_two = ans_two.replace('(','')

		if ")" in ans_two:

			ans_two = ans_two.replace(')','')

		if "(" in ans_three:

			ans_three = ans_three.replace('(','')

		if ")" in ans_three:

			ans_three = ans_three.replace(')','')

		ans=[]
		ans.insert(0,ans_one)
		ans.insert(1,ans_two)
		ans.insert(2,ans_three)
		
		print(rear_l,simp_r)
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

		#a
		temp=rear_l[1]
		a=""
		v=0
		while temp[v] != var_type[0]:

			a=a+str(temp[v])
			v=v+1

		if a == "":

			a = "1"

		if a == "-":

			a = "-1"

		#ax^4 + bx^3 +cx^2 +dx +e
		if "^3" in rear_l[3]:

			temp=rear_l[3]

			if rear_l[2] == "-":

				b = "-"

			else:

				b=""

			v=0
			while temp[v] != var_type[0]:

				b=b+str(temp[v])
				v=v+1

			if b == "":

				b = "1"

			if b == "-":

				b = "-1"

			#ax^4 + bx^3 +cx^2 +dx +e
			if "^2" in rear_l[5]:

				temp=rear_l[5]

				if rear_l[4] == "-":

					c = "-"

				else:

					c = ""

				v=0
				while temp[v] != var_type[0]:

					c=c+str(temp[v])
					v=v+1

				if c == "":

					c = "1"

				if c == "-":

					c= "-1"
				
				#ax^4 + bx^3 +cx^2 +dx +e
				if var_type[0] in rear_l[7]:

					temp=rear_l[7]

					if rear_l[6] == "-":

						d = "-"

					else:

						d = ""

					v=0
					while temp[v] != var_type[0]:

						d=d+str(temp[v])
						v=v+1

					if d == "":

						d = "1"

					if d == "-":

						d = "-1"

					if rear_l[8] == "-":

						e = "-"
						e = e+rear_l[9]

					else:
	
						e = rear_l[9]

				#d = 0
				#ax^4 + bx^3 + cx^2 + e
				else:
					
					d = 0

					if rear_l[6] == "-":

						e = "-"
						e = e+rear_l[7]

					else:
	
						e = rear_l[7]

			#c = 0
			#ax^4 + bx^3 + dx + e
			else:

				c = 0
		
				temp=rear_l[5]

				if rear_l[4] == "-":

					d = "-"

				else:

					d = ""

				v=0
				while temp[v] != var_type[0]:

					d=d+str(temp[v])
					v=v+1

				if d == "":

					d = "1"

				if d == "-":

					d = "-1"

				if rear_l[6] == "-":

					e = "-"
					e = e+rear_l[7]

				else:
	
					e = rear_l[7]

		#b = 0
		#ax^4 + cx^2 + dx + e
		else:

			b = 0

			#ax^4 + cx^2 + dx + e
			if "^2" in rear_l[3]:

				temp=rear_l[3]

				if rear_l[2] == "-":

					c = "-"

				else:

					c = ""

				v=0
				while temp[v] != var_type[0]:

					c=c+str(temp[v])
					v=v+1

				if c == "":

					c = "1"

				if c == "-":

					c = "-1"
	
				#ax^4 + cx^2 + dx + e
				if var_type[0] in rear_l[5]:

					temp=rear_l[5]

					if rear_l[4] == "-":

						d = "-"

					else:

						d = ""

					v=0
					while temp[v] != var_type[0]:

						d=d+str(temp[v])
						v=v+1

					if d == "":

						d = "1"

					if d == "-":

						d = "-1"

					if rear_l[6] == "-":

						e = "-"
						e = e+rear_l[7]

					else:

						e=rear_l[7]

				#ax^4 + cx^2 + e
				else:

					d = 0

					if rear_l[4] == "-":

						e = "-"
						e = e+rear_l[5]

					else:

						e=rear_l[5]
					

			# c = 0
			#ax^4 + dx + e
			else:

				c = 0
				#ax^4 + dx + e
				if var_type[0] in rear_l[3]:

					temp=rear_l[3]

					if rear_l[2] == "-":

						d = "-"

					else:

						d = ""

					v=0
					while temp[v] != var_type[0]:

						d=d+str(temp[v])
						v=v+1

					if d == "":

						d = "1"

					if d == "-":

						d = "-1"

					if rear_l[4] == "-":

						e = "-"
						e = e+rear_l[5]

					else:

						e=rear_l[5]

				#ax^4 + e
				else:

					d = 0

					if rear_l[2] == "-":

						e = "-"
						e = e+rear_l[3]

					else:

						e=rear_l[3] 

		print(a,b,c,d,e)

		a = float(a)
		b = float(b)
		c = float(c)
		d = float(d)
		e = float(e)		

		delta_zero = (c**2)-(3*b*d)+(12*a*e)
		delta_one = (2*(c**3))-(9*b*c*d)+(27*(b**2)*e)+(27*a*(d**2))-(72*a*c*e)

		print("delta_zero",delta_zero,"delta_one",delta_one)

		big_q = cube_root(((delta_one)+((delta_one**2)-(4*delta_zero**3))**(1/2))/2)

		p = ((8*a*c)-(3*(b**2)))/(8*(a**2))
		q = ((b**3)-(4*a*b*c)+(8*(a**2)*d))/(8*(a**3))

		s = (1/2)*(((-2/3*p)+((1/(3*a))*((big_q)+(delta_zero/big_q))))**(1/2))

		print("big_q",big_q,"p",p,"q",q,"s",s)

		ans_one = (-1*b/(4*a))-s+((1/2)*(((-4*(s**2))-(2*p)+(q/s))**(1/2)))
		ans_two = (-1*b/(4*a))-s-((1/2)*(((-4*(s**2))-(2*p)+(q/s))**(1/2)))
		ans_three = (-1*b/(4*a))+s+((1/2)*(((-4*(s**2))-(2*p)-(q/s))**(1/2)))
		ans_four = (-1*b/(4*a))+s-((1/2)*(((-4*(s**2))-(2*p)-(q/s))**(1/2)))

		if isinstance(ans_one, complex):

			if round(1-ans_one.imag,10) == 1.0000000000:

				ans_one = ans_one.real

		if isinstance(ans_two, complex):

			if round(1-ans_two.imag,10) == 1.0000000000:

				ans_two = ans_two.real

		if isinstance(ans_three, complex):

			if round(1-ans_three.imag,10) == 1.0000000000:

				ans_three = ans_three.real

		if isinstance(ans_four, complex):

			if round(1-ans_four.imag,10) == 1.0000000000:

				ans_four = ans_four.real

		ans_one = str(ans_one)
		ans_two = str(ans_two)
		ans_three = str(ans_three)
		ans_four = str(ans_four)

		if "(" in ans_one:

			ans_one = ans_one.replace('(','')

		if ")" in ans_one:

			ans_one = ans_one.replace(')','')

		if "(" in ans_two:

			ans_two = ans_two.replace('(','')

		if ")" in ans_two:

			ans_two = ans_two.replace(')','')

		if "(" in ans_three:

			ans_three = ans_three.replace('(','')

		if ")" in ans_three:

			ans_three = ans_three.replace(')','')

		if "(" in ans_four:

			ans_four = ans_four.replace('(','')

		if ")" in ans_four:

			ans_four = ans_four.replace(')','')

		ans=[]
		ans.insert(0,ans_one)
		ans.insert(1,ans_two)
		ans.insert(2,ans_three)
		ans.insert(3,ans_four)
		
		print(rear_l,simp_r)
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

		coeff=[]
		for s in range(int(new_n_order[0]),-1,-1):

			for i in range(0,len(rear_l)):

				if "^"+str(s) in rear_l[i]:
					
					temp = rear_l[i]
					a=""
					v=0
					while temp[v] != var_type[0]:

						a = a+str(temp[v])
						v+=1

					v += 2
					b=""
					while v != len(temp):

						b = b+str(temp[v])
						v+=1

					if int(b) == s: 

						if a == "":

							a = 1

						if a == "-":

							a = -1

						if rear_l[i-1] == "-":

							a = -1*float(a)

						coeff.append(float(a))
						#print("1st case","rear_l[i]",rear_l[i],"s",s,"i",i,"coeff",coeff)

				elif ("^" not in rear_l[i]) & (var_type[0] in rear_l[i]) & (s==1):
				
					temp = rear_l[i]
					a=""
					v=0
					while temp[v] != var_type[0]:

						a = a+str(temp[v])
						v+=1

					if a == "":

						a = 1

					if a == "-":

						a = -1

					if rear_l[i-1] == "-":

						a = -1*float(a)

					coeff.append(float(a))
					#print("2nd case","rear_l[i]",rear_l[i],"s",s,"i",i,"coeff",coeff)

				elif (is_number(rear_l[i]) == True) & (s==0):
				
					a = float(rear_l[i])
					if rear_l[i-1] == "-":

						a = -1*a					

					coeff.append(a)
					#print("3rd case","rear_l[i]",rear_l[i],"s",s,"i",i,"coeff",coeff)

		#print("coeff before JT",coeff)

		ans = jenkins_traub.real_poly(coeff,int(new_n_order[0]))

		for i in range(0,len(ans)):

			ans[i] = round(ans[i].real,6)+(round(ans[i].imag,6))*1j

			if round(1-ans[i].imag,7) == 1.0000000:
			
				ans[i] = ans[i].real

			if "(" in str(ans[i]):

				ans[i] = str(ans[i]).replace('(','')

			if ")" in str(ans[i]):

				ans[i] = str(ans[i]).replace(')','') 

		return ans


		

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
		eq_index=j
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

		if (a[s+1].isdigit() == True) or (a[s+1] == "."): #if the next index is a number or a periodw

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


if var_num > 0:

	if len(var_type) > 1:

		print("Multivariable problems are not yet supported.")

	else:

		#print(master)
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
		
			print("The value of",str(var_type[0]),"is",str(ans[0]),"\n")

		if len(ans) > 1:

			print("The values of",str(var_type[0]),"are")
			for s in range(0,len(ans)):

				print(str(ans[s]))

		print("")

else:
 	
	print(master)
	ans=calculate(master,0)


	print("The result of the above equation is",ans,"\n")
	the_end = time.time()
	mem_tot = the_end - start
	print("Start", start, "s End", the_end, "s", mem_tot, "s")

	satoshi_amt = round(mem_tot*0.0000845)

	print("The cost is", satoshi_amt, "sats")



