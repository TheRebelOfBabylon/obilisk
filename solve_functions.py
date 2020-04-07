#Solve functions
from BEMDAS_algo_v3 import bracketify, stringify, grouping, is_number, foiling, is_even, bracket_add
import copy

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

def exp_foiling(br, x, var):

	br_one = br[:]
	br_two = br[:]

	if is_even(x):

		#print("x is even and is "+str(x))
		while x != 1:

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

		while x != 0:

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


class Solve_Func:

	def __init__(self, eqn, var):

		self.eqn = eqn
		self.var = var

	#1. remove any divisions
	#1.1 Identify divisors in an eqn
	#Inputs 	- eqn (LHS or RHS of equation in array format)
	#		- var (single character string that is the variable in an equation ex: "x"
	#Outputs	- divisors (array of divisors in array format)

	def identify_div(self):

		
		s=0
		divisors=[]
		while s != len(self.eqn):
	
			#What do we do if COS(()/())? or (()/())^7. Maybe it would be wise to make a marker that indicates a bracket is preceded by a special op like COS 
			if ("(" in self.eqn[s]) and (self.eqn[s-1] == "/") and (")" in self.eqn[s-2]) and (s != 0):

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
	def redundant_br(self):

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

							print("\n"+new_br_string)
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

				#elif (self.eqn[s] == "("+str(c)) and (self.eqn[s-1] == "("+str(c-1)):

					

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

	def multiply_br(self,divers):

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

						if eqn_chk == True:

							#print(k, self.eqn[k])
							if self.eqn[k] == "*":

								k+=1
								if self.eqn[k] == "("+str(c):

									if eqn_chk == True:

										#print("Found one: ", k, self.eqn[k])
										del self.eqn[s:k]
										#print(self.eqn, s, self.eqn[s])
										break

									else:

										s = k

					s+=1
				
				k = s
				while self.eqn[k] != ")2":

					k+=1

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

						i.insert(len(i)-1, str(x))
						i.insert(len(i)-1, "^")

				d = 0
				#print(s, self.eqn[s], i)
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

					s+=1

		eqn_string = stringify(self.eqn)
		print(eqn_string)
		return self

	#Function to remove any ()/() = 1:
	#Inputs	-self (the class object)
	#	-divisors (an array of arrays of the divisors)
	#outputs -self (the equation with modifications)

	def redundant_div(self, divisors):

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

						br=["(1"]
						k = s
						while self.eqn[k] == ")"+str(c-1):

							br.append(self.eqn[k])
							k+=1

						br.append(")1")
						br_string = stringify(br)

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

								i.insert(len(i)-1, str(x))
								i.insert(len(i)-1, "^")

					s+=1

			i.insert(0,"(1")
			i.append(")1")
			div_string.append(stringify(i))
						

		#print(div_string)

		for i in div_string:

			for c in range(b-1,1,-1):
		
				s=0
				while s != len(self.eqn):

					if self.eqn[s] == "("+str(c):

						k = s+1
						d=0
						br = ""
						while self.eqn[k] != ")"+str(c):

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
							self.var = var[0]
							self.eqn, deg = grouping(self.eqn)
							#print(self.eqn)
							s=0

					s+=1

		return self

	#Function removes all brackets by finding brackets with exponents, bracket multiplication, add or sub and foils out 
	#Inputs	- self (the equation)
	#Outputs	- self (the modified equation)

	def bracket_remover(self):

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
					new_br = exp_foiling(bra,x, self.var)
					#print(new_br)
					new_br_string = stringify(new_br)
					print("= "+new_br_string)
					eqn_string = stringify(self.eqn)
					eqn_string = eqn_string.replace(br+"^"+str(x),"("+new_br_string+")")
					self.eqn, var = bracketify(eqn_string)
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
						br.insert(0,"(1")
						br.append(")1")
						br_string = stringify(br)
						print("= "+br_string)
				
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
						self.eqn, var = bracketify(eqn_string)
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
						br.insert(0,"(1")
						br.append(")1")
						br_string = stringify(br)
						print("= "+br_string)
				
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
						self.eqn, var = bracketify(eqn_string)
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
						br.insert(0,"(1")
						br.append(")1")
						br_string = stringify(br)
						print("= "+br_string)
				
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
						self.eqn, var = bracketify(eqn_string)
						self.var = var[0]
						self.eqn, deg = grouping(self.eqn)
						eqn_string = stringify(self.eqn)
						print("\n"+eqn_string)
						s=-1
	
				s+=1

			#Now to check for ()*()
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
						br.insert(0,"(1")
						br.append(")1")
						br_string = stringify(br)
						print("= "+br_string)
				
						eqn_string = stringify(self.eqn)
						eqn_string = eqn_string.replace(br_string_one+op+br_string_two, "("+br_string+")")
						self.eqn, var = bracketify(eqn_string)
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

	