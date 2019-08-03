import math
import cmath

print('\nEnter an equation: ')

a = input()

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
	26 : "SQRT",
	27 : "^",
	28 : "*",
	29 : "/",
	30 : "+",
	31 : "-"

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

				else:
					
					solution.insert(sol_cnt,n[t-1]+op+n[t+1])
					calc = operation(float(n[t-1]),op,float(n[t+1]))
					print("OP"+str(sol_cnt+1)+"___",solution[sol_cnt],"=",calc)
					sol_cnt=sol_cnt+1
					n[t-1] = str(calc)
					del n[t:t+2]
					t=t-1 #line added to make sure all ops are performed
					length=len(n)
					#print(n, calc)
			t=t+1

	return calc

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
	elif (a[s] == "-") & (a[s-1] != "("):
	
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

#print(master)
p=0
#for i in range (0,len(master)):
	
	#if (master[i].isdigit() == True) or ("." in master[i]):
		
		#pass

	#elif ("(" in master[i]) or (")" in master[i]):
	
		#pass

	#else:

		#for s in oper_dict:

			#if master[i] == oper_dict[s]:
				
				#p=1
				#break

		#if p==1:

			#pass

		#else:

			#print('There is a variable. It is "',master[i],'"')

 
ans=calculate(master,0)


print("The result of the above equation is",ans,"\n")


