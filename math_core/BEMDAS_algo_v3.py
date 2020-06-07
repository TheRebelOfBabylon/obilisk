import math
import cmath
import os
import psutil
from math_core import calculus
from math_core.algebra import *
from math_core import jenkins_traub

process = psutil.Process(os.getpid())
beginning = process.memory_info().rss

solution=[]
sol_cnt=0

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

def inference(eqn):

	master=[]
	s=0
	for i in range(0,len(eqn)):

		if ("(" in eqn[i]) and (is_number(eqn[i-1]) == True):

			master.append("*")
			master.append(eqn[i])

		elif (eqn[i] in oper_dict.values()) and (is_number(eqn[i-1]) == True):

			master.append("*")
			master.append(eqn[i])

		elif ("(" in eqn[i]) and (")" in eqn[i-1]) and (s != 0):

			master.append("*")
			master.append(eqn[i])

		else:

			master.append(eqn[i])

	#print(master)
	return master

#To detect divisions by zero
def div_check(x,y):

	try:
		x/y

	except ZeroDivisionError:

		return True

	else:

		return False

def operation(num_one,oper,num_two):

	try:

		num_one = float(num_one)

	except:

		num_one = complex(num_one)

	try:

		num_two = float(num_two)

	except:

		num_two = complex(num_two)

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
			
			if ("(" in n[t]) and ("j" not in n[t]):
				
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

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "SEC"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = 1/COS("+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "CSC"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = 1/SIN("+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "COT"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = 1/TAN("+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ASEC"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ACOS(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACSC"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ASIN(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACOT"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ATAN(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ASECH"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ACOSH(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACSCH"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ASINH(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "ACOTH"):

					calc = operation(0,op,n[t+1])
					solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+op+"("+n[t+1]+") = ATANH(1/"+n[t+1]+") = "+str(calc))
					print(solution[sol_cnt])
					sol_cnt=sol_cnt+1
					n[t] = str(calc)
					del n[t+1]
					length=len(n)
					#print(n, calc)

				elif (n[t] == "LOG"):

					calc = operation(n[t+1],op,n[t+2])
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
				
				calc = operation(n[t-1],op,n[t+1])
				solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+n[t-1]+op+n[t+1]+" = "+str(calc))
				print(solution[sol_cnt])
				sol_cnt=sol_cnt+1
				n[t-1] = str(calc)
				del n[t:t+2]
				t=t-1 #line added to make sure all ops are performed
				length=len(n)
				#print(n, calc)

			elif n[t] == op1:

				calc = operation(n[t-1],op1,n[t+1])
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

#Need to rewrite simplify function to calculate any numerical values within a variable type equation. Also combine all similar terms like the beginning of isolate

### equations that need to be considered in further development: 4xcos(x) + 6sin(x), 4cos(x)^2, anything where variable is in the exponent, 69tan(-x)

def combining(eqn, var_type, highest_deg):

	print("in combining", eqn, var_type, highest_deg)

	global oper_dict, solution, sol_cnt
	#Tentative order of terms: ()^c ()/() ()*() c*() ()+-() cos() x^2 x 69
	#Might need to add SQRT()^2 to list 
	#0 compute any low hanging fruit terms ex: cos(x)+3cos(x)+x^2-x^2+x-69x+1+472+2+sin(90)+log(3,3)+3^1 -> cos(x)+3cos(x)+x^2-x^2+x-69x+1+472+2+1+1+1
	
	i = 0
	while i != len(eqn):

		#If this index is an operation in the dictionary
		if eqn[i] in oper_dict.values():

			if eqn[i] == "LOG":

				s=i+2
				j=eqn[s-1]
				j=j.replace('(','')
				temp=""
				while s != ",":

					temp += eqn[s]
					s += 1

				try:

					x = float(temp)
					
					s += 1
					temp=""
					while s != ")"+j:

						temp += eqn[s]
						s += 1

					try:
	
						y = float(temp)
						calc = operation(str(x),eqn[i],str(y))
						eqn[i] = str(calc)
						del eqn[i+1:s]

					except:

						#there is a variable inside this operation and it is not a low hanging fruit
						pass

				except:

					#there is a variable inside this operation and it is not a low hanging fruit
					pass

			else:

				s=i+2
				j=eqn[s-1]
				j=j.replace('(','')
				temp=""
				while eqn[s] != ")"+j:

					temp += eqn[s]
					s += 1

				try:

					x = float(temp)
					calc = operation(0,eqn[i],str(x))
					eqn[i] = str(calc)
					del eqn[i+1:s]

				except:

					#there is a variable inside this operation and it is not a low hanging fruit
					pass

		elif eqn[i] == "^":

			if (is_number(eqn[i-1]) == True) and (is_number(eqn[i+1]) == True):

				calc = operation(eqn[i-1],eqn[i],eqn[i+1])
				eqn[i-1] = str(calc)
				del eqn[i:i+1]

		elif (eqn[i] == "/") or (eqn[i] == "*"):

			if (is_number(eqn[i-1]) == True) and (is_number(eqn[i+1]) == True):

				calc = operation(eqn[i-1],eqn[i],eqn[i+1])
				eqn[i-1] = str(calc)
				del eqn[i:i+1]

		i+=1

	print("after calculating low hanging fruit", eqn)
	#1 put all the terms in descending order (highest exponent to lowest) ex: cos(x)+3cos(x)+x^2-x^2+x-69x+1+472+2+1+1+1

	rearranged=[]
	n=0
	t=0
	while t != len(eqn):

		if eqn[t] == "/":

			if "-" in eqn[t-1]:

				#ex: -2/-x
				if "-" in eqn[t+1]:

					if n == 0:		

						rearranged.insert(n,eqn[t-1])
						rearranged[n] = rearranged[n].replace('-','')
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						rearranged[n] = rearranged[n].replace('-','')
						n+=1

					else:
			
						rearranged.insert(n,"+")
						n=n+1
						rearranged.insert(n,eqn[t-1])
						rearranged[n] = rearranged[n].replace('-','')
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						rearranged[n] = rearranged[n].replace('-','')
						n+=1

				# ex: 2/-x
				else:

					rearranged.insert(n,"-")

					if n == 0:		

						rearranged[n]=rearranged[n]+eqn[t-1]
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

					else:
			
						n=n+1
						rearranged.insert(n,eqn[t-1])
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

			else:
						
				#-2/x
				if "-" in eqn[t+1]:

					rearranged.insert(n,"-")

					if n == 0:		

						rearranged[n]=rearranged[n]+eqn[t-1]
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

					else:
			
						n=n+1
						rearranged.insert(n,eqn[t-1])
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

				#2/x
				else:
						
					if n == 0:

						rearranged.insert(n,eqn[t-1])
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

					else:

						rearranged.insert(n,"+")
						n=n+1
						rearranged.insert(n,eqn[t-1])
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

			del eqn[t-1:t+2]
			#print("eqn is now:",eqn)
			t=-1

		elif eqn[t] == "*":

			if "-" in eqn[t-1]:

				#ex: -2*-x
				if "-" in eqn[t+1]:

					if n == 0:		

						rearranged.insert(n,eqn[t-1])
						rearranged[n] = rearranged[n].replace('-','')
						n=n+1
						rearranged.insert(n,"*")
						n+=1
						rearranged.insert(n,eqn[t+1])
						rearranged[n] = rearranged[n].replace('-','')
						n+=1

					else:
			
						rearranged.insert(n,"+")
						n=n+1
						rearranged.insert(n,eqn[t-1])
						rearranged[n] = rearranged[n].replace('-','')
						n=n+1
						rearranged.insert(n,"*")
						n+=1
						rearranged.insert(n,eqn[t+1])
						rearranged[n] = rearranged[n].replace('-','')
						n+=1

				# ex: 2*-x
				else:

					rearranged.insert(n,"-")

					if n == 0:		

						rearranged[n]=rearranged[n]+eqn[t-1]
						n=n+1
						rearranged.insert(n,"*")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

					else:
			
						n=n+1
						rearranged.insert(n,eqn[t-1])
						n=n+1
						rearranged.insert(n,"*")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

			else:
						
				#-2*x
				if "-" in eqn[t+1]:

					rearranged.insert(n,"-")

					if n == 0:		

						rearranged[n]=rearranged[n]+eqn[t-1]
						n=n+1
						rearranged.insert(n,"*")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

					else:
			
						n=n+1
						rearranged.insert(n,eqn[t-1])
						n=n+1
						rearranged.insert(n,"*")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

				#2*x
				else:
						
					if n == 0:

						rearranged.insert(n,eqn[t-1])
						n=n+1
						rearranged.insert(n,"*")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

					else:

						rearranged.insert(n,"+")
						n=n+1
						rearranged.insert(n,eqn[t-1])
						n=n+1
						rearranged.insert(n,"/")
						n+=1
						rearranged.insert(n,eqn[t+1])
						n+=1

			del eqn[t-1:t+2]
			#print("eqn is now:",eqn)
			t=-1

		t+=1

	print("rearranged", rearranged)
	for t in range(0,len(eqn)):

		var_check=False
		for var in var_type:

			if var in eqn[t]:

				var_check=True

		if var_check == True:
			
			#print("the index is one of the variables", eqn[t])
			check=False
			oper=""
			for op in oper_dict.values():

				if op in eqn[t]:

					check=True
					oper = op

			print(check)
			if check == True:

				if eqn[t-1] == "-":
						
					if "-"+oper in eqn[t]:

						if n == 0:

							rearranged.insert(n,eqn[t])
							n=n+1

						else:

							rearranged.insert(n,"+")
							n=n+1
							rearranged.insert(n,eqn[t])
							n=n+1

					else:

						rearranged.insert(n,"-")

						if n == 0:		

							rearranged[n]=rearranged[n]+eqn[t]
							n=n+1

						else:
			
							n=n+1
							rearranged.insert(n,eqn[t])
							n=n+1

				elif eqn[t-1] == "+":

					if "-"+oper in eqn[t]:

						rearranged.insert(n,"-")

						if n == 0:		

							rearranged[n]=rearranged[n]+eqn[t]
							n=n+1

						else:
			
							n=n+1
							rearranged.insert(n,eqn[t])
							n=n+1

					else:
							
						if n == 0:

							rearranged.insert(n,eqn[t])
							n=n+1

						else:

							rearranged.insert(n,"+")
							n=n+1
							rearranged.insert(n,eqn[t])
							n=n+1

				else:

					if "-"+oper in eqn[t]:

						rearranged.insert(n,"-")

						if n == 0:		

							rearranged[n]=rearranged[n]+eqn[t]
							n=n+1

						else:
			
							n=n+1
							rearranged.insert(n,eqn[t])
							n=n+1

					else:
							
						if n == 0:

							rearranged.insert(n,eqn[t])
							n=n+1

						else:

							rearranged.insert(n,"+")
							n=n+1
							rearranged.insert(n,eqn[t])
							n=n+1
	
	#print(rearranged)
	for s in range(highest_deg,-1,-1):		

		for t in range(0,len(eqn)):

			print(eqn[t], rearranged)
			#print("s > 1?", s>1)
			if s > 1:

				var_check=False
				for var in var_type:

					if var in eqn[t]:

						var_check=True
						work_var=var

				check=False
				for op in oper_dict.values():

					if op in eqn[t]:

						check=True

				if (var_check == True) & ("^"+str(s) in eqn[t]) & (check == False):

					temp = eqn[t]
					v=0
					while temp[v] != work_var:

						v+=1

					v += 2
					b=""
					while v != len(temp):

						b = b+str(temp[v])
						v+=1

					if int(float(b)) == s:

						if eqn[t-1] == "-":
						
							if "-" in eqn[t]:

								if n == 0:

									rearranged.insert(n,eqn[t])
									n=n+1

								else:

									rearranged.insert(n,"+")
									n=n+1
									rearranged.insert(n,eqn[t])
									n=n+1

							else:

								rearranged.insert(n,"-")

								if n == 0:		

									rearranged[n]=rearranged[n]+eqn[t]
									n=n+1

								else:
			
									n=n+1
									rearranged.insert(n,eqn[t])
									n=n+1

						elif eqn[t-1] == "+":

							if "-" in eqn[t]:

								if n == 0:		

									rearranged.insert(n,eqn[t])
									n=n+1

								else:
			
									rearranged.insert(n,"-")
									n=n+1
									rearranged.insert(n,eqn[t])
									rearranged[n] = rearranged[n].replace('-','')
									n=n+1

							else:
							
								if n == 0:

									rearranged.insert(n,eqn[t])
									n=n+1

								else:

									rearranged.insert(n,"+")
									n=n+1
									rearranged.insert(n,eqn[t])
									n=n+1

						else:

							if "-" in eqn[t]:

								if n == 0:		

									rearranged.insert(n,eqn[t])
									n=n+1

								else:
			
									rearranged.insert(n,eqn[t])
									n=n+1

							else:
							
								if n == 0:

									rearranged.insert(n,eqn[t])
									n=n+1

								else:

									rearranged.insert(n,"+")
									n=n+1
									rearranged.insert(n,eqn[t])
									n=n+1

			elif s == 1:

				#print("s was equal to 1")
				var_check=False
				for var in var_type:

					if var in eqn[t]:

						var_check=True
						work_var=var

				check=False
				for op in oper_dict.values():

					if op in eqn[t]:

						check=True

				if (var_check == True) & ("^" not in eqn[t]) & (check == False):

					if eqn[t-1] == "-":
						
						if "-" in eqn[t]:

							if n == 0:

								rearranged.insert(n,eqn[t])
								n=n+1

							else:

								rearranged.insert(n,"+")
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

						else:

							rearranged.insert(n,"-")

							if n == 0:		

								rearranged[n]=rearranged[n]+eqn[t]
								n=n+1

							else:
			
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

					elif eqn[t-1] == "+":

						if "-" in eqn[t]:

							rearranged.insert(n,"-")

							if n == 0:		

								rearranged[n]=rearranged[n]+eqn[t]
								n=n+1

							else:
			
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

						else:
							
							if n == 0:

								rearranged.insert(n,eqn[t])
								n=n+1

							else:

								rearranged.insert(n,"+")
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

					else:

						if "-" in eqn[t]:

							rearranged.insert(n,"-")

							if n == 0:		

								rearranged[n]=rearranged[n]+eqn[t]
								n=n+1

							else:
			
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

						else:
							
							if n == 0:

								rearranged.insert(n,eqn[t])
								n=n+1

							else:

								rearranged.insert(n,"+")
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

			else:

				if is_number(eqn[t]) == True:

					if eqn[t-1] == "-":
					
						if "-" in eqn[t]:

							if n == 0:

								rearranged.insert(n,eqn[t])
								n=n+1

							else:

								rearranged.insert(n,"+")
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

						else:

							rearranged.insert(n,"-")

							if n == 0:		

								rearranged[n]=rearranged[n]+eqn[t]
								n=n+1

							else:
			
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

					elif eqn[t-1] == "+":

						if "-" in eqn[t]:

							rearranged.insert(n,"-")

							if n == 0:		

								rearranged[n]=rearranged[n]+eqn[t]
								n=n+1

							else:
			
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

						else:
							
							if n == 0:

								rearranged.insert(n,eqn[t])
								n=n+1

							else:

								rearranged.insert(n,"+")
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

					else:

						if "-" in eqn[t]:

							rearranged.insert(n,"-")

							if n == 0:		

								rearranged[n]=rearranged[n]+eqn[t]
								n=n+1

							else:
			
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

						else:
							
							if n == 0:

								rearranged.insert(n,eqn[t])
								n=n+1

							else:

								rearranged.insert(n,"+")
								n=n+1
								rearranged.insert(n,eqn[t])
								n=n+1

	print("after rearranging", rearranged)
	#2 add up all similar terms ex: 4cos(x)-68x+478

	t=0
	while t!= len(rearranged):

		if rearranged[t] == "+":

			var_check_one=False
			var_check_two=False

			for var in var_type:

				if var in rearranged[t-1]:

					var_check_one=True

				if var in rearranged[t+1]:

					var_check_two=True

			if (var_check_one == True) & (var_check_two == True):

				check_one=False
				check_two=False
				for op in oper_dict.values():

					if op in rearranged[t-1]:

						check_one=True

					if op in rearranged[t+1]:

						check_two=True


				if (check_one == True) and (check_two == True):

					#it could be this (4sin(x) + 6cos(x))
					temp_one=str(rearranged[t-1])
					temp_two=str(rearranged[t+1])
					v=0
					x=""
					while is_number(temp_one[v]) == True:

						x+=str(temp_one[v])
						v+=1

					if x == "":

						x = "1"

					elif x == "-":

						x = "-1"

					if rearranged[t-2] == "-":

						if "-" in x:

							x = x.replace('-','')

						else:

							x = "-"+x

					x=float(x)

					op=""
					while temp_one[v] != ")":

						op+=str(temp_one[v])
						v+=1

					op+=str(temp_one[v])

					if op in temp_two:

						#same operators and variables so we can add them together
						v=0
						y=""
						while is_number(temp_two[v]) == True:

							y+=str(temp_two[v])
							v+=1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=float(y)
					
						z=x+y

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+op+" + "+str(y)+op+" = "+str(z)+op)
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1
				
						z=str(z)
	
						if float(z) == 0.0:

							del rearranged[t-1:t+2]
							#print(rearranged,rearranged[t])
							if (rearranged[t-1] == "-") or (rearranged[t-1] == "+"):

								del rearranged[t-1]
								t=0

							elif rearranged[t] == "+":

								del rearranged[t]
								t=0

						else:
	
							rearranged[t-1]=z+op
							del rearranged[t:t+2]

							if (rearranged[t-2] == "-") & ("-" in rearranged[t-1]):

								rearranged[t-1] = rearranged[t-1].replace('-','')

							if (rearranged[t-2] == "-") & (float(z) > 0):

								rearranged[t-2] = "+"

							t=0

						string = stringify(rearranged)
						print(string,"\n")

		elif rearranged[t] == "-":

			var_check_one=False
			var_check_two=False

			for var in var_type:

				if var in rearranged[t-1]:

					var_check_one=True

				if var in rearranged[t+1]:

					var_check_two=True

			if (var_check_one == True) & (var_check_two == True):

				check_one=False
				check_two=False
				for op in oper_dict.values():

					if op in rearranged[t-1]:

						check_one=True

					if op in rearranged[t+1]:

						check_two=True


				if (check_one == True) and (check_two == True):

					#it could be this (4sin(x) + 6cos(x))
					temp_one=str(rearranged[t-1])
					temp_two=str(rearranged[t+1])
					v=0
					x=""
					while is_number(temp_one[v]) == True:

						x+=str(temp_one[v])
						v+=1

					if x == "":

						x = "1"

					elif x == "-":

						x = "-1"

					if rearranged[t-2] == "-":

						if "-" in x:

							x = x.replace('-','')

						else:

							x = "-"+x

					x=float(x)

					op=""
					while temp_one[v] != ")":

						op+=str(temp_one[v])
						v+=1

					op+=str(temp_one[v])

					if op in temp_two:

						#same operators and variables so we can add them together
						v=0
						y=""
						while is_number(temp_two[v]) == True:

							y+=str(temp_two[v])
							v+=1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=float(y)
					
						z=x-y

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+op+" - "+str(y)+op+" = "+str(z)+op)
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1
				
						z=str(z)
	
						if float(z) == 0.0:

							del rearranged[t-1:t+2]
							if (rearranged[t-1] == "-") or (rearranged[t-1] == "+"):

								del rearranged[t-1]
								t=0

							elif rearranged[t] == "-":

								del rearranged[t]
								t=0

						else:
	
							rearranged[t-1]=z+op
							del rearranged[t:t+2]

							if (rearranged[t-2] == "-") & ("-" in rearranged[t-1]):

								rearranged[t-1] = rearranged[t-1].replace('-','')

							t=0

						string = stringify(rearranged)
						print(string,"\n")

		t+=1

	work_var_one=""
	work_var_two=""
	for s in range(highest_deg,-1,-1):		

		t=0
		while t!=len(rearranged):

			if s > 1:

				if rearranged[t] == "+":

					work_var=""
					for var in var_type:

						if (var in rearranged[t-1]) and (var in rearranged[t+1]):

							work_var = var

					if ("^"+str(s) in rearranged[t-1]) & ("^"+str(s) in rearranged[t+1]) & (work_var != ""):# and both strings share the same base

						temp_one=str(rearranged[t-1])
						temp_two=str(rearranged[t+1])
						v=0
						x=""
						while temp_one[v] != work_var:

							x=x+str(temp_one[v])
							v=v+1
						
						if x == "":

							x = "1"

						elif x == "-":

							x = "-1"

						if rearranged[t-2] == "-":

							if "-" in x:

								x = x.replace('-','')

							else:

								x = "-"+x

						x=float(x)

						v=0
						y=""
						while temp_two[v] != work_var:

							y=y+str(temp_two[v])
							v=v+1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=float(y)

						z=x+y

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+work_var+"^"+str(s)+" + "+str(y)+work_var+"^"+str(s)+" = "+str(z)+work_var+"^"+str(s))
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1
				
						z=str(z)
	
						if float(z) == 0.0:

							del rearranged[t-1:t+2]
							#print(rearranged,rearranged[t])
							if (rearranged[t-1] == "-") or (rearranged[t-1] == "+"):

								del rearranged[t-1]
								t=0

							elif rearranged[t] == "+":

								del rearranged[t]
								t=0

						else:
	
							rearranged[t-1]=z+work_var+"^"+str(s)
							del rearranged[t:t+2]

							if (rearranged[t-2] == "-") & ("-" in rearranged[t-1]):

								rearranged[t-1] = rearranged[t-1].replace('-','')

							if (rearranged[t-2] == "-") & (float(z) > 0):

								rearranged[t-2] = "+"

							t=0

						string = stringify(rearranged)
						print(string,"\n")

				if rearranged[t] == "-":

					work_var=""
					for var in var_type:

						if (var in rearranged[t-1]) and (var in rearranged[t+1]):

							work_var = var

					if ("^"+str(s) in rearranged[t-1]) & ("^"+str(s) in rearranged[t+1]) & (work_var != ""):# and both strings share the same base

						temp_one=str(rearranged[t-1])
						temp_two=str(rearranged[t+1])
						v=0
						x=""
						while temp_one[v] != work_var:

							x=x+str(temp_one[v])
							v=v+1

						if x == "":

							x = "1"

						elif x == "-":

							x = "-1"

						if rearranged[t-2] == "-":

							if "-" in x:

								x = x.replace('-','')

							else:

								x = "-"+x

						x=float(x)

						v=0
						y=""
						while temp_two[v] != work_var:

							y=y+str(temp_two[v])
							v=v+1

						if y == "":

							y = "1"

						elif y == "-":

							y = "-1"

						y=float(y)
						z=x-y

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+work_var+"^"+str(s)+" + "+str(y)+work_var+"^"+str(s)+" = "+str(z)+work_var+"^"+str(s))
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1

						z=str(z)

						if float(z) == 0.0:

							del rearranged[t-1:t+2]
							if (rearranged[t-1] == "-") or (rearranged[t-1] == "+"):

								del rearranged[t-1]
								t=0

							elif rearranged[t] == "-":

								del rearranged[t]
								t=0

						else:
	
							rearranged[t-1]=z+work_var+"^"+str(s)
							del rearranged[t:t+2]

							if (rearranged[t-2] == "-") & ("-" in rearranged[t-1]):

								rearranged[t-1] = rearranged[t-1].replace('-','')

							t=0

						string = stringify(rearranged)
						print(string,"\n")

			elif int(s) == 1:

				if rearranged[t] == "+":

					var_check_one=False
					var_check_two=False

					for var in var_type:

						if var in rearranged[t-1]:

							var_check_one=True
							work_var_one=var

						if var in rearranged[t+1]:

							var_check_two=True
							work_var_two=var

					if (var_check_one == True) & (var_check_two == True) & ("^" not in rearranged[t-1]) & ("^" not in rearranged[t+1]) & (work_var_one == work_var_two):

						check_one=False
						check_two=False
	
						for op in oper_dict.values():

							if op in rearranged[t-1]:

								check_one=True

							if op in rearranged[t+1]:

								check_two=True

						if (check_one == False) and (check_two == False):

							temp_one=str(rearranged[t-1])
							temp_two=str(rearranged[t+1])
							v=0
							x=""
							while temp_one[v] != work_var_one:

								x=x+str(temp_one[v])
								v=v+1

							if x == "":

								x = "1"

							elif x == "-":

								x = "-1"

							if rearranged[t-2] == "-":

								if "-" in x:

									x = x.replace('-','')

								else:

									x = "-"+x

							x=float(x)

							v=0
							y=""
							while temp_two[v] != work_var_two:

								y=y+str(temp_two[v])
								v=v+1

							if y == "":

								y = "1"

							elif y == "-":

								y = "-1"

							y=float(y)
							z=x+y						

							solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+work_var_one+" + "+str(y)+work_var_one+" = "+str(z)+work_var_one)
							print(solution[sol_cnt])
							sol_cnt=sol_cnt+1

							z=str(z)
	
							if float(z) == 0.0:

								del rearranged[t-1:t+2]
								if (rearranged[t-1] == "-") or (rearranged[t-1] == "+"):

									del rearranged[t-1]
									t=0

								elif rearranged[t] == "+":

									del rearranged[t]
									t=0

							else:
	
								rearranged[t-1]=z+work_var_one
								del rearranged[t:t+2]

								if (rearranged[t-2] == "-") & ("-" in rearranged[t-1]):

									rearranged[t-1] = rearranged[t-1].replace('-','')

								t=0

							string = stringify(rearranged)
							print(string,"\n")

				if rearranged[t] == "-":

					var_check_one=False
					var_check_two=False

					for var in var_type:

						if var in rearranged[t-1]:

							var_check_one=True
							work_var_one=var

						if var in rearranged[t+1]:

							var_check_two=True
							work_var_two=var

					if (var_check_one == True) & (var_check_two == True) & ("^" not in rearranged[t-1]) & ("^" not in rearranged[t+1]) & (work_var_one == work_var_two):

						check_one=False
						check_two=False
	
						for op in oper_dict.values():

							if op in rearranged[t-1]:

								check_one=True

							if op in rearranged[t+1]:

								check_two=True

						if (check_one == False) and (check_two == False):

							temp_one=str(rearranged[t-1])
							temp_two=str(rearranged[t+1])
							v=0
							x=""
							while temp_one[v] != work_var_one:

								x=x+str(temp_one[v])
								v=v+1

							if x == "":

								x = "1"

							elif x == "-":

								x = "-1"

							if rearranged[t-2] == "-":

								if "-" in x:

									x = x.replace('-','')

								else:

									x = "-"+x

							x=float(x)

							v=0
							y=""
							while temp_two[v] != work_var_two:

								y=y+str(temp_two[v])
								v=v+1

							if y == "":

								y = "1"

							elif y == "-":

								y = "-1"

							y=float(y)
							z=x-y

							solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+work_var_one+" - "+str(y)+work_var_one+" = "+str(z)+work_var_one)
							print(solution[sol_cnt])
							sol_cnt=sol_cnt+1

							z=str(z)

							if float(z) == 0.0:

								del rearranged[t-1:t+2]
								if (rearranged[t-1] == "-") or (rearranged[t-1] == "+"):

									del rearranged[t-1]
									t=0

								elif (rearranged[t-2] == "-") or (rearranged[t-2] == "+"):

									del rearranged[t-2]
									t=0

								elif rearranged[t] == "-":

									del rearranged[t]
									t=0

							else:
	
								rearranged[t-1]=z+work_var_one
								del rearranged[t:t+2]
							
								if (rearranged[t-2] == "-") & ("-" in rearranged[t-1]):

									rearranged[t-1] = rearranged[t-1].replace('-','')

								t=0

							string = stringify(rearranged)
							print(string,"\n")

			else:

				if rearranged[t] == "+":

					if (is_number(rearranged[t-1]) == True) and (is_number(rearranged[t+1]) == True):

						x=float(rearranged[t-1])
						y=float(rearranged[t+1])
						z=x+y						

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+" + "+str(y)+" = "+str(z))
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1

						z=str(z)
	
						if float(z) == 0.0:

							del rearranged[t-1:t+2]
							if (rearranged[t-1] == "-") or (rearranged[t-1] == "+"):

								del rearranged[t-1]
								t=0

							elif rearranged[t] == "+":

								del rearranged[t]
								t=0

						else:
	
							rearranged[t-1]=z
							del rearranged[t:t+2]

							if (rearranged[t-2] == "-") & ("-" in rearranged[t-1]):

								rearranged[t-1] = rearranged[t-1].replace('-','')

							t=0

						string = stringify(rearranged)
						print(string,"\n")

				if rearranged[t] == "-":

					if (is_number(rearranged[t-1]) == True) and (is_number(rearranged[t+1]) == True):

						x=float(rearranged[t-1])
						y=float(rearranged[t+1])
						z=x-y

						solution.insert(sol_cnt,"OP"+str(sol_cnt)+"___ "+str(x)+" - "+str(y)+" = "+str(z))
						print(solution[sol_cnt])
						sol_cnt=sol_cnt+1

						z=str(z)

						if float(z) == 0.0:

							del rearranged[t-1:t+2]
							if (rearranged[t-1] == "-") or (rearranged[t-1] == "+"):

								del rearranged[t-1]
								t=0

							elif (rearranged[t-2] == "-") or (rearranged[t-2] == "+"):

								del rearranged[t-2]
								t=0

							elif rearranged[t] == "-":

								del rearranged[t]
								t=0

						else:
	
							rearranged[t-1]=z
							del rearranged[t:t+2]
							
							if (rearranged[t-2] == "-") & ("-" in rearranged[t-1]):

								rearranged[t-1] = rearranged[t-1].replace('-','')

							t=0

						string = stringify(rearranged)
						print(string,"\n")

			t=t+1

	rearranged.insert(0,eqn[0])
	rearranged.append(eqn[len(eqn)-1])
	return rearranged


def is_number(s):

	try:
			
		float(s)
		return True

	except ValueError:
		
		try:

			complex(s)
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

def stringify(l):

	temp=""
	for s in range(1,len(l)-1):

		if ("(" in str(l[s])) and ("j" not in str(l[s])):
		
			temp += "("

		elif (")" in str(l[s])) and ("j" not in str(l[s])):
	
			temp += ")"

		else:

			temp=temp+str(l[s])

	return temp

def lower_b_lvl(b, lvl):

	print("lvl", lvl)

	for i in range(0,len(b)):

		if "(" in b[i]:

			b[i] = "("

		if ")" in b[i]:

			b[i] = ")"

	br = 0
	for i in range(0,len(b)):

		if "(" in b[i]:

			br += 1
			b[i] = "("+str(br)

		if ")" in b[i]:

			b[i] = ")"+str(br)
			br -= 1

	print(b)

	return b

#This function groups terms around variables into a single index
def grouping(eqn):

	global oper_dict

	#print("Inside grouping", eqn)
	#Start with combining with constants and powers into one index
	i=0
	p=0
	b=0
	p_b=0
	var=[]
	b_open=0
	b_close=0
	b_loc=0
	while i != len(eqn):

		mod = False
		#print(eqn)
		#This index has a variable in it
		if ("(" in eqn[i]) & (eqn[i] not in oper_dict.values()):

			b+=1
			b_open += 1
			b_loc = i

			for op in oper_dict.values():

				if op == eqn[i-1]:

					p_b=b
					p=i

		if (")" in eqn[i]) & (eqn[i] not in oper_dict.values()):

			if eqn[i] == ")"+str(p_b):

				p_b=0
				p=0

			b-=1
			b_close += 1

		if (eqn[i].isalpha() == True) and (len(eqn[i]) == 1):

			#print("eqn[i]", eqn[i])
			if eqn[i] not in var:

				var.append(eqn[i])

			if (eqn[i+1] == "^") and (is_number(eqn[i+2]) == True):

				eqn[i] = eqn[i]+"^"+eqn[i+2]
				del eqn[i+1:i+3]
				mod = True
				#print(eqn)

			if (is_number(eqn[i-1]) == True):
	
				eqn[i-1] = eqn[i-1]+eqn[i]
				del eqn[i]
				mod = True
				#print(eqn)

			if (eqn[i-1] == "*") and (is_number(eqn[i-2]) == True):

				eqn[i-2] = eqn[i-2]+eqn[i]
				del eqn[i-1:i+1]
				mod = True
				#print(eqn)

			if ((b_open != b_close) and (eqn[b_loc-1] in oper_dict.values())) or (p != 0):

				if p != 0:

					b_loc = p

				temp=eqn[b_loc-1]
				#print(temp)
				j=eqn[b_loc]
				j=j.replace('(','')
				u=b_loc
				while eqn[u] != ")"+j:

					if "(" in eqn[u]:

						temp+="("

					elif ")" in eqn[u]:

						temp+=")"

					else:
					
						temp+=eqn[u]

					u+=1

				temp+=")"
				eqn[b_loc-1]=temp
				del eqn[b_loc:u+1]
				#print("eqn[b_loc]",eqn[b_loc])
				
				if (eqn[b_loc] == "^") and (is_number(eqn[b_loc+1]) == True):

					temp = eqn[b_loc-1]+"^"+eqn[b_loc+1]
					eqn[b_loc-1] = temp
					del eqn[b_loc:b_loc+2]

				mod = True
				#print(eqn)

			if mod == True:

				i = 0

		i += 1

	#This section of code was added because when grouping is fed an equation that is already grouped, it fails
	#print("Made it here", eqn)
	if len(var) == 0:

		for i in range(0,len(eqn)):

			
			if ("(" not in eqn[i]) and (")" not in eqn[i]) and (eqn[i] not in "*/+-") and (is_number(eqn[i]) == False):

				check = False
				oper=""
				for op in oper_dict.values():

					if op in eqn[i]:
					
						check == True
						oper = op

				if check == False:

					if "^" in eqn[i]:

						temp = eqn[i]
						j = 0
						while temp[j] != "^":

							j+=1

						j-=1
						if temp[j] not in var:

							var.append(temp[j])

					else:

						temp = eqn[i]
						x = temp[len(temp)-1]

						if x not in var:

							var.append(x)
		
				else:

					temp = eqn[i]
					temp = temp.replace(oper,'')
					j = 0
					x = ""
					while j != len(temp):

						if temp[j].isalpha() == True:

							x = temp[j]

						j+=1

					if x != "":

						if x not in var:

							var.append(x)					

	#print("Now we here", eqn)
	eqn_deg=[]
	for s in eqn:

		for t in var:

			if t in s:

				if "^" in s:

					check = False
					for op in oper_dict.values():

						if op in s:

							check = True

					if check == False:

						q=0
						temp = s
						#print("temp",temp)

					
						while temp[q] != "^":
			
							q+=1

						q+=1
						pow=""
						while (q != len(temp)):

							if (is_number(temp[q]) == True) or (temp[q] == "."):

								pow+= temp[q]
								#print(pow, "q = "+str(q), "len(temp) = "+str(len(temp)))
								q+=1

						pow = int(float(pow))

						if pow not in eqn_deg:
					
							eqn_deg.append(pow)
							#print(s, eqn_deg)

				else:

					check = False
					for op in oper_dict.values():

						if op in s:

							check = True

					if check == False:

						if 1 not in eqn_deg:

							eqn_deg.append(1)
							#print(s, eqn_deg)

		if is_number(s) == True:

			if 0 not in eqn_deg:

				eqn_deg.append(0)
				#print(s, eqn_deg)

	#print("eqn_deg", eqn_deg, eqn)
	new_eqn_deg=[]
	s = 0
	while s != len(eqn_deg):

		k=0

		for t in eqn_deg:

			if eqn_deg[s] < t:

				k=1

		if k != 1:

			new_eqn_deg.append(eqn_deg[s])
			del eqn_deg[s]
			s=-1

		s+=1

	if len(eqn) > 1:

		if eqn[1] == "-":

			eqn[1] = eqn[1]+eqn[2]
			del eqn[2]

	#print("new_eqn_deg", new_eqn_deg)
	return eqn, new_eqn_deg

#*** Add or subtract two bracket expressions***
#** br_one - is a list item not a string
#** op - is either "+" or "-". If op is anything else, Returns an error
#** br_two - is a list item not a string
#** var - is a single string of the variable that is common to both bracket expression, ex: "x"

def bracket_add(br_one, op, br_two, var):

	if op not in "+-":

		return Error

	br_one, br_one_deg = grouping(br_one)
	br_two, br_two_deg = grouping(br_two)

	br_one = Poly_Func(br_one)
	br_one_coeff = br_one.get_coeff(br_one_deg[0], var)

	br_two = Poly_Func(br_two)
	br_two_coeff = br_two.get_coeff(br_two_deg[0], var)

	ans_coeff=[]

	#print("br_one_deg = "+str(br_one_deg[0]))
	#print("br_two_deg = "+str(br_two_deg[0]))

	if op == "+":

		if br_one_deg[0] > br_two_deg[0]:

			for i in range(0,br_two_deg[0]+1):

				#print(i)
				ans_coeff.insert(0,br_one_coeff.eqn[len(br_one_coeff.eqn)-1-i]+br_two_coeff.eqn[len(br_two_coeff.eqn)-1-i])

			i+=1
			while len(br_one_coeff.eqn)-1-i != -1:

				#print(i)
				ans_coeff.insert(0,br_one_coeff.eqn[len(br_one_coeff.eqn)-1-i])
				i+=1

		elif br_two_deg[0] > br_one_deg[0]:

			for i in range(0,br_one_deg[0]+1):

				ans_coeff.insert(0,br_one_coeff.eqn[len(br_one_coeff.eqn)-1-i]+br_two_coeff.eqn[len(br_two_coeff.eqn)-1-i])

			i+=1
			while len(br_two_coeff.eqn)-1-i != -1:

				ans_coeff.insert(0,br_two_coeff.eqn[len(br_two_coeff.eqn)-1-i])
				i+=1

		else:

			for i in range(0,br_one_deg[0]+1):

				ans_coeff.insert(0,br_one_coeff.eqn[len(br_one_coeff.eqn)-1-i]+br_two_coeff.eqn[len(br_two_coeff.eqn)-1-i])

	elif op == "-":

		if br_one_deg[0] > br_two_deg[0]:

			for i in range(0,br_two_deg[0]+1):

				ans_coeff.insert(0,br_one_coeff.eqn[len(br_one_coeff.eqn)-1-i]-br_two_coeff.eqn[len(br_two_coeff.eqn)-1-i])

			i+=1
			while len(br_one_coeff.eqn)-1-i != -1:

				ans_coeff.insert(0,br_one_coeff.eqn[len(br_one_coeff.eqn)-1-i])
				i+=1

		elif br_two_deg[0] > br_one_deg[0]:

			for i in range(0,br_one_deg[0]+1):

				ans_coeff.insert(0,br_one_coeff.eqn[len(br_one_coeff.eqn)-1-i]-br_two_coeff.eqn[len(br_two_coeff.eqn)-1-i])

			i+=1
			while len(br_two_coeff.eqn)-1-i != -1:

				ans_coeff.insert(0,0-br_two_coeff.eqn[len(br_two_coeff.eqn)-1-i])
				i+=1

		else:

			for i in range(0,br_one_deg[0]+1):

				ans_coeff.insert(0,br_one_coeff.eqn[len(br_one_coeff.eqn)-1-i]-br_two_coeff.eqn[len(br_two_coeff.eqn)-1-i])

	ans=[]
	j=0
	highest_deg_ans = len(ans_coeff)-1

	if highest_deg_ans > 1:

		for i in range(highest_deg_ans,1,-1):

			if not ans:
			
				if ans_coeff[j] == 1:

					ans.append(var)
					ans.append("^")
					ans.append(str(float(i)))
					j+=1

				elif ans_coeff[j] == 0:

					pass
					j+=1

				elif ans_coeff[j] < 0:

					if ans_coeff[j] == -1:

						ans.append("-"+var)
						ans.append("^")
						ans.append(str(float(i)))
						j+=1

					else:

						ans.append(str(ans_coeff[j]))
						ans.append(var)
						ans.append("^")
						ans.append(str(float(i)))
						j+=1

				else:

					ans.append(str(ans_coeff[j]))
					ans.append(var)
					ans.append("^")
					ans.append(str(float(i)))
					j+=1

			else:

				if ans_coeff[j] == 1:
					
					ans.append("+")
					ans.append(var)
					ans.append("^")
					ans.append(str(float(i)))
					j+=1

				elif ans_coeff[j] == 0:

					pass
					j+=1

				elif ans_coeff[j] < 0:

					if ans_coeff[j] == -1:

						ans.append("-")
						ans.append(var)
						ans.append("^")
						ans.append(str(float(i)))
						j+=1

					else:

						ans.append("-")
						ans.append(str(abs(ans_coeff[j])))
						ans.append(var)
						ans.append("^")
						ans.append(str(float(i)))
						j+=1

				else:

					ans.append("+")
					ans.append(str(ans_coeff[j]))
					ans.append(var)
					ans.append("^")
					ans.append(str(float(i)))
					j+=1

		if ans_coeff[j] == 1:

			ans.append("+")
			ans.append(var)
			j+=1

		elif ans_coeff[j] == 0:

			pass
			j+=1

		elif ans_coeff[j] < 0:

			if ans_coeff[j] == -1:

				ans.append("-")
				ans.append(var)
				j+=1

			else:

				ans.append("-")
				ans.append(str(abs(ans_coeff[j])))
				ans.append(var)
				j+=1

		else:
 
			ans.append("+")
			ans.append(str(ans_coeff[j]))
			ans.append(var)
			j+=1

		if ans_coeff[j] == 0:

			pass

		else:

			if ans_coeff[j] < 0:

				ans.append("-")
				ans.append(str(abs(ans_coeff[j])))

			else:
	
				ans.append("+")
				ans.append(str(ans_coeff[j]))

	else:

		if ans_coeff[j] == 1:

			ans.append("+")
			ans.append(var)
			j+=1
			
		elif ans_coeff[j] == 0:

			pass
			j+=1

		elif ans_coeff[j] < 0:

			if ans_coeff[j] == -1:

				ans.append("-")
				ans.append(var)
				j+=1

			else:

				ans.append("-")
				ans.append(str(abs(ans_coeff[j])))
				ans.append(var)
				j+=1


		else:

			ans.append("+")
			ans.append(str(ans_coeff[j]))
			ans.append(var)
			j+=1

		if ans_coeff[j] == 0:

			pass

		else:

			if ans_coeff[j] < 0:

				ans.append("-")
				ans.append(str(abs(ans_coeff[j])))

			else:
	
				ans.append("+")
				ans.append(str(ans_coeff[j]))

	return ans

#This function takes two brackets in array form and foils them out.
#Both brackets must be of minimum degree 1
def foiling(b_one, b_two, var_type):

	#print(b_one,b_two)

	b_one, b_one_deg = grouping(b_one)
	#print("b_one", b_one, "b_one_deg", b_one_deg)

	b_two, b_two_deg = grouping(b_two)
	#print("b_two", b_two, "b_two_deg", b_two_deg)

	#Create array with only coefficients
	b_one = Poly_Func(b_one)
	b_one_coeff = b_one.get_coeff(b_one_deg[0],var_type)

	b_two = Poly_Func(b_two)
	b_two_coeff = b_two.get_coeff(b_two_deg[0],var_type)

	#print("b_one_coeff = ", b_one_coeff.eqn, "b_two_coeff = ", b_two_coeff.eqn) 

	ans_coeff=[]
	ans_powers=[]
	b_one_pow=len(b_one_coeff.eqn)-1
	b_two_pow=len(b_two_coeff.eqn)-1

	#Foiling
	for i in range(0,len(b_one_coeff.eqn)):

		for j in range(0,len(b_two_coeff.eqn)):

			ans_coeff.append(b_one_coeff.eqn[i]*b_two_coeff.eqn[j])
			ans_powers.append((b_one_pow-i)+(b_two_pow-j))

	#print("ans_coeff = ", ans_coeff)
	#Simplifying the answer
	simp_ans_coeff=[]
	temp_ind=[]
	temp=0
	for i in range(ans_powers[0],-1,-1):

		for j in range(0,len(ans_powers)):

			if ans_powers[j] == i:

				temp+=ans_coeff[j]

		simp_ans_coeff.append(temp)
		temp=0

	#print("simp_ans_coeff = ", simp_ans_coeff)
	ans=[]
	j=0
	highest_deg_ans = len(simp_ans_coeff)-1

	if highest_deg_ans > 1:

		for i in range(highest_deg_ans,1,-1):

			if not ans:

				if simp_ans_coeff[j].imag == 0:
			
					if simp_ans_coeff[j] == 1:

						ans.append(var_type)
						ans.append("^")
						ans.append(str(float(i)))
						j+=1

					elif simp_ans_coeff[j] == 0:

						pass
						j+=1

					elif simp_ans_coeff[j] < 0:

						if simp_ans_coeff[j] == -1:

							ans.append("-"+var_type)
							ans.append("^")
							ans.append(str(float(i)))
							j+=1

						else:

							ans.append(str(simp_ans_coeff[j]))
							ans.append(var_type)
							ans.append("^")
							ans.append(str(float(i)))
							j+=1

					else:

						ans.append(str(simp_ans_coeff[j]))
						ans.append(var_type)
						ans.append("^")
						ans.append(str(float(i)))
						j+=1

				#simp_coeff_ans[j] is a complex number
				else:

					ans.append(str(simp_ans_coeff[j]))
					ans.append(var_type)
					ans.append("^")
					ans.append(str(float(i)))
					j+=1

			else:

				if simp_ans_coeff[j].imag == 0:
				
					if simp_ans_coeff[j] == 1:
					
						ans.append("+")
						ans.append(var_type)
						ans.append("^")
						ans.append(str(float(i)))
						j+=1

					elif simp_ans_coeff[j] == 0:

						pass
						j+=1

					elif simp_ans_coeff[j] < 0:

						if simp_ans_coeff[j] == -1:

							ans.append("-")
							ans.append(var_type)
							ans.append("^")
							ans.append(str(float(i)))
							j+=1

						else:

							ans.append("-")
							ans.append(str(abs(simp_ans_coeff[j])))
							ans.append(var_type)
							ans.append("^")
							ans.append(str(float(i)))
							j+=1

					else:

						ans.append("+")
						ans.append(str(simp_ans_coeff[j]))
						ans.append(var_type)
						ans.append("^")
						ans.append(str(float(i)))
						j+=1

				#simp_coeff_ans[j] is a complex number
				else:

					ans.append("+")
					ans.append(str(simp_ans_coeff[j]))
					ans.append(var_type)
					ans.append("^")
					ans.append(str(float(i)))
					j+=1

		if simp_ans_coeff[j].imag == 0:

			if simp_ans_coeff[j] == 1:

				ans.append("+")
				ans.append(var_type)
				j+=1

			elif simp_ans_coeff[j] == 0:

				pass
				j+=1

			elif simp_ans_coeff[j] < 0:

				if simp_ans_coeff[j] == -1:

					ans.append("-")
					ans.append(var_type)
					j+=1

				else:

					ans.append("-")
					ans.append(str(abs(simp_ans_coeff[j])))
					ans.append(var_type)
					j+=1

			else:
 
				ans.append("+")
				ans.append(str(simp_ans_coeff[j]))
				ans.append(var_type)
				j+=1

		else:

			ans.append("+")
			ans.append(str(simp_ans_coeff[j]))
			ans.append(var_type)
			j+=1

		if simp_ans_coeff[j].imag == 0:

			if simp_ans_coeff[j] == 0:

				pass

			else:

				if simp_ans_coeff[j] < 0:

					ans.append("-")
					ans.append(str(abs(simp_ans_coeff[j])))

				else:
	
					ans.append("+")
					ans.append(str(simp_ans_coeff[j]))

		else:

			ans.append("+")
			ans.append(str(simp_ans_coeff[j]))

	else:

		if not ans:

			if simp_ans_coeff[j].imag == 0:

				if simp_ans_coeff[j] == 1:

					ans.append(var_type)
					j+=1
			
				elif simp_ans_coeff[j] == 0:

					pass
					j+=1

				elif simp_ans_coeff[j] < 0:

					if simp_ans_coeff[j] == -1:

						ans.append("-")
						ans.append(var_type)
						j+=1

					else:

						ans.append("-")
						ans.append(str(abs(simp_ans_coeff[j])))
						ans.append(var_type)
						j+=1

				else:

					ans.append(str(simp_ans_coeff[j]))
					ans.append(var_type)
					j+=1

			else:

				ans.append(str(simp_ans_coeff[j]))
				ans.append(var_type)
				j+=1

		else:

			if simp_ans_coeff[j].imag == 0:

				if simp_ans_coeff[j] == 1:

					ans.append("+")
					ans.append(var_type)
					j+=1
			
				elif simp_ans_coeff[j] == 0:

					pass
					j+=1

				elif simp_ans_coeff[j] < 0:

					if simp_ans_coeff[j] == -1:

						ans.append("-")
						ans.append(var_type)
						j+=1

					else:

						ans.append("-")
						ans.append(str(abs(simp_ans_coeff[j])))
						ans.append(var_type)
						j+=1

				else:

					ans.append("+")
					ans.append(str(simp_ans_coeff[j]))
					ans.append(var_type)
					j+=1

			else:

				ans.append("+")
				ans.append(str(simp_ans_coeff[j]))
				ans.append(var_type)
				j+=1

		if simp_ans_coeff[j].imag == 0:

			if simp_ans_coeff[j] == 0:

				pass

			else:

				if simp_ans_coeff[j] < 0:

					ans.append("-")
					ans.append(str(abs(simp_ans_coeff[j])))

				else:
	
					ans.append("+")
					ans.append(str(simp_ans_coeff[j]))

		else:

			ans.append("+")
			ans.append(str(simp_ans_coeff[j]))

	#print("ans = ", ans)
	return ans		


def bracketing(LHS,RHS,var_type):

	global var_dict

	#LHS first
	
	b=0
	b_open=0
	b_close=0
	bracket_lvl_l=0
	bracket_master_l=[]
	bracket=[]
	bracket_master=[]
	i_master_l=[]
	foil=False
	

	for s in range(0,len(LHS)):

		if "(" in LHS[s]:

			b += 1
			i = s
			b_open += 1
			bracket_lvl_l += 1

		if ")" in LHS[s]:

			b -= 1
			b_close += 1

		#if there's a variable inside a bracket other than (1
		if (var_type[0] in LHS[s]) and (b_open > 1) and (b_open != b_close):
			
			bracket.append("(")
			k=i+1
			while ")"+str(bracket_lvl_l) not in LHS[k]:

				bracket.append(LHS[k])
				k += 1

			bracket.append(")")
			i_master_l.append(i)
			bracket_master_l.append(bracket)

			if bracket not in bracket_master:

				bracket_master.append(bracket)

			bracket.clear()

	#RHS
	
	b=0
	b_open=0
	b_close=0
	bracket_lvl_r=0
	bracket_master_r=[]
	i_master_r=[]

	for s in range(0,len(RHS)):

		if "(" in RHS[s]:

			b += 1
			i = s
			b_open += 1
			bracket_lvl_r += 1

		if ")" in RHS[s]:

			b -= 1
			b_close += 1

		#if there's a variable inside a bracket other than (1
		if (var_type[0] in RHS[s]) and (b_open > 1) and (b_open != b_close):
			
			bracket.append("(")
			k=i+1
			while ")"+str(bracket_lvl_r) not in RHS[k]:

				bracket.append(RHS[k])
				k += 1

			bracket.append(")")
			i_master_r.append(i)
			bracket_master_r.append(bracket)

			if bracket not in bracket_master:

				bracket_master.append(bracket)

			bracket.clear()

	#Check if there are any duplicates at all
	duplicate=False
	dup_cnt=0
	dupes=[]
	temp=[]
	for i in range(0,len(bracket_master_l)):

		temp.clear()
		temp=bracket_master_l
		del temp[i]

		for j in range(0,len(temp)):

			if bracket_master_l[i] == temp[j]:

				duplicate = True
				dup_cnt += 1

				if bracket_master_l[i] not in dupes:

					dupes.append(stringify(bracket_master_l[i]))

		for j in range(0,len(bracket_master_r)):

			if bracket_master_l[i] == bracket_master_r[j]:

				duplicate = True
				dup_cnt += 1
				
				if bracket_master_l[i] not in dupes:

					dupes.append(stringify(bracket_master_l[i]))

	for i in range(0,len(bracket_master_r)):

		for j in range(0,len(bracket_master_l)):

			if bracket_master_r[i] == bracket_master_l[j]:

				duplicate = True
				dup_cnt += 1

				if bracket_master_r[i] not in dupes:

					dupes.append(stringify(bracket_master_r[i]))

		temp.clear()
		temp=bracket_master_r
		del temp[i]

		for j in range(0,len(temp)):

			if bracket_master_r[i] == temp[j]:

				duplicate = True
				dup_cnt += 1

				if bracket_master_r[i] not in dupes:

					dupes.append(stringify(bracket_master_r[i]))

	if duplicate == True:

		if dup_cnt == 1:

			if len(bracket_master) == 1:

				#we can substitute directly
				
				#First lets get a string of the equation
				string_eqn = stringify(LHS)
				string_eqn += "="+stringify(RHS)

				#Second lets replace the bracket by a variable that isn't the inputted variable
				string_eqn = string_eqn.replace(dupes[0],var_dict[var_type])

				#!!!! Call the bracketify function !!!!
				#return bracketified eqn

			#There may be duplicates but they can't be substituted easily so we simply foil out the equation to remove the brackets
			else:

				#First we walk LHS and RHS and foil any brackets multiplied by any constants

				#Maybe we should work our way outwards. Start with inner most constant, bracket pairs and work outwards
				#Go through each side of the eqn, find highest bracket number. Then search for these pairs for every bracket number
				#in descending order.

				#*** What if the bracket has an exponent? You can't multiply the constant... -_-				

				for j in range(bracket_lvl_l,0,-1):

					t=0
					while t != len(LHS):

						if (LHS[t] == "("+str(j)) and (LHS[t-1] == "*") and (is_number(LHS[t-2]) == True):

							x=["(1"]
							x.append(LHS[t-2])
							x.append(")1")
							br=[]
							s=t
							while s != ")"+str(bracket_lvl_l):

								br.append(LHS[s])
								s+=1

							br.append(LHS[s])

							br, br_deg = grouping(br,var_type)
							result = foiling(x,br,var_type)

							y = t-2
							del LHS[y:s]
							for k in result:

								LHS.insert(y,k)

				for j in range(bracket_lvl_r,0,-1):

					t=0
					while t != len(RHS):

						if (RHS[t] == "("+str(j)) and (RHS[t-1] == "*") and (is_number(RHS[t-2]) == True):

							x=["(1"]
							x.append(RHS[t-2])
							x.append(")1")
							br=[]
							s=t
							while s != ")"+str(bracket_lvl_r):

								br.append(RHS[s])
								s+=1

							br.append(RHS[s])

							br, br_deg = grouping(br,var_type)
							result = foiling(x,br,var_type)

							y = t-2
							del RHS[y:s]
							for k in result:

								RHS.insert(y,k)
				
				#Next is to foil out any brackets ex: (2x+1)(3x+2)... wait what do we do with (2x+1)((3x+4)/(4x+5))
						  
				
				#Find the relationship between duplicates
				#for i in dupes:
				

				

		else:
		
			#do a substitution and then foil and try calculating
			pass

	else:

		#there still might be a relationship. If not, then call the foil function because there are no duplicates at all
		pass
			
			

def isolate(l, r, lvl, var_type):

	global var_index_l, var_index_r, oper_dict_two, solution, sol_cnt
	
	op=""
	op1=""

	#print(l,r)

	#Simplify both sides of equation
	
	simp_l = combining(l)
	simp_r = combining(r)	

	#Grouping
	#LHS
	bracket=["0"]
	bracket_temp=""
	b=0
	b_open = 0
	b_close = 0
	bracket_lvl = 1
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
							b += 1

						if ")" in simp_l[z]:

							bracket_temp += ")"
							b -= 1

						else:

							bracket_temp += simp_l[z] 
							bracket.append(str(simp_l[z]))
							
						z += 1

					z += 1
					bracket.append(")"+str(b))
					bracket_temp += ")"
					#print("bracket",bracket)
					
					if simp_l[i-1] in anti_dict:
			
						bracket.insert(0,simp_l[i-1])
						bracket_temp = simp_l[i-1] + bracket_temp
						simp_l[i-1] = var_type[0]
						del simp_l[i:z+1]
						s=-1
						b=0
						b_open = 0
						b_close = 0

					else:

						simp_l[i] = var_type[0]
						del simp_l[i+1:z]
						print("HEYHEYHEY", simp_l, bracket, bracket_temp)
						s=-1
						b=0
						b_open = 0
						b_close = 0
						#print("4",simp_l)

					bracket_lvl += 1

	
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
					bracket_lvl += 1

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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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

		if (var_type[0] not in simp_l[v]) & (is_number(simp_l[v]) == True) & (simp_l[v-1] not in oper_dict_two.values()) & (simp_l[v+1] not in oper_dict_two.values()): #& you're not within variable bracket range
	
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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
					string = stringify(simp_l)
					string += "="+stringify(simp_r)
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

						string = stringify(rear_l)
						string += "="+stringify(simp_r)
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

						string = stringify(rear_l)
						string += "="+stringify(simp_r)
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

						string = stringify(rear_l)
						string += "="+stringify(simp_r)
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

						string = stringify(rear_l)
						string += "="+stringify(simp_r)
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

				string = stringify(rear_l)
				string += "="+stringify(simp_r)
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

				string = stringify(rear_l)
				string += "="+stringify(simp_r)
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

				string = stringify(rear_l)
				string += "="+stringify(simp_r)
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

				string = stringify(rear_l)
				string += "="+stringify(simp_r)
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

				string = stringify(rear_l)
				string += "="+stringify(simp_r)
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

				string = stringify(rear_l)
				string += "="+stringify(simp_r)
				print(string,"\n")
				solution.insert(sol_cnt,string)
				sol_cnt += 1
			
			t=t+1

		#print(rear_l,simp_r)

		if bracket[0] == "0":

			ans=[]
			ans.insert(0,var_type[0]+" = "+str(simp_r[1]))
			return ans

		else:

			solution.insert(sol_cnt,"-- Reintroducing "+bracket_temp+" --")
			print(solution[sol_cnt],"\n")
			sol_cnt=sol_cnt+1
			string = stringify(bracket)
			string += "="+stringify(simp_r)
			print(string)
			solution.insert(sol_cnt,string)
			sol_cnt += 1
			simp_r[1] = str(simp_r[1])
			bracket = lower_b_lvl(bracket,bracket_lvl)
			ans = isolate(bracket,simp_r,0, var_type)
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

			ans[s] = var_type[0]+" = "+str(ans[s])		

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

			ans[s] = var_type[0]+" = "+str(ans[s])
		

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

			ans[s] = var_type[0]+" = "+str(ans[s])
		
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

		string = stringify(rear_l.eqn)
		string += "="+stringify(simp_r)
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

				ans.insert(0,var_type+" = 0")
					

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

			ans[i] = var_type[0]+" = "+str(ans[i]) 

		return ans

def imaginary_num(br):

	i=0
	mod_chk = False
	br_copy = br[:]
	while i != len(br_copy):

		if (")" in br_copy[i]) and (br_copy[i] != ")1") and (br_copy[i-1] == "j") and (is_number(br_copy[i-2]) == True):

			b = br_copy[i]
			b = b.replace(')','')
			b = int(b)
			k = i-1
			temp = []
			while br_copy[k] != "("+str(b):

				temp.insert(0,br_copy[k])
				k -= 1

			temp_string = ""
			for s in temp:

				temp_string += s

			temp = temp_string

			#print("temp = "+temp, is_number(temp))
			#let's double check it is an imaginary number
			if is_number(temp) == True:

				#print("It's a number")
				if isinstance(complex(temp), complex) == True:
	
					del br_copy[k:i]
					br_copy[k] = temp
					mod_chk = True
					i = -1

		if (")" in br_copy[i]) and (br_copy[i] == ")1") and (br_copy[i-1] == "j") and (is_number(br_copy[i-2]) == True):

			b = br_copy[i]
			b = b.replace(')','')
			b = int(b)
			k = i-1
			temp = []
			while br_copy[k] != "("+str(b):

				if ")" in br_copy[k]:

					temp.insert(0,")")

				else:

					temp.insert(0,br_copy[k])

				k -= 1

			temp_string = ""
			for s in temp:

				temp_string += s

			temp = temp_string

			#print("temp = "+temp, is_number(temp))
			#let's double check it is an imaginary number
			if is_number(temp) == True:

				#print("It's a number")
				if isinstance(complex(temp), complex) == True:
	
					del br_copy[k+1:i]
					br_copy.insert(k+1, temp)
					mod_chk = True
					i = -1

		i += 1

	if mod_chk == True:

		br = br_copy[:]

	return br

def bracketify(a):

	#Gotta add a check for imaginary numbers

	master=[]
	numtemp=[]
	var_type=[]
	a = "(" + a + ")00000"

	i=0
	j=0#walk the master array
	b=0
	k=0
	temp=""
	s=0
	var_num=0
	#Transform input string array into code-readable format
	while s != len(a)-5:

		#print(master, a[s], s)
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
		elif a[s] == "E":

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

			if (a[s+1].isdigit() == True) or (a[s+1] == "."): #if the next index is a number or a period or j

				i=i+1

			elif (a[s+1] == "e") and (a[s+2] in "+-") and (a[s+3].isdigit() == True):
			
				#print(a[s],str(s)+" out of "+str(len(a)-1))

				i+=1
				s+=1
				numtemp.insert(i,a[s])
				#print(numtemp)
				i+=1
				s+=1
				numtemp.insert(i,a[s])
				#print(numtemp)
				i+=1 

			elif (a[s] == "-") & (a[s-1].isdigit() == False):

				master.insert(j,"-1")
				j=j+1
				master.insert(j,"*")
				j=j+1
				numtemp.clear()
		
			else:

				for k in range(0,i+1):

					temp=str(temp)+str(numtemp[k])

				master.insert(j,str(float(temp)))
				j=j+1
				i=0
				numtemp.clear()
				temp = "" #clear up temp

		s=s+1

	#print("now for inference")
	master=inference(master)
	#print(master)
	#print("now for imaginary_num")
	master=imaginary_num(master)
	#print(master)

	if not var_type:

		var_type.append("")
	
	return master, var_type

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
	var_type=[]
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
		elif a[s] == "E":

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

			elif (a[s+1] == "e") and (a[s+2] in "+-") and (a[s+3].isdigit() == True):
			
				i+=1
				s+=1
				numtemp.insert(i,a[s])
				i+=1
				s+=1
				numtemp.insert(i,a[s])
				i+=1

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
	#print(master,var_num,var_type,(var_num != 0) or (len(var_type) != 0))
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

			
			ans=isolate(LHS,RHS,1,var_type)
			#print("YEEEEHAAAWWW",ans)
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

			return solution, ans

	else:

		master=inference(master)
		ans=["0"]
		ans[0]=calculate(master,0)

		try:

			ans[0] = complex(ans[0])

		except:

			pass

		if isinstance(ans[0], complex) == True:

			if ans[0].imag == 0:

				ans[0] = str(ans[0].real)

		print(ans)
		solution.insert(sol_cnt,"The final answer is "+str(ans))
		print(solution[sol_cnt])
		#print(solution)
		the_end = process.memory_info().rss
		mem_tot = abs(the_end - beginning)
		solution.insert(sol_cnt+1,mem_tot)
		#print(mem_tot, "bytes", beginning, "bytes", the_end, "bytes")

		return solution, ans


