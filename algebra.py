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

		del ans[len(ans)-1]

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
		
			for i in range(0,len(self.eqn)):

				if "^"+str(s) in self.eqn[i]:
				
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

				elif (is_number(self.eqn[i]) == True) & (s==0):
				
					a = float(self.eqn[i])
					if self.eqn[i-1] == "-":

						a = -1*a					

					coeff.append(a)

		return Poly_Func(coeff)

	#Normalizes polynomial
	def normalize(self):

		if self.eqn[0] == 1:

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
