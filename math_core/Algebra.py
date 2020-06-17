"""Methods for polynomial root finding."""
from __future__ import annotations
import math
import cmath
from math_core.Equation import Equation, is_number, oper_dict
import random

from typing import Tuple, List, Union

def cube_root(x: Union[int, float, complex]) -> Union[int, float, complex]:
	"""Function takes the cubic root of a number. Created to ensure proper sign of answer is given."""
	if isinstance(x, complex):

		return x**(1/3)
	
	else:

		if x >= 0.0:

			return x**(1/3)

		else:

			return -(-x)**(1/3)


def poly_add(left_p: List[Union[int, float, complex]],right_p: List[Union[int, float, complex]]) -> Algebra:
	"""Function takes two polynomials and adds them together."""
	left_len = len(left_p)-1
	right_len = len(right_p)-1
	ans = []

	if left_len > right_len:

		for i in right_p:
			
			ans.insert(0,left_p[left_len]+right_p[right_len])
			left_len -= 1
			right_len -= 1

		ans.insert(0,left_p[0])

	elif right_len > left_len:

		for i in left_p:
			
			ans.insert(0,left_p[left_len]+right_p[right_len])
			left_len -= 1
			right_len -= 1

		ans.insert(0,right_p[0])

	elif left_len == right_len:

		for i in left_p:
			
			ans.insert(0,left_p[left_len]+right_p[right_len])
			left_len -= 1
			right_len -= 1

	return Algebra(ans)

class Algebra(Equation):
	"""This class is used in polynomial root finding problems. Objects of this class have a single attribute being the equation in List[str] format."""
	def __init__(self, eqn_string: str):
		Equation.__init__(self, eqn_string)
		self.deg = []
		self.coeff = []
		self.grouping()
		self.eqn_string_update()
		self.get_coeff()

	def lin_divide(self, divisor: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
		"""Function does synthetic division of a polynomial. Divisor can only be a linear polynomial."""
		a = (-1*divisor[1])/divisor[0]
		b = 0
		ans = []
		n=0
		for i in self.coeff:

			ans.append(i+b)
			b = ans[-1]*a

		return ans

	def poly_multiply(self, x: Union[int, float, complex]) -> List[Union[int, float, complex]]:
		"""Multiply a polynomial by a constant."""

		new_eqn=[]
		for i in self.coeff:

			new_eqn.append(x*i)

		return new_eqn

	def evaluate(self, value: Union[int, float, complex]) -> Union[int, float, complex]:
		"""Evaluates the polynomial at a given value."""

		ans = 0
		for i, j in zip(self.coeff, self.deg):

			ans += i*(value ** j)

		return ans

	def get_coeff(self):
		"""Transforms polynomial equation into a list of coefficients in order of highest to lowest power."""
		coeff=[]

		for s in range(self.deg[0],-1,-1):
			
			did_append = False
			
			for i in range(0,len(self.eqn)):
				
				if "^"+str(float(s)) in self.eqn[i]:
				
					temp = self.eqn[i]
					a=""
					v=0
					while temp[v] != self.var_type[0]:

						a = a+str(temp[v])
						v+=1

					v += 2
					b=""
					while v != len(temp):

						b = b+str(temp[v])
						v+=1

					if int(float(b)) == s:

						if a == "":

							a = 1

						if a == "-":

							a = -1

						if self.eqn[i-1] == "-":

							a = -1*float(a)

						coeff.append(float(a))
						did_append = True

				elif ("^" not in self.eqn[i]) & (self.var_type[0] in self.eqn[i]) & (s==1):
				
					temp = self.eqn[i]
					a=""
					v=0
					while temp[v] != self.var_type[0]:

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
				
					a = complex(self.eqn[i])

					if round(a.imag,6) == 0:

						a = float(a.real)
				
					if self.eqn[i-1] == "-":

						a = -1*a					

					coeff.append(a)
					did_append = True

			if not did_append:

				coeff.append(0) 

		self.coeff = coeff

	def normalize(self) -> List[Union[int, float, complex]]:
		"""Normalizes the polynomial."""
		norm=self.coeff[:]
		if (norm[0] == 1) or (norm[0] == 0):

			return norm

		else:

			const = norm[0]
			for i in range(0,len(norm)):

				norm[i] /= const

			return norm
		
	#Creates a cauchy polynomial
	def cauchy_poly(self) -> List[Union[int, float, complex]]:
		"""Normalizes polynomial and takes the absolute value of each coefficient."""
		cauchy = []
		norm = self.normalize()
		for i in range(0,len(norm)-1):

			cauchy.append(abs(norm[i]))

		cauchy.append(-1*abs(norm[i+1]))

		return cauchy

	def newton_raphson(self, err: Union[int, float] = 1e-5) -> Union[int, float, complex]:
		"""Finds roots of polynomial using Newton-Raphson method."""
		from math_core.Calculus import Calculus
		der = Calculus(self.eqn_string)
		der.coeff = der.coeff_derivative()
		x = random.uniform(0,1)
		
		while abs(self.evaluate(x)) > abs(err):

			x = x-((self.evaluate(x))/(der.evaluate(x)))
			#print("x",x)

		return x

	def quadratic(self) -> List[Union[int, float, complex]]:
		"""Solve quadratic polynomials using the quadratic formula."""
		if len(self.coeff) != 3:
			raise ValueError("Quadratics must have 3 terms.")
		self.solution.append("")
		print("\n-- Using the quadratic formula --")
		self.solution.append("-- Using the quadratic formula --")
		print("ax^2 + bx + c = 0")
		self.solution.append("ax^2 + bx + c = 0")
		print("x = (-b +/- √(b^2 - 4ac))/2a\n")
		self.solution.append("x = (-b +/- √(b^2 - 4ac))/2a")

		self.solution.append("")
		a = self.coeff[0]
		print("a = "+str(a))
		self.solution.append("a = "+str(a))
		b = self.coeff[1]
		print("b = "+str(b))
		self.solution.append("b = "+str(b))
		c = self.coeff[2]
		print("c = "+str(c))
		self.solution.append("c = "+str(c))
		print("")

		ans=[0,0]
		ans[0] = ((-1*b)+((b**2)-(4*a*c))**0.5)/(2*a)
		ans[-1] = ((-1*b)-((b**2)-(4*a*c))**0.5)/(2*a)

		self.solution.append("\nThe final answers are:")
		for i in ans:
			self.solution.append(str(i))

		return ans

	def cardano(self) -> List[Union[int, float, complex]]:
		"""Root finding formula for cubic polynomials."""
		if len(self.coeff) != 4:
			raise ValueError("Cubics must have 4 terms.")
		self.solution.append("")
		print("\n-- Using Cardano's Formula: --")
		self.solution.append("-- Using Cardano's Formula: --")
		print("ax^3 + bx^2 + cx + d = 0\n")
		self.solution.append("ax^3 + bx^2 + cx + d = 0")
		print("x1 = s+t-(b/3a)")
		self.solution.append("x1 = s+t-(b/3a)")
		print("x2 = -(s+t)/2 - (b/3a) + (i*√3/2)*(s-t)")
		self.solution.append("x2 = -(s+t)/2 - (b/3a) + (i*√3/2)*(s-t)")
		print("x3 = -(s+t)/2 - (b/3a) - (i*√3/2)*(s-t)\n")
		self.solution.append("x3 = -(s+t)/2 - (b/3a) - (i*√3/2)*(s-t)")
	
		self.solution.append("")
		a = self.coeff[0]
		print("a = "+str(a))
		self.solution.append("a = "+str(a))
		b = self.coeff[1]
		print("b = "+str(b))
		self.solution.append("b = "+str(b))
		c = self.coeff[2]
		print("c = "+str(c))
		self.solution.append("c = "+str(c))
		d = self.coeff[3]
		print("d = "+str(d))
		self.solution.append("d = "+str(d))
		print("")

		#depressed cubic
		p = ((3*a*c)-(b**2))/(9*(a**2))
		q = ((9*a*b*c)-(27*(a**2)*d)-(2*(b**3)))/(54*(a**3))

		self.solution.append("")
		print("Depressed cubic: y^3 + 3py - 2q = 0\n")
		self.solution.append("Depressed cubic: y^3 + 3py - 2q = 0")
		print("y^3+"+str(3*p)+"y+"+str(-2*q)+"=0")
		self.solution.append("y^3+"+str(3*p)+"y+"+str(-2*q)+"=0")
		self.solution.append("")
		print("p = (3ac - b^2)/9a^2 = "+str(p))
		self.solution.append("p = (3ac - b^2)/9a^2 = "+str(p))
		print("q = (9abc - 27a^2d - 2b^3)/54a^3 = "+str(q)+"\n")
		self.solution.append("q = (9abc - 27a^2d - 2b^3)/54a^3 = "+str(q))

		s = cube_root((q)+(((p)**3)+((q)**2))**(1/2))
		t = cube_root((q)-(((p)**3)+((q)**2))**(1/2))

		self.solution.append("")
		print("s = (q + √(p^3 + q^2))^(1/3) = "+str(s))
		self.solution.append("s = (q + √(p^3 + q^2))^(1/3) = "+str(s))
		print("t = (q - √(p^3 + q^2))^(1/3) = "+str(t)+"\n")
		self.solution.append("t = (q - √(p^3 + q^2))^(1/3) = "+str(t))

		ans = [0,0,0]
		ans[0] = s+t-(b/(3*a))
		ans[1] = (-1*((s+t)/2))-(b/(3*a))+(((1j*(3**0.5))/2)*(s-t))
		ans[-1] = (-1*((s+t)/2))-(b/(3*a))-(((1j*(3**0.5))/2)*(s-t))

		self.solution.append("\nThe final answers are:")
		for i in ans:
			self.solution.append(str(i))

		return ans

	#Quartic root formula
	def ferrari(self) -> List[Union[int, float, complex]]:
		"""Root finding formula for quartic polynomials."""
		if len(self.coeff) != 5:
			raise ValueError("Quartics must have 5 terms.")
		self.solution.append("")
		print("\n-- Using Ferrari's Method: --")
		self.solution.append("-- Using Ferrari's Method: --")
		print("ax^4 + bx^3 + cx^2 + dx + e = 0\n")
		self.solution.append("ax^4 + bx^3 + cx^2 + dx + e = 0")
	
		self.solution.append("")
		a = self.coeff[0]
		print("a = "+str(a))
		self.solution.append("a = "+str(a))
		b = self.coeff[1]
		print("b = "+str(b))
		self.solution.append("b = "+str(b))
		c = self.coeff[2]
		print("c = "+str(c))
		self.solution.append("c = "+str(c))
		d = self.coeff[3]
		print("d = "+str(d))
		self.solution.append("d = "+str(d))
		e = self.coeff[4]
		print("e = "+str(e))
		self.solution.append("e = "+str(e))
		print("")

		#depressed quartic

		self.solution.append("")
		print("Substitution: x = y-(b/4a)\n")
		self.solution.append("Substitution: x = y-(b/4a)")
		print("Depressed quartic: y^4 + py^2 + qy + r = 0")
		self.solution.append("Depressed quartic: y^4 + py^2 + qy + r = 0")

		self.solution.append("")
		print("y1 = √((-1/2)*(2z - p)) + √((1/2)*(-2z - p + 2q/√(2z - p)))")
		self.solution.append("y1 = √((-1/2)*(2z - p)) + √((1/2)*(-2z - p + 2q/√(2z - p)))")

		print("y2 = √((-1/2)*(2z - p)) - √((1/2)*(-2z - p + 2q/√(2z - p)))")
		self.solution.append("y2 = √((-1/2)*(2z - p)) - √((1/2)*(-2z - p + 2q/√(2z - p)))")

		print("y3 = √((1/2)*(2z - p)) + √((1/2)*(-2z - p - 2q/√(2z - p)))")
		self.solution.append("y3 = √((1/2)*(2z - p)) + √((1/2)*(-2z - p - 2q/√(2z - p)))")

		print("y4 = √((1/2)*(2z - p)) - √((1/2)*(-2z - p - 2q/√(2z - p)))\n")
		self.solution.append("y4 = √((1/2)*(2z - p)) - √((1/2)*(-2z - p - 2q/√(2z - p)))")

		p = (c/a)-((3*b**2)/(8*a**2))
		q = (d/a)-((b*c)/(2*a**2))+(b**3/(8*a**3))
		r = (e/a)-((b*d)/(4*a**2))+(((b**2)*c)/(16*a**3))-((3*b**4)/(256*a**4))

		self.solution.append("")
		print("p = ((c/a) - 3b^2)/8a^2 = "+str(p))
		self.solution.append("p = ((c/a) - 3b^2)/8a^2 = "+str(p))
		print("q = ((d/a) - bc/(2a^2) + b^3)/8a^3 = "+str(q))
		self.solution.append("q = ((d/a) - bc/(2a^2) + b^3)/8a^3 = "+str(q))
		print("r = ((e/a) - bd/(4a^2) + b^2c/16a^3 - 3b^4)/256a^4 = "+str(q)+"\n")
		self.solution.append("r = ((e/a) - bd/(4a^2) + b^2c/16a^3 - 3b^4)/256a^4 = "+str(q))

		self.solution.append("")
		depressed = "y^4+"+str(p)+"y^2+"+str(q)+"y+"+str(r)+"=0"
		print("Depressed quartic is "+depressed+"\n")
		self.solution.append("Depressed quartic is "+depressed)

		self.solution.append("")
		#resolvent cubic
		print("Resolvent cubic: 8z^3 - 4pz^2 - 8rz + (4pr - q^2) = 0")
		self.solution.append("Resolvent cubic: 8z^3 - 4pz^2 - 8rz + (4pr - q^2) = 0")
		resolvent = "8z^3+"+str(-4*p)+"z^2+"+str(-8*r)+"z+"+str((4*p*r)-(q**2))
		print(resolvent+"=0")
		self.solution.append(resolvent+"=0")

		cubic = Algebra(resolvent)
		cubic_ans = cubic.cardano()

		for i in cubic.solution:

			self.solution.append(i)

		self.solution.append("")
		print("the values of z of "+resolvent+" are")
		self.solution.append("the values of z of "+resolvent+" are")

		for i in cubic_ans:

			print(i)
			self.solution.append(i)

		for i in cubic_ans:

			try:

				self.solution.append("")
				print("\nTrying "+str(i)+" to find roots of depressed quartic "+depressed+" ...\n")
				self.solution.append("Trying "+str(i)+" to find roots of depressed quartic "+depressed+" ...")

				s = i
	
				y_one = ((-1/2)*((2*s)-p)**(1/2))+((1/2)*((-2*s)-p+(2*q/((2*s)-p)**(1/2)))**(1/2))
				y_two = ((-1/2)*((2*s)-p)**(1/2))-((1/2)*((-2*s)-p+(2*q/((2*s)-p)**(1/2)))**(1/2))
				y_three = ((1/2)*((2*s)-p)**(1/2))+((1/2)*((-2*s)-p-(2*q/((2*s)-p)**(1/2)))**(1/2))
				y_four = ((1/2)*((2*s)-p)**(1/2))-((1/2)*((-2*s)-p-(2*q/((2*s)-p)**(1/2)))**(1/2))

			except ZeroDivisionError:

				print("attempt failed...")
				self.solution.append("attempt failed...")

			else:

				break

		print("Success!\n")
		self.solution.append("Success!")
		self.solution.append("")

		print("The values of y are")
		self.solution.append("The values of y are")
		print(y_one)
		self.solution.append(str(y_one))
		print(y_two)
		self.solution.append(str(y_two))
		print(y_three)
		self.solution.append(str(y_three))
		print(y_four,"\n")
		self.solution.append(str(y_four))
		self.solution.append("\n")

		print("Recall x = y-(b/4a)\n")
		self.solution.append("Recall x = y-(b/4a)")
		self.solution.append("")

		ans = [0,0,0,0]

		ans[0] = y_one-(b/(4*a))
		self.solution.append("x = "+str(y_one)+"-("+str(b)+"/(4*"+str(a)+"))")
		ans[1] = y_two-(b/(4*a))
		self.solution.append("x = "+str(y_two)+"-("+str(b)+"/(4*"+str(a)+"))")
		ans[2] = y_three-(b/(4*a))
		self.solution.append("x = "+str(y_three)+"-("+str(b)+"/(4*"+str(a)+"))")
		ans[-1] = y_four-(b/(4*a))
		self.solution.append("x = "+str(y_four)+"-("+str(b)+"/(4*"+str(a)+"))")

		self.solution.append("\nThe final answers are:")
		for i in ans:

			self.solution.append(str(i))

		return ans

	def grouping(self):
		"""This function groups terms around variables into a single index."""

		# print("Inside grouping", eqn)
		# Start with combining with constants and powers into one index
		i = 0
		p = 0
		b = 0
		p_b = 0
		var = []
		b_open = 0
		b_close = 0
		b_loc = 0
		while i != len(self.eqn):

			mod = False
			# print(eqn)
			# This index has a variable in it
			if ("(" in self.eqn[i]) & (self.eqn[i] not in oper_dict.values()):

				b += 1
				b_open += 1
				b_loc = i

				for op in oper_dict.values():

					if op == self.eqn[i - 1]:
						p_b = b
						p = i

			if (")" in self.eqn[i]) & (self.eqn[i] not in oper_dict.values()):

				if self.eqn[i] == ")" + str(p_b):
					p_b = 0
					p = 0

				b -= 1
				b_close += 1

			if (self.eqn[i].isalpha() == True) and (len(self.eqn[i]) == 1):

				# print("eqn[i]", eqn[i])
				if self.eqn[i] not in var:
					var.append(self.eqn[i])

				if (self.eqn[i + 1] == "^") and (is_number(self.eqn[i + 2]) == True):
					self.eqn[i] = self.eqn[i] + "^" + self.eqn[i + 2]
					del self.eqn[i + 1:i + 3]
					mod = True
				# print(eqn)

				if (is_number(self.eqn[i - 1]) == True):
					self.eqn[i - 1] = self.eqn[i - 1] + self.eqn[i]
					del self.eqn[i]
					mod = True
				# print(eqn)

				if (self.eqn[i - 1] == "*") and (is_number(self.eqn[i - 2]) == True):
					self.eqn[i - 2] = self.eqn[i - 2] + self.eqn[i]
					del self.eqn[i - 1:i + 1]
					mod = True
				# print(eqn)

				if ((b_open != b_close) and (self.eqn[b_loc - 1] in oper_dict.values())) or (p != 0):

					if p != 0:
						b_loc = p

					temp = self.eqn[b_loc - 1]
					# print(temp)
					j = self.eqn[b_loc]
					j = j.replace('(', '')
					u = b_loc
					while self.eqn[u] != ")" + j:

						if "(" in self.eqn[u]:

							temp += "("

						elif ")" in self.eqn[u]:

							temp += ")"

						else:

							temp += self.eqn[u]

						u += 1

					temp += ")"
					self.eqn[b_loc - 1] = temp
					del self.eqn[b_loc:u + 1]
					# print("eqn[b_loc]",eqn[b_loc])

					if (self.eqn[b_loc] == "^") and (is_number(self.eqn[b_loc + 1]) == True):
						temp = self.eqn[b_loc - 1] + "^" + self.eqn[b_loc + 1]
						self.eqn[b_loc - 1] = temp
						del self.eqn[b_loc:b_loc + 2]

					mod = True
				# print(eqn)

				if mod == True:
					i = 0

			i += 1

		# This section of code was added because when grouping is fed an equation that is already grouped, it fails
		# print("Made it here", eqn)
		if len(var) == 0:

			for i in range(0, len(self.eqn)):

				if ("(" not in self.eqn[i]) and (")" not in self.eqn[i]) and (self.eqn[i] not in "*/+-") and (
						is_number(self.eqn[i]) == False):

					check = False
					oper = ""
					for op in oper_dict.values():

						if op in self.eqn[i]:
							check == True
							oper = op

					if check == False:

						if "^" in self.eqn[i]:

							temp = self.eqn[i]
							j = 0
							while temp[j] != "^":
								j += 1

							j -= 1
							if temp[j] not in var:
								var.append(temp[j])

						else:

							temp = self.eqn[i]
							x = temp[-1]

							if x not in var:
								var.append(x)

					else:

						temp = self.eqn[i]
						temp = temp.replace(oper, '')
						j = 0
						x = ""
						while j != len(temp):

							if temp[j].isalpha() == True:
								x = temp[j]

							j += 1

						if x != "":

							if x not in var:
								var.append(x)

		# print("Now we here", eqn)
		eqn_deg = []
		for s in self.eqn:

			for t in var:

				if t in s:

					if "^" in s:

						check = False
						for op in oper_dict.values():

							if op in s:
								check = True

						if check == False:

							q = 0
							temp = s
							# print("temp",temp)

							while temp[q] != "^":
								q += 1

							q += 1
							pow = ""
							while (q != len(temp)):

								if (is_number(temp[q]) == True) or (temp[q] == "."):
									pow += temp[q]
									# print(pow, "q = "+str(q), "len(temp) = "+str(len(temp)))
									q += 1

							pow = int(float(pow))

							if pow not in eqn_deg:
								eqn_deg.append(pow)
						# print(s, eqn_deg)

					else:

						check = False
						for op in oper_dict.values():

							if op in s:
								check = True

						if check == False:

							if 1 not in eqn_deg:
								eqn_deg.append(1)
						# print(s, eqn_deg)

			if is_number(s) == True:

				if 0 not in eqn_deg:
					eqn_deg.append(0)
			# print(s, eqn_deg)

		# print("eqn_deg", eqn_deg, eqn)
		new_eqn_deg = []
		s = 0
		while s != len(eqn_deg):

			k = 0

			for t in eqn_deg:

				if eqn_deg[s] < t:
					k = 1

			if k != 1:
				new_eqn_deg.append(eqn_deg[s])
				del eqn_deg[s]
				s = -1

			s += 1

		if len(self.eqn) > 1:

			if self.eqn[1] == "-":
				self.eqn[1] = self.eqn[1] + self.eqn[2]
				del self.eqn[2]

		# print("new_eqn_deg", new_eqn_deg)
		self.deg = new_eqn_deg
		self.eqn_string_update()
