
from math_core.Equation import Equation, stringify
import math, cmath
from typing import List, Tuple, Union

def is_even(s: Union[int, float]) -> bool:
    """Tests if number is even."""
    if s % 2 == 0:

        return True

    else:

        return False

def div_check(x: Union[int, float, complex], y: Union[int, float, complex]) -> bool:
    """Detects divisions by zero."""
    try:
        x / y

    except ZeroDivisionError:

        return True

    else:

        return False

def operation(num_one: str, oper: str, num_two: str) -> Union[int, float, complex]:
    """Takes two numbers in string format and performs specified input operation."""
    try:

        num_one = float(num_one)

    except:

        num_one = complex(num_one)

    try:

        num_two = float(num_two)

    except:

        num_two = complex(num_two)

    operation_ans = 0

    if oper == "^":

        operation_ans = num_one ** num_two

    elif oper == "/":

        # Check if division by zero
        if div_check(num_one, num_two) == True:

            operation_ans = math.inf

        else:

            operation_ans = num_one / num_two

    elif oper == "*":

        operation_ans = num_one * num_two

    elif oper == "+":

        operation_ans = num_one + num_two

    elif oper == "-":

        operation_ans = num_one - num_two

    elif oper == "SIN":

        num_two = math.radians(num_two)
        operation_ans = round(math.sin(num_two), 7)

    elif oper == "COS":

        num_two = math.radians(num_two)
        operation_ans = round(math.cos(num_two), 7)

    elif oper == "TAN":

        num_two = math.radians(num_two)
        operation_ans = round(math.tan(num_two), 7)

    elif oper == "SEC":

        num_two = math.radians(num_two)
        if div_check(1, round(math.cos(num_two), 7)) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(1 / math.cos(num_two), 7)

    elif oper == "CSC":

        num_two = math.radians(num_two)
        if div_check(1, round(math.sin(num_two), 7)) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(1 / math.sin(num_two), 7)

    elif oper == "COT":

        num_two = math.radians(num_two)
        if div_check(1, round(math.tan(num_two), 7)) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(1 / math.tan(num_two), 7)

    elif oper == "ASIN":

        operation_ans = math.asin(num_two)
        operation_ans = round(math.degrees(operation_ans), 7)

    elif oper == "ACOS":

        operation_ans = math.acos(num_two)
        operation_ans = round(math.degrees(operation_ans), 7)

    elif oper == "ATAN":

        operation_ans = math.atan(num_two)
        operation_ans = round(math.degrees(operation_ans), 7)

    elif oper == "ASEC":

        if div_check(1, num_two) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(math.degrees(math.acos(1 / num_two)), 7)

    elif oper == "ACSC":

        if div_check(1, num_two) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(math.degrees(math.asin(1 / num_two)), 7)

    elif oper == "ACOT":

        if div_check(1, num_two) == True:

            operation_ans = round(math.degrees(math.atan(math.inf)), 7)

        else:

            operation_ans = round(math.degrees(math.atan(1 / num_two)), 7)

    elif oper == "SINH":

        operation_ans = round(math.sinh(num_two), 7)

    elif oper == "COSH":

        operation_ans = round(math.cosh(num_two), 7)

    elif oper == "TANH":

        operation_ans = round(math.tanh(num_two), 7)

    elif oper == "SECH":

        if div_check(1, round(math.cosh(num_two), 7)) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(1 / math.cosh(num_two), 7)

    elif oper == "CSCH":

        if div_check(1, round(math.sinh(num_two), 7)) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(1 / math.sinh(num_two), 7)

    elif oper == "COTH":

        if div_check(1, round(math.tanh(num_two), 7)) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(1 / math.tanh(num_two), 7)

    elif oper == "ASINH":

        operation_ans = round(math.asinh(num_two), 7)

    elif oper == "ACOSH":

        operation_ans = round(math.acosh(num_two), 7)

    elif oper == "ATANH":

        operation_ans = round(math.atanh(num_two), 7)

    elif oper == "ASECH":

        if div_check(1, num_two) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(math.acosh(1 / num_two), 7)

    elif oper == "ACSCH":

        if div_check(1, num_two) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(math.asinh(1 / num_two), 7)

    elif oper == "ACOTH":

        if div_check(1, num_two) == True:

            operation_ans = math.inf

        else:

            operation_ans = round(math.atanh(1 / num_two), 7)

    elif oper == "LN":

        operation_ans = math.log(num_two)

    elif oper == "LOG":

        operation_ans = math.log(num_two, num_one)

    elif oper == "SQRT":

        operation_ans = cmath.sqrt(num_two)

    return operation_ans

trig_one = [
    "SIN",
    "COS",
    "TAN",
    "ASIN",
    "ACOS",
    "ATAN",
    "SINH",
    "COSH",
    "TANH",
    "SECH",
    "CSCH",
    "COTH",
    "ASINH",
    "ACOSH",
    "ATANH",
    "LN",
    "SQRT",
]

trig_two = {
    "SEC": "COS",
    "CSC": "SIN",
    "COT": "TAN",
    "ASEC": "ACOS",
    "ACSC": "ASIN",
    "ACOT": "ATAN",
    "ASECH": "ACOSH",
    "ACSCH": "ASINH",
    "ACOTH": "ATANH",
}

class Arithmetic(Equation):

    def calculate(self, solution: List[Union[str, int]] = [1], is_first: bool = True) -> Union[int, float, complex]:
        """Using the rules of BEMDAS, function solves any arithmetic problem."""
        #print("At the beginning b = "+str(b), self.eqn)
        op = "0"
        oper = "x"
        y = 0
        z = 0
        t = 0
        b = 1
        bracket = []
        if len(self.eqn) == 3:
            calc = complex(self.eqn_string)
            if calc.imag == 0:
                calc = calc.real
        brack_num = 0
        length = len(self.eqn)
        from math_core.Equation import oper_dict

        while t <= (length - 1):

            # print(t,n[t],length)

            if (self.eqn[t] == "("+str(b+1)) :

                b+=1
                brack_num = ")" + str(b)
                y = t + 1
                while brack_num not in self.eqn[y]:
                    bracket.insert(z, self.eqn[y])
                    z = z + 1
                    y = y + 1

                del self.eqn[(t + 1):(t + len(bracket) + 2)]
                length = len(self.eqn)
                #print(self.eqn,bracket,length)
                bracket.insert(0, "(1")
                bracket.append(")1")
                bracket_string = stringify(bracket)
                #print(bracket, bracket_string, "b = "+str(b))
                bracket_inst = Arithmetic(bracket_string)
                #print("do we ever get here?")
                self.eqn[t] = str(bracket_inst.calculate(solution=solution, is_first=False))
                if is_first:
                    self.eqn_string_update()
                    if not self.mathjax_flag:
                        if solution[-1] != "Equation is now " + self.eqn_string:
                            solution.append("Equation is now " + self.eqn_string)
                    else:
                        mathjax_str = self.solution_mathjax_format(self.eqn_string)
                        if solution[-1] != "Equation is now " + mathjax_str:
                            solution.append("Equation is now " + mathjax_str)
                b = b - 1
                bracket.clear()

            t = t + 1

        # for loop to walk list of operations
        for s in oper_dict.values():

            op = s

            # while loop to walk the inputted array
            t = 0
            while t <= (length - 1):
                # print(s,t,self.eqn[t],length)

                if length == 1:
                    calc = self.eqn[t]

                if self.eqn[t] == op:

                    if op in trig_one:

                        calc = operation(0, op, self.eqn[t + 1])
                        solution.append("Step "+str(solution[0])+":")
                        solution[0]=solution[0]+1
                        if not self.mathjax_flag:
                            solution.append(op.lower() + "(" + self.eqn[t + 1] + ") = " + str(calc))
                        else:
                            mathjax_str = self.solution_mathjax_format(op.lower() + "(" + self.eqn[t + 1] + ") = " + str(calc))
                            solution.append(mathjax_str)
                        #print(solution)
                        self.eqn[t] = str(calc)
                        del self.eqn[t + 1]
                        length = len(self.eqn)
                    # print(self.eqn, calc)

                    elif op in trig_two:

                        calc = operation(0, op, self.eqn[t + 1])
                        solution.append("Step " + str(solution[0]) + ":")
                        solution[0] = solution[0] + 1
                        if not self.mathjax_flag:
                            solution.append(op.lower() + "(" + self.eqn[t + 1] + ") = 1/"+trig_two[op]+"(" + self.eqn[t + 1] + ") = " + str(calc))
                        else:
                            mathjax_str = self.solution_mathjax_format(op.lower() + "(" + self.eqn[t + 1] + ") = 1/"+trig_two[op]+"(" + self.eqn[t + 1] + ") = " + str(calc))
                            solution.append(mathjax_str)
                        #print(solution)
                        self.eqn[t] = str(calc)
                        del self.eqn[t + 1]
                        length = len(self.eqn)
                    # print(self.eqn, calc)

                    elif op == "LOG":

                        calc = operation(self.eqn[t + 1], op, self.eqn[t + 2])
                        solution.append("Step " + str(solution[0]) + ":")
                        solution[0] = solution[0] + 1
                        if not self.mathjax_flag:
                            solution.append("Log(" + self.eqn[t + 1] + ", " + self.eqn[t + 2] + ") = " + str(calc))
                        else:
                            mathjax_str = self.solution_mathjax_format("Log(" + self.eqn[t + 1] + ", " + self.eqn[t + 2] + ") = " + str(calc))
                            solution.append(mathjax_str)
                        #print(solution)
                        self.eqn[t] = str(calc)
                        del self.eqn[t + 1:t + 3]
                        # print(self.eqn)
                        length = len(self.eqn)

                    if is_first:
                        self.eqn_string_update()
                        if not self.mathjax_flag:
                            if solution[-1] != "Equation is now " + self.eqn_string:
                                solution.append("Equation is now " + self.eqn_string)
                        else:
                            mathjax_str = self.solution_mathjax_format(self.eqn_string)
                            if solution[-1] != "Equation is now " + mathjax_str:
                                solution.append("Equation is now " + mathjax_str)

                t = t + 1

        # After resolving complex calculations, now to resolve ^*/+-
        for s in range(0, 3):

            if s == 0:

                op = "^"
                op1 = ""

            elif s == 1:

                op = "*"
                op1 = "/"

            elif s == 2:

                op = "+"
                op1 = "-"

            t = 0
            while t <= length - 1:

                if self.eqn[t] == op:

                    calc = operation(self.eqn[t - 1], op, self.eqn[t + 1])
                    solution.append("Step " + str(solution[0]) + ":")
                    solution[0] = solution[0] + 1
                    if not self.mathjax_flag:
                        solution.append(self.eqn[t - 1] + op + self.eqn[t + 1] + " = " + str(calc))
                    else:
                        mathjax_str = self.solution_mathjax_format(self.eqn[t - 1] + op + self.eqn[t + 1] + " = " + str(calc))
                        solution.append(mathjax_str)
                    #print(solution)
                    self.eqn[t - 1] = str(calc)
                    del self.eqn[t:t + 2]
                    t = t - 1  # line added to make sure all ops are performed
                    length = len(self.eqn)
                    if is_first:
                        self.eqn_string_update()
                        if not self.mathjax_flag:
                            if solution[-1] != "Equation is now " + self.eqn_string:
                                solution.append("Equation is now " + self.eqn_string)
                        else:
                            mathjax_str = self.solution_mathjax_format(self.eqn_string)
                            if solution[-1] != "Equation is now " + mathjax_str:
                                solution.append("Equation is now " + mathjax_str)
                # print(n, calc)

                elif self.eqn[t] == op1:

                    calc = operation(self.eqn[t - 1], op1, self.eqn[t + 1])
                    solution.append("Step " + str(solution[0]) + ":")
                    solution[0] = solution[0] + 1
                    if not self.mathjax_flag:
                        solution.append(self.eqn[t - 1] + op1 + self.eqn[t + 1] + " = " + str(calc))
                    else:
                        mathjax_str = self.solution_mathjax_format(self.eqn[t - 1] + op1 + self.eqn[t + 1] + " = " + str(calc))
                        solution.append(mathjax_str)
                    #print(solution)
                    self.eqn[t - 1] = str(calc)
                    del self.eqn[t:t + 2]
                    t = t - 1  # line added to make sure all ops are performed
                    length = len(self.eqn)
                    if is_first:
                        self.eqn_string_update()
                        if not self.mathjax_flag:
                            if solution[-1] != "Equation is now " + self.eqn_string:
                                solution.append("Equation is now " + self.eqn_string)
                        else:
                            mathjax_str = self.solution_mathjax_format(self.eqn_string)
                            if solution[-1] != "Equation is now " + mathjax_str:
                                solution.append("Equation is now " + mathjax_str)
                # print(n, calc)

                t = t + 1

        if is_first:

            solution.append("Final answer is "+str(calc))

            for i in range(1, len(solution)):
                self.solution.append(solution[i])

        return calc

