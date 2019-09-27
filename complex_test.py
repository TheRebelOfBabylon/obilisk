import math
import cmath

num_one = -1.4939328
num_two = -1.4939329
num_three = -0.55457722-1.4929750j

if (round(num_one.real,5) == round(num_two.real,5)) and (round(num_one.imag,5) == round(num_two.imag,5)):

	print("Same real and imaginary part")

else:

	print("They aren't the same")