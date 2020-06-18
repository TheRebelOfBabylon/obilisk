"""All methods related to calculus type problems."""
from __future__ import annotations
import math
import cmath
from math_core.Algebra import Algebra
from typing import List, Tuple, Union

class Calculus(Algebra):

	def poly_derivative(self) -> List[str]:
		"""Takes first derivative of a polynomial."""
		#loop from highest exponent to 1. Apply normal derivative rules
		der=[]
		n = 0

		for s in range(self.deg[0],0,-1):

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

						der.insert(n,new_a+self.var_type[0])
						n=n+1

					else:

						der.insert(n,new_a+self.var_type[0]+"^"+str(s-1))
						n=n+1

					if (self.eqn[i+1] == "+") & (self.var_type[0] in self.eqn[i+2]):

						der.insert(n,"+")
						n=n+1

					if (self.eqn[i+1] == "-") & (self.var_type[0] in self.eqn[i+2]):

						der.insert(n,"-")
						n=n+1

				# is it a power of 1 term
				elif ("^" not in self.eqn[i]) & (self.var_type[0] in self.eqn[i]) & (s == 1):

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

					der.insert(n,a)
					n=n+1

					if (self.eqn[i+1] == "+") & (self.var_type[0] in self.eqn[i+2]):

						der.insert(n,"+")
						n=n+1

					if (self.eqn[i+1] == "-") & (self.var_type[0] in self.eqn[i+2]):

						der.insert(n,"-")
						n=n+1

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