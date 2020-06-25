"""Methods for polynomial root finding."""
from __future__ import annotations
import math
import cmath
from math_core.Equation import Equation, is_number, oper_dict, stringify, bracketify
import random
import copy

from typing import Tuple, List, Union, Dict

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

def cube_root(x: Union[int, float, complex]) -> Union[int, float, complex]:
    """Function takes the cubic root of a number. Created to ensure proper sign of answer is given."""
    if isinstance(x, complex):

        return x ** (1 / 3)

    else:

        if x >= 0.0:

            return x ** (1 / 3)

        else:

            return -(-x) ** (1 / 3)


def poly_add(left_p: List[Union[int, float, complex]], right_p: List[Union[int, float, complex]]) -> List[
    Union[int, float, complex]]:
    """Function takes two polynomials and adds them together."""
    left_len = len(left_p) - 1
    right_len = len(right_p) - 1
    ans = []

    if left_len > right_len:

        for i in right_p:
            ans.insert(0, left_p[left_len] + right_p[right_len])
            left_len -= 1
            right_len -= 1

        ans.insert(0, left_p[0])

    elif right_len > left_len:

        for i in left_p:
            ans.insert(0, left_p[left_len] + right_p[right_len])
            left_len -= 1
            right_len -= 1

        ans.insert(0, right_p[0])

    elif left_len == right_len:

        for i in left_p:
            ans.insert(0, left_p[left_len] + right_p[right_len])
            left_len -= 1
            right_len -= 1

    return ans


def bracket_add(br_one_coeff: List[Union[int, float, complex]], op: str, br_two_coeff: List[Union[int, float, complex]],
                var: str) -> List[str]:
    """Add or subtract two bracket expressions."""
    if op not in "+-":
        raise Exception("Operation not supported.")

    br_one_deg = len(br_one_coeff) - 1
    br_two_deg = len(br_two_coeff) - 1
    ans_coeff = []

    # print("br_one_deg = "+str(br_one_deg[0]))
    # print("br_two_deg = "+str(br_two_deg[0]))

    if op == "+":

        if br_one_deg > br_two_deg:

            for i in range(0, br_two_deg + 1):
                # print(i)
                ans_coeff.insert(0, br_one_coeff[-1 - i] + br_two_coeff[-1 - i])

            i += 1
            while len(br_one_coeff) - 1 - i != -1:
                # print(i)
                ans_coeff.insert(0, br_one_coeff[-1 - i])
                i += 1

        elif br_two_deg > br_one_deg:

            for i in range(0, br_one_deg + 1):
                ans_coeff.insert(0, br_one_coeff[-1 - i] + br_two_coeff[-1 - i])

            i += 1
            while len(br_two_coeff) - 1 - i != -1:
                ans_coeff.insert(0, br_two_coeff[-1 - i])
                i += 1

        else:

            for i in range(0, br_one_deg + 1):
                ans_coeff.insert(0, br_one_coeff[-1 - i] + br_two_coeff[-1 - i])

    elif op == "-":

        if br_one_deg > br_two_deg:

            for i in range(0, br_two_deg + 1):
                ans_coeff.insert(0, br_one_coeff[-1 - i] - br_two_coeff[-1 - i])

            i += 1
            while len(br_one_coeff) - 1 - i != -1:
                ans_coeff.insert(0, br_one_coeff[-1 - i])
                i += 1

        elif br_two_deg > br_one_deg:

            for i in range(0, br_one_deg + 1):
                ans_coeff.insert(0, br_one_coeff[-1 - i] - br_two_coeff[-1 - i])

            i += 1
            while len(br_two_coeff) - 1 - i != -1:
                ans_coeff.insert(0, 0 - br_two_coeff[-1 - i])
                i += 1

        else:

            for i in range(0, br_one_deg + 1):
                ans_coeff.insert(0, br_one_coeff[-1 - i] - br_two_coeff[-1 - i])

    ans = []
    j = 0
    highest_deg_ans = len(ans_coeff) - 1

    if highest_deg_ans > 1:

        for i in range(highest_deg_ans, 1, -1):

            if not ans:

                if ans_coeff[j] == 1:

                    ans.append(var)
                    ans.append("^")
                    ans.append(str(float(i)))
                    j += 1

                elif ans_coeff[j] == 0:

                    pass
                    j += 1

                elif ans_coeff[j] < 0:

                    if ans_coeff[j] == -1:

                        ans.append("-" + var)
                        ans.append("^")
                        ans.append(str(float(i)))
                        j += 1

                    else:

                        ans.append(str(ans_coeff[j]))
                        ans.append(var)
                        ans.append("^")
                        ans.append(str(float(i)))
                        j += 1

                else:

                    ans.append(str(ans_coeff[j]))
                    ans.append(var)
                    ans.append("^")
                    ans.append(str(float(i)))
                    j += 1

            else:

                if ans_coeff[j] == 1:

                    ans.append("+")
                    ans.append(var)
                    ans.append("^")
                    ans.append(str(float(i)))
                    j += 1

                elif ans_coeff[j] == 0:

                    pass
                    j += 1

                elif ans_coeff[j] < 0:

                    if ans_coeff[j] == -1:

                        ans.append("-")
                        ans.append(var)
                        ans.append("^")
                        ans.append(str(float(i)))
                        j += 1

                    else:

                        ans.append("-")
                        ans.append(str(abs(ans_coeff[j])))
                        ans.append(var)
                        ans.append("^")
                        ans.append(str(float(i)))
                        j += 1

                else:

                    ans.append("+")
                    ans.append(str(ans_coeff[j]))
                    ans.append(var)
                    ans.append("^")
                    ans.append(str(float(i)))
                    j += 1

        if ans_coeff[j] == 1:

            ans.append("+")
            ans.append(var)
            j += 1

        elif ans_coeff[j] == 0:

            pass
            j += 1

        elif ans_coeff[j] < 0:

            if ans_coeff[j] == -1:

                ans.append("-")
                ans.append(var)
                j += 1

            else:

                ans.append("-")
                ans.append(str(abs(ans_coeff[j])))
                ans.append(var)
                j += 1

        else:

            ans.append("+")
            ans.append(str(ans_coeff[j]))
            ans.append(var)
            j += 1

        if ans_coeff[j] == 0:

            pass

        else:

            if ans_coeff[j] < 0:

                ans.append("-")
                ans.append(str(abs(ans_coeff[j])))

            else:

                ans.append("+")
                ans.append(str(ans_coeff[j]))

    else:

        if ans_coeff[j] == 1:

            ans.append("+")
            ans.append(var)
            j += 1

        elif ans_coeff[j] == 0:

            pass
            j += 1

        elif ans_coeff[j] < 0:

            if ans_coeff[j] == -1:

                ans.append("-")
                ans.append(var)
                j += 1

            else:

                ans.append("-")
                ans.append(str(abs(ans_coeff[j])))
                ans.append(var)
                j += 1


        else:

            ans.append("+")
            ans.append(str(ans_coeff[j]))
            ans.append(var)
            j += 1

        if ans_coeff[j] == 0:

            pass

        else:

            if ans_coeff[j] < 0:

                ans.append("-")
                ans.append(str(abs(ans_coeff[j])))

            else:

                ans.append("+")
                ans.append(str(ans_coeff[j]))

    return ans


def bracketing(bracket: List[str], var_type: List[str], bracket_dict: Dict, lvl: int = 1):
    """Function recursively identifies brackets, creates a new variable for it and stores it in a variable: bracket dictionary."""
    global var_dict

    sub_br = []
    s = 1
    b = lvl
    b_open = 1
    b_close = 0
    while s != len(bracket):

        if "(" in bracket[s]:

            sub_br.append(bracket[s])
            b += 1
            b_open += 1
            t = s + 1
            while bracket[t] != ")" + str(b):
                sub_br.append(bracket[t])
                t += 1

            sub_br.append(bracket[t])
            # print("sub_br", sub_br, b)
            br = stringify(sub_br)

            del bracket[s + 1:t + 1]
            # print("bracket", bracket, "bracket_dict", bracket_dict)
            if br in bracket_dict:

                bracket[s] = bracket_dict[br]
                b = lvl
                b_open = 1
                s = 0
                # print("bracket is now:", bracket, "bracket_dict", bracket_dict)
                sub_br.clear()

            else:

                # print("here we go, bracket-ception")
                new_br, bracket_dict = bracketing(sub_br, var_type, bracket_dict, lvl=b)
                # print("new bracket", new_br, "bracket_dict", bracket_dict)

                if (len(new_br) == 3) and (is_number(new_br[1])):

                    bracket[s] = new_br[1]
                    b = lvl
                    b_open = 1
                    s = 0
                    sub_br.clear()

                else:

                    new_br_string = stringify(new_br)

                    if new_br_string in bracket_dict:

                        bracket[s] = bracket_dict[new_br_string]
                        b = lvl
                        b_open = 1
                        s = 0
                        # print("bracket is now:", bracket, "bracket_dict", bracket_dict)
                        sub_br.clear()

                    else:

                        # set current index to equal a new variable, and store bracket in a dictionary where key is variable and value is contents of bracket.
                        if bracket_dict:

                            for var in bracket_dict.values():
                                new_var = var_dict[var]

                        else:

                            new_var = var_dict[var_type[0]]

                        # print(new_br_string)
                        bracket_dict[new_br_string] = new_var
                        bracket[s] = new_var
                        # print("bracket after brackception:", bracket, "bracket_dict", bracket_dict)
                        b = lvl
                        b_open = 1
                        s = 0
                        sub_br.clear()

        s += 1

    # print("made it through")
    for var in bracket_dict.values():

        if var not in var_type:
            var_type.append(var)

    # print("bracket after grouping", bracket)

    return bracket, bracket_dict


class Algebra(Equation):
    """This class is used in polynomial root finding problems. Objects of this class have a single attribute being the equation in List[str] format."""

    def __init__(self, eqn_string: str = None):
        self.lhs = []
        self.rhs = []
        self.deg = []
        self.coeff = []
        if not eqn_string:
            self.eqn_string = ""
            self.eqn = []
            self.var_type = []
            self.solution = []
        else:
            Equation.__init__(self, eqn_string)
            self.grouping()
            self.eqn_string_update()
            self.seperate_eqn()

    def lin_divide(self, divisor: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
        """Function does synthetic division of a polynomial. Divisor can only be a linear polynomial."""
        a = (-1 * divisor[1]) / divisor[0]
        b = 0
        ans = []
        n = 0
        for i in self.coeff:
            ans.append(i + b)
            b = ans[-1] * a

        return ans

    def poly_multiply(self, x: Union[int, float, complex]) -> List[Union[int, float, complex]]:
        """Multiply a polynomial by a constant."""

        new_eqn = []
        for i in self.coeff:
            new_eqn.append(x * i)

        return new_eqn

    def evaluate(self, value: Union[int, float, complex]) -> Union[int, float, complex]:
        """Evaluates the polynomial at a given value."""

        ans = 0
        if not self.deg:
            j = len(self.coeff) - 1
            for i in self.coeff:
                ans += i * (value ** j)
                j -= 1
        else:
            for i, j in zip(self.coeff, self.deg):
                ans += i * (value ** j)

        return ans

    def get_coeff(self):
        """Transforms polynomial equation into a list of coefficients in order of highest to lowest power."""
        if (len(self.rhs) != 3) or (not self.lhs):
            raise ValueError("You must properly isolate the equation first.")
        coeff = []

        for s in range(self.deg[0], -1, -1):

            did_append = False

            for i in range(0, len(self.lhs)):

                if "^" + str(float(s)) in self.lhs[i]:

                    temp = self.lhs[i]
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

                        if self.lhs[i - 1] == "-":
                            a = -1 * float(a)

                        coeff.append(float(a))
                        did_append = True

                elif ("^" not in self.lhs[i]) & (self.var_type[0] in self.lhs[i]) & (s == 1):

                    temp = self.lhs[i]
                    a = ""
                    v = 0
                    while temp[v] != self.var_type[0]:
                        a = a + str(temp[v])
                        v += 1

                    if a == "":
                        a = 1

                    if a == "-":
                        a = -1

                    if self.lhs[i - 1] == "-":
                        a = -1 * float(a)

                    coeff.append(float(a))
                    did_append = True

                elif (is_number(self.lhs[i]) == True) & (s == 0):

                    a = complex(self.lhs[i])

                    if round(a.imag, 6) == 0:
                        a = float(a.real)

                    if self.lhs[i - 1] == "-":
                        a = -1 * a

                    coeff.append(a)
                    did_append = True

            if not did_append:
                coeff.append(0)

        self.coeff = coeff

    def update_params_from_coeff(self):
        """Update object attributes from self.coeff."""
        if not self.coeff:
            raise ValueError("Nothing given for self.coeff.")
        if not self.var_type:
            raise ValueError("No value given for self.var_type.")
        if not self.deg:
            j = len(self.coeff) - 1
            temp_string = ""
            for i in self.coeff:
                if j > 1:
                    if temp_string:
                        # Checking if the coefficient is complex
                        if isinstance(i, complex):
                            temp_string += "+"
                            temp_string += str(i) + self.var_type[0] + "^" + str(j)
                        else:
                            if i < 0.0:
                                temp_string += "-"
                                if abs(i) == 1.0:
                                    temp_string += self.var_type[0] + "^" + str(j)
                                else:
                                    temp_string += str(abs(i)) + self.var_type[0] + "^" + str(j)
                            else:
                                temp_string += "+"
                                if i == 1.0:
                                    temp_string += self.var_type[0] + "^" + str(j)
                                else:
                                    temp_string += str(i) + self.var_type[0] + "^" + str(j)
                    else:
                        if isinstance(i, complex):
                            temp_string += str(i) + self.var_type[0] + "^" + str(j)
                        else:
                            if i == 1.0:
                                temp_string += self.var_type[0] + "^" + str(j)
                            elif i == -1.0:
                                temp_string += "-" + self.var_type[0] + "^" + str(j)
                            else:
                                temp_string += str(i) + self.var_type[0] + "^" + str(j)
                elif j == 1:
                    if temp_string:
                        # Checking if the coefficient is complex
                        if isinstance(i, complex):
                            temp_string += "+"
                            temp_string += str(i) + self.var_type[0]
                        else:
                            if i < 0.0:
                                temp_string += "-"
                                if abs(i) == 1.0:
                                    temp_string += self.var_type[0]
                                else:
                                    temp_string += str(abs(i)) + self.var_type[0]
                            else:
                                temp_string += "+"
                                if i == 1.0:
                                    temp_string += self.var_type[0]
                                else:
                                    temp_string += str(i) + self.var_type[0]
                    else:
                        if isinstance(i, complex):
                            temp_string += str(i) + self.var_type[0]
                        else:
                            if i == 1.0:
                                temp_string += self.var_type[0]
                            elif i == -1.0:
                                temp_string += "-" + self.var_type[0]
                            else:
                                temp_string += str(i) + self.var_type[0]
                else:
                    if isinstance(i, complex):
                        if not temp_string:
                            temp_string += str(i)
                        else:
                            temp_string += "+" + str(i)
                    else:
                        if i > 0.0:
                            if not temp_string:
                                temp_string += str(i)
                            else:
                                temp_string += "+" + str(i)
                        else:
                            temp_string += str(i)
                self.deg.append(j)
                j -= 1
        else:
            temp_string = ""
            for i, j in zip(self.coeff, self.deg):
                if j > 1:
                    if temp_string:
                        # Checking if the coefficient is complex
                        if isinstance(i, complex):
                            temp_string += "+"
                            temp_string += str(i) + self.var_type[0] + "^" + str(j)
                        else:
                            if i < 0.0:
                                temp_string += "-"
                                if abs(i) == 1.0:
                                    temp_string += self.var_type[0] + "^" + str(j)
                                else:
                                    temp_string += str(abs(i)) + self.var_type[0] + "^" + str(j)
                            else:
                                temp_string += "+"
                                if i == 1.0:
                                    temp_string += self.var_type[0] + "^" + str(j)
                                else:
                                    temp_string += str(i) + self.var_type[0] + "^" + str(j)
                    else:
                        if isinstance(i, complex):
                            temp_string += str(i) + self.var_type[0] + "^" + str(j)
                        else:
                            if i == 1.0:
                                temp_string += self.var_type[0] + "^" + str(j)
                            elif i == -1.0:
                                temp_string += "-" + self.var_type[0] + "^" + str(j)
                            else:
                                temp_string += str(i) + self.var_type[0] + "^" + str(j)
                elif j == 1:
                    if temp_string:
                        # Checking if the coefficient is complex
                        if isinstance(i, complex):
                            temp_string += "+"
                            temp_string += str(i) + self.var_type[0]
                        else:
                            if i < 0.0:
                                temp_string += "-"
                                if abs(i) == 1.0:
                                    temp_string += self.var_type[0]
                                else:
                                    temp_string += str(abs(i)) + self.var_type[0]
                            else:
                                temp_string += "+"
                                if i == 1.0:
                                    temp_string += self.var_type[0]
                                else:
                                    temp_string += str(i) + self.var_type[0]
                    else:
                        if isinstance(i, complex):
                            temp_string += str(i) + self.var_type[0]
                        else:
                            if i == 1.0:
                                temp_string += self.var_type[0]
                            elif i == -1.0:
                                temp_string += "-" + self.var_type[0]
                            else:
                                temp_string += str(i) + self.var_type[0]
                else:
                    if isinstance(i, complex):
                        if not temp_string:
                            temp_string += str(i)
                        else:
                            temp_string += "+" + str(i)
                    else:
                        if i > 0.0:
                            if not temp_string:
                                temp_string += str(i)
                            else:
                                temp_string += "+" + str(i)
                        else:
                            temp_string += str(i)
        self.eqn_string = temp_string
        if not self.solution:
            self.solution.append("The inputted equation is " + self.eqn_string)
        self.bracketify()
        self.grouping()

    def reset_params(self):
        """Function resets all object attributes"""
        self.eqn_string = ""
        self.eqn = []
        self.lhs = []
        self.rhs = []
        self.var_type = []
        self.solution = []
        self.deg = []
        self.coeff = []

    def seperate_eqn(self):
        """Method seperates eqn attribute into LHS and RHS attributes."""
        if not self.eqn:
            raise ValueError("No value provided for eqn attribute.")
        eqn_copy = copy.deepcopy(self.eqn)
        i = 0
        while eqn_copy[i] != "=":
            self.lhs.append(eqn_copy[i])
            i += 1
        self.lhs.append(")1")
        self.rhs.append("(1")
        i += 1
        while i != len(eqn_copy):
            self.rhs.append(eqn_copy[i])
            i += 1

    def normalize(self) -> List[Union[int, float, complex]]:
        """Normalizes the polynomial."""
        norm = self.coeff[:]
        if (norm[0] == 1) or (norm[0] == 0):

            return norm

        else:

            const = norm[0]
            for i in range(0, len(norm)):
                norm[i] /= const

            return norm

    # Creates a cauchy polynomial
    def cauchy_poly(self) -> List[Union[int, float, complex]]:
        """Normalizes polynomial and takes the absolute value of each coefficient."""
        cauchy = []
        norm = self.normalize()
        for i in range(0, len(norm) - 1):
            cauchy.append(abs(norm[i]))

        cauchy.append(-1 * abs(norm[i + 1]))

        return cauchy

    def newton_raphson(self, err: Union[int, float] = 1e-5) -> Union[int, float, complex]:
        """Finds roots of polynomial using Newton-Raphson method."""
        from math_core.Calculus import Calculus
        der = Calculus()
        der.coeff = self.coeff_derivative()
        x = random.uniform(0, 1)

        while abs(self.evaluate(x)) > abs(err):
            x = x - ((self.evaluate(x)) / (der.evaluate(x)))
            # print("x",x)

        return x

    def quadratic(self) -> List[Union[int, float, complex]]:
        """Solve quadratic polynomials using the quadratic formula."""
        if len(self.coeff) != 3:
            raise ValueError("Quadratics must have 3 terms.")
        self.solution.append("")
        print("\n-- Using the quadratic formula --")
        self.solution.append("-- Using the quadratic formula --")
        print("ax^2 + bx + c = 0")
        self.solution.append("ax^2 + bx + c = 0")
        print("x = (-b +/- √(b^2 - 4ac))/2a\n")
        self.solution.append("x = (-b +/- √(b^2 - 4ac))/2a")

        self.solution.append("")
        a = self.coeff[0]
        print("a = " + str(a))
        self.solution.append("a = " + str(a))
        b = self.coeff[1]
        print("b = " + str(b))
        self.solution.append("b = " + str(b))
        c = self.coeff[2]
        print("c = " + str(c))
        self.solution.append("c = " + str(c))
        print("")

        ans = [0, 0]
        ans[0] = ((-1 * b) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        ans[-1] = ((-1 * b) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

        self.solution.append("\nThe final answers are:")
        for i in ans:
            self.solution.append(str(i))

        return ans

    def cardano(self) -> List[Union[int, float, complex]]:
        """Root finding formula for cubic polynomials."""
        if len(self.coeff) != 4:
            raise ValueError("Cubics must have 4 terms.")
        self.solution.append("")
        print("\n-- Using Cardano's Formula: --")
        self.solution.append("-- Using Cardano's Formula: --")
        print("ax^3 + bx^2 + cx + d = 0\n")
        self.solution.append("ax^3 + bx^2 + cx + d = 0")
        print("x1 = s+t-(b/3a)")
        self.solution.append("x1 = s+t-(b/3a)")
        print("x2 = -(s+t)/2 - (b/3a) + (i*√3/2)*(s-t)")
        self.solution.append("x2 = -(s+t)/2 - (b/3a) + (i*√3/2)*(s-t)")
        print("x3 = -(s+t)/2 - (b/3a) - (i*√3/2)*(s-t)\n")
        self.solution.append("x3 = -(s+t)/2 - (b/3a) - (i*√3/2)*(s-t)")

        self.solution.append("")
        a = self.coeff[0]
        print("a = " + str(a))
        self.solution.append("a = " + str(a))
        b = self.coeff[1]
        print("b = " + str(b))
        self.solution.append("b = " + str(b))
        c = self.coeff[2]
        print("c = " + str(c))
        self.solution.append("c = " + str(c))
        d = self.coeff[3]
        print("d = " + str(d))
        self.solution.append("d = " + str(d))
        print("")

        # depressed cubic
        p = ((3 * a * c) - (b ** 2)) / (9 * (a ** 2))
        q = ((9 * a * b * c) - (27 * (a ** 2) * d) - (2 * (b ** 3))) / (54 * (a ** 3))

        self.solution.append("")
        print("Depressed cubic: y^3 + 3py - 2q = 0\n")
        self.solution.append("Depressed cubic: y^3 + 3py - 2q = 0")
        print("y^3+" + str(3 * p) + "y+" + str(-2 * q) + "=0")
        self.solution.append("y^3+" + str(3 * p) + "y+" + str(-2 * q) + "=0")
        self.solution.append("")
        print("p = (3ac - b^2)/9a^2 = " + str(p))
        self.solution.append("p = (3ac - b^2)/9a^2 = " + str(p))
        print("q = (9abc - 27a^2d - 2b^3)/54a^3 = " + str(q) + "\n")
        self.solution.append("q = (9abc - 27a^2d - 2b^3)/54a^3 = " + str(q))

        s = cube_root((q) + (((p) ** 3) + ((q) ** 2)) ** (1 / 2))
        t = cube_root((q) - (((p) ** 3) + ((q) ** 2)) ** (1 / 2))

        self.solution.append("")
        print("s = (q + √(p^3 + q^2))^(1/3) = " + str(s))
        self.solution.append("s = (q + √(p^3 + q^2))^(1/3) = " + str(s))
        print("t = (q - √(p^3 + q^2))^(1/3) = " + str(t) + "\n")
        self.solution.append("t = (q - √(p^3 + q^2))^(1/3) = " + str(t))

        ans = [0, 0, 0]
        ans[0] = s + t - (b / (3 * a))
        ans[1] = (-1 * ((s + t) / 2)) - (b / (3 * a)) + (((1j * (3 ** 0.5)) / 2) * (s - t))
        ans[-1] = (-1 * ((s + t) / 2)) - (b / (3 * a)) - (((1j * (3 ** 0.5)) / 2) * (s - t))

        self.solution.append("\nThe final answers are:")
        for i in ans:
            self.solution.append(str(i))

        return ans

    # Quartic root formula
    def ferrari(self) -> List[Union[int, float, complex]]:
        """Root finding formula for quartic polynomials."""
        if len(self.coeff) != 5:
            raise ValueError("Quartics must have 5 terms.")
        self.solution.append("")
        print("\n-- Using Ferrari's Method: --")
        self.solution.append("-- Using Ferrari's Method: --")
        print("ax^4 + bx^3 + cx^2 + dx + e = 0\n")
        self.solution.append("ax^4 + bx^3 + cx^2 + dx + e = 0")

        self.solution.append("")
        a = self.coeff[0]
        print("a = " + str(a))
        self.solution.append("a = " + str(a))
        b = self.coeff[1]
        print("b = " + str(b))
        self.solution.append("b = " + str(b))
        c = self.coeff[2]
        print("c = " + str(c))
        self.solution.append("c = " + str(c))
        d = self.coeff[3]
        print("d = " + str(d))
        self.solution.append("d = " + str(d))
        e = self.coeff[4]
        print("e = " + str(e))
        self.solution.append("e = " + str(e))
        print("")

        # depressed quartic

        self.solution.append("")
        print("Substitution: x = y-(b/4a)\n")
        self.solution.append("Substitution: x = y-(b/4a)")
        print("Depressed quartic: y^4 + py^2 + qy + r = 0")
        self.solution.append("Depressed quartic: y^4 + py^2 + qy + r = 0")

        self.solution.append("")
        print("y1 = √((-1/2)*(2z - p)) + √((1/2)*(-2z - p + 2q/√(2z - p)))")
        self.solution.append("y1 = √((-1/2)*(2z - p)) + √((1/2)*(-2z - p + 2q/√(2z - p)))")

        print("y2 = √((-1/2)*(2z - p)) - √((1/2)*(-2z - p + 2q/√(2z - p)))")
        self.solution.append("y2 = √((-1/2)*(2z - p)) - √((1/2)*(-2z - p + 2q/√(2z - p)))")

        print("y3 = √((1/2)*(2z - p)) + √((1/2)*(-2z - p - 2q/√(2z - p)))")
        self.solution.append("y3 = √((1/2)*(2z - p)) + √((1/2)*(-2z - p - 2q/√(2z - p)))")

        print("y4 = √((1/2)*(2z - p)) - √((1/2)*(-2z - p - 2q/√(2z - p)))\n")
        self.solution.append("y4 = √((1/2)*(2z - p)) - √((1/2)*(-2z - p - 2q/√(2z - p)))")

        p = (c / a) - ((3 * b ** 2) / (8 * a ** 2))
        q = (d / a) - ((b * c) / (2 * a ** 2)) + (b ** 3 / (8 * a ** 3))
        r = (e / a) - ((b * d) / (4 * a ** 2)) + (((b ** 2) * c) / (16 * a ** 3)) - ((3 * b ** 4) / (256 * a ** 4))

        self.solution.append("")
        print("p = ((c/a) - 3b^2)/8a^2 = " + str(p))
        self.solution.append("p = ((c/a) - 3b^2)/8a^2 = " + str(p))
        print("q = ((d/a) - bc/(2a^2) + b^3)/8a^3 = " + str(q))
        self.solution.append("q = ((d/a) - bc/(2a^2) + b^3)/8a^3 = " + str(q))
        print("r = ((e/a) - bd/(4a^2) + b^2c/16a^3 - 3b^4)/256a^4 = " + str(q) + "\n")
        self.solution.append("r = ((e/a) - bd/(4a^2) + b^2c/16a^3 - 3b^4)/256a^4 = " + str(q))

        self.solution.append("")
        depressed = "y^4+" + str(p) + "y^2+" + str(q) + "y+" + str(r) + "=0"
        print("Depressed quartic is " + depressed + "\n")
        self.solution.append("Depressed quartic is " + depressed)

        self.solution.append("")
        # resolvent cubic
        print("Resolvent cubic: 8z^3 - 4pz^2 - 8rz + (4pr - q^2) = 0")
        self.solution.append("Resolvent cubic: 8z^3 - 4pz^2 - 8rz + (4pr - q^2) = 0")
        resolvent = "8z^3+" + str(-4 * p) + "z^2+" + str(-8 * r) + "z+" + str((4 * p * r) - (q ** 2))
        print(resolvent + "=0")
        self.solution.append(resolvent + "=0")

        cubic = Algebra(resolvent)
        cubic_ans = cubic.cardano()

        for i in cubic.solution:
            self.solution.append(i)

        self.solution.append("")
        print("the values of z of " + resolvent + " are")
        self.solution.append("the values of z of " + resolvent + " are")

        for i in cubic_ans:
            print(i)
            self.solution.append(i)

        for i in cubic_ans:

            try:

                self.solution.append("")
                print("\nTrying " + str(i) + " to find roots of depressed quartic " + depressed + " ...\n")
                self.solution.append("Trying " + str(i) + " to find roots of depressed quartic " + depressed + " ...")

                s = i

                y_one = ((-1 / 2) * ((2 * s) - p) ** (1 / 2)) + (
                            (1 / 2) * ((-2 * s) - p + (2 * q / ((2 * s) - p) ** (1 / 2))) ** (1 / 2))
                y_two = ((-1 / 2) * ((2 * s) - p) ** (1 / 2)) - (
                            (1 / 2) * ((-2 * s) - p + (2 * q / ((2 * s) - p) ** (1 / 2))) ** (1 / 2))
                y_three = ((1 / 2) * ((2 * s) - p) ** (1 / 2)) + (
                            (1 / 2) * ((-2 * s) - p - (2 * q / ((2 * s) - p) ** (1 / 2))) ** (1 / 2))
                y_four = ((1 / 2) * ((2 * s) - p) ** (1 / 2)) - (
                            (1 / 2) * ((-2 * s) - p - (2 * q / ((2 * s) - p) ** (1 / 2))) ** (1 / 2))

            except ZeroDivisionError:

                print("attempt failed...")
                self.solution.append("attempt failed...")

            else:

                break

        print("Success!\n")
        self.solution.append("Success!")
        self.solution.append("")

        print("The values of y are")
        self.solution.append("The values of y are")
        print(y_one)
        self.solution.append(str(y_one))
        print(y_two)
        self.solution.append(str(y_two))
        print(y_three)
        self.solution.append(str(y_three))
        print(y_four, "\n")
        self.solution.append(str(y_four))
        self.solution.append("\n")

        print("Recall x = y-(b/4a)\n")
        self.solution.append("Recall x = y-(b/4a)")
        self.solution.append("")

        ans = [0, 0, 0, 0]

        ans[0] = y_one - (b / (4 * a))
        self.solution.append("x = " + str(y_one) + "-(" + str(b) + "/(4*" + str(a) + "))")
        ans[1] = y_two - (b / (4 * a))
        self.solution.append("x = " + str(y_two) + "-(" + str(b) + "/(4*" + str(a) + "))")
        ans[2] = y_three - (b / (4 * a))
        self.solution.append("x = " + str(y_three) + "-(" + str(b) + "/(4*" + str(a) + "))")
        ans[-1] = y_four - (b / (4 * a))
        self.solution.append("x = " + str(y_four) + "-(" + str(b) + "/(4*" + str(a) + "))")

        self.solution.append("\nThe final answers are:")
        for i in ans:
            self.solution.append(str(i))

        return ans

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
            if ("(" in self.eqn[i]) & (self.eqn[i] not in oper_dict.values()):

                b += 1
                b_open += 1
                b_loc = i

                for op in oper_dict.values():

                    if op == self.eqn[i - 1]:
                        p_b = b
                        p = i

            if (")" in self.eqn[i]) & (self.eqn[i] not in oper_dict.values()):

                if self.eqn[i] == ")" + str(p_b):
                    p_b = 0
                    p = 0

                b -= 1
                b_close += 1

            if (self.eqn[i].isalpha() == True) and (len(self.eqn[i]) == 1):

                # print("eqn[i]", eqn[i])
                if self.eqn[i] not in var:
                    var.append(self.eqn[i])

                if (self.eqn[i + 1] == "^") and (is_number(self.eqn[i + 2]) == True):
                    self.eqn[i] = self.eqn[i] + "^" + self.eqn[i + 2]
                    del self.eqn[i + 1:i + 3]
                    mod = True
                # print(eqn)

                if (is_number(self.eqn[i - 1]) == True):
                    self.eqn[i - 1] = self.eqn[i - 1] + self.eqn[i]
                    del self.eqn[i]
                    mod = True
                # print(eqn)

                if (self.eqn[i - 1] == "*") and (is_number(self.eqn[i - 2]) == True):
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

        if len(self.eqn) > 1:

            if self.eqn[1] == "-":
                self.eqn[1] = self.eqn[1] + self.eqn[2]
                del self.eqn[2]

        # print("new_eqn_deg", new_eqn_deg)
        self.deg = new_eqn_deg
        self.eqn_string_update()

    def isolate(self):
        """method arranges the equation to have variables on LHS and constants on RHS."""
        bracket_dict = {}
        global var_dict

        # as a first step, check if there’s a variable to the power of the variable. If so, end and return an error. Else continue
        b = 0
        j = 0
        s = 0
        b_open = 0
        b_close = 0
        eqn = [self.lhs[:], self.rhs[:]]
        # LHS first
        for i in eqn:
            for k in range(0, len(i)):

                # print("self.lhs[k]", i[k])

                if "(" in i[k]:
                    b += 1
                    j = k
                    b_open += 1

                if ")" in i[k]:
                    b -= 1
                    b_close += 1

                if i[k] == "^":
                    s = k

                if (i[k] == self.var_type[0]):

                    # print("There's a variable")

                    # is it x^x?
                    # print("Test 1: x^x?", i[k - 1] == "^", i[k - 2] == self.var_type[0])
                    if (i[k - 1] == "^") and (i[k - 2] == self.var_type[0]):
                        raise ValueError("Cannot calculate x^x or any other variation")

                    # is it x^(19+x) or something like that?
                    # print("Test 2: x^(...x)?", b_open != b_close, s < j, i[s - 1] == self.var_type[0], "(" in i[s + 1])
                    if (b_open != b_close) and (s < j) and (i[s - 1] == self.var_type[0]) and ("(" in i[s + 1]):

                        l = k
                        b_temp = 0
                        while l != s:

                            if "(" in i[l]:
                                b_temp -= 1

                            if ")" in i[l]:
                                b_temp += 1

                            l -= 1

                        if b_temp != 0:
                            raise ValueError("Cannot calculate x^x or any other variation")

                    # is it (x^2-5x+6)^x or something like that?
                    # print("Test 3: (...x...)^x?", i[k - 1] == "^", ")" in i[k - 2])
                    if (i[k - 1] == "^") and (")" in i[k - 2]):

                        l = k - 2
                        while i[l] != "(" + str(b + 1):

                            if i[l] == self.var_type[0]:
                                raise ValueError("Cannot calculate x^x or any other variation")

                            l -= 1

                    # is it (x^2-5x+6)^(19+x)
                    # print("Test 4: (...x...)^(...x...)?", b_open != b_close, s < j, ")" in i[s - 1], "(" in i[s + 1])
                    if (b_open != b_close) and (s < j) and (")" in i[s - 1]) and ("(" in i[s + 1]) and (s != 0):

                        l = k
                        b_temp = 0
                        while l != s:

                            if "(" in i[l]:
                                b_temp -= 1

                            if ")" in i[l]:
                                b_temp += 1

                            l -= 1

                        if b_temp != 0:

                            # we know the variable is in the exponent now is it also in the base
                            l = s - 1
                            b_temp = i[l]
                            b_temp = b_temp.replace(")", "")
                            while i[l] != "(" + b_temp:

                                if i[l] == self.var_type[0]:
                                    raise ValueError("Cannot calculate x^x or any other variation")

                                l -= 1

        # make a copy of LHS and RHS. Store as global variables
        l_og = self.lhs[:]
        l_new, bracket_dict = bracketing(self.lhs, self.var_type, bracket_dict)

        s = 0
        while s == 0:

            br = stringify(l_new)
            length = len(br)
            if br in bracket_dict:

                del l_new[1:length + 1]
                l_new.insert(1, bracket_dict[br])

            else:

                s = 1

        #print(l_og, l_new, bracket_dict)

        r_og = self.rhs[:]
        r_new, bracket_dict = bracketing(self.rhs, self.var_type, bracket_dict)

        s = 0
        while s == 0:

            br = stringify(r_new)
            length = len(br)
            if br in bracket_dict:

                del r_new[1:length + 1]
                r_new.insert(1, bracket_dict[br])

            else:

                s = 1

        #print(r_og, r_new, bracket_dict)

        # Lets take note of the variables in l and r now
        work_var_l = []
        work_var_r = []
        for var in bracket_dict.values():

            for i, j in zip(l_new, r_new):

                if var in i:
                    work_var_l.append(var)

                if var in j:
                    work_var_r.append(var)

        for i, j in zip(l_new, r_new):

            if (self.var_type[0] in i) and (self.var_type[0] not in work_var_l):
                work_var_l.append(self.var_type[0])

            if (self.var_type[0] in j) and (self.var_type[0] not in work_var_r):
                work_var_r.append(self.var_type[0])

        #print("YOOOOOOOOOOO", work_var_l, work_var_r, bracket_dict)

        if (len(work_var_l) == 1) and (len(work_var_r) == 1):

            if (work_var_l[0] == work_var_r[0]):

                work_var = work_var_l
                if work_var == self.var_type[0]:

                    ans = solving(l_new, r_new, work_var[0])

                else:

                    # solve and keep resubbing
                    while work_var != self.var_type[0]:

                        if any(isinstance(sub, list) for sub in r_new) == True:

                            ans = []
                            for i in r_new:
                                temp_string = stringify(i)
                                temp = Equation(temp_string)
                                ans_temp = solving(l_new, temp.eqn, work_var[0])
                                ans.append(ans_temp)
                                temp = None
                        else:

                            ans = solving(l_new, r_new, work_var[0])

                        for i in ans:
                            print(work_var[0] + " = " + str(i))

                        for i in bracket_dict:

                            if bracket_dict[i] == work_var[0]:
                                print(work_var[0] + " = " + i)
                                l_new_string = i

                        # is the new resubstitution a single variable or does more resubbing need to be done?
                        work_var_l = []
                        for var in bracket_dict.values():

                            for i in range(0, len(l_new_string)):

                                if var in l_new_string[i]:
                                    work_var_l.append(var)

                        if len(work_var_l) > 1:

                            while len(work_var_l) != 1:

                                for i in work_var_l:

                                    for k in bracket_dict:

                                        if bracket_dict[k] == i:
                                            print(i + " = " + k)
                                            l_new_string = l_new_string.replace(i, k)

                                work_var_l = []
                                for var in bracket_dict.values():

                                    for i in range(0, len(l_new_string)):

                                        if var in l_new_string[i]:
                                            work_var_l.append(var)

                        r_new = []
                        for i in ans:
                            print(l_new_string + " = " + str(i))
                            temp = Equation(str(i))
                            r_new.append(temp.eqn)
                            temp = None

                        l_new_obj = Equation(l_new_string)
                        l_new, work_var = l_new_obj.eqn, l_new_obj.var_type[0]
                        l_new_obj = None

            else:

                # Now we should check if the variables are one character apart. Ex: z and a or a and b
                if (work_var_l[0] == var_dict[work_var_r[0]]):

                    #print(work_var_l[0], var_dict[work_var_r[0]])
                    for x in bracket_dict:

                        if bracket_dict[x] == work_var_l[0]:
                            sub = x

                    #print("we here one", sub)
                    br = stringify(l_new)
                    br = br.replace(work_var_l[0], "(" + sub + ")")
                    #print(br)
                    l_new_obj = Equation(br)
                    l_new, work_var = l_new_obj.eqn, l_new_obj.var_type[0]
                    l_new_obj = None
                    print(l_new)

                    # solve and keep resubbing
                    while (l_new[1] != self.var_type[0]) and (len(l_new) != 3):

                        if any(isinstance(sub, list) for sub in r_new) == True:

                            l_new_string = stringify(l_new)
                            l_new_obj = Equation(l_new_string)
                            l_new, work_var = l_new_obj.eqn, l_new_obj.var_type[0]
                            l_new_obj = None

                            ans = []
                            for i in r_new:
                                temp_string = stringify(i)
                                temp = Equation(temp_string)
                                ans_temp = solving(l_new, temp.eqn, work_var[0])
                                ans.append(ans_temp)
                                temp = None
                        else:

                            ans = solving(l_new, r_new, work_var[0])

                        l_new_string = work_var
                        #print("bottle caps", l_new_string, ans)
                        r_new = []

                        if any(isinstance(sub, list) for sub in ans) == True:

                            for i in ans:
                                print(work_var + " = " + str(i[0]))
                                r_temp = Equation(str(i[0]))
                                r_new.append(r_temp.eqn)
                                r_temp = None

                        else:

                            for i in ans:
                                print(work_var[0] + " = " + str(i))
                                r_temp = Equation(str(i))
                                r_new.append(r_temp.eqn)
                                r_temp = None

                        resub = False
                        for i in bracket_dict:

                            if bracket_dict[i] == work_var[0]:
                                print(work_var[0] + " = " + i)
                                l_new_string = i
                                resub = True

                        # Is there a resub?is the new resubstitution a single variable or does more resubbing need to be done?

                        if resub == True:

                            work_var_l = []
                            for var in bracket_dict.values():

                                for i in range(0, len(l_new_string)):

                                    if var in l_new_string[i]:
                                        work_var_l.append(var)

                            if len(work_var_l) > 1:

                                while len(work_var_l) != 1:

                                    for i in work_var_l:

                                        for k in bracket_dict:

                                            if bracket_dict[k] == i:
                                                print(i + " = " + k)
                                                l_new_string = l_new_string.replace(i, "(" + k + ")")
                                                print(l_new_string)

                                    work_var_l = []
                                    for var in bracket_dict.values():

                                        for i in range(0, len(l_new_string)):

                                            if var in l_new_string[i]:
                                                work_var_l.append(var)

                                    if not work_var_l:

                                        for i in range(0, len(l_new_string)):

                                            if (self.var_type[0] in l_new_string[i]) and (self.var_type[0] not in work_var_l):
                                                work_var_l.append(self.var_type[0])

                            for i in ans:
                                print(l_new_string + " = " + str(i))

                        l_new_obj = Equation(l_new_string)
                        l_new, work_var = l_new_obj.eqn, l_new_obj.var_type[0]
                        l_new_obj = None

                elif (work_var_r[0] == var_dict[work_var_l[0]]):

                    for x in bracket_dict:

                        if bracket_dict[x] == work_var_r[0]:
                            sub = x

                    print("we here one", sub)
                    br = stringify(r_new)
                    br = br.replace(work_var_r[0], "(" + sub + ")")
                    print(br)

                else:

                    ans = solving(l_og, r_og, self.var_type[0])

                    l_new_obj = Equation(self.var_type[0])
                    l_new, l_var = l_new_obj.eqn, l_new_obj.var_type[0]
                    l_new_obj = None

                    r_new = []
                    for i in ans:
                        temp = Equation(str(i))
                        r_new.append(temp.eqn)
                        temp = None
        else:

            # print(l_og_string+" = "+r_og_string)

            ans = solving(l_og, r_og, self.var_type[0])

            l_new_obj = Equation(self.var_type[0])
            l_new, l_var = l_new_obj.eqn, l_new_obj.var_type[0]
            l_new_obj = None
            r_new = []
            for i in ans:
                temp = Equation(str(i))
                r_new.append(temp.eqn)
                temp = None

        print("Made it to the end", "l", "r")

        return l_new, r_new
