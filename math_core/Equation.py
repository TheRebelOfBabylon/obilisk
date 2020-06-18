from typing import List, Tuple, Union
import math, cmath

oper_dict = {

    0: "SIN",
    1: "COS",
    2: "TAN",
    3: "SEC",
    4: "CSC",
    5: "COT",
    6: "ASIN",
    7: "ACOS",
    8: "ATAN",
    9: "ASEC",
    10: "ACSC",
    11: "ACOT",
    12: "SINH",
    13: "COSH",
    14: "TANH",
    15: "SECH",
    16: "CSCH",
    17: "COTH",
    18: "ASINH",
    19: "ACOSH",
    20: "ATANH",
    21: "ASECH",
    22: "ACSCH",
    23: "ACOTH",
    24: "LN",
    25: "LOG",
    26: "SQRT"

}

def is_number(s: str) -> bool:
    """Function tests if a string is a number."""
    try:

        float(s)
        return True

    except ValueError:

        try:

            complex(s)
            return True

        except ValueError:

            return False

def bracketify(a: str) -> Tuple[List[str], List[str]]:
    "Takes equation in string format and transforms into list of strings."
    # Gotta add a check for imaginary numbers

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
        elif (a[s].isalpha() == True) & (a[s - 1].isalpha() == False) & (a[s + 1].isalpha() == False) & (a[s] != "d"):

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

def stringify(l: List[str]) -> str:
    """Takes equation in format List of strings and returns human-readable string."""
    temp = ""
    for s in range(1, len(l) - 1):

        if ("(" in str(l[s])) and ("j" not in str(l[s])):

            temp += "("

        elif (")" in str(l[s])) and ("j" not in str(l[s])):

            temp += ")"

        else:

            temp = temp + str(l[s])

    for i in oper_dict.values():

        if i in temp:

            temp = temp.replace(i, i.lower())

    return temp

def inference(eqn: List[str]) -> List[str]:
    """Equation adds * symbol between constants and brackets or constants and complex math operations."""
    master = []
    s = 0
    for i in range(0, len(eqn)):

        if ("(" in eqn[i]) and (is_number(eqn[i - 1]) == True):

            master.append("*")
            master.append(eqn[i])

        elif (eqn[i] in oper_dict.values()) and (is_number(eqn[i - 1]) == True):

            master.append("*")
            master.append(eqn[i])

        elif ("(" in eqn[i]) and (")" in eqn[i - 1]) and (s != 0):

            master.append("*")
            master.append(eqn[i])

        else:

            master.append(eqn[i])

    # print(master)
    return master

def imaginary_num(br: List[str]) -> List[str]:
    """Removes brackets around complex numbers."""
    i = 0
    mod_chk = False
    br_copy = br[:]
    while i != len(br_copy):

        if (")" in br_copy[i]) and (br_copy[i] != ")1") and (br_copy[i - 1] == "j") and (
                is_number(br_copy[i - 2]) == True):

            b = br_copy[i]
            b = b.replace(')', '')
            b = int(b)
            k = i - 1
            temp = []
            while br_copy[k] != "(" + str(b):
                temp.insert(0, br_copy[k])
                k -= 1

            temp_string = ""
            for s in temp:
                temp_string += s

            temp = temp_string

            # print("temp = "+temp, is_number(temp))
            # let's double check it is an imaginary number
            if is_number(temp) == True:

                # print("It's a number")
                if isinstance(complex(temp), complex) == True:
                    del br_copy[k:i]
                    br_copy[k] = temp
                    mod_chk = True
                    i = -1

        if (")" in br_copy[i]) and (br_copy[i] == ")1") and (br_copy[i - 1] == "j") and (
                is_number(br_copy[i - 2]) == True):

            b = br_copy[i]
            b = b.replace(')', '')
            b = int(b)
            k = i - 1
            temp = []
            while br_copy[k] != "(" + str(b):

                if ")" in br_copy[k]:

                    temp.insert(0, ")")

                else:

                    temp.insert(0, br_copy[k])

                k -= 1

            temp_string = ""
            for s in temp:
                temp_string += s

            temp = temp_string

            # print("temp = "+temp, is_number(temp))
            # let's double check it is an imaginary number
            if is_number(temp) == True:

                # print("It's a number")
                if isinstance(complex(temp), complex) == True:
                    del br_copy[k + 1:i]
                    br_copy.insert(k + 1, temp)
                    mod_chk = True
                    i = -1

        i += 1

    if mod_chk == True:
        br = br_copy[:]

    return br

class Equation():

    def __init__(self, eqn_string: str = None):

        if not eqn_string:
            self.eqn_string = ""
            self.eqn = []
            self.var_type = []
            self.solution = []
        else:
            self.eqn_string = eqn_string
            self.eqn = []
            self.var_type = []
            self.solution = []
            self.solution.append("The inputted equation is "+eqn_string)
            self.bracketify()

    def bracketify(self) -> Tuple[List[str], List[str]]:
        "Takes equation in string format and transforms into list of strings."
        master = []
        numtemp = []
        var_type = []
        a = self.eqn_string
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

        self.eqn = master
        self.var_type = var_type

    def eqn_string_update(self) -> str:
        """Takes objects equation in format List of strings and updates eqn_string parameter."""
        temp = ""
        s=1
        while s != len(self.eqn) - 1:

            if ("(" in str(self.eqn[s])) and ("j" not in str(self.eqn[s])):

                temp += "("

            elif (")" in str(self.eqn[s])) and ("j" not in str(self.eqn[s])):

                temp += ")"

            elif self.eqn[s] == "LOG":

                temp += self.eqn[s].lower()
                i = s+1
                if "(" in self.eqn[i]:
                    temp_two = self.eqn[i]
                    temp_two = temp_two.replace("(",'')
                    temp += "("
                    i+=1
                    while self.eqn[i] != ")"+temp_two:
                        temp += str(self.eqn[i])
                        i+=1
                    i+=1
                    if "(" in self.eqn[i]:
                        temp += ","
                        temp_two = self.eqn[i]
                        temp_two = temp_two.replace("(", '')
                        i+=1
                        while self.eqn[i] != ")"+temp_two:
                            temp += str(self.eqn[i])
                            i+=1
                        temp += ")"
                        if i+1 >= len(self.eqn)-1:
                            break
                        else:
                            s = i+1
                else:
                    temp += "("
                    temp += str(self.eqn[i])
                    temp += ","
                    if "(" in self.eqn[i+1]:
                        i += 1
                        temp_two = self.eqn[i]
                        temp_two = temp_two.replace("(", '')
                        i+=1
                        while self.eqn[i] != ")"+temp_two:
                            temp += str(self.eqn[i])
                            i+=1
                        temp += ")"
                        if i+1 >= len(self.eqn)-1:
                            break
                        else:
                            s = i+1
                    elif i+3 >= len(self.eqn)-1:
                        temp += str(self.eqn[i+1])
                        temp += ")"
                        break
                    else:
                        i+=1
                        temp += str(self.eqn[i])
                        temp += ")"
                        s = i+1

            else:

                temp = temp + str(self.eqn[s])

            s+=1

        for i in oper_dict.values():
            if i in temp:
                temp = temp.replace(i, i.lower())
        self.eqn_string = temp