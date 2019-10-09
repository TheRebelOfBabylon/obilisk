import math
import cmath
import calculus
import random

def is_number(s):

	try:
			
		float(s)
		return True

	except ValueError:
		
		return False

def cube_root(x):

	if isinstance(x, complex):

		return x**(1/3)
	
	else:

		if x >= 0.0:

			return x**(1/3)

		else:

			return -(-x)**(1/3)

#Takes two polynomials and adds them together
def poly_add(left_p,right_p):

	left_len = len(left_p)-1
	right_len = len(right_p)-1
	ans = []

	if left_len > right_len:

		for i in right_p:
			
			ans.insert(0,left_p[left_len]+right_p[right_len])
			left_len -= 1
			right_len -= 1

		ans.insert(0,left_p[0])

		return Poly_Func(ans)

	elif right_len > left_len:

		for i in left_p:
			
			ans.insert(0,left_p[left_len]+right_p[right_len])
			left_len -= 1
			right_len -= 1

		ans.insert(0,right_p[0])

		return Poly_Func(ans)

	elif left_len == right_len:

		for i in left_p:
			
			ans.insert(0,left_p[left_len]+right_p[right_len])
			left_len -= 1
			right_len -= 1

		return Poly_Func(ans)

class Poly_Func:

	def __init__(self,eqn):

		self.eqn = eqn

	def stringify(self,var_type):

		highest_deg = len(self.eqn)-1
		temp=""
		i=0
		for s in range(highest_deg,-1,-1):

			if i != highest_deg:

				if self.eqn[i] == 1:

					if s > 1:

						temp += var_type+"^"+str(s)

					elif s == 1:

						temp += var_type

					else:

						temp += "1"

					if self.eqn[i+1] < 0:

						pass
					
					else:

						temp += "+"

				elif self.eqn[i] == -1:

					if s > 1:

						temp += "-"+var_type+"^"+str(s)

					elif s == 1:

						temp += "-"+var_type

					else:

						temp += "-1"

					if self.eqn[i+1] < 0:

						pass
					
					else:

						temp += "+"

				else:

					if s > 1:

						temp += str(self.eqn[i])+var_type+"^"+str(s)

					elif s == 1:

						temp += str(self.eqn[i])+var_type

					else:

						temp += str(self.eqn[i])

					if self.eqn[i+1] < 0:

						pass
					
					else:

						temp += "+"

			else:

				if self.eqn[i] == 1:

					if s > 1:

						temp += var_type+"^"+str(s)

					elif s == 1:

						temp += var_type

					else:

						temp += "1"

				elif self.eqn[1] == -1:


					if s > 1:

						temp += "-"+var_type+"^"+str(s)

					elif s == 1:

						temp += "-"+var_type

					else:

						temp += "-1"

				else:

					if s > 1:

						temp += str(self.eqn[i])+var_type+"^"+str(s)

					elif s == 1:

						temp += str(self.eqn[i])+var_type

					else:

						temp += str(self.eqn[i])
	
			i += 1

		return temp

	""" Does synthetic division of a polynomial, only linear terms, no quadratics
	    divisor - array of coefficients of divisor
	"""
	def lin_divide(self,divisor):

		a = (-1*divisor[1])/divisor[0]
		b = 0
		ans = []
		n=0
		for i in self.eqn:

			ans.append(i+b)
			b = ans[n]*a
			n += 1

		return Poly_Func(ans)
			

	#Multiply a polynomial by a constant, x
	def poly_multiply(self, x):

		new_eqn=[]
		for i in self.eqn:

			new_eqn.append(x*i)

		return Poly_Func(new_eqn)

	#Evaluates the polynomial at given value
	def evaluate(self,value):

		exponent=len(self.eqn)-1
		ans = 0
		for i in self.eqn:

			ans += i*(value ** exponent)
			exponent -= 1

		return ans

	
	#Transforms polynomial equation into array of coefficients
	def get_coeff(self,highest_deg,var_type):

		coeff=[]

		for s in range(highest_deg,-1,-1):
			
			did_append = False
			
			for i in range(0,len(self.eqn)):
				
				if "^"+str(s) in self.eqn[i]:
				
					temp = self.eqn[i]
					a=""
					v=0
					while temp[v] != var_type:

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

						if self.eqn[i-1] == "-":

							a = -1*float(a)

						coeff.append(float(a))
						did_append = True

				elif ("^" not in self.eqn[i]) & (var_type in self.eqn[i]) & (s==1):
				
					temp = self.eqn[i]
					a=""
					v=0
					while temp[v] != var_type:

						a = a+str(temp[v])
						v+=1

					if a == "":

						a = 1

					if a == "-":

						a = -1

					if self.eqn[i-1] == "-":

						a = -1*float(a)

					coeff.append(float(a))
					did_append = True

				elif (is_number(self.eqn[i]) == True) & (s==0):
				
					a = float(self.eqn[i])
					if self.eqn[i-1] == "-":

						a = -1*a					

					coeff.append(a)
					did_append = True

			if not did_append:

				coeff.append(0) 

		return Poly_Func(coeff)

	#Normalizes polynomial
	def normalize(self):

		if (self.eqn[0] == 1) or (self.eqn[0] == 0):

			return Poly_Func(self.eqn)

		else:

			const = self.eqn[0]
			for i in range(0,len(self.eqn)):

				self.eqn[i] /= const

			return Poly_Func(self.eqn)
		
	#Creates a cauchy polynomial
	def cauchy_poly(self):

		self.normalize()
		cauchy=[]

		for i in range(0,len(self.eqn)-1):

			cauchy.append(abs(self.eqn[i]))

		cauchy.insert(len(cauchy),-1*abs(self.eqn[i+1]))

		return Poly_Func(cauchy)

	#Finds root of polynomial using Newton-Raphson Method
	def newton_raphson(self,err):

		der = calculus.coeff_derivative(self.eqn)
		x = random.uniform(0,1)
		
		while abs(self.evaluate(x)) > abs(err):

			x = x-((self.evaluate(x))/(der.evaluate(x)))
			#print("x",x, self.evaluate(x))

		return x

	#Quadratic Formula
	def quadratic(self):

		print("\n-- Using the quadratic formula --")
		print("ax^2 + bx + c = 0")
		print("x = (-b +/- SQRT(b^2 - 4ac))/2a\n")

		a = self.eqn[0]
		print("a = "+str(a))
		b = self.eqn[1]
		print("b = "+str(b))
		c = self.eqn[2]
		print("c = "+str(c))
		print("")

		ans=[0,0]
		ans[0] = ((-1*b)+((b**2)-(4*a*c))**0.5)/(2*a)
		ans[1] = ((-1*b)-((b**2)-(4*a*c))**0.5)/(2*a)

		return ans

	#Cubic root formula
	def cardano(self):

		print("\n-- Using Cardano's Formula: --")
		print("ax^3 + bx^2 + cx + d = 0\n")
		print("x1 = s+t-(b/3a)")
		print("x2 = -(s+t)/2 - (b/3a) + (i*SQRT(3)/2)*(s-t)")
		print("x3 = -(s+t)/2 - (b/3a) - (i*SQRT(3)/2)*(s-t)\n")
	
		a = self.eqn[0]
		print("a = "+str(a))
		b = self.eqn[1]
		print("b = "+str(b))
		c = self.eqn[2]
		print("c = "+str(c))
		d = self.eqn[3]
		print("d = "+str(d))
		print("")

		#depressed cubic
		p = ((3*a*c)-(b**2))/(9*(a**2))
		q = ((9*a*b*c)-(27*(a**2)*d)-(2*(b**3)))/(54*(a**3))

		print("Depressed cubic: y^3 + 3py - 2q = 0\n")
		print("y^3+"+str(3*p)+"y+"+str(-2*q)+"=0")
		print("p = (3ac - b^2)/9a^2 = "+str(p))
		print("q = (9abc - 27a^2d - 2b^3)/54a^3 = "+str(q)+"\n")

		s = cube_root((q)+(((p)**3)+((q)**2))**(1/2))
		t = cube_root((q)-(((p)**3)+((q)**2))**(1/2))

		print("s = (q + SQRT(p^3 + q^2))^(1/3) = "+str(s))
		print("t = (q - SQRT(p^3 + q^2))^(1/3) = "+str(t)+"\n")

		ans = [0,0,0]
		ans[0] = s+t-(b/(3*a))
		ans[1] = (-1*((s+t)/2))-(b/(3*a))+(((1j*(3**0.5))/2)*(s-t))
		ans[2] = (-1*((s+t)/2))-(b/(3*a))-(((1j*(3**0.5))/2)*(s-t))

		return ans

	#Quartic root formula
	def ferrari(self):

		print("\n-- Using Ferrari's Method: --")
		print("ax^4 + bx^3 + cx^2 + dx + e = 0\n")
	
		a = self.eqn[0]
		print("a = "+str(a))
		b = self.eqn[1]
		print("b = "+str(b))
		c = self.eqn[2]
		print("c = "+str(c))
		d = self.eqn[3]
		print("d = "+str(d))
		e = self.eqn[4]
		print("e = "+str(e))
		print("")

		#depressed quartic

		print("Substitution: x = y-(b/4a)\n")
		print("Depressed quartic: y^4 + py^2 + qy + r = 0")

		print("y1 = SQRT((-1/2)*(2z - p)) + SQRT((1/2)*(-2z - p + 2q/SQRT(2z - p)))")
		print("y2 = SQRT((-1/2)*(2z - p)) - SQRT((1/2)*(-2z - p + 2q/SQRT(2z - p)))")
		print("y3 = SQRT((1/2)*(2z - p)) + SQRT((1/2)*(-2z - p - 2q/SQRT(2z - p)))")
		print("y4 = SQRT((1/2)*(2z - p)) - SQRT((1/2)*(-2z - p - 2q/SQRT(2z - p)))\n")

		p = (c/a)-((3*b**2)/(8*a**2))
		q = (d/a)-((b*c)/(2*a**2))+(b**3/(8*a**3))
		r = (e/a)-((b*d)/(4*a**2))+(((b**2)*c)/(16*a**3))-((3*b**4)/(256*a**4))

		print("p = ((c/a) - 3b^2)/8a^2 = "+str(p))
		print("q = ((d/a) - bc/(2a^2) + b^3)/8a^3 = "+str(q))
		print("r = ((e/a) - bd/(4a^2) + b^2c/16a^3 - 3b^4)/256a^4 = "+str(q)+"\n")

		depressed = "y^4+"+str(p)+"y^2+"+str(q)+"y+"+str(r)+"=0"
		print("Depressed quartic is "+depressed+"\n")

		#resolvent cubic
		print("Resolvent cubic: 8z^3 - 4pz^2 - 8rz + (4pr - q^2) = 0")
		resolvent = "8z^3+"+str(-4*p)+"z^2+"+str(-8*r)+"z+"+str((4*p*r)-(q**2))+"=0"
		print(resolvent)

		cubic = [8,-4*p,-8*r,(4*p*r)-(q**2)]
		cubic = Poly_Func(cubic)
		cubic_ans = cubic.cardano()

		print("the values of z of "+resolvent+" are")

		for i in cubic_ans:

			print(i)

		for i in cubic_ans:

			try:

				print("\nTrying "+str(i)+" to find roots of depressed quartic "+depressed+" ...\n")

				s = i
	
				y_one = ((-1/2)*((2*s)-p)**(1/2))+((1/2)*((-2*s)-p+(2*q/((2*s)-p)**(1/2)))**(1/2))
				y_two = ((-1/2)*((2*s)-p)**(1/2))-((1/2)*((-2*s)-p+(2*q/((2*s)-p)**(1/2)))**(1/2))
				y_three = ((1/2)*((2*s)-p)**(1/2))+((1/2)*((-2*s)-p-(2*q/((2*s)-p)**(1/2)))**(1/2))
				y_four = ((1/2)*((2*s)-p)**(1/2))-((1/2)*((-2*s)-p-(2*q/((2*s)-p)**(1/2)))**(1/2))

			except ZeroDivisionError:

				print("attempt failed...")

			else:

				break

		print("Success!\n")

		print("The values of y are")
		print(y_one)
		print(y_two)
		print(y_three)
		print(y_four,"\n")

		print("Recall x = y-(b/4a)\n")

		ans = [0,0,0,0]

		ans[0] = y_one-(b/(4*a))
		ans[1] = y_two-(b/(4*a))
		ans[2] = y_three-(b/(4*a))
		ans[3] = y_four-(b/(4*a))

		return ans
