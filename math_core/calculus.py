"""All methods related to calculus type problems."""
import math
import cmath
from math_core import algebra
from typing import List, Tuple, Union

def poly_derivative(eqn: List[str],order: int,var_type: str) -> List[str]:
	"""Takes first derivative of a polynomial."""
	#loop from highest exponent to 1. Apply normal derivative rules
	der=[]
	n = 0

	for s in range(order,0,-1):
	
		#walk eqn
		for i in range(0,len(eqn)-1):

			if "^"+str(s) in eqn[i]:

				temp = eqn[i]
				a = ""
				v = 0
				while temp[v] != var_type:

					a = a+str(temp[v])
					v=v+1

				if a == "":

					a = "1"

				if a == "-":

					a = "-1"

				new_a = str(s*float(a))

				if s == 2:

					der.insert(n,new_a+var_type)
					n=n+1

				else:

					der.insert(n,new_a+var_type+"^"+str(s-1))
					n=n+1

				if (eqn[i+1] == "+") & (var_type in eqn[i+2]):

					der.insert(n,"+")
					n=n+1

				if (eqn[i+1] == "-") & (var_type in eqn[i+2]):

					der.insert(n,"-")
					n=n+1

			# is it a power of 1 term
			elif ("^" not in eqn[i]) & (var_type in eqn[i]) & (s == 1):

				temp = eqn[i]
				a = ""
				v = 0
				while temp[v] != var_type:

					a = a+str(temp[v])
					v=v+1

				if a == "":

					a = "1"

				if a == "-":

					a = "-1"

				der.insert(n,a)
				n=n+1

				if (eqn[i+1] == "+") & (var_type in eqn[i+2]):

					der.insert(n,"+")
					n=n+1

				if (eqn[i+1] == "-") & (var_type in eqn[i+2]):

					der.insert(n,"-")
					n=n+1
	
	der.insert(0,"(1")
	der.insert(len(der),")1")

	return der

#input eqn - array of coefficients of a given polynomial
#output - array of coefficients of derivative
def coeff_derivative(eqn: List[Union[int, float, complex]]) -> algebra.Poly_Func:
	"""Takes first derivative of a polynomial. Input eqn is a list of coefficients."""
	expo = len(eqn)-1
	der=[]
	for i in eqn:

		if expo == 0:

			pass

		else:

			der.append(i*expo)
			expo -= 1

	return algebra.Poly_Func(der)

		