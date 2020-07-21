from typing import List, Tuple, Union
import math, cmath

var_dict = {

    "a": "b",
    "b": "c",
    "c": "d",
    "d": "e",
    "e": "f",
    "f": "g",
    "g": "h",
    "h": "i",
    "i": "j",
    "j": "k",
    "k": "l",
    "l": "m",
    "m": "n",
    "n": "o",
    "o": "p",
    "p": "q",
    "q": "r",
    "r": "s",
    "s": "t",
    "t": "u",
    "u": "v",
    "v": "w",
    "w": "x",
    "x": "y",
    "y": "z",
    "z": "a"

}

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

    if "derivative of " in a:

        calculus_chk = True
        a = a.replace("derivative of ", '')

    elif "derivative " in a:

        calculus_chk = True
        a = a.replace("derivative ", '')

    elif "d/d" in a:

        calculus_chk = True

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
    #First combine complex numbers into a single index
    i = 0
    mod_chk = False
    br_copy = br[:]
    while i != len(br_copy):
        if ("j" in br_copy[i]) and (br_copy[i-1] in "+-") and (is_number(br_copy[i-2])):
            temp = br_copy[i-2]+br_copy[i-1]+br_copy[i]
            br_copy[i-2] = temp
            del br_copy[i-1:i+1]
            print(br_copy)
            i -= 1
            mod_chk = True
        i += 1

    i = 0
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

    if mod_chk:
        br = br_copy[:]

    return br

class Equation():

    def __init__(self, eqn_string: str = None):

        if not eqn_string:
            self.eqn_string = ""
            self.eqn = []
            self.deg = []
            self.var_type = []
            self.solution = []
        else:
            self.eqn_string = eqn_string
            self.eqn = []
            self.deg = []
            self.var_type = []
            self.solution = []
            self.solution.append("The inputted equation is "+eqn_string)
            self.bracketify()
            if self.var_type[0] != "":
                self.grouping()

    def bracketify(self) -> Tuple[List[str], List[str]]:
        "Takes equation in string format and transforms into list of strings."
        master = []
        numtemp = []
        var_type = []
        a = self.eqn_string
        if "derivative of " in a:

            calculus_chk = True
            a = a.replace("derivative of ", '')

        elif "derivative " in a:

            calculus_chk = True
            a = a.replace("derivative ", '')
        else:
            calculus_chk = False
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

            elif (a[s] == "/" and a[s-1] == "d") or (a[s] == "/" and a[s-2] == "d"):
                s += 1
                continue

            elif (a[s] == "/" and a[s-1] != "d") or (a[s] == "/" and a[s-2] != "d"):
                print(s, a, s-1, a[s-1], s-2, a[s-2])
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
            elif (a[s].isalpha() == True) and (a[s - 1].isalpha() == False) and (a[s + 1].isalpha() == False) and (
                    a[s] != "d") and (a[s] != "j"):

                master.insert(j, str(a[s]))
                if str(a[s]) not in var_type:
                    var_type.insert(var_num, str(a[s]))
                    var_num = var_num + 1

                j = j + 1

            elif a[s].isalpha() and a[s-1] == "d" and a[s-2] == "/" and a[s-3].isalpha() and a[s-4] == "d":
                #print("bingo")
                master.insert(j, "d"+str(a[s-3])+"/d"+str(a[s]))
                if str(a[s]) not in var_type:
                    var_type.insert(var_num, str(a[s]))
                    var_num += 1
                j += 1

            elif a[s].isalpha() and a[s-1] == "d" and a[s-2] == "/" and a[s-3] == "d":
                #print("bingo")
                master.insert(j, "d/d"+str(a[s]))
                if str(a[s]) not in var_type:
                    var_type.insert(var_num, str(a[s]))
                    var_num += 1
                j += 1

            elif a[s] == "d" or (a[s] == "/" and a[s-1] == "d") or (a[s].isalpha() and a[s-1] == "d" and a[s] not in var_type):
                s += 1
                continue
            # the following code is for handling large numbers and decimals
            else:

                numtemp.insert(i, a[s])

                if (a[s + 1].isdigit()) or (a[s + 1] == ".") or (a[s+1] == "j"):  # if the next index is a number or a period or j

                    i = i + 1

                elif (a[s + 1] == "e") and (a[s + 2] in "+-") and (a[s + 3].isdigit()):

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

                elif (a[s] == "-") and (not a[s - 1].isdigit()):

                    master.insert(j, "-1")
                    j = j + 1
                    master.insert(j, "*")
                    j = j + 1
                    numtemp.clear()

                else:

                    for k in range(0, i + 1):
                        temp = str(temp) + str(numtemp[k])

                    if complex(temp).imag != 0:

                        if complex(temp).real == 0:

                            master.insert(j, str(complex(temp).imag*1j))
                            j = j + 1
                            i = 0
                            numtemp.clear()
                            temp = ""  # clear up temp

                        else:

                            master.insert(j, str(complex(temp)))
                            j = j + 1
                            i = 0
                            numtemp.clear()
                            temp = ""  # clear up temp

                    elif temp == "0j":

                        master.insert(j, str(complex(temp)))
                        j = j + 1
                        i = 0
                        numtemp.clear()
                        temp = ""  # clear up temp

                    else:

                        master.insert(j, str(float(temp)))
                        j = j + 1
                        i = 0
                        numtemp.clear()
                        temp = ""  # clear up temp

            s += 1
        #print("YEEEHAW", master)
        # print("now for inference")
        master = inference(master)
        # print(master)
        # print("now for imaginary_num")
        master = imaginary_num(master)
        #print("After imaginary_num", master)

        if not var_type:
            var_type.append("")

        if calculus_chk:

            master.insert(1, "d/d"+str(var_type[0]))
            master.insert(1, "=")
            if var_type[0] != "y":
                master.insert(1, "dy/d"+str(var_type[0]))
            else:
                master.insert(1, "d"+var_dict[var_type[0]]+"/d"+str(var_type[0]))
            master.insert(4, "(2")
            master.insert(-1, ")2")

        self.eqn = master
        self.var_type = var_type

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
            if ("(" in self.eqn[i]) and (self.eqn[i] not in oper_dict.values()):

                b += 1
                b_open += 1
                b_loc = i

                for op in oper_dict.values():

                    if op == self.eqn[i - 1]:
                        p_b = b
                        p = i

            if (")" in self.eqn[i]) and (self.eqn[i] not in oper_dict.values()):

                if self.eqn[i] == ")" + str(p_b):
                    p_b = 0
                    p = 0

                b -= 1
                b_close += 1

            if (self.eqn[i].isalpha()) and (len(self.eqn[i]) == 1):

                # print("eqn[i]", eqn[i])
                if self.eqn[i] not in var:
                    var.append(self.eqn[i])

                if (self.eqn[i + 1] == "^") and (is_number(self.eqn[i + 2])):
                    self.eqn[i] = self.eqn[i] + "^" + self.eqn[i + 2]
                    del self.eqn[i + 1:i + 3]
                    mod = True
                # print(eqn)

                if (is_number(self.eqn[i - 1])):
                    self.eqn[i - 1] = self.eqn[i - 1] + self.eqn[i]
                    del self.eqn[i]
                    mod = True
                # print(eqn)

                if (")" in self.eqn[i-1]) and (is_number(self.eqn[i-2])) and ("(" in self.eqn[i-3]):
                    self.eqn[i-3] = "("+self.eqn[i-2]+")"+self.eqn[i]
                    del self.eqn[i-2:i+1]
                    mod = True

                if (self.eqn[i - 1] == "*") and (is_number(self.eqn[i - 2])):
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

        var_chk = False
        for s in self.eqn:
            if self.var_type[0] in s:
                var_chk = True

        if not var_chk:
            del new_eqn_deg[0]

        if len(self.eqn) > 1:

            if self.eqn[1] == "-":
                self.eqn[1] = self.eqn[1] + self.eqn[2]
                del self.eqn[2]

        # print("new_eqn_deg", new_eqn_deg)
        self.deg = new_eqn_deg
        self.eqn_string_update()

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