#Solve functions
from math_core.BEMDAS_algo_v3 import bracketify, stringify, grouping, is_number, foiling, is_even, bracket_add, calculate
import copy
from math_core import jenkins_traub
from math_core.algebra import Poly_Func
from typing import List, Tuple, Union
from __future__ import annotations

#1. remove any divisions
#1.1 check if there's any redundant brackets and remove ex: ((x-1)/(x-2))^8 = (x-1)^8/(x-2)^8
#1.2 bracket or terms with variables distribution ex: 69*(x+2)^8*3x*((x-1)^8/(x+2)^8-(x-1)^6/(x+2)^6) = 69*(3x*(x+2)^8*(x-1)^8/(x+2)^8-3x*(x+2)^8*(x-1)^6/(x+2)^6)
#1.3 check if there's any ()/() = 1 and remove
#2. remove any exponents on brackets
#2.1 check if there's any redundant brackets
#3. foil out bracket multiplication starting inwards then out. Every change of level of bracket means removing redundant brackets
#4. foil out bracket multiplied by a constant
#5. Bracket addition or subtraction
#7. Place in standard form (variables on one side, constants on the other, simplify)
#8. Solve based on highest level variable

#Function takes a bracket and foils it out per it's exponent ex: (x+2)^8 = x^8+16x^7+112x^6+448x^5+1120x^4+1792x^3+1792x^2+1024x+256
#Inputs		- br (the bracket in array form)
#		- x (the float value of the exponent)
#Outputs	- result (result in bracket form)

def exp_foiling(br: List[str], x: float, var: str) -> List[str]:

	br_one = br[:]
	br_two = br[:]

	if is_even(x):

		print("x is even and is "+str(x))
		while x != 1.0:

			if is_even(x):

				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"(2")
				br.append(")2")
				br_one = br[:]
				br_two = br[:]
				x/=2

			else:
									
				br = foiling(br_one, br_two, var)
				#print(br)
				br.insert(0,"(2")
				br.append(")2")
				br_one = br[:]
				x-=2

				while x != 0:

					#print(br_one, br_two)
					br = foiling(br_one, br_two, var)
					#print(br)
					br.insert(0,"(2")
					br.append(")2")
					br_one = br[:]
					x-=1

				break
	
		result = br
		result, var_res = grouping(result)
		#res_string = stringify(result)
		#print(res_string)

	else:
					
		#print("x is odd and is "+str(x))
					
		#print(br_one, br_two)
		br = foiling(br_one, br_two, var)
		br.insert(0,"(2")
		br.append(")2")
		br_one = br
		x-=2

		while x != 0.0:

			#print(br_one, br_two)
			br = foiling(br_one, br_two, var)
			br.insert(0,"(2")
			br.append(")2")
			br_one = br
			x-=1

		result = br
		result, var_res = grouping(result)
		#res_string = stringify(result)
		#print(res_string)

	return result

#Function checks if a string has a complex number in it. Returns True or False
#Inputs		- string (the string we are checking)
#		- var (the variable character)
#Outputs	- True or False

def is_complex_coeff(string: str, var: str) -> bool:

	if var in string:

		coeff = ""
		k=0
		while string[k] != var:

			coeff+=string[k]

			k+=1

		if coeff == "":

			coeff = "1"

		elif coeff == "-":

			coeff = "-1"

		coeff = complex(coeff)

		if coeff.imag == 0:

			return False

		else:

			return True

	else:

		coeff = complex(string)

		if coeff.imag == 0:

			return False

		else:

			return True

#Function that takes two sides of an equation and then puts all variable terms on LHS, constants on RHS, combines the terms. Returns rearranged equations and highest degree of the equation
#***ATTENTION*** Equation must be rid of all brackets, must be in proper polynomial format to use. Might have to add a check and return an error ***
#Inputs		- l (LHS of the equation in array format)
#		- r (RHS of the equation in array format)
#		- var (single character string of the variable)
#Outputs	- l (rearranged LHS of the equation in array format)
#		- r (rearranged RHS of the equation in array format)

def rearrange(l: List[str], r: List[str], var: str) -> Tuple[List[str], List[str], float]:

	#First all variable terms must go from RHS to LHS
	s = 0
	while s != len(r):

		if var in r[s]:

			if is_complex_coeff(r[s], var) == False:

				if "-" in r[s]:

					if r[s-1] == "-":

						l.insert(len(l)-1,"-")
						temp = r[s]
						temp = temp.replace("-",'')
						l.insert(len(l)-1,temp)
						del r[s-1:s+1]

					else:

						l.insert(len(l)-1,"+")
						temp = r[s]
						temp = temp.replace("-",'')
						l.insert(len(l)-1,temp)

						if s == 1:

							del r[s]

						else:

							del r[s-1:s+1]

				else:

					if r[s-1] == "-":

						l.insert(len(l)-1,"+")
						l.insert(len(l)-1,r[s])
						del r[s-1:s+1]					

					else:

						l.insert(len(l)-1,"-")
						l.insert(len(l)-1,r[s])

						if s == 1:

							del r[s]

						else:

							del r[s-1:s+1]

			else:

				if r[s-1] == "-":

					l.insert(len(l)-1,"+")
					l.insert(len(l)-1,r[s])
					del r[s-1:s+1]					

				else:

					l.insert(len(l)-1,"-")
					l.insert(len(l)-1,r[s])

					if s == 1:

						del r[s]

					else:

						del r[s-1:s+1]

			s=-1

		s+=1

	#print(l, r)
	#Now we will take out any unnecessary operation signs from RHS and Also if the second element of LHS is a term with a negative inside, then we will make two indexes
	#First RHS
	if r[1] == "+":

		del r[1]

	elif r[1] == "-":

		del r[1]
		if is_complex_coeff(r[1], var) == False:

			r[1] = r[1].replace(r[1],"-"+r[1])

	elif (r[0] == "(1") and (r[1] == ")1"):

		r.insert(1,"0")

	if "-" in l[1]:

		if is_complex_coeff(l[1], var) == False:

			l[1] = l[1].replace("-",'')
			l.insert(1,"-")

	print(l, r)
	#Now we move constants from LHS to RHS
	s = 0
	while s != len(l):

		if is_number(l[s]) == True:

			if is_complex_coeff(l[s], var) == False:

				if "-" in l[s]:

					if l[s-1] == "-":

						r.insert(len(r)-1,"-")
						temp = l[s]
						temp = temp.replace("-",'')
						r.insert(len(r)-1,temp)
						del l[s-1:s+1]

					else:

						r.insert(len(r)-1,"+")
						temp = l[s]
						temp = temp.replace("-",'')
						r.insert(len(r)-1,temp)

						if s == 1:

							del l[s]

						else:
			
							del l[s-1:s+1]

				else:
		
					if l[s-1] == "-":

						r.insert(len(r)-1,"+")
						r.insert(len(r)-1,l[s])
						del l[s-1:s+1]

					else:

						r.insert(len(r)-1,"-")
						r.insert(len(r)-1,l[s])

						if s == 1:

							del l[s]

						else:
			
							del l[s-1:s+1]

			else:

				if l[s-1] == "-":

					r.insert(len(r)-1,"+")
					r.insert(len(r)-1,l[s])
					del l[s-1:s+1]

				else:

					r.insert(len(r)-1,"-")
					r.insert(len(r)-1,l[s])

					if s == 1:

						del l[s]

					else:
			
						del l[s-1:s+1]

			s=-1

		s+=1

	#print(l,r)
	#Now we need to establish all the powers of x on LHS and store them in an array called l_deg
	l_deg=[]
	for s in l:

		if var+"^" in s:

			temp = s
			x = ""
			k = 0
			while temp[k] != "^":

				k+=1

			k+=1
			while k != len(temp):

				x += temp[k]
				k+=1

			if x not in l_deg:

				l_deg.append(x)

		elif (var in s) and ("^" not in s):

			x = "1.0"

			if x not in l_deg:

				l_deg.append(x)

	#print(l_deg)
	#Now to put all the terms in l_deg in numerical order
	l_deg_ordered=[]
	for s in l_deg:

		if not l_deg_ordered:

			l_deg_ordered.append(s)

		else:

			if float(s) > float(l_deg_ordered[0]):

				if s not in l_deg_ordered:

					l_deg_ordered.insert(0,s)

			else:

				if s not in l_deg_ordered:

					k=0
					while k != len(l_deg_ordered):

						if (float(s) > float(l_deg_ordered[k])) and (s not in l_deg_ordered):

							l_deg_ordered.insert(k,s)

						k+=1

					if s not in l_deg_ordered:

						l_deg_ordered.append(s)

		#print(l_deg_ordered)

	#print(l_deg_ordered)
	rear_l=[]
	for i in l_deg_ordered:

		for s in range(0,len(l)):

			if var+"^"+i in l[s]:

				if is_complex_coeff(l[s], var) == False:

					if "-" in l[s]:

						if l[s-1] == "-":

							if not rear_l:

								temp = l[s]
								temp = temp.replace("-",'')
								rear_l.append(temp)

							else:

								rear_l.append("+")
								temp = l[s]
								temp = temp.replace("-",'')
								rear_l.append(temp)

						else:

							if not rear_l:

								rear_l.append(l[s])

							else:

								rear_l.append("-")
								temp = l[s]
								temp = temp.replace("-",'')
								rear_l.append(temp)
	
					else:

						if l[s-1] == "-":

							if not rear_l:

								rear_l.append("-"+l[s])

							else:

								rear_l.append("-")
								rear_l.append(l[s])

						else:

							if not rear_l:

								rear_l.append(l[s])

							else:

								rear_l.append("+")
								rear_l.append(l[s])

				else:

					if l[s-1] == "-":

						if not rear_l:

							rear_l.append("-"+l[s])

						else:

							rear_l.append("-")
							rear_l.append(l[s])

					else:

						if not rear_l:

							rear_l.append(l[s])

						else:

							rear_l.append("+")
							rear_l.append(l[s])
						

			elif (i == "1.0") and (var in l[s]) and ("^" not in l[s]):

				if is_complex_coeff(l[s], var) == False:

					if "-" in l[s]:

						if l[s-1] == "-":

							if not rear_l:

								temp = l[s]
								temp = temp.replace("-",'')
								rear_l.append(temp)

							else:

								rear_l.append("+")
								temp = l[s]
								temp = temp.replace("-",'')
								rear_l.append(temp)

						else:

							if not rear_l:

								rear_l.append(l[s])

							else:

								rear_l.append("-")
								temp = l[s]
								temp = temp.replace("-",'')
								rear_l.append(temp)
	
					else:

						if l[s-1] == "-":

							if not rear_l:

								rear_l.append("-"+l[s])

							else:

								rear_l.append("-")
								rear_l.append(l[s])

						else:

							if not rear_l:

								rear_l.append(l[s])

							else:

								rear_l.append("+")
								rear_l.append(l[s])

				else:

					if l[s-1] == "-":

						if not rear_l:

							rear_l.append("-"+l[s])

						else:

							rear_l.append("-")
							rear_l.append(l[s])

					else:

						if not rear_l:

							rear_l.append(l[s])

						else:

							rear_l.append("+")
							rear_l.append(l[s])

	rear_l.insert(0,"(1")
	rear_l.append(")1")
	#print(rear_l)
	#l_string = stringify(rear_l)
	#l_string = l_string.replace(".0",'')
	#l_string = l_string.replace("-"," - ")
	#l_string = l_string.replace("+"," + ")
	#print(l_string)
	#Now we combine all similar terms
	for i in l_deg_ordered:

		s = 0
		while s != len(rear_l):

			if var+"^"+i in rear_l[s]:

				if s != 1:

					if (rear_l[s-1] in "+-") and (var+"^"+i in rear_l[s-2]):

						term_one = rear_l[s-2]

						if is_complex_coeff(term_one, var) == False:

							if rear_l[s-3] == "-":

								if "-" not in term_one:

									rear_l[s-3] = "+"
									term_one = "-"+term_one

						op = rear_l[s-1]
						term_two = rear_l[s]

						term_one = term_one.replace(var+"^"+i,'')
						term_two = term_two.replace(var+"^"+i,'')

						if term_one == "":

							term_one = "1.0"

						elif term_one == "-":

							term_one = "-1.0"

						if term_two == "":

							term_two = "1.0"

						elif term_two == "-":

							term_two = "-1.0"

						if op == "+":

							new_term = complex(term_one)+complex(term_two)

						elif op == "-":

							new_term = complex(term_one)-complex(term_two)

						else:

							print("shits broken")

						if new_term.imag == 0:

							new_term = str(new_term.real)
							if "-" in new_term:

								if s-2 == 1:

									rear_l[s-2] = new_term+var+"^"+i
									del rear_l[s-1:s+1]

								else:

									if rear_l[s-3] == "-":

										rear_l[s-3] = "+"
										new_term = new_term.replace("-",'')
										rear_l[s-2] = new_term+var+"^"+i
										del rear_l[s-1:s+1]

									else:

										rear_l[s-3] = "-"
										new_term = new_term.replace("-",'')
										rear_l[s-2] = new_term+var+"^"+i
										del rear_l[s-1:s+1]

							elif new_term == "0.0":

								if s-2 == 1:

									del rear_l[s-2:s+1]							

								else:

									del rear_l[s-3:s+1]

							elif new_term == "1.0":

								rear_l[s-2] = var+"^"+i
								del rear_l[s-1:s+1]

							elif new_term == "-1.0":

								if s-2 == 1:

									rear_l[s-2] = "-"+var+"^"+i
									del rear_l[s-1:s+1]

								else:

									if rear_l[s-3] == "-":

										rear_l[s-3] = "+"
										rear_l[s-2] = var+"^"+i
										del rear_l[s-1:s+1]

									else:

										rear_l[s-3] = "-"
										rear_l[s-2] = var+"^"+i
										del rear_l[s-1:s+1]
	
							else:

								rear_l[s-2] = new_term+var+"^"+i
								del rear_l[s-1:s+1]

						else:

							new_term = str(new_term)
							rear_l[s-2] = new_term+var+"^"+i
							del rear_l[s-1:s+1]

						s=-1

			elif (i == "1.0") and (var in rear_l[s]) and ("^" not in rear_l[s]):

				if s != 1:

					if (rear_l[s-1] in "+-") and (var in rear_l[s-2]) and ("^" not in rear_l[s-2]):

						term_one = rear_l[s-2]

						if is_complex_coeff(term_one, var) == False:

							if rear_l[s-3] == "-":

								if "-" not in term_one:

									rear_l[s-3] = "+"
									term_one = "-"+term_one

						op = rear_l[s-1]
						term_two = rear_l[s]

						term_one = term_one.replace(var,'')
						term_two = term_two.replace(var,'')

						if term_one == "":

							term_one = "1.0"

						elif term_one == "-":

							term_one = "-1.0"

						if term_two == "":

							term_two = "1.0"

						elif term_two == "-":

							term_two = "-1.0"

						if op == "+":

							new_term = complex(term_one)+complex(term_two)

						elif op == "-":

							new_term = complex(term_one)-complex(term_two)

						else:

							print("shits broken")

						if new_term.imag == 0:

							new_term = str(new_term.real)
							if "-" in new_term:

								if s-2 == 1:

									rear_l[s-2] = new_term+var
									del rear_l[s-1:s+1]

								else:

									if rear_l[s-3] == "-":

										rear_l[s-3] = "+"
										rear_l[s-2] = new_term+var
										del rear_l[s-1:s+1]

									else:

										rear_l[s-3] = "-"
										new_term = new_term.replace("-",'')
										rear_l[s-2] = new_term+var
										del rear_l[s-1:s+1]
	
							elif new_term == "0.0":

								if s-2 == 1:

									del rear_l[s-2:s+1]							

								else:

									del rear_l[s-3:s+1]

							elif new_term == "1.0":

								rear_l[s-2] = var
								del rear_l[s-1:s+1]

							elif new_term == "-1.0":

								if s-2 == 1:

									rear_l[s-2] = "-"+var
									del rear_l[s-1:s+1]

								else:

									if rear_l[s-3] == "-":

										rear_l[s-3] = "+"
										rear_l[s-2] = var
										del rear_l[s-1:s+1]

									else:

										rear_l[s-3] = "-"
										rear_l[s-2] = var
										del rear_l[s-1:s+1]

							else:

								rear_l[s-2] = new_term+var
								del rear_l[s-1:s+1]

						else:

							new_term = str(new_term)
							rear_l[s-2] = new_term+var
							del rear_l[s-1:s+1]

						s=-1

			s+=1

	#print(rear_l)
	#l_string = stringify(rear_l)
	#print(l_string)

	rear_r = ["(1", "0", ")1"]
	rear_r[1] = calculate(r,0)
	#print(rear_r)

	#Find the highest deg
	highest_deg=0.0
	for s in l:

		if var+"^" in s:

			temp = s
			x = ""
			k = 0
			while temp[k] != "^":

				k+=1

			k+=1
			while k != len(temp):

				x += temp[k]
				k+=1

			if float(x) > highest_deg:

				highest_deg = float(x)

		elif (var in s) and ("^" not in s):

			x = 1.0

			if float(x) > highest_deg:

				highest_deg = float(x)

	return rear_l, rear_r, highest_deg

#Function takes the divisors array and returns an array of unique asymptotes
#Inputs		- divisors (array of divisors from an equation)
#			- var (str of the single character variable)
#Outputs	- asymptotes (array of asymptotes)

def find_asymptotes(divisors: [str], var: str) -> List[Union[int, float, complex]]:

	asymptotes=[]
	for i in divisors:

		temp = i
		s = 0
		while s != len(temp):

			if (is_number(temp[s]) == True) and (temp[s-1] == "^") and (temp[s-2] == ")2"):

				del temp[s-1:s+1]
				temp.insert(0,"(1")
				temp.append(")1")
				temp = Solve_Func(temp, var)
				temp = temp.redundant_br()
				temp.eqn, r_temp, temp_deg = rearrange(temp.eqn, ["(1", "0", ")1"], temp.var)
				ans = solver(temp.eqn, r_temp, temp_deg, temp.var)

				if ans[0] not in asymptotes:

					asymptotes.append(ans[0])

				break

			elif (temp[s] != "^") and (temp[s-1] == ")2") :

				temp.insert(0, "(1")
				temp.append(")1")
				temp = Solve_Func(temp, var)
				temp = temp.redundant_br()
				temp.eqn, r_temp, temp_deg = rearrange(temp.eqn, ["(1", "0", ")1"], temp.var)
				ans = solver(temp.eqn, r_temp, temp_deg, temp.var)

				if ans[0] not in asymptotes:

					asymptotes.append(ans[0])

				break

			s+=1

	return asymptotes

#Function solves an equation using a method determined by the highest order term. Returns an array of answers
#Inputs		- l (LHS of the equation in array format) Must be simplified
#		- r (RHS of the equation in array format) Must be simplified
#		- var (single character string that is the variable in the equation)
#		- highest deg (float of the highest order term)
#Outputs	- ans (array of answers)

def solver(l: List[str], r: List[str], deg: float, var: str) -> List[Union[int, float, complex]]:

	solution=[]
	sol_cnt=0

	if deg == 1.0:

		#print("yeet", l ,r)
		s = 0
		while s != len(l):

			if var in l[s]:

				value = l[s]
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

				r[1] = str(other_value/value)
				l[s] = var
				l_string = stringify(l)
				r_string = stringify(r)
				print(l_string+" = "+r_string)
				
			s+=1

		if (len(l) == 3) and (l[1] == var):

			ans = []
			temp = complex(r[1])

			if round(temp.imag,6) == 0:

				temp = temp.real

			ans.append(temp)

	elif deg == 2.0:

		if "-" in r[1]:

			r[1] = r[1].replace('-','')
			l.insert(len(l)-1,"+")
			l.insert(len(l)-1,r[1])
			r[1] = "0"

		else:

			l.insert(len(l)-1,"-")
			l.insert(len(l)-1,r[1])
			r[1] = "0"

		#Quadratic Formula

		l = Poly_Func(l)
		coeff = l.get_coeff(int(deg),var)
		ans, solution, sol_cnt = coeff.quadratic(solution, sol_cnt)

		for s in range(0,len(ans)):

			if round(ans[s].imag,6) == 0:

				ans[s] = ans[s].real	

	#3rd or polynomial

	elif deg == 3.0:

		if "-" in r[1]:

			r[1] = r[1].replace('-','')
			l.insert(len(l)-1,"+")
			rear_l.insert(len(l)-1,r[1])
			r[1] = "0"

		else:

			l.insert(len(l)-1,"-")
			l.insert(len(l)-1,r[1])
			r[1] = "0"

		#Cubic Function Formula

		l = Poly_Func(l)
		coeff = l.get_coeff(int(deg),var)
		ans, solution, sol_cnt = coeff.cardano(solution, sol_cnt)

		for s in range(0,len(ans)):

			if round(ans[s].imag,6) == 0:

				ans[s] = ans[s].real	

	#Ferrari's Method
	elif deg == 4.0:

		if "-" in r[1]:

			r[1] = r[1].replace('-','')
			l.insert(len(l)-1,"+")
			l.insert(len(l)-1,r[1])
			r[1] = "0"

		else:

			l.insert(len(l)-1,"-")
			l.insert(len(l)-1,r[1])
			r[1] = "0"

		l = Poly_Func(l)
		coeff = l.get_coeff(int(deg),var)
		#print(coeff.eqn)
		ans, solution, sol_cnt = coeff.ferrari(solution, sol_cnt)

		for s in range(0,len(ans)):

			if round(ans[s].imag,6) == 0:

				ans[s] = ans[s].real		

	#For any polynomial of nth degree where n>=5
	else:

		if "-" in r[1]:

			r[1] = r[1].replace('-','')
			l.insert(len(l)-1,"+")
			l.insert(len(l)-1,r[1])
			r[1] = "0"

		else:

			l.insert(len(l)-1,"-")
			l.insert(len(l)-1,r[1])
			r[1] = "0"

		l = Poly_Func(l)
		coeff=l.get_coeff(int(float(deg)),var)
		test=l.get_coeff(int(float(deg)),var)
		test_two=l.get_coeff(int(float(deg)),var)
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

		string = stringify(l.eqn)
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
						ans = jenkins_traub.real_poly(coeff,int(float(deg))-i)

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

			ans = jenkins_traub.real_poly(coeff,int(float(deg)))

		print(ans)

		for i in range(0,len(ans)):

			if round(ans[i].imag,5) == 0:
			
				ans[i] = ans[i].real

	return ans

class Solve_Func:

	def __init__(self, eqn: List[str], var: str):

		self.eqn = eqn
		self.var = var

	#1. remove any divisions
	#1.1 Identify divisors in an eqn
	#Inputs 	- eqn (LHS or RHS of equation in array format)
	#		- var (single character string that is the variable in an equation ex: "x"
	#Outputs	- divisors (array of divisors in array format)

	def identify_div(self) -> List[List[str]]:

		s=0
		divisors=[]
		while s != len(self.eqn):
	
			#What do we do if COS(()/())? or (()/())^7. Maybe it would be wise to make a marker that indicates a bracket is preceded by a special op like COS 
			if ("(" in self.eqn[s]) and (self.eqn[s-1] == "/") and (s != 0):

				#print("s is currently "+str(s),self.eqn[s])
				br_string = "("
				k = s+1
				while ")" not in self.eqn[k]:

					br_string+=self.eqn[k]
					k+=1

				k+=1
				br_string+=")"
			
				exp_check = False
				if self.eqn[k] == "^":

					exp_check == True
					br_string+="^"+self.eqn[k+1]
				
				k = 0
				b = 0
				while k != s:

					if "(" in self.eqn[k]:

						b+=1

					elif ")" in self.eqn[k]:

						b-=1

					k+=1
 
				x = 1
				c = b
				while k != len(self.eqn):

					if "(" in self.eqn[k]:

						b+=1

					elif ")" in self.eqn[k]:

						b-=1

					if (is_number(self.eqn[k]) == True) and (self.eqn[k-1] == "^") and (self.eqn[k-2] == ")"+str(c)):

						x*=float(self.eqn[k])
						c-=1

					elif (self.eqn[k-1] != "^") and (self.eqn[k-2] == ")"+str(c)):

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
				divisors.append(br)

			elif ((is_number(self.eqn[s]) == True) or (self.var in self.eqn[s])) and (self.eqn[s-1] == "/") and (s != 0):

				br_string = self.eqn[s]

				k = 0
				b = 0
				b_open = 0
				b_close = 0
				while k != s:

					if "(" in self.eqn[k]:

						b_open+=1
						b+=1

					elif ")" in self.eqn[k]:

						b_close+=1
						b-=1

					k+=1
 
				x = 1
				c = b
				while k != len(self.eqn):

					if "(" in self.eqn[k]:

						b_open+=1
						b+=1

					elif ")" in self.eqn[k]:

						b_close+=1
						b-=1

					if (is_number(self.eqn[k]) == True) and (self.eqn[k-1] == "^") and (self.eqn[k-2] == ")"+str(c)):

						x*=float(self.eqn[k])
						c-=1

					elif (self.eqn[k-1] != "^") and (self.eqn[k-2] == ")"+str(c)):

						c-=1

					k+=1

				if x > 1:

					br_string = "("+br_string+")^"+str(x)
				
				print("The divisor is: "+br_string)
			
				br, br_var = bracketify(br_string)
				br, br_deg = grouping(br)
				del br[0]
				del br[len(br)-1]

				print(br)
				divisors.append(br)

			s+=1

		return divisors

	#Removes redundant brakets ex: (()+()) = ()+() or ex: (()/())^c = ()^c/()^c
	#Inputs		-self (Solve_Func object)
	#Outputs	-return initial eqn array with no redundant brackets
	def redundant_br(self) -> Solve_Func:

		b=0
		for s in self.eqn:

			if "(" in s:

				temp = s
				temp = temp.replace("(","")
				temp = int(temp)

				if temp > b:

					b = temp

		for c in range(b-1,1,-1):

			s=0
			while s != len(self.eqn):

				#first is there a constant, a divisor or an exponent on a pair of brackets? a*()^x/b or a*()/b
				if (self.eqn[s] == "("+str(c)) and (self.eqn[s-1] == "*"):

					k = s
					d = 0
					br_string = ""
					case_type = 0
					while self.eqn[k] != ")"+str(c):

						if self.eqn[k] == "("+str(c+1):

							br_string += "("
							d+=1

						elif self.eqn[k] == ")"+str(c+1):

							br_string += ")"
							d-=1

						elif "(" in self.eqn[k]:

							br_string += "("

						elif ")" in self.eqn[k]:

							br_string += ")"

						elif (self.eqn[k] in "+-*/") and (d == 0):
				
							br_string += self.eqn[k]
							if (self.eqn[k] in "+-") and (case_type == 0):

								case_type = 1

							elif (self.eqn[k] in "+-") and (case_type == 1):

								pass
	
							elif (self.eqn[k] in "*/") and (case_type == 0):

								case_type = 2

							elif (self.eqn[k] in "*/") and (case_type == 2):

								pass

							else:

								case_type = 3

						else:

							br_string += self.eqn[k]

						k+=1

					br_string += ")"
					print(br_string, "constant case_type = "+str(case_type))
					k+=1
					if (self.eqn[k] == "^"):

						br_string += "^"+self.eqn[k+1]
						if (case_type == 0) or (case_type == 1) or (case_type == 3):

							print("no redundant brackets found")

						else:
					
							new_br_string = ""
							i = 1
							m = br_string.find(")^")
							while i != m:

								new_br_string += br_string[i]
								i+=1

							new_br_string = new_br_string.replace(")",")^"+self.eqn[k+1])
							eqn_string = stringify(self.eqn)
							print(eqn_string)
							eqn_string = eqn_string.replace(br_string, new_br_string)
							print(eqn_string)
							self.eqn, eqn_var = bracketify(eqn_string)
							self.eqn, eqn_deg = grouping(self.eqn)
							s=0

					elif (self.eqn[k] in "/*"):

						print("no redundant brackets found")

					else:

						if (case_type == 0):

							new_br_string = ""
							for i in range(1,len(br_string)-1):

								new_br_string += br_string[i]

							eqn_string = stringify(self.eqn)
							print(eqn_string)
							eqn_string = eqn_string.replace(br_string, new_br_string)
							print(eqn_string)
							self.eqn, eqn_var = bracketify(eqn_string)
							self.eqn, eqn_deg = grouping(self.eqn)
							s=0

						elif (case_type == 1) or (case_type == 3):

							print("no redundant brackets found")

						else:

							new_br_string = ""
							for i in range(1,len(br_string)-1):

								new_br_string += br_string[i]

							eqn_string = stringify(self.eqn)
							print(eqn_string)
							eqn_string = eqn_string.replace(br_string, new_br_string)
							print(eqn_string)
							self.eqn, eqn_var = bracketify(eqn_string)
							self.eqn, eqn_deg = grouping(self.eqn)
							s=0

				elif self.eqn[s] == "("+str(c):

					k = s
					d = 0
					br_string = ""
					case_type = 0
					while self.eqn[k] != ")"+str(c):

						if self.eqn[k] == "("+str(c+1):

							br_string += "("
							d+=1

						elif self.eqn[k] == ")"+str(c+1):

							br_string += ")"
							d-=1

						elif "(" in self.eqn[k]:

							br_string += "("

						elif ")" in self.eqn[k]:

							br_string += ")"

						elif (self.eqn[k] in "+-*/") and (d == 0):
				
							br_string += self.eqn[k]
							if (self.eqn[k] in "+-") and (case_type == 0):

								case_type = 1

							elif (self.eqn[k] in "+-") and (case_type == 1):

								pass
	
							elif (self.eqn[k] in "*/") and (case_type == 0):

								case_type = 2

							elif (self.eqn[k] in "*/") and (case_type == 2):

								pass

							else:

								case_type = 3

						else:

							br_string += self.eqn[k]

						k+=1

					br_string += ")"
					print(br_string, "no constant case_type = "+str(case_type))
					k+=1
					if (self.eqn[k] == "^"):

						if (case_type == 0) or (case_type == 1) or (case_type == 3):

							print("no redundant brackets found")

						else:
					
							br_string += "^"+self.eqn[k+1]
							new_br_string = ""
							i = 1
							m = br_string.find(")^")
							d=0
							max=0
							while i != m:

								if br_string[i] == "(":

									d+=1

									if d > max:

										max = d

								elif br_string[i] == ")":

									d-=1

								new_br_string += br_string[i]
								i+=1

							if max <= 1 :

								print("\n"+new_br_string)
								new_br_string = new_br_string.replace(")",")^"+self.eqn[k+1])
								eqn_string = stringify(self.eqn)
								print(eqn_string)
								eqn_string = eqn_string.replace(br_string, new_br_string)
								print(eqn_string)
								self.eqn, eqn_var = bracketify(eqn_string)
								self.eqn, eqn_deg = grouping(self.eqn)
								s=0

							else:

								eqn_string = stringify(self.eqn)
								new_br_string = ""
								m = br_string.find(")^")
								br_string = br_string.replace("^"+self.eqn[k+1], '')
								i = m-1
								d=0
								while i != 1:

									if br_string[i] == ")":

										d+=1

									elif br_string[i] == "(":

										d-=1

									if d <= 1:

										new_br_string = br_string[i] + new_br_string

									else:

										new_new_br_string = new_br_string.replace(")",")^"+self.eqn[k+1])
										br_string_prime = br_string.replace(new_br_string, new_new_br_string)
										print(eqn_string)
										eqn_string = eqn_string.replace(br_string+"^"+self.eqn[k+1], br_string_prime)
										print(eqn_string)
										new_br_string = br_string_prime
										i-=1
										while d != 0:
											print(i, d, br_string[i])
											if br_string[i] == ")":

												d+=1

											elif br_string[i] == "(":

												d-=1

											i-=1

										new_br_string = br_string[i]

									i-=1

								print("\n"+new_br_string)
								new_new_br_string = new_br_string.replace(")",")^"+self.eqn[k+1])
								br_string_prime = br_string.replace(new_br_string, new_new_br_string)
								print(eqn_string)
								print("BOO", br_string, new_br_string, new_new_br_string, br_string_prime)
								eqn_string = eqn_string.replace(br_string+"^"+self.eqn[k+1], br_string_prime)
								print(eqn_string)
								self.eqn, eqn_var = bracketify(eqn_string)
								self.eqn, eqn_deg = grouping(self.eqn)
								s=0

					elif (self.eqn[k] in "/*"):

						print("no redundant brackets found")

					else:

						if case_type == 1:

							print("no redundant brackets found")

						else:

							new_br_string = ""
							for i in range(1,len(br_string)-1):

								new_br_string += br_string[i]

							eqn_string = stringify(self.eqn)
							print(eqn_string)
							eqn_string = eqn_string.replace(br_string, new_br_string)
							print(eqn_string)
							self.eqn, eqn_var = bracketify(eqn_string)
							self.eqn, eqn_deg = grouping(self.eqn)
							s=0

				s+=1

		if (self.eqn[1] == "(2") and (self.eqn[len(self.eqn)-2] == ")2"):

			s=1
			d=0
			chk_var = False
			while s != len(self.eqn)-2:

				if self.eqn[s] == ")2":

					chk_var = True
					break

				s+=1

			if chk_var == False:

				del self.eqn[len(self.eqn)-2]
				del self.eqn[1]			

		return self

	#Function to multiply in divisors to the highest bracket level
	#Inputs	- self (the Solve_Func object)
	#	- divisors (array containing divisors in array form)
	#Outputs	- self.eqn (the input equation modified)

	def multiply_br(self, divers: List[List[str]]) -> Solve_Func:

		div_copy = copy.deepcopy(divers)
		#print("At the beginning",self.eqn, div_copy)
		#First determine the highest bracket level
		b=0
		for s in self.eqn:

			if "(" in s:

				temp = s
				temp = temp.replace("(","")
				temp = int(temp)

				if temp > b:

					b = temp

		#Next multiply in the divisors
		div_string = []
		for i in div_copy:

			s=0
			d=0
			while s != len(self.eqn):

				if "(" in self.eqn[s]:

					d+=1

				elif ")" in self.eqn[s]:

					d-=1

				if ((is_number(self.eqn[s]) == True) or (self.var in self.eqn[s])) and (d == 1):

					s+=1
					self.eqn.insert(s,"*")
					s+=1
					for n in range(len(i)-1,-1,-1):

						self.eqn.insert(s,i[n])

					d=1
					s+=len(i)
					#print(self.eqn, s)

					while self.eqn[s] != ")1":

						if "(" in self.eqn[s]:

							d+=1

						elif ")" in self.eqn[s]:

							d-=1

						if (self.eqn[s] in "+-") and (d == 1):

							break

						s+=1

					if s == len(self.eqn)-1:

						s-=1

					#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

				elif self.eqn[s] == "(2":

					self.eqn.insert(s,"*")
					for n in range(len(i)-1,-1,-1):

						self.eqn.insert(s,i[n])

					d=1
					s+=len(i)
					#print(self.eqn, s)

					while self.eqn[s] != ")1":

						if "(" in self.eqn[s]:

							d+=1

						elif ")" in self.eqn[s]:

							d-=1

						if (self.eqn[s] in "+-") and (d == 1):

							break

						s+=1

					if s == len(self.eqn)-1:

						s-=1

				s+=1

			temp = i[:]
			temp.insert(0,"(1")
			temp.append(")1")
			div_string.append(stringify(temp))

		eqn_string = stringify(self.eqn)
		print(eqn_string)

		for c in range(2,b):

			for i in div_copy:

				#need to find divisor outside of "("+str(c), then need to delete it and multiply it into all terms inside of "("+str(c)
				#print("inside multiply_br", i)
				s = 0
				while s != len(self.eqn):

					if self.eqn[s] == i[0]:

						k = s
						#print(k, self.eqn[s], i[0])
						k+=1
						eqn_chk = True
						for n in range(1,len(i)):

							if self.eqn[k] != i[n]:

								#print(k, self.eqn[k], i[n])
								eqn_chk = False
								break

							else:

								#print(k, self.eqn[k], i[n])
								k+=1

						#print("k = "+str(k), self.eqn[k])
						if eqn_chk == True:

							#print(k, self.eqn[k])
							if self.eqn[k] == "*":

								k+=1
								if self.eqn[k] == "("+str(c):

									m = k
									while self.eqn[m] != ")"+str(c):

										m+=1

									
									if self.eqn[m+1] == "^":
										print("GREEN HELL", m+2, self.eqn[m+2], self.eqn)
										x = 1/float(self.eqn[m+2])
										n=0
										exp_chk = False
										while n != len(i):

											if i[n] == "^":

												if float(i[n+1])*x > 1:

													i[n+1] = str(float(i[n+1])*x)
													exp_chk = True

												else:

													eqn_chk = False
													
												break

											n+=1

										if exp_chk == False:

											if x > 1:

												i.insert(len(i), "^")
												i.insert(len(i), str(x))

											else:

												eqn_chk = False

									if eqn_chk == True:

										#print("Found one: ", k, self.eqn[k])
										del self.eqn[s:k]
										#print(self.eqn, s, self.eqn[s])
										break

									else:

										s = k

					s+=1

				d = 0
				#print(s, self.eqn[s], self.eqn, i)
				while s != len(self.eqn):

					if "(" in self.eqn[s]:

						d+=1

					elif ")" in self.eqn[s]:

						d-=1

					if ((is_number(self.eqn[s]) == True) or (self.var in self.eqn[s])) and (d == 1):

						s+=1
						self.eqn.insert(s,"*")
						s+=1
						for n in range(len(i)-1,-1,-1):

							if "(" in i[n]:

								self.eqn.insert(s,"("+str(c+1))

							elif ")" in i[n]:

								self.eqn.insert(s,")"+str(c+1))

							else:

								self.eqn.insert(s,i[n])

						s+=len(i)-2
						d=1
						#print(self.eqn, s)

						while self.eqn[s] != ")1":

							if "(" in self.eqn[s]:
	
								d+=1

							elif ")" in self.eqn[s]:

								d-=1

							if (self.eqn[s] in "+-") and (d == 1):

								break

							s+=1

						if s == len(self.eqn)-1:

							s-=1

						#print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

					elif self.eqn[s] == "("+str(c+1):

						#print("d = "+str(d), self.eqn[s], s)
						self.eqn.insert(s,"*")
						for n in range(len(i)-1,-1,-1):

							if "(" in i[n]:

								self.eqn.insert(s,"("+str(c+1))

							elif ")" in i[n]:

								self.eqn.insert(s,")"+str(c+1))

							else:

								self.eqn.insert(s,i[n])

						s+=len(i)
						d=1
						#print("here",s, self.eqn[s], self.eqn)

						while self.eqn[s] != ")1":

							if "(" in self.eqn[s]:

								d+=1

							elif ")" in self.eqn[s]:

								d-=1

							if (self.eqn[s] in "+-") and (d == 1):

								break

							s+=1

						if s == len(self.eqn)-1:

							s-=1

					s+=1

		eqn_string = stringify(self.eqn)
		print(eqn_string)
		return self

	#Function to remove any ()/() = 1:
	#Inputs	-self (the class object)
	#	-divisors (an array of arrays of the divisors)
	#outputs -self (the equation with modifications)

	def redundant_div(self, divisors: List[List[str]]) -> Solve_Func:

		#First determine the highest bracket level
		b=0
		for s in self.eqn:

			if "(" in s:

				temp = s
				temp = temp.replace("(","")
				temp = int(temp)

				if temp > b:

					b = temp

		div_copy = copy.deepcopy(divisors)
		#print(div_copy)
		div_string=[]
		
		for i in div_copy:

			for c in range(b,1,-1):

				s = 0
				while s != len(self.eqn):

					if "("+str(c-1) == self.eqn[s]:

						br=[]
						k = s
						while self.eqn[k] != ")"+str(c-1):

							br.append(self.eqn[k])
							k+=1

						br.append(self.eqn[k])
						#print(br[0] != "(1", br[len(br)-1] != ")1", br)
						if (br[0] != "(1") and (br[len(br)-1] != ")1"):

							br.insert(0,"(1")
							br.append(")1")

						br_string = stringify(br)

						if k != len(self.eqn)-1:

							#print("REEEEEE", br_string, k+1, self.eqn[k+1], self.eqn)
							if self.eqn[k+1] == "^":

								x = 1/float(self.eqn[k+2])
								n=0
								exp_chk = False
								while n != len(i):

									if i[n] == "^":

										i[n+1] = str(float(i[n+1])*x)
										exp_chk = True

									n+=1

								if exp_chk == False:

									i.insert(len(i), "^")
									i.insert(len(i), str(x))

					s+=1

			i.insert(0,"(1")
			i.append(")1")
			div_string.append(stringify(i))
						

		#print("voila",div_string)

		for i in div_string:

			for c in range(b,1,-1):
		
				#print("does it even get this far")
				s=0
				while s != len(self.eqn):

					if self.eqn[s] == "("+str(c-1):

						k = s+1
						d=0
						br = ""
						while self.eqn[k] != ")"+str(c-1):

							if "(" in self.eqn[k]:

								br+="("
								d+=1

							elif ")" in self.eqn[k]:

								br+=")"
								d-=1

							else:

								if (self.eqn[k] in "+-") and (d==0):

									#print(br)
									if ("/"+i in br) and (i+"*" in br):

										eqn_string = stringify(self.eqn)
										new_br = br.replace(i+"*","")
										new_br = new_br.replace("/"+i,'')
										eqn_string = eqn_string.replace(br,new_br)
										#print(eqn_string)
										self.eqn, var = bracketify(eqn_string)

										if var:

											self.var = var[0]

										self.eqn, deg = grouping(self.eqn)
										#print(self.eqn)
										s=0

									else:

										br=""

								else:

									br+=self.eqn[k]

							k+=1

						#print(br)
						eqn_string = stringify(self.eqn)
						if ("/"+i in br) and (i+"*" in br):

							new_br = br.replace(i+"*","")
							new_br = new_br.replace("/"+i,'')
							eqn_string = eqn_string.replace(br,new_br)
							#print(eqn_string)
							self.eqn, var = bracketify(eqn_string)
							
							if var:

								self.var = var[0]

							self.eqn, deg = grouping(self.eqn)
							#print(self.eqn)
							s=0

					s+=1

		return self

	#Function removes all brackets by finding brackets with exponents, bracket multiplication, add or sub and foils out 
	#Inputs	- self (the equation)
	#Outputs	- self (the modified equation)

	def bracket_remover(self) -> Solve_Func:

		b=0
		for s in self.eqn:

			if "(" in s:

				temp = s
				temp = temp.replace("(","")
				temp = int(temp)

				if temp > b:

					b = temp

		for c in range(b,1,-1):

			s=0
			while s != len(self.eqn):

				if (is_number(self.eqn[s]) == True) and (self.eqn[s-1] == "^") and (self.eqn[s-2] == ")"+str(c)):

					x = float(self.eqn[s])
					k = s-2
					d=0
					br=""
					while self.eqn[k] != "("+str(c):

						if ")" in self.eqn[k]:

							br = ")"+br
							d+=1

						elif "(" in self.eqn[k]:

							br = "("+br
							d-=1

						else:

							if (self.eqn[k-1] == ")"+str(c+1)) and (self.eqn[k] in "+-") and (self.eqn[k+1] == "("+str(c+1)):

								break

							else:

								br = self.eqn[k]+br

						k-=1

					br = "("+br
					print("\n"+br+"^"+str(x))
					bra, bra_var = bracketify(br)
					bra, bra_deg = grouping(bra)
					del bra[0]
					del bra[len(bra)-1]
					#print(bra)
					
					if x > 1.0:

						new_br = exp_foiling(bra,x, self.var)
						#print(new_br)
						new_br_string = stringify(new_br)
						print("= "+new_br_string)
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br+"^"+str(x),"("+new_br_string+")")
						self.eqn, var = bracketify(eqn_string)

						if var:

								self.var = var[0]

						self.eqn, deg = grouping(self.eqn)
						eqn_string = stringify(self.eqn)
						print("\n"+eqn_string)
						s=-1

				s+=1

			#Now to check for ()*() or c*() or ()*c
			s=0
			while s != len(self.eqn):

				if (self.eqn[s] == "("+str(c)) and (self.eqn[s-1] == "*") and (self.eqn[s-2] == ")"+str(c)):

					br_string_one = ""
					br_string_two = ""
					k = s
					m = s-2

					check_two = False
					d=0
					while self.eqn[k] != ")"+str(c):

						if "(" in self.eqn[k]:

							br_string_two += "("
							d+=1

						elif ")" in self.eqn[k]:

							br_string_two += ")"
							d-=1

						else:

							if (self.eqn[k-1] == ")"+str(c+1)) and (self.eqn[k] in "+-") and (self.eqn[k+1] == "("+str(c+1)):

								check_two = True
								break

							else:

								br_string_two += self.eqn[k]

						k+=1

					br_string_two += ")"
					check_one = False
					d=0
					while self.eqn[m] != "("+str(c):

						if ")" in self.eqn[m]:

							br_string_one = ")"+br_string_one
							d+=1

						elif "(" in self.eqn[m]:

							br_string_one = "("+br_string_one
							d-=1

						else:

							if (self.eqn[m-1] == ")"+str(c+1)) and (self.eqn[m] in "+-") and (self.eqn[m+1] == "("+str(c+1)):

								check_one = True
								break

							else:

								br_string_one = self.eqn[m]+br_string_one

						m-=1

					if (check_one == False) and (check_two == False):

						br_string_one = "("+br_string_one
						print("\n"+br_string_one+"*"+br_string_two)

						br_one, br_one_var = bracketify(br_string_one)
						br_one, br_one_deg = grouping(br_one)
						del br_one[0]
						del br_one[len(br_one)-1]

						br_two, br_two_var = bracketify(br_string_two)
						br_two, br_two_deg = grouping(br_two)
						del br_two[0]
						del br_two[len(br_two)-1]

						br = foiling(br_one, br_two, self.var)
						
						if not br:

							br = ["0"]

						br.insert(0,"(1")
						br.append(")1")
						br_string = stringify(br)
						print("= "+br_string)
				
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
						self.eqn, var = bracketify(eqn_string)

						if var:

							self.var = var[0]

						self.eqn, deg = grouping(self.eqn)
						eqn_string = stringify(self.eqn)
						print("\n"+eqn_string)
						s=-1
						
				elif ((is_number(self.eqn[s]) == True) or (self.var in self.eqn[s])) and (self.eqn[s-1] == "*") and (self.eqn[s-2] == ")"+str(c)):

					#print("WOOAAHH NELLY")
					br_string_one = ""
					br_string_two = self.eqn[s]
					k = s
					m = s-2

					check_one = False
					d=0
					while self.eqn[m] != "("+str(c):

						if ")" in self.eqn[m]:

							br_string_one = ")"+br_string_one
							d+=1

						elif "(" in self.eqn[m]:

							br_string_one = "("+br_string_one
							d-=1

						else:

							if (self.eqn[m-1] == ")"+str(c+1)) and (self.eqn[m] in "+-") and (self.eqn[m+1] == "("+str(c+1)):

								check_one = True
								break

							else:

								br_string_one = self.eqn[m]+br_string_one

						m-=1

					if check_one == False:

						#br_string_one = "("+br_string_one+")"
						print("\n"+br_string_one+"*"+br_string_two)

						br_one, br_one_var = bracketify(br_string_one)
						br_one, br_one_deg = grouping(br_one)
						del br_one[0]
						del br_one[len(br_one)-1]

						br_two, br_two_var = bracketify("("+br_string_two+")")
						br_two, br_two_deg = grouping(br_two)
						del br_two[0]
						del br_two[len(br_two)-1]

						br = foiling(br_one, br_two, self.var)
						
						if not br:

							br = ["0"]

						br.insert(0,"(1")
						br.append(")1")
						br_string = stringify(br)
						print("= "+br_string)
				
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
						self.eqn, var = bracketify(eqn_string)
						
						if var:

							self.var = var[0]

						self.var = var[0]
						self.eqn, deg = grouping(self.eqn)
						eqn_string = stringify(self.eqn)
						print("\n"+eqn_string)
						s=-1

				elif (self.eqn[s] == "("+str(c)) and (self.eqn[s-1] == "*") and ((is_number(self.eqn[s-2]) == True) or (self.var in self.eqn[s-2])):

					#print("WOOAAHH NELLY")
					br_string_one = self.eqn[s-2]
					br_string_two = ""
					k = s
					m = s-2

					check_two = False
					d=0
					while self.eqn[k] != ")"+str(c):

						if "(" in self.eqn[k]:

							br_string_two += "("
							d+=1

						elif ")" in self.eqn[k]:

							br_string_two += ")"
							d-=1

						else:

							if (self.eqn[k-1] == ")"+str(c+1)) and (self.eqn[k] in "+-") and (self.eqn[k+1] == "("+str(c+1)):

								check_two = True
								break

							else:

								br_string_two += self.eqn[k]

						k+=1

					br_string_two += ")"

					if check_two == False:

						#br_string_one = "("+br_string_one+")"
						print("\n"+br_string_one+"*"+br_string_two)

						br_one, br_one_var = bracketify("("+br_string_one+")")
						br_one, br_one_deg = grouping(br_one)
						del br_one[0]
						del br_one[len(br_one)-1]

						br_two, br_two_var = bracketify(br_string_two)
						br_two, br_two_deg = grouping(br_two)
						del br_two[0]
						del br_two[len(br_two)-1]

						br = foiling(br_one, br_two, self.var)
						
						if not br:

							br = ["0"]

						br.insert(0,"(1")
						br.append(")1")
						br_string = stringify(br)
						print("= "+br_string)
				
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
						self.eqn, var = bracketify(eqn_string)
						
						if var:

							self.var = var[0]

						self.eqn, deg = grouping(self.eqn)
						eqn_string = stringify(self.eqn)
						print("\n"+eqn_string)
						s=-1
	
				s+=1

			#Now to check for ()+-()
			s=0
			while s != len(self.eqn):

				if (self.eqn[s] == "("+str(c)) and (self.eqn[s-1] in "+-") and (self.eqn[s-2] == ")"+str(c)):

					br_string_one = ""
					br_string_two = ""
					op = self.eqn[s-1]
					k = s
					m = s-2

					check_two = False
					d=0
					while self.eqn[k] != ")"+str(c):

						if "(" in self.eqn[k]:

							br_string_two += "("
							d+=1

						elif ")" in self.eqn[k]:

							br_string_two += ")"
							d-=1

						else:

							if (self.eqn[k-1] == ")"+str(c+1)) and (self.eqn[k] in "+-") and (self.eqn[k+1] == "("+str(c+1)):

								check_two = True
								break

							else:

								br_string_two += self.eqn[k]

						k+=1

					br_string_two += ")"
					check_one = False
					d=0
					while self.eqn[m] != "("+str(c):

						if ")" in self.eqn[m]:

							br_string_one = ")"+br_string_one
							d+=1

						elif "(" in self.eqn[m]:

							br_string_one = "("+br_string_one
							d-=1

						else:

							if (self.eqn[m-1] == ")"+str(c+1)) and (self.eqn[m] in "+-") and (self.eqn[m+1] == "("+str(c+1)):

								check_one = True
								break

							else:

								br_string_one = self.eqn[m]+br_string_one

						m-=1

					if (check_one == False) and (check_two == False):

						br_string_one = "("+br_string_one
						print("\n"+br_string_one+op+br_string_two)

						br_one, br_one_var = bracketify(br_string_one)
						br_one, br_one_deg = grouping(br_one)
						del br_one[0]
						del br_one[len(br_one)-1]

						br_two, br_two_var = bracketify(br_string_two)
						br_two, br_two_deg = grouping(br_two)
						del br_two[0]
						del br_two[len(br_two)-1]

						br = bracket_add(br_one, op, br_two, self.var)
						
						if not br:

							br = ["0"]

						br.insert(0,"(1")
						br.append(")1")
						br_string = stringify(br)
						print("= "+br_string)
				
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br_string_one+op+br_string_two, "("+br_string+")")
						self.eqn, var = bracketify(eqn_string)

						if var:

							self.var = var[0]

						self.eqn, deg = grouping(self.eqn)
						eqn_string = stringify(self.eqn)
						print("\n"+eqn_string)
						s=-1

				s+=1

			#print("before redundant_br", self.eqn)
			self = self.redundant_br()
			#print("after redundant_br", self.eqn)
			eqn_string = stringify(self.eqn)
			print(eqn_string)

		return self


	