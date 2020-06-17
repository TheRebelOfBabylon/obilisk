import math
import cmath
import random
from math_core.Calculus import Calculus

from typing import List, Union, Tuple

def real_poly(eqn: Calculus) -> List[Union[int, float, complex]]:
	"""Top level function which calls the rpoly, Jenkins-Traub algorithm."""
	num_roots = eqn.deg[0]
	ans = []			

	#Fundamental theorem of algebra says number of highest exponent is the number of roots
	i = 0
	while i != eqn.deg[0]:

		root = rpoly(eqn)
		ans.append(root)
		i += 1
		last_run = (num_roots - 1 == i)		

		#if not last_run:

		divisor = [1,-1*root]
		#print("x+"+str(divisor[1]))
		new_eqn = eqn.lin_divide(divisor)
		del new_eqn[-1]
		#print(new_eqn.eqn)
		#TODO create a new method in algebra that updates all attributes when given a coeff type array
		eqn.coeff = new_eqn
		#eqn.update_attributes()

	return ans

def rpoly(eqn: Calculus) -> Union[int, float, complex]:
	"""RPOLY Jenkins-Traub algorithm for polynomial root finding."""
	coeff = eqn
	coeff.coeff = coeff.normalize()
	#coeff.update_attributes()
	#print(coeff.eqn)

	#Stage 1: No-shift process. Assuming M = 5

	#TODO - Change Equation constructor so that the input string is optional
	K = coeff.coeff_derivative()
	#print(K.eqn)

	for i in range(0,5):

		constant = -1*K.evaluate(0)/coeff.evaluate(0)
		#print("Constant is",constant)
		P_z = coeff.poly_multiply(constant)
		#print("P_z",P_z.eqn)
		K_prime = Algebra.poly_add(K.coeff,P_z.coeff)
		#print("K_prime",K_prime.eqn)
		divisor = [1,0]
		new_K = K_prime.lin_divide(divisor)
		del new_K.coeff[-1]
		#print("new_K",new_K.eqn)
		K = new_K
		#print(i)

	#Stage 2: Fixed-shift Process

	t_curr = t_old = t_new = None
	stage_two_success = False
	root_found = False

	while not root_found:
	
		while not stage_two_success:

			s = get_random_root(coeff)
			#print("s",s)

			for i in range(0,100):
				
				constant = -1*K.evaluate(s)/coeff.evaluate(s)
				P_z = coeff.poly_multiply(constant)
				K_prime = Algebra.poly_add(K.coeff,P_z.coeff)
				divisor = [1,-1*s]
				new_K = K_prime.lin_divide(divisor)
				del new_K.coeff[-1]

				K_bar = K.normalize()
				new_K_bar = new_K.normalize()

				t_curr = s-(coeff.evaluate(s)/K_bar.evaluate(s))
				t_new = s-(coeff.evaluate(s)/new_K_bar.evaluate(s))

				if i > 0 and abs(t_curr - t_old) <= 0.5*abs(t_old) and abs(t_new - t_curr) <= 0.5*abs(t_curr):

					stage_two_success = True
					#print("break",stage_two_success,root_found)
					break

				t_old = t_curr
				K = new_K
				#print("Stage 2: K",K.eqn)

			if not stage_two_success:

				print("Retrying Stage 2")

		#Stage 3: Variable-shift process

		old_err = coeff.evaluate(s)
		curr_err = 1
		K_bar = K.normalize()
		s = s-(coeff.evaluate(s)/K_bar.evaluate(s))
		old_s = 0
		stage_three_success = False

		for i in range(0,10000):

			if abs(coeff.evaluate(s)) < abs(10**(-5)):

				stage_three_success = True
				break

			constant = -1*K.evaluate(s)/coeff.evaluate(s)
			P_z = coeff.poly_multiply(constant)
			K_prime = Algebra.poly_add(K.coeff,P_z.coeff)
			divisor = [1,-1*s]
			new_K = K_prime.lin_divide(divisor)
			del new_K.coeff[-1]
			new_K_bar = new_K.normalize()

			s = s-(coeff.evaluate(s)/new_K_bar.evaluate(s))
			curr_err = coeff.evaluate(s)

			K = new_K

			if math.isnan(s.imag) and math.isnan(s.real):

				stage_three_success = False
				break

		if stage_three_success:

			#print("Root is",s)
			root_found = True

		else:

			stage_two_success = False

	return s
	
def get_random_root(eqn: Algebra) -> Union[int, float, complex]:
	"""Function for finding random roots."""
	cauchy_eqn = eqn.cauchy_poly()
	#print("Cauchy",cauchy_eqn.eqn)
	beta = cauchy_eqn.newton_raphson())
	#print("beta",beta)
	rand = random.uniform(0,1)*2*math.pi
	root = abs(beta)*cmath.exp(1j*rand)
	return root



	