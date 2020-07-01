"""All methods related to calculus type problems."""
from __future__ import annotations
import math
import cmath
from math_core.Equation import is_number, stringify
from math_core.Algebra import Algebra
from typing import List, Tuple, Union
import copy

class Calculus(Algebra):

	def find_expression_to_der(self):
		"""Method takes eqn attribute of the equation and isolates part to derive and stores in eqn"""
		eqn_temp = []
		for s in range(0, len(self.eqn)):
			if (self.eqn[s] == "(2") and (self.eqn[s-1] == "d/d"+self.var_type[0]):
				k = s+1
				while self.eqn[k] != ")2":
					eqn_temp.append(self.eqn[k])
					k += 1
				break
		if not eqn_temp:
			for s in range(0, len(self.eqn)):
				if (self.eqn[s] == "=") and ("'" in self.eqn[s-1]):
					k = s+1
					while self.eqn[k] != ")1":
						eqn_temp.append(self.eqn[k])
						k += 1
		eqn_temp.insert(0, "(1")
		eqn_temp.append(")1")
		self.eqn = copy.deepcopy(eqn_temp)
		self.solution.append(stringify(self.lhs)+"="+stringify(self.eqn))
		self.get_coeff()

	def get_coeff(self):
		"""Transforms polynomial equation into a list of coefficients in order of highest to lowest power."""
		coeff = []
		for s in range(self.deg[0], -1, -1):

			did_append = False

			for i in range(0, len(self.eqn)):

				if "^" + str(float(s)) in self.eqn[i]:

					temp = self.eqn[i]
					a = ""
					v = 0
					while temp[v] != self.var_type[0]:
						a = a + str(temp[v])
						v += 1

					v += 2
					b = ""
					while v != len(temp):
						b = b + str(temp[v])
						v += 1

					if int(float(b)) == s:

						if a == "":
							a = 1

						if a == "-":
							a = -1

						if self.eqn[i - 1] == "-":
							a = -1 * float(a)

						coeff.append(float(a))
						did_append = True

				elif ("^" not in self.eqn[i]) & (self.var_type[0] in self.eqn[i]) & (s == 1):

					temp = self.eqn[i]
					a = ""
					v = 0
					while temp[v] != self.var_type[0]:
						a = a + str(temp[v])
						v += 1

					if a == "":
						a = 1

					if a == "-":
						a = -1

					if self.eqn[i - 1] == "-":
						a = -1 * float(a)

					coeff.append(float(a))
					did_append = True

				elif (is_number(self.eqn[i])) & (s == 0):

					a = complex(self.eqn[i])

					if round(a.imag, 6) == 0:
						a = float(a.real)

					if self.eqn[i - 1] == "-":
						a = -1 * a

					coeff.append(a)
					did_append = True

			if not did_append:
				coeff.append(0)

		self.coeff = coeff

	def poly_derivative(self) -> List[str]:
		"""Takes first derivative of a polynomial."""
		#loop from highest exponent to 1. Apply normal derivative rules
		der=[]
		n = 0

		if self.deg[0] == 0:
			self.solution.append("The derivative of "+self.eqn[1]+" is 0")
			der.append("0")
		else:
			for s in range(self.deg[0],-1,-1):

				#walk eqn
				for i in range(0,len(self.eqn)-1):

					if "^"+str(s) in self.eqn[i]:

						temp = self.eqn[i]
						a = ""
						v = 0
						while temp[v] != self.var_type[0]:

							a = a+str(temp[v])
							v+=1

						if a == "":

							a = "1"

						if a == "-":

							a = "-1"

						new_a = str(s*float(a))

						if s == 2:

							self.solution.append("The derivative of "+self.eqn[i]+" is "+new_a+self.var_type[0])
							der.insert(n,new_a+self.var_type[0])
							n=n+1

						else:

							self.solution.append("The derivative of " + self.eqn[i] + " is "+new_a+self.var_type[0]+"^"+str(s-1))
							der.insert(n,new_a+self.var_type[0]+"^"+str(s-1))
							n=n+1

						if (self.eqn[i+1] == "+") and (self.var_type[0] in self.eqn[i+2]):

							der.insert(n,"+")
							n=n+1

						if (self.eqn[i+1] == "-") and (self.var_type[0] in self.eqn[i+2]):

							der.insert(n,"-")
							n=n+1

					# is it a power of 1 term
					elif ("^" not in self.eqn[i]) and (self.var_type[0] in self.eqn[i]) and (s == 1):

						temp = self.eqn[i]
						a = ""
						v = 0
						while temp[v] != self.var_type[0]:

							a = a+str(temp[v])
							v=v+1

						if a == "":

							a = "1"

						if a == "-":

							a = "-1"

						self.solution.append(
							"The derivative of " + self.eqn[i] + " is " + a)
						der.insert(n,a)
						n=n+1

						if (self.eqn[i+1] == "+") and (self.var_type[0] in self.eqn[i+2]):

							der.insert(n,"+")
							n=n+1

						if (self.eqn[i+1] == "-") and (self.var_type[0] in self.eqn[i+2]):

							der.insert(n,"-")
							n=n+1

					elif (is_number(self.eqn[i])) and (s == 0):

						self.solution.append(
							"The derivative of " + self.eqn[i] + " is 0")

		der.insert(0,"(1")
		der.insert(len(der),")1")

		return der

	def coeff_derivative(self, update_self_coeff: bool = False) -> List[Union[int, float, complex]]:
		"""Takes first derivative of a polynomial. Input eqn is a list of coefficients."""
		der=[]
		expo = len(self.coeff)-1
		for i in self.coeff:

			if expo == 0:

				pass

			else:

				der.append(i*expo)
				expo -= 1

		if update_self_coeff:
			self.coeff = der
		return der

	def derivative(self):
		"""Finds the derivative of the equation and updates all parameters"""
		self.find_expression_to_der()
		der = self.poly_derivative()
		self.coeff_derivative(update_self_coeff=True)
		#LHS first
		self.lhs[1] = self.lhs[1].replace('/d'+self.var_type[0], '')
		self.lhs[1] = self.lhs[1].replace('d','')
		self.lhs[1] = self.lhs[1].replace(self.lhs[1], self.lhs[1]+"'")
		#RHS
		self.rhs = copy.deepcopy(der)
		self.solution.append("The final answer is "+stringify(self.lhs)+"="+stringify(self.rhs))
		#eqn
		self.eqn.clear()
		s = 0
		while s != len(self.lhs)-1:
			self.eqn.append(self.lhs[s])
			s += 1
		self.eqn.append("=")
		s = 1
		while s != len(self.rhs):
			self.eqn.append(self.rhs[s])
			s += 1
		self.grouping()
