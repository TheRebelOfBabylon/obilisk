from typing import List, Tuple, Union

class Equation():

    def __init__(self, eqn_string: str):
        self.eqn_string = eqn_string
        self.eqn, self.var_type = self.bracketify(self.eqn_string)
        self.solution = []
        
    def bracketify(self, a: str) -> Tuple[List[str], List[str]]:
        "Takes equation in string format and transforms into list of strings."
        master = []
        numtemp = []
        var_type = []
        a = "(" + a + ")00000"

        i = 0
        j = 0  # walk the master array
        b = 0
        k = 0
        temp = ""
        s = 0
        var_num = 0
        # Transform input string array into code-readable format
        while s != len(a) - 5:

            # print(master, a[s], s)
            if a[s] == "(":

                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            elif a[s] == "^":

                master.insert(j, "^")
                j = j + 1

            elif a[s] == "/":

                master.insert(j, "/")
                j = j + 1

            elif a[s] == "*":

                master.insert(j, "*")
                j = j + 1

            elif a[s] == "+":

                master.insert(j, "+")
                j = j + 1

            # checks if previous digit is a number so that it doesn't mistake a negative number for an operation
            elif (a[s] == "-") & ((a[s - 1] == ")") or (a[s - 1].isdigit() == True) or (a[s - 1].isalpha() == True)):

                master.insert(j, "-")
                j = j + 1

            # Sine
            elif (a[s] == "s") & (a[s + 1] == "i") & (a[s + 3] != "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "SIN")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Cosine
            elif (a[s] == "c") & (a[s + 1] == "o") & (a[s + 2] == "s") & (a[s + 3] != "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "COS")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Tangent
            elif (a[s] == "t") & (a[s + 1] == "a") & (a[s + 3] != "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "TAN")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Secant
            elif (a[s] == "s") & (a[s + 1] == "e") & (a[s + 3] != "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "SEC")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Cosecant
            elif (a[s] == "c") & (a[s + 1] == "s") & (a[s + 3] != "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "CSC")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Cotangent
            elif (a[s] == "c") & (a[s + 1] == "o") & (a[s + 2] == "t") & (a[s + 3] != "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "COT")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Arc Sine
            elif (a[s] == "a") & (a[s + 1] == "s") & (a[s + 2] == "i") & (a[s + 4] != "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ASIN")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Arc Cosine
            elif (a[s] == "a") & (a[s + 1] == "c") & (a[s + 2] == "o") & (a[s + 3] == "s") & (a[s + 4] != "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ACOS")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Arc Tangent
            elif (a[s] == "a") & (a[s + 1] == "t") & (a[s + 4] != "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ATAN")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Arc Secant
            elif (a[s] == "a") & (a[s + 1] == "s") & (a[s + 2] == "e") & (a[s + 4] != "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ASEC")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Arc Cosecant
            elif (a[s] == "a") & (a[s + 1] == "c") & (a[s + 2] == "s") & (a[s + 4] != "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ACSC")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Arc Cotangent
            elif (a[s] == "a") & (a[s + 1] == "c") & (a[s + 2] == "o") & (a[s + 3] == "t") & (a[s + 4] != "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ACOT")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Sine
            elif (a[s] == "s") & (a[s + 1] == "i") & (a[s + 3] == "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "SINH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Cosine
            elif (a[s] == "c") & (a[s + 1] == "o") & (a[s + 2] == "s") & (a[s + 3] == "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "COSH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Tangent
            elif (a[s] == "t") & (a[s + 1] == "a") & (a[s + 3] == "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "TANH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Secant
            elif (a[s] == "s") & (a[s + 1] == "e") & (a[s + 3] == "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "SECH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Cosecant
            elif (a[s] == "c") & (a[s + 1] == "s") & (a[s + 3] == "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "CSCH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Cotangent
            elif (a[s] == "c") & (a[s + 1] == "o") & (a[s + 2] == "t") & (a[s + 3] == "h") & (a[s - 1] != "a"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "COTH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Arc Sine
            elif (a[s] == "a") & (a[s + 1] == "s") & (a[s + 2] == "i") & (a[s + 4] == "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ASINH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Arc Cosine
            elif (a[s] == "a") & (a[s + 1] == "c") & (a[s + 2] == "o") & (a[s + 3] == "s") & (a[s + 4] == "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ACOSH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Arc Tangent
            elif (a[s] == "a") & (a[s + 1] == "t") & (a[s + 2] == "a") & (a[s + 4] == "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ATANH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Arc Secant
            elif (a[s] == "a") & (a[s + 1] == "s") & (a[s + 2] == "e") & (a[s + 4] == "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ASECH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Arc Cosecant
            elif (a[s] == "a") & (a[s + 1] == "c") & (a[s + 2] == "s") & (a[s + 4] == "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ACSCH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Hyperbolic Arc Cotangent
            elif (a[s] == "a") & (a[s + 1] == "c") & (a[s + 2] == "o") & (a[s + 3] == "t") & (a[s + 4] == "h"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "ACOTH")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Natural Logarithm
            elif (a[s] == "l") & (a[s + 1] == "n"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "LN")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # Logarithm
            elif (a[s] == "l") & (a[s + 1] == "o"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "LOG")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            elif a[s] == ",":

                master.insert(j, ")" + str(b))
                b = b - 1
                j = j + 1
                b = b + 1
                master.insert(j, "(" + str(b))
                j = j + 1

            # Square Root
            elif (a[s] == "s") & (a[s + 1] == "q"):

                while a[s] != "(":
                    s = s + 1

                master.insert(j, "SQRT")
                j = j + 1
                b = b + 1  # system has knowledge of current amount of open brackets
                master.insert(j, "(" + str(b))
                j = j + 1

            # PI
            elif (a[s] == "P") & (a[s + 1] == "I"):

                master.insert(j, str(math.pi))
                s = s + 1
                j = j + 1

            # Euler's number
            elif a[s] == "E":

                master.insert(j, str(math.e))
                j = j + 1

            elif a[s] == ")":

                master.insert(j, ")" + str(b))
                b = b - 1
                j = j + 1

            elif a[s] == "=":

                master.insert(j, "=")
                j = j + 1

            # The following code is for single character variables
            elif (a[s].isalpha() == True) & (a[s - 1].isalpha() == False) & (a[s + 1].isalpha() == False) & (
                    a[s] != "d"):

                master.insert(j, str(a[s]))
                if str(a[s]) not in var_type:
                    var_type.insert(var_num, str(a[s]))
                    var_num = var_num + 1

                j = j + 1

            # the following code is for handling large numbers and decimals
            else:

                numtemp.insert(i, a[s])

                if (a[s + 1].isdigit() == True) or (a[s + 1] == "."):  # if the next index is a number or a period or j

                    i = i + 1

                elif (a[s + 1] == "e") and (a[s + 2] in "+-") and (a[s + 3].isdigit() == True):

                    # print(a[s],str(s)+" out of "+str(len(a)-1))

                    i += 1
                    s += 1
                    numtemp.insert(i, a[s])
                    # print(numtemp)
                    i += 1
                    s += 1
                    numtemp.insert(i, a[s])
                    # print(numtemp)
                    i += 1

                elif (a[s] == "-") & (a[s - 1].isdigit() == False):

                    master.insert(j, "-1")
                    j = j + 1
                    master.insert(j, "*")
                    j = j + 1
                    numtemp.clear()

                else:

                    for k in range(0, i + 1):
                        temp = str(temp) + str(numtemp[k])

                    master.insert(j, str(float(temp)))
                    j = j + 1
                    i = 0
                    numtemp.clear()
                    temp = ""  # clear up temp

            s = s + 1

        # print("now for inference")
        master = inference(master)
        # print(master)
        # print("now for imaginary_num")
        master = imaginary_num(master)
        # print(master)

        if not var_type:
            var_type.append("")

        return master, var_type