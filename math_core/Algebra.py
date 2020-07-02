"""Methods for polynomial root finding."""
from __future__ import annotations
import math
import cmath
from math_core.Equation import Equation, is_number, oper_dict, stringify, bracketify
from math_core.Arithmetic import Arithmetic, is_even
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

def is_complex_coeff(string: str, var: str) -> bool:
    """Function checks if a monomial string has a complex coefficient. Returns True or False."""
    if var in string:

        coeff = ""
        k=0
        while string[k] != var:

            coeff+=string[k]

            k+=1

        if coeff == "":

            coeff = "1"

        elif coeff == "-":

            coeff = "-1"

        coeff = complex(coeff)

        if coeff.imag == 0:

            return False

        else:

            return True

    else:

        coeff = complex(string)

        if coeff.imag == 0:

            return False

        else:

            return True

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

def foiling(b_one: List[str], b_two: List[str], var_type: str) -> List[str]:
    """Polynomial multiplication. Both polynomials must be of atleast degree 1."""
    print(b_one, b_two, var_type)
    b_one_string = stringify(b_one)
    b_one_obj = Algebra(b_one_string+"=0")

    b_two_string = stringify(b_two)
    b_two_obj = Algebra(b_two_string+"=0")

    # Create array with only coefficients
    b_one_obj.get_coeff()
    b_two_obj.get_coeff()
    b_one_coeff = copy.deepcopy(b_one_obj.coeff)
    b_two_coeff = copy.deepcopy(b_two_obj.coeff)
    b_one_obj, b_two_obj = None, None
    # print("b_one_coeff = ", b_one_coeff.eqn, "b_two_coeff = ", b_two_coeff.eqn)

    ans_coeff = []
    ans_powers = []
    b_one_pow = len(b_one_coeff) - 1
    b_two_pow = len(b_two_coeff) - 1

    # Foiling
    for i in range(0, len(b_one_coeff)):

        for j in range(0, len(b_two_coeff)):
            ans_coeff.append(b_one_coeff[i] * b_two_coeff[j])
            ans_powers.append((b_one_pow - i) + (b_two_pow - j))

    # print("ans_coeff = ", ans_coeff)
    # Simplifying the answer
    simp_ans_coeff = []
    temp_ind = []
    temp = 0
    for i in range(ans_powers[0], -1, -1):

        for j in range(0, len(ans_powers)):

            if ans_powers[j] == i:
                temp += ans_coeff[j]

        simp_ans_coeff.append(temp)
        temp = 0

    # print("simp_ans_coeff = ", simp_ans_coeff)
    ans = []
    j = 0
    highest_deg_ans = len(simp_ans_coeff) - 1

    if highest_deg_ans > 1:

        for i in range(highest_deg_ans, 1, -1):

            if not ans:

                if simp_ans_coeff[j].imag == 0:

                    if simp_ans_coeff[j] == 1:

                        ans.append(var_type)
                        ans.append("^")
                        ans.append(str(float(i)))
                        j += 1

                    elif simp_ans_coeff[j] == 0:

                        pass
                        j += 1

                    elif simp_ans_coeff[j] < 0:

                        if simp_ans_coeff[j] == -1:

                            ans.append("-" + var_type)
                            ans.append("^")
                            ans.append(str(float(i)))
                            j += 1

                        else:

                            ans.append(str(simp_ans_coeff[j]))
                            ans.append(var_type)
                            ans.append("^")
                            ans.append(str(float(i)))
                            j += 1

                    else:

                        ans.append(str(simp_ans_coeff[j]))
                        ans.append(var_type)
                        ans.append("^")
                        ans.append(str(float(i)))
                        j += 1

                # simp_coeff_ans[j] is a complex number
                else:

                    ans.append(str(simp_ans_coeff[j]))
                    ans.append(var_type)
                    ans.append("^")
                    ans.append(str(float(i)))
                    j += 1

            else:

                if simp_ans_coeff[j].imag == 0:

                    if simp_ans_coeff[j] == 1:

                        ans.append("+")
                        ans.append(var_type)
                        ans.append("^")
                        ans.append(str(float(i)))
                        j += 1

                    elif simp_ans_coeff[j] == 0:

                        pass
                        j += 1

                    elif simp_ans_coeff[j] < 0:

                        if simp_ans_coeff[j] == -1:

                            ans.append("-")
                            ans.append(var_type)
                            ans.append("^")
                            ans.append(str(float(i)))
                            j += 1

                        else:

                            ans.append("-")
                            ans.append(str(abs(simp_ans_coeff[j])))
                            ans.append(var_type)
                            ans.append("^")
                            ans.append(str(float(i)))
                            j += 1

                    else:

                        ans.append("+")
                        ans.append(str(simp_ans_coeff[j]))
                        ans.append(var_type)
                        ans.append("^")
                        ans.append(str(float(i)))
                        j += 1

                # simp_coeff_ans[j] is a complex number
                else:

                    ans.append("+")
                    ans.append(str(simp_ans_coeff[j]))
                    ans.append(var_type)
                    ans.append("^")
                    ans.append(str(float(i)))
                    j += 1

        if simp_ans_coeff[j].imag == 0:

            if simp_ans_coeff[j] == 1:

                ans.append("+")
                ans.append(var_type)
                j += 1

            elif simp_ans_coeff[j] == 0:

                pass
                j += 1

            elif simp_ans_coeff[j] < 0:

                if simp_ans_coeff[j] == -1:

                    ans.append("-")
                    ans.append(var_type)
                    j += 1

                else:

                    ans.append("-")
                    ans.append(str(abs(simp_ans_coeff[j])))
                    ans.append(var_type)
                    j += 1

            else:

                ans.append("+")
                ans.append(str(simp_ans_coeff[j]))
                ans.append(var_type)
                j += 1

        else:

            ans.append("+")
            ans.append(str(simp_ans_coeff[j]))
            ans.append(var_type)
            j += 1

        if simp_ans_coeff[j].imag == 0:

            if simp_ans_coeff[j] == 0:

                pass

            else:

                if simp_ans_coeff[j] < 0:

                    ans.append("-")
                    ans.append(str(abs(simp_ans_coeff[j])))

                else:

                    ans.append("+")
                    ans.append(str(simp_ans_coeff[j]))

        else:

            ans.append("+")
            ans.append(str(simp_ans_coeff[j]))

    else:

        if not ans:

            if simp_ans_coeff[j].imag == 0:

                if simp_ans_coeff[j] == 1:

                    ans.append(var_type)
                    j += 1

                elif simp_ans_coeff[j] == 0:

                    pass
                    j += 1

                elif simp_ans_coeff[j] < 0:

                    if simp_ans_coeff[j] == -1:

                        ans.append("-")
                        ans.append(var_type)
                        j += 1

                    else:

                        ans.append("-")
                        ans.append(str(abs(simp_ans_coeff[j])))
                        ans.append(var_type)
                        j += 1

                else:

                    ans.append(str(simp_ans_coeff[j]))
                    ans.append(var_type)
                    j += 1

            else:

                ans.append(str(simp_ans_coeff[j]))
                ans.append(var_type)
                j += 1

        else:

            if simp_ans_coeff[j].imag == 0:

                if simp_ans_coeff[j] == 1:

                    ans.append("+")
                    ans.append(var_type)
                    j += 1

                elif simp_ans_coeff[j] == 0:

                    pass
                    j += 1

                elif simp_ans_coeff[j] < 0:

                    if simp_ans_coeff[j] == -1:

                        ans.append("-")
                        ans.append(var_type)
                        j += 1

                    else:

                        ans.append("-")
                        ans.append(str(abs(simp_ans_coeff[j])))
                        ans.append(var_type)
                        j += 1

                else:

                    ans.append("+")
                    ans.append(str(simp_ans_coeff[j]))
                    ans.append(var_type)
                    j += 1

            else:

                ans.append("+")
                ans.append(str(simp_ans_coeff[j]))
                ans.append(var_type)
                j += 1

        if simp_ans_coeff[j].imag == 0:

            if simp_ans_coeff[j] == 0:

                pass

            else:

                if simp_ans_coeff[j] < 0:

                    ans.append("-")
                    ans.append(str(abs(simp_ans_coeff[j])))

                else:

                    ans.append("+")
                    ans.append(str(simp_ans_coeff[j]))

        else:

            ans.append("+")
            ans.append(str(simp_ans_coeff[j]))

    return ans

def exp_foiling(br: List[str], x: float, var: str) -> List[str]:
    """Function will foil out polynomial expressions raised to a certain power ex: (x+3)^8."""

    br_one = br[:]
    br_two = br[:]

    if is_even(x):

        print("x is even and is "+str(x))
        while x != 1.0:

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

        result = Equation(stringify(br))
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

        while x != 0.0:

            #print(br_one, br_two)
            br = foiling(br_one, br_two, var)
            br.insert(0,"(2")
            br.append(")2")
            br_one = br
            x-=1

        result = Equation(stringify(br))
        #res_string = stringify(result)
        #print(res_string)

    return result.eqn

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


def solving(eqn: Algebra) -> List[Union[int, float, complex]]:

    l_div, r_div = eqn.identify_div()

    #print("What", l_div, r_div)

    # l_div = []
    if not l_div:

        # l_div = [] = r_div
        if not r_div:

            eqn.redundant_br()
            eqn.bracket_remover()
            eqn.rearrange()
            ans = eqn.solver()
            asy = []

        # l_div = [] != r_div
        else:

            eqn.redundant_br()
            eqn.multiply_br(r_div)
            eqn.redundant_div(r_div)
            eqn.bracket_remover()
            eqn.rearrange()
            ans = eqn.solver()
            asy = eqn.find_asymptotes(r_div)

    # l_div != []
    else:

        # l_div != [] = r_div
        if not r_div:

            eqn.redundant_br()
            eqn.multiply_br(l_div)
            eqn.redundant_div(l_div)
            print(stringify(eqn.lhs)+" = "+stringify(eqn.rhs))
            eqn.bracket_remover()
            eqn.rearrange()
            ans = eqn.solver()
            asy = eqn.find_asymptotes(l_div)

        # l_div != [] != r_div
        else:

            print("we should be here", l_div, r_div)

            eqn.redundant_br()
            eqn.multiply_br(l_div)
            eqn.redundant_div(l_div)
            eqn.multiply_br(r_div)
            eqn.redundant_div(r_div)
            print("AYO", stringify(eqn.lhs) + " = " + stringify(eqn.rhs))
            eqn.bracket_remover()
            eqn.rearrange()
            ans = eqn.solver()
            l_asy = eqn.find_asymptotes(l_div)
            r_asy = eqn.find_asymptotes(r_div)

            asy = []
            for i in l_asy:

                if i not in asy:
                    asy.append(i)

            for i in r_asy:

                if i not in asy:
                    asy.append(i)

    new_ans = []
    for i in ans:

        i = complex(i)
        if round(i.imag, 4) == 0:

            temp = round(i.real, 6)
            new_ans.append(temp)

        else:

            temp = round(i.real, 6) + round(i.imag, 6) * 1j
            new_ans.append(temp)

    if asy:

        for i in asy:

            asy_temp = complex(i)
            k = 0
            while k != len(new_ans):

                if round(new_ans[k].real, 1) + round(new_ans[k].imag, 1) * 1j == asy_temp:
                    del new_ans[k]
                    k = -1

                k += 1

    return new_ans


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
        if self.var_type[0] == "":

            for i in self.lhs:

                if is_number(i):
                    temp = complex(i)
                    if temp.imag == 0.0:
                        coeff.append(temp.real)
                    else:
                        coeff.append(temp)
        else:

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

                    elif (is_number(self.lhs[i])) & (s == 0):

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
                            elif i == 0.0:
                                j -= 1
                                continue
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
                            elif i == 0.0:
                                j -= 1
                                continue
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
                            elif i == 0.0:
                                j -= 1
                                continue
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
                            elif i == 0.0:
                                j -= 1
                                continue
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
                            elif i == 0.0:
                                continue
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
                            elif i == 0.0:
                                continue
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
                            elif i == 0.0:
                                continue
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
                            elif i == 0.0:
                                continue
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

    def update_attr(self):
        """Method updates all object attributes."""
        if not self.lhs or not self.rhs:
            raise ValueError("LHS and RHS attributes need values for this method.")
        self.eqn.clear()
        self.eqn = copy.deepcopy(self.lhs)
        self.eqn[-1] = "="
        for i in range(1, len(self.rhs)):
            self.eqn.append(self.rhs[i])
        new_var_type=[]
        for i in self.var_type:
            for j in self.eqn:
                if i in j:
                    if i not in new_var_type:
                        new_var_type.append(i)
        self.var_type.clear()
        self.var_type = copy.deepcopy(new_var_type)
        self.grouping()
        self.eqn_string = stringify(self.lhs)+"="+stringify(self.rhs)
        self.get_coeff()
        #self.update_params_from_coeff()

    def reset_params(self):
        """Method resets all object attributes"""
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

    def identify_div(self) -> Tuple[List[str]]:
        """Method identifies divisors and returns them in array format."""

        divisors = [[], []]
        eqn_parts = ["lhs", "rhs"]
        n = 0
        for side in eqn_parts:
            s = 0
            i = getattr(self, side)
            while s != len(i):
                # What do we do if COS(()/())? or (()/())^7. Maybe it would be wise to make a marker that indicates a bracket is preceded by a special op like COS
                if ("(" in i[s]) and (i[s - 1] == "/") and (s != 0):

                    # print("s is currently "+str(s),self.eqn[s])
                    br_string = "("
                    k = s + 1
                    while ")" not in i[k]:
                        br_string += i[k]
                        k += 1

                    k += 1
                    br_string += ")"

                    exp_check = False
                    if i[k] == "^":
                        exp_check == True
                        br_string += "^" + i[k + 1]

                    k = 0
                    b = 0
                    while k != s:

                        if "(" in i[k]:

                            b += 1

                        elif ")" in i[k]:

                            b -= 1

                        k += 1

                    x = 1
                    c = b
                    while k != len(i):

                        if "(" in i[k]:

                            b += 1

                        elif ")" in i[k]:

                            b -= 1

                        if (is_number(i[k]) == True) and (i[k - 1] == "^") and (
                                i[k - 2] == ")" + str(c)):

                            x *= float(i[k])
                            c -= 1

                        elif (i[k - 1] != "^") and (i[k - 2] == ")" + str(c)):

                            c -= 1

                        k += 1

                    if (x > 1) and (exp_check == False):

                        br_string = br_string + "^" + str(x)

                    elif (x > 1) and (exp_check == True):

                        x_temp = float(br_string[-1])
                        x *= x_temp
                        new_br_string = ""
                        i = 0
                        while br_string[i] != "^":
                            new_br_string += br_string[i]

                        new_br_string += "^" + str(x)
                        br_string = new_br_string

                    print("The divisor is: " + br_string)

                    br = Equation(br_string)
                    del br.eqn[0]
                    del br.eqn[-1]

                    #print(br.eqn)
                    divisors[n].append(br.eqn)

                elif ((is_number(i[s]) == True) or (self.var_type[0] in i[s])) and (i[s - 1] == "/") and (
                        s != 0):

                    br_string = i[s]

                    k = 0
                    b = 0
                    b_open = 0
                    b_close = 0
                    while k != s:

                        if "(" in i[k]:

                            b_open += 1
                            b += 1

                        elif ")" in i[k]:

                            b_close += 1
                            b -= 1

                        k += 1

                    x = 1
                    c = b
                    while k != len(i):

                        if "(" in i[k]:

                            b_open += 1
                            b += 1

                        elif ")" in i[k]:

                            b_close += 1
                            b -= 1

                        if (is_number(i[k]) == True) and (i[k - 1] == "^") and (
                                i[k - 2] == ")" + str(c)):

                            x *= float(i[k])
                            c -= 1

                        elif (i[k - 1] != "^") and (i[k - 2] == ")" + str(c)):

                            c -= 1

                        k += 1

                    if x > 1:
                        br_string = "(" + br_string + ")^" + str(x)

                    print("The divisor is: " + br_string)

                    br = Equation(br_string)
                    del br.eqn[0]
                    del br.eqn[-1]

                    #print(br.eqn)
                    divisors[n].append(br.eqn)

                s += 1

            n += 1

        return divisors

    def redundant_br(self):
        """Method removes redundant brackets ex: (()+()) = ()+() or ex: (()/())^c = ()^c/()^c."""
        eqn_parts = ["lhs", "rhs"]
        for side in eqn_parts:
            z = getattr(self, side)
            #print("HELLO", stringify(z))
            b=0
            for s in z:

                if "(" in s:

                    temp = s
                    temp = temp.replace("(","")
                    temp = int(temp)

                    if temp > b:

                        b = temp

            for c in range(b-1,1,-1):

                s = 0
                while s != len(z):

                    #print(s, "length of z is "+str(len(z)))
                    #first is there a constant, a divisor or an exponent on a pair of brackets? a*()^x/b or a*()/b
                    if (z[s] == "("+str(c)) and (z[s-1] == "*"):

                        k = s
                        d = 0
                        br_string = ""
                        case_type = 0
                        while z[k] != ")"+str(c):

                            if z[k] == "("+str(c+1):

                                br_string += "("
                                d+=1

                            elif z[k] == ")"+str(c+1):

                                br_string += ")"
                                d-=1

                            elif "(" in z[k]:

                                br_string += "("

                            elif ")" in z[k]:

                                br_string += ")"

                            elif (z[k] in "+-*/") and (d == 0):

                                br_string += z[k]
                                if (z[k] in "+-") and (case_type == 0):

                                    case_type = 1

                                elif (z[k] in "+-") and (case_type == 1):

                                    pass

                                elif (z[k] in "*/") and (case_type == 0):

                                    case_type = 2

                                elif (z[k] in "*/") and (case_type == 2):

                                    pass

                                else:

                                    case_type = 3

                            else:

                                br_string += z[k]

                            k+=1

                        br_string += ")"
                        #print(br_string, "constant case_type = "+str(case_type))
                        k+=1
                        if (z[k] == "^"):

                            br_string += "^"+z[k+1]
                            if (case_type == 0) or (case_type == 1) or (case_type == 3):

                                print("no redundant brackets found")

                            else:

                                new_br_string = ""
                                i = 1
                                m = br_string.find(")^")
                                while i != m:

                                    new_br_string += br_string[i]
                                    i+=1

                                new_br_string = new_br_string.replace(")",")^"+z[k+1])
                                eqn_string = stringify(z)
                                #print(eqn_string)
                                eqn_string = eqn_string.replace(br_string, new_br_string)
                                #print(eqn_string)
                                eqn_temp = Equation(eqn_string)
                                setattr(self, side, eqn_temp.eqn)
                                z = getattr(self, side)
                                eqn_temp = None
                                s = 0

                        elif (z[k] in "/*"):

                            print("no redundant brackets found")

                        else:

                            if (case_type == 0):

                                new_br_string = ""
                                for i in range(1,len(br_string)-1):

                                    new_br_string += br_string[i]

                                eqn_string = stringify(z)
                                #print(eqn_string)
                                eqn_string = eqn_string.replace(br_string, new_br_string)
                                #print(eqn_string)
                                eqn_temp = Equation(eqn_string)
                                setattr(self, side, eqn_temp.eqn)
                                z = getattr(self, side)
                                eqn_temp = None
                                s=0

                            elif (case_type == 1) or (case_type == 3):

                                print("no redundant brackets found")

                            else:

                                new_br_string = ""
                                for i in range(1,len(br_string)-1):

                                    new_br_string += br_string[i]

                                eqn_string = stringify(z)
                                #print(eqn_string)
                                eqn_string = eqn_string.replace(br_string, new_br_string)
                                #print(eqn_string)
                                eqn_temp = Equation(eqn_string)
                                setattr(self, side, eqn_temp.eqn)
                                z = getattr(self, side)
                                eqn_temp = None
                                s=0

                    elif z[s] == "("+str(c):

                        k = s
                        d = 0
                        br_string = ""
                        case_type = 0
                        while z[k] != ")"+str(c):

                            if z[k] == "("+str(c+1):

                                br_string += "("
                                d+=1

                            elif z[k] == ")"+str(c+1):

                                br_string += ")"
                                d-=1

                            elif "(" in z[k]:

                                br_string += "("

                            elif ")" in z[k]:

                                br_string += ")"

                            elif (z[k] in "+-*/") and (d == 0):

                                br_string += z[k]
                                if (z[k] in "+-") and (case_type == 0):

                                    case_type = 1

                                elif (z[k] in "+-") and (case_type == 1):

                                    pass

                                elif (z[k] in "*/") and (case_type == 0):

                                    case_type = 2

                                elif (z[k] in "*/") and (case_type == 2):

                                    pass

                                else:

                                    case_type = 3

                            else:

                                br_string += z[k]

                            k+=1

                        br_string += ")"
                        #print(br_string, "no constant case_type = "+str(case_type))
                        k+=1
                        if (z[k] == "^"):

                            if (case_type == 0) or (case_type == 1) or (case_type == 3):

                                print("no redundant brackets found")

                            else:

                                br_string += "^"+z[k+1]
                                new_br_string = ""
                                i = 1
                                m = br_string.find(")^")
                                d=0
                                max=0
                                while i != m:

                                    if br_string[i] == "(":

                                        d+=1

                                        if d > max:

                                            max = d

                                    elif br_string[i] == ")":

                                        d-=1

                                    new_br_string += br_string[i]
                                    i+=1

                                if max <= 1 :

                                    #print("\n"+new_br_string)
                                    new_br_string = new_br_string.replace(")",")^"+z[k+1])
                                    eqn_string = stringify(z)
                                    #print(eqn_string)
                                    eqn_string = eqn_string.replace(br_string, new_br_string)
                                    #print(eqn_string)
                                    eqn_temp = Equation(eqn_string)
                                    #print(stringify(self.lhs) + " = " + stringify(self.rhs), stringify(z))
                                    setattr(self, side, eqn_temp.eqn)
                                    z = getattr(self, side)
                                    #print(stringify(self.lhs)+" = "+stringify(self.rhs), stringify(z))
                                    eqn_temp = None
                                    s=0

                                else:

                                    eqn_string = stringify(z)
                                    new_br_string = ""
                                    m = br_string.find(")^")
                                    br_string = br_string.replace("^"+z[k+1], '')
                                    i = m-1
                                    d=0
                                    while i != 1:

                                        if br_string[i] == ")":

                                            d+=1

                                        elif br_string[i] == "(":

                                            d-=1

                                        if d <= 1:

                                            new_br_string = br_string[i] + new_br_string

                                        else:

                                            new_new_br_string = new_br_string.replace(")",")^"+z[k+1])
                                            br_string_prime = br_string.replace(new_br_string, new_new_br_string)
                                            #print(eqn_string)
                                            eqn_string = eqn_string.replace(br_string+"^"+z[k+1], br_string_prime)
                                            #print(eqn_string)
                                            new_br_string = br_string_prime
                                            i-=1
                                            while d != 0:
                                                #print(i, d, br_string[i])
                                                if br_string[i] == ")":

                                                    d+=1

                                                elif br_string[i] == "(":

                                                    d-=1

                                                i-=1

                                            new_br_string = br_string[i]

                                        i-=1

                                    #print("\n"+new_br_string)
                                    new_new_br_string = new_br_string.replace(")",")^"+z[k+1])
                                    br_string_prime = br_string.replace(new_br_string, new_new_br_string)
                                    #print(eqn_string)
                                    #print("BOO", br_string, new_br_string, new_new_br_string, br_string_prime)
                                    eqn_string = eqn_string.replace(br_string+"^"+z[k+1], br_string_prime)
                                    #print(eqn_string)
                                    eqn_temp = Equation(eqn_string)
                                    setattr(self, side, eqn_temp.eqn)
                                    z = getattr(self, side)
                                    eqn_temp = None
                                    s=0

                        elif (z[k] in "/*"):

                            print("no redundant brackets found")

                        else:

                            if case_type == 1:

                                print("no redundant brackets found")

                            else:

                                new_br_string = ""
                                for i in range(1,len(br_string)-1):

                                    new_br_string += br_string[i]

                                eqn_string = stringify(z)
                                #print(eqn_string)
                                eqn_string = eqn_string.replace(br_string, new_br_string)
                                #print(eqn_string)
                                eqn_temp = Equation(eqn_string)
                                setattr(self, side, eqn_temp.eqn)
                                z = getattr(self, side)
                                eqn_temp = None
                                s = 0
                    s += 1

            if (z[1] == "(2") and (z[-2] == ")2"):

                s=1
                d=0
                chk_var = False
                while s != len(side)-2:

                    if z[s] == ")2":

                        chk_var = True
                        break

                    s+=1

                if chk_var == False:

                    del z[-2]
                    del z[1]

            #setattr(self, side, eqn_temp.eqn)

    def bracket_remover(self):
        """Function removes all brackets by performing various operations to make expressions mathematically equivalent."""
        eqn_parts = ["lhs", "rhs"]
        for side in eqn_parts:
            b=0
            z = getattr(self, side)
            for s in z:

                if "(" in s:

                    temp = s
                    temp = temp.replace("(","")
                    temp = int(temp)

                    if temp > b:

                        b = temp

            for c in range(b,1,-1):

                s = 0
                while s != len(z):

                    if (is_number(z[s]) == True) and (z[s-1] == "^") and (z[s-2] == ")"+str(c)):

                        x = float(z[s])
                        k = s-2
                        d=0
                        br_string=""
                        while z[k] != "("+str(c):

                            if ")" in z[k]:

                                br_string = ")"+br_string
                                d+=1

                            elif "(" in z[k]:

                                br_string = "("+br_string
                                d-=1

                            else:

                                if (z[k-1] == ")"+str(c+1)) and (z[k] in "+-") and (z[k+1] == "("+str(c+1)):

                                    break

                                else:

                                    br_string = z[k]+br_string

                            k-=1

                        br_string = "("+br_string
                        #print("\n"+br+"^"+str(x))
                        br = Equation(br_string)
                        bra = br.eqn
                        br = None
                        del bra[0]
                        del bra[-1]
                        #print(bra)

                        if x > 1.0:

                            new_br = exp_foiling(bra, x, self.var_type[0])
                            #print(new_br)
                            new_br_string = stringify(new_br)
                            print("= "+new_br_string)
                            eqn_string = stringify(z)
                            eqn_string = eqn_string.replace(br_string+"^"+str(x), "("+new_br_string+")")
                            eqn_temp = Equation(eqn_string)
                            # if eqn_temp.var_type[0]:
                            #
                            #         self.var = eqn_temp.var_type[0]
                            setattr(self, side, eqn_temp.eqn)
                            z = getattr(self, side)
                            eqn_temp = None
                            s=-1

                    s+=1

                #Now to check for ()*() or c*() or ()*c
                s=0
                while s != len(z):

                    if (z[s] == "("+str(c)) and (z[s-1] == "*") and (z[s-2] == ")"+str(c)):

                        br_string_one = ""
                        br_string_two = ""
                        k = s
                        m = s-2

                        check_two = False
                        d=0
                        while z[k] != ")"+str(c):

                            if "(" in z[k]:

                                br_string_two += "("
                                d+=1

                            elif ")" in z[k]:

                                br_string_two += ")"
                                d-=1

                            else:

                                if (z[k-1] == ")"+str(c+1)) and (z[k] in "+-") and (z[k+1] == "("+str(c+1)):

                                    check_two = True
                                    break

                                else:

                                    br_string_two += z[k]

                            k+=1

                        br_string_two += ")"
                        check_one = False
                        d=0
                        while z[m] != "("+str(c):

                            if ")" in z[m]:

                                br_string_one = ")"+br_string_one
                                d+=1

                            elif "(" in z[m]:

                                br_string_one = "("+br_string_one
                                d-=1

                            else:

                                if (z[m-1] == ")"+str(c+1)) and (z[m] in "+-") and (z[m+1] == "("+str(c+1)):

                                    check_one = True
                                    break

                                else:

                                    br_string_one = z[m]+br_string_one

                            m-=1

                        if (check_one == False) and (check_two == False):

                            br_string_one = "("+br_string_one
                            print("\n"+br_string_one+"*"+br_string_two)

                            br_one = Equation(br_string_one)
                            del br_one.eqn[0]
                            del br_one.eqn[-1]

                            br_two = Equation(br_string_two)
                            del br_two.eqn[0]
                            del br_two.eqn[-1]

                            br = foiling(br_one.eqn, br_two.eqn, self.var_type[0])
                            br_one, br_two = None, None

                            if not br:

                                br = ["0"]

                            br.insert(0,"(1")
                            br.append(")1")
                            br_string = stringify(br)
                            print("= "+br_string)

                            eqn_string = stringify(z)
                            eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
                            eqn_temp = Equation(eqn_string)
                            # if var:
                            #
                            #     self.var = var[0]

                            setattr(self, side, eqn_temp.eqn)
                            z = getattr(self, side)
                            eqn_temp = None
                            s=-1

                    elif ((is_number(z[s]) == True) or (self.var_type[0] in z[s])) and (z[s-1] == "*") and (z[s-2] == ")"+str(c)):

                        #print("WOOAAHH NELLY")
                        br_string_one = ""
                        br_string_two = z[s]
                        k = s
                        m = s-2

                        check_one = False
                        d=0
                        while z[m] != "("+str(c):

                            if ")" in z[m]:

                                br_string_one = ")"+br_string_one
                                d+=1

                            elif "(" in z[m]:

                                br_string_one = "("+br_string_one
                                d-=1

                            else:

                                if (z[m-1] == ")"+str(c+1)) and (z[m] in "+-") and (z[m+1] == "("+str(c+1)):

                                    check_one = True
                                    break

                                else:

                                    br_string_one = z[m]+br_string_one

                            m-=1

                        if check_one == False:

                            #br_string_one = "("+br_string_one+")"
                            print("\n"+br_string_one+"*"+br_string_two)

                            br_one = Equation(br_string_one)
                            del br_one.eqn[0]
                            del br_one.eqn[-1]

                            br_two = Equation(br_string_two)
                            del br_two.eqn[0]
                            del br_two.eqn[-1]

                            br = foiling(br_one.eqn, br_two.eqn, self.var_type[0])
                            br_one, br_two = None, None
                            if not br:

                                br = ["0"]

                            br.insert(0,"(1")
                            br.append(")1")
                            br_string = stringify(br)
                            print("= "+br_string)

                            eqn_string = stringify(z)
                            eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
                            eqn_temp = Equation(eqn_string)
                            # if var:
                            #
                            #     self.var = var[0]
                            setattr(self, side, eqn_temp.eqn)
                            z = getattr(self, side)
                            eqn_temp = None
                            s=-1

                    elif (z[s] == "("+str(c)) and (z[s-1] == "*") and ((is_number(z[s-2]) == True) or (self.var_type[0] in z[s-2])):

                        #print("WOOAAHH NELLY")
                        br_string_one = z[s-2]
                        br_string_two = ""
                        k = s
                        m = s-2

                        check_two = False
                        d=0
                        while z[k] != ")"+str(c):

                            if "(" in z[k]:

                                br_string_two += "("
                                d+=1

                            elif ")" in z[k]:

                                br_string_two += ")"
                                d-=1

                            else:

                                if (z[k-1] == ")"+str(c+1)) and (z[k] in "+-") and (z[k+1] == "("+str(c+1)):

                                    check_two = True
                                    break

                                else:

                                    br_string_two += z[k]

                            k+=1

                        br_string_two += ")"

                        if check_two == False:

                            #br_string_one = "("+br_string_one+")"
                            print("\n"+br_string_one+"*"+br_string_two)

                            br_one = Equation(br_string_one)
                            br_two = Equation(br_string_two)

                            br = foiling(br_one.eqn, br_two.eqn, self.var_type[0])

                            if not br:

                                br = ["0"]

                            br.insert(0,"(1")
                            br.append(")1")
                            br_string = stringify(br)
                            print("= "+br_string)

                            eqn_string = stringify(z)
                            eqn_string = eqn_string.replace(br_string_one+"*"+br_string_two, "("+br_string+")")
                            eqn_temp = Equation(eqn_string)
                            # if var:
                            #
                            #     self.var = var[0]
                            setattr(self, side, eqn_temp.eqn)
                            z = getattr(self, side)
                            s=-1

                    s+=1

                #Now to check for ()+-()
                s=0
                while s != len(z):

                    if (z[s] == "("+str(c)) and (z[s-1] in "+-") and (z[s-2] == ")"+str(c)):

                        br_string_one = ""
                        br_string_two = ""
                        op = z[s-1]
                        k = s
                        m = s-2

                        check_two = False
                        d=0
                        while z[k] != ")"+str(c):

                            if "(" in z[k]:

                                br_string_two += "("
                                d+=1

                            elif ")" in z[k]:

                                br_string_two += ")"
                                d-=1

                            else:

                                if (z[k-1] == ")"+str(c+1)) and (z[k] in "+-") and (z[k+1] == "("+str(c+1)):

                                    check_two = True
                                    break

                                else:

                                    br_string_two += z[k]

                            k+=1

                        br_string_two += ")"
                        check_one = False
                        d=0
                        while z[m] != "("+str(c):

                            if ")" in z[m]:

                                br_string_one = ")"+br_string_one
                                d+=1

                            elif "(" in z[m]:

                                br_string_one = "("+br_string_one
                                d-=1

                            else:

                                if (z[m-1] == ")"+str(c+1)) and (z[m] in "+-") and (z[m+1] == "("+str(c+1)):

                                    check_one = True
                                    break

                                else:

                                    br_string_one = z[m]+br_string_one

                            m-=1

                        if (check_one == False) and (check_two == False):

                            br_string_one = "("+br_string_one
                            print("\n"+br_string_one+op+br_string_two)

                            br_one = Algebra(br_string_one+"=0")
                            br_one.get_coeff()
                            del br_one.eqn[0]
                            del br_one.eqn[-1]

                            br_two = Algebra(br_string_two+"=0")
                            br_two.get_coeff()
                            del br_two.eqn[0]
                            del br_two.eqn[-1]

                            br = bracket_add(br_one.coeff, op, br_two.coeff, self.var_type[0])

                            if not br:

                                br = ["0"]

                            br.insert(0,"(1")
                            br.append(")1")
                            br_string = stringify(br)
                            print("= "+br_string)

                            eqn_string = stringify(z)
                            eqn_string = eqn_string.replace(br_string_one+op+br_string_two, "("+br_string+")")
                            eqn_temp = Equation(eqn_string)
                            # if var:
                            #
                            #     self.var = var[0]
                            setattr(self, side, eqn_temp.eqn)
                            z = getattr(self, side)
                            s=-1

                    s+=1

                #print("before redundant_br", self.eqn)
                self.redundant_br()
                #print("after redundant_br", self.eqn)
                eqn_string = stringify(z)
                print(eqn_string)

    def multiply_br(self, divers: List[List[str]]):
        """Method takes divisors and multiplies them into an equation."""
        div_copy = copy.deepcopy(divers)
        #print("At the beginning",self.eqn, div_copy)
        #First determine the highest bracket level
        eqn_parts = ["lhs", "rhs"]
        for side in eqn_parts:
            z = getattr(self, side)
            b=0
            for s in z:

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
                while s != len(z):

                    if "(" in z[s]:

                        d+=1

                    elif ")" in z[s]:

                        d-=1

                    if ((is_number(z[s])) or (self.var_type[0] in z[s])) and (d == 1):

                        s+=1
                        z.insert(s,"*")
                        s+=1
                        for n in range(len(i)-1,-1,-1):

                            z.insert(s,i[n])

                        d=1
                        s+=len(i)
                        #print(self.eqn, s)

                        while z[s] != ")1":

                            if "(" in z[s]:

                                d+=1

                            elif ")" in z[s]:

                                d-=1

                            if (z[s] in "+-") and (d == 1):

                                break

                            s+=1

                        if s == len(z)-1:

                            s-=1

                        #print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

                    elif z[s] == "(2":

                        z.insert(s,"*")
                        for n in range(len(i)-1,-1,-1):

                            z.insert(s,i[n])

                        d=1
                        s+=len(i)
                        #print(self.eqn, s)

                        while z[s] != ")1":

                            if "(" in z[s]:

                                d+=1

                            elif ")" in z[s]:

                                d-=1

                            if (z[s] in "+-") and (d == 1):

                                break

                            s+=1

                        if s == len(z)-1:

                            s-=1

                    s+=1

                temp = i[:]
                temp.insert(0,"(1")
                temp.append(")1")
                div_string.append(stringify(temp))

            eqn_string = stringify(z)
            print(eqn_string)

            for c in range(2,b):

                for i in div_copy:

                    #need to find divisor outside of "("+str(c), then need to delete it and multiply it into all terms inside of "("+str(c)
                    #print("inside multiply_br", i)
                    s = 0
                    while s != len(z):

                        if z[s] == i[0]:

                            k = s
                            #print(k, self.eqn[s], i[0])
                            k+=1
                            eqn_chk = True
                            for n in range(1,len(i)):

                                if z[k] != i[n]:

                                    #print(k, self.eqn[k], i[n])
                                    eqn_chk = False
                                    break

                                else:

                                    #print(k, self.eqn[k], i[n])
                                    k+=1

                            #print("k = "+str(k), self.eqn[k])
                            if eqn_chk:

                                #print(k, self.eqn[k])
                                if z[k] == "*":

                                    k+=1
                                    if z[k] == "("+str(c):

                                        m = k
                                        while z[m] != ")"+str(c):

                                            m+=1


                                        if z[m+1] == "^":
                                            #print("GREEN HELL", m+2, z[m+2], z)
                                            x = 1/float(z[m+2])
                                            n=0
                                            exp_chk = False
                                            while n != len(i):

                                                if i[n] == "^":

                                                    if float(i[n+1])*x > 1:

                                                        i[n+1] = str(float(i[n+1])*x)
                                                        exp_chk = True

                                                    else:

                                                        eqn_chk = False

                                                    break

                                                n+=1

                                            if not exp_chk:

                                                if x > 1:

                                                    i.insert(len(i), "^")
                                                    i.insert(len(i), str(x))

                                                else:

                                                    eqn_chk = False

                                        if eqn_chk:

                                            #print("Found one: ", k, self.eqn[k])
                                            del z[s:k]
                                            #print(self.eqn, s, self.eqn[s])
                                            break

                                        else:

                                            s = k

                        s+=1

                    d = 0
                    #print(s, self.eqn[s], self.eqn, i)
                    while s != len(z):

                        if "(" in z[s]:

                            d+=1

                        elif ")" in z[s]:

                            d-=1

                        if ((is_number(z[s])) or (self.var_type[0] in z[s])) and (d == 1):

                            s+=1
                            z.insert(s,"*")
                            s+=1
                            for n in range(len(i)-1,-1,-1):

                                if "(" in i[n]:

                                    z.insert(s,"("+str(c+1))

                                elif ")" in i[n]:

                                    z.insert(s,")"+str(c+1))

                                else:

                                    z.insert(s,i[n])

                            s+=len(i)-2
                            d=1
                            #print(self.eqn, s)

                            while z[s] != ")1":

                                if "(" in z[s]:

                                    d+=1

                                elif ")" in z[s]:

                                    d-=1

                                if (z[s] in "+-") and (d == 1):

                                    break

                                s+=1

                            if s == len(z)-1:

                                s-=1

                            #print("k = "+str(k), "len(l)-1 = "+str(len(l)-1))

                        elif z[s] == "("+str(c+1):

                            #print("d = "+str(d), self.eqn[s], s)
                            z.insert(s,"*")
                            for n in range(len(i)-1,-1,-1):

                                if "(" in i[n]:

                                    z.insert(s,"("+str(c+1))

                                elif ")" in i[n]:

                                    z.insert(s,")"+str(c+1))

                                else:

                                    z.insert(s,i[n])

                            s+=len(i)
                            d=1
                            #print("here",s, self.eqn[s], self.eqn)

                            while z[s] != ")1":

                                if "(" in z[s]:

                                    d+=1

                                elif ")" in z[s]:

                                    d-=1

                                if (z[s] in "+-") and (d == 1):

                                    break

                                s+=1

                            if s == len(z)-1:

                                s-=1

                        s+=1

            eqn_string = stringify(z)
            print(eqn_string)

    def redundant_div(self, divisors: List[List[str]]):
        """Removes any ()/() = 1 expressions"""
        eqn_parts = ["lhs", "rhs"]
        for side in eqn_parts:
            z = getattr(self, side)
            #First determine the highest bracket level
            b=0
            for s in z:

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
                    while s != len(z):

                        if "("+str(c-1) == z[s]:

                            br=[]
                            k = s
                            while z[k] != ")"+str(c-1):

                                br.append(z[k])
                                k+=1

                            br.append(z[k])
                            #print(br[0] != "(1", br[-1] != ")1", br)
                            if (br[0] != "(1") and (br[-1] != ")1"):

                                br.insert(0,"(1")
                                br.append(")1")

                            br_string = stringify(br)

                            if k != len(z)-1:

                                #print("REEEEEE", br_string, k+1, self.eqn[k+1], self.eqn)
                                if z[k+1] == "^":

                                    x = 1/float(z[k+2])
                                    n=0
                                    exp_chk = False
                                    while n != len(i):

                                        if i[n] == "^":

                                            i[n+1] = str(float(i[n+1])*x)
                                            exp_chk = True

                                        n+=1

                                    if exp_chk == False:

                                        i.insert(len(i), "^")
                                        i.insert(len(i), str(x))

                        s+=1

                i.insert(0,"(1")
                i.append(")1")
                div_string.append(stringify(i))


            #print("voila",div_string)

            for i in div_string:

                for c in range(b,1,-1):

                    #print("does it even get this far")
                    s=0
                    while s != len(z):

                        if z[s] == "("+str(c-1):

                            k = s+1
                            d=0
                            br = ""
                            while z[k] != ")"+str(c-1):

                                if "(" in z[k]:

                                    br+="("
                                    d+=1

                                elif ")" in z[k]:

                                    br+=")"
                                    d-=1

                                else:

                                    if (z[k] in "+-") and (d==0):

                                        #print(br)
                                        if ("/"+i in br) and (i+"*" in br):

                                            eqn_string = stringify(z)
                                            new_br = br.replace(i+"*","")
                                            new_br = new_br.replace("/"+i,'')
                                            eqn_string = eqn_string.replace(br,new_br)
                                            eqn_temp = Equation(eqn_string)
                                            setattr(self, side, eqn_temp.eqn)
                                            z = getattr(self, side)
                                            eqn_temp = None
                                            s=0

                                        else:

                                            br=""

                                    else:

                                        br+=z[k]

                                k+=1

                            #print(br)
                            eqn_string = stringify(z)
                            if ("/"+i in br) and (i+"*" in br):

                                new_br = br.replace(i+"*","")
                                new_br = new_br.replace("/"+i,'')
                                eqn_string = eqn_string.replace(br,new_br)
                                eqn_temp = Equation(eqn_string)
                                setattr(self, side, eqn_temp.eqn)
                                z = getattr(self, side)
                                eqn_temp = None
                                s=0

                        s+=1

    def find_asymptotes(self, divisors: [str]) -> List[Union[int, float, complex]]:
        """Functions takes array of divisors and returns asymptotes."""
        asymptotes = []
        for i in divisors:

            temp = i
            s = 0
            while s != len(temp):

                if (is_number(temp[s]) == True) and (temp[s - 1] == "^") and (temp[s - 2] == ")2"):

                    del temp[s - 1:s + 1]
                    temp.insert(0, "(1")
                    temp.append(")1")
                    temp_string = stringify(temp)
                    temp = Algebra(temp_string+"=0")
                    temp.redundant_br()
                    temp.rearrange()
                    ans = temp.solver()

                    if ans[0] not in asymptotes:
                        asymptotes.append(ans[0])

                    temp = None
                    break

                elif (temp[s] != "^") and (temp[s - 1] == ")2"):

                    temp.insert(0, "(1")
                    temp.append(")1")
                    temp_string = stringify(temp)
                    temp = Algebra(temp_string+"=0")
                    temp.redundant_br()
                    temp.rearrange()
                    ans = temp.solver()

                    if ans[0] not in asymptotes:
                        asymptotes.append(ans[0])

                    temp = None
                    break

                s += 1

        return asymptotes

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
        eqn_og = Algebra(self.eqn_string)
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
        r_new, bracket_dict = bracketing(self.rhs, self.var_type, bracket_dict)
        #print(stringify(l_new)+" = "+stringify(r_new), self.var_type)
        s = 0
        while s == 0:

            br = stringify(r_new)
            length = len(br)
            if br in bracket_dict:

                del r_new[1:length + 1]
                r_new.insert(1, bracket_dict[br])

            else:

                s = 1

        new_eqn_string = stringify(l_new)+"="+stringify(r_new)
        new_eqn = Algebra(new_eqn_string)
        print(new_eqn.eqn_string)
        # Lets take note of the variables in l and r now
        work_var_l = []
        work_var_r = []
        for var in bracket_dict.values():

            for i, j in zip(new_eqn.lhs, new_eqn.rhs):

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

                    ans = solving(new_eqn)

                else:

                    # solve and keep resubbing
                    while work_var != self.var_type[0]:

                        if any(isinstance(sub, list) for sub in new_eqn.rhs) == True:

                            ans = []
                            for i in new_eqn.rhs:
                                temp_string = stringify(new_eqn.lhs)+"="+stringify(i)
                                temp_eqn = Algebra(temp_string)
                                ans_temp = solving(temp_eqn)
                                ans.append(ans_temp)
                                temp_eqn = None
                        else:

                            ans = solving(new_eqn)

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

                        new_eqn.rhs = []
                        for i in ans:
                            print(l_new_string + " = " + str(i))
                            temp = Equation(str(i))
                            new_eqn.rhs.append(temp.eqn)
                            temp = None

                        l_new_obj = Equation(l_new_string)
                        new_eqn.lhs, work_var = l_new_obj.eqn, l_new_obj.var_type[0]
                        l_new_obj = None

            else:

                # Now we should check if the variables are one character apart. Ex: z and a or a and b
                if (work_var_l[0] == var_dict[work_var_r[0]]):
                    print("This one")
                    #print(work_var_l[0], var_dict[work_var_r[0]])
                    for x in bracket_dict:

                        if bracket_dict[x] == work_var_l[0]:
                            sub = x

                    #print("we here one", sub)
                    br = stringify(new_eqn.lhs)
                    br = br.replace(work_var_l[0], "(" + sub + ")")
                    #print(br)
                    l_new_obj = Equation(br)
                    new_eqn.lhs, work_var = l_new_obj.eqn, l_new_obj.var_type[0]
                    new_eqn.update_attr()
                    l_new_obj = None
                    #print(new_eqn.lhs)

                    # solve and keep resubbing
                    while (new_eqn.lhs[1] != self.var_type[0]) and (len(new_eqn.lhs) != 3):

                        if any(isinstance(sub, list) for sub in new_eqn.rhs) == True:

                            l_new_string = stringify(new_eqn.lhs)
                            l_new_obj = Equation(l_new_string)
                            new_eqn.lhs, work_var = l_new_obj.eqn, l_new_obj.var_type[0]
                            new_eqn.update_attr()
                            l_new_obj = None

                            ans = []
                            for i in new_eqn.rhs:
                                temp_string = l_new_string+"="+stringify(i)
                                temp_eqn = Algebra(temp_string)
                                ans_temp = solving(temp_eqn)
                                ans.append(ans_temp)
                                temp_eqn = None
                        else:

                            ans = solving(new_eqn)

                        l_new_string = work_var
                        #print("bottle caps", l_new_string, ans)
                        new_eqn.rhs = []

                        if any(isinstance(sub, list) for sub in ans) == True:

                            for i in ans:
                                print(work_var + " = " + str(i[0]))
                                r_temp = Equation(str(i[0]))
                                new_eqn.rhs.append(r_temp.eqn)
                                r_temp = None

                        else:

                            for i in ans:
                                print(work_var[0] + " = " + str(i))
                                r_temp = Equation(str(i))
                                new_eqn.rhs.append(r_temp.eqn)
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
                        new_eqn.lhs, work_var = l_new_obj.eqn, l_new_obj.var_type[0]
                        l_new_obj = None

                elif (work_var_r[0] == var_dict[work_var_l[0]]):
                    print("That one")
                    for x in bracket_dict:

                        if bracket_dict[x] == work_var_r[0]:
                            sub = x

                    print("we here one", sub)
                    br = stringify(new_eqn.rhs)
                    br = br.replace(work_var_r[0], "(" + sub + ")")
                    print(br)

                else:

                    ans = solving(eqn_og)

                    l_new_obj = Equation(self.var_type[0])
                    new_eqn.lhs, l_var = l_new_obj.eqn, l_new_obj.var_type[0]
                    l_new_obj = None

                    new_eqn.rhs = []
                    for i in ans:
                        temp = Equation(str(i))
                        new_eqn.rhs.append(temp.eqn)
                        temp = None
        else:

            # print(l_og_string+" = "+r_og_string)

            ans = solving(eqn_og)

            l_new_obj = Equation(self.var_type[0])
            new_eqn.lhs, l_var = l_new_obj.eqn, l_new_obj.var_type[0]
            l_new_obj = None
            new_eqn.rhs = []
            for i in ans:
                temp = Equation(str(i))
                new_eqn.rhs.append(temp.eqn)
                temp = None

        print("Made it to the end", "l", "r")

        return new_eqn.lhs, new_eqn.rhs

    def rearrange(self):
        """
        Function takes LHS and RHS, moves all variables to LHS, constants to RHS and combines all similar terms.
        Equation must be rid of all brackets, and in proper polynomial format to use. Returns rearranged LHS and RHS.
        """

        """TO-DO: Add a check to ensure LHS and RHS inputs are of proper format."""
        # First all variable terms must go from RHS to LHS
        var = self.var_type[0]
        s = 0
        while s != len(self.rhs):

            if var in self.rhs[s]:

                if not is_complex_coeff(self.rhs[s], var):

                    if "-" in self.rhs[s]:

                        if self.rhs[s - 1] == "-":

                            self.lhs.insert(-1, "-")
                            temp = self.rhs[s]
                            temp = temp.replace("-", '')
                            self.lhs.insert(-1, temp)
                            del self.rhs[s - 1:s + 1]

                        else:

                            self.lhs.insert(-1, "+")
                            temp = self.rhs[s]
                            temp = temp.replace("-", '')
                            self.lhs.insert(-1, temp)

                            if s == 1:

                                del self.rhs[s]

                            else:

                                del self.rhs[s - 1:s + 1]

                    else:

                        if self.rhs[s - 1] == "-":

                            self.lhs.insert(-1, "+")
                            self.lhs.insert(-1, self.rhs[s])
                            del self.rhs[s - 1:s + 1]

                        else:

                            self.lhs.insert(-1, "-")
                            self.lhs.insert(-1, self.rhs[s])

                            if s == 1:

                                del self.rhs[s]

                            else:

                                del self.rhs[s - 1:s + 1]

                else:

                    if self.rhs[s - 1] == "-":

                        self.lhs.insert(-1, "+")
                        self.lhs.insert(-1, self.rhs[s])
                        del self.rhs[s - 1:s + 1]

                    else:

                        self.lhs.insert(-1, "-")
                        self.lhs.insert(-1, self.rhs[s])

                        if s == 1:

                            del self.rhs[s]

                        else:

                            del self.rhs[s - 1:s + 1]

                s = -1

            s += 1

        # print(l, r)
        # Now we will take out any unnecessary operation signs from RHS and Also if the second element of LHS is a term with a negative inside, then we will make two indexes
        # First RHS
        if self.rhs[1] == "+":

            del self.rhs[1]

        elif self.rhs[1] == "-":

            del self.rhs[1]
            if not is_complex_coeff(self.rhs[1], var):
                self.rhs[1] = self.rhs[1].replace(self.rhs[1], "-" + self.rhs[1])

        elif (self.rhs[0] == "(1") and (self.rhs[1] == ")1"):

            self.rhs.insert(1, "0")

        if "-" in self.rhs[1]:

            if not is_complex_coeff(self.rhs[1], var):
                self.rhs[1] = self.rhs[1].replace("-", '')
                self.lhs.insert(1, "-")

        print(stringify(self.lhs)+"="+stringify(self.rhs))
        # Now we move constants from LHS to RHS
        s = 0
        while s != len(self.lhs):

            if is_number(self.lhs[s]):

                if not is_complex_coeff(self.lhs[s], var):

                    if "-" in self.lhs[s]:

                        if self.lhs[s - 1] == "-":

                            self.rhs.insert(-1, "-")
                            temp = self.lhs[s]
                            temp = temp.replace("-", '')
                            self.rhs.insert(-1, temp)
                            del self.lhs[s - 1:s + 1]

                        else:

                            self.rhs.insert(-1, "+")
                            temp = self.lhs[s]
                            temp = temp.replace("-", '')
                            self.rhs.insert(-1, temp)

                            if s == 1:

                                del self.lhs[s]

                            else:

                                del self.lhs[s - 1:s + 1]

                    else:

                        if self.lhs[s - 1] == "-":

                            self.rhs.insert(-1, "+")
                            self.rhs.insert(-1, self.lhs[s])
                            del self.lhs[s - 1:s + 1]

                        else:

                            self.rhs.insert(-1, "-")
                            self.rhs.insert(-1, self.lhs[s])

                            if s == 1:

                                del self.lhs[s]

                            else:

                                del self.lhs[s - 1:s + 1]

                else:

                    if self.lhs[s - 1] == "-":

                        self.rhs.insert(-1, "+")
                        self.rhs.insert(-1, self.lhs[s])
                        del self.lhs[s - 1:s + 1]

                    else:

                        self.rhs.insert(-1, "-")
                        self.rhs.insert(-1, self.lhs[s])

                        if s == 1:

                            del self.lhs[s]

                        else:

                            del self.lhs[s - 1:s + 1]

                s = -1

            s += 1

        # print(l,r)
        # Now we need to establish all the powers of x on LHS and store them in an array called l_deg
        l_deg = []
        for s in self.lhs:

            if var + "^" in s:

                temp = s
                x = ""
                k = 0
                while temp[k] != "^":
                    k += 1

                k += 1
                while k != len(temp):
                    x += temp[k]
                    k += 1

                if x not in l_deg:
                    l_deg.append(x)

            elif (var in s) and ("^" not in s):

                x = "1.0"

                if x not in l_deg:
                    l_deg.append(x)

        # print(l_deg)
        # Now to put all the terms in l_deg in numerical order
        l_deg_ordered = []
        for s in l_deg:

            if not l_deg_ordered:

                l_deg_ordered.append(s)

            else:

                if float(s) > float(l_deg_ordered[0]):

                    if s not in l_deg_ordered:
                        l_deg_ordered.insert(0, s)

                else:

                    if s not in l_deg_ordered:

                        k = 0
                        while k != len(l_deg_ordered):

                            if (float(s) > float(l_deg_ordered[k])) and (s not in l_deg_ordered):
                                l_deg_ordered.insert(k, s)

                            k += 1

                        if s not in l_deg_ordered:
                            l_deg_ordered.append(s)

            # print(l_deg_ordered)

        rear_l = []
        for i in l_deg_ordered:

            for s in range(0, len(self.lhs)):

                if var + "^" + i in self.lhs[s]:

                    if not is_complex_coeff(self.lhs[s], var):

                        if "-" in self.lhs[s]:

                            if self.lhs[s - 1] == "-":

                                if not rear_l:

                                    temp = self.lhs[s]
                                    temp = temp.replace("-", '')
                                    rear_l.append(temp)

                                else:

                                    rear_l.append("+")
                                    temp = self.lhs[s]
                                    temp = temp.replace("-", '')
                                    rear_l.append(temp)

                            else:

                                if not rear_l:

                                    rear_l.append(self.lhs[s])

                                else:

                                    rear_l.append("-")
                                    temp = self.lhs[s]
                                    temp = temp.replace("-", '')
                                    rear_l.append(temp)

                        else:

                            if self.lhs[s - 1] == "-":

                                if not rear_l:

                                    rear_l.append("-" + self.lhs[s])

                                else:

                                    rear_l.append("-")
                                    rear_l.append(self.lhs[s])

                            else:

                                if not rear_l:

                                    rear_l.append(self.lhs[s])

                                else:

                                    rear_l.append("+")
                                    rear_l.append(self.lhs[s])

                    else:

                        if self.lhs[s - 1] == "-":

                            if not rear_l:

                                rear_l.append("-" + self.lhs[s])

                            else:

                                rear_l.append("-")
                                rear_l.append(self.lhs[s])

                        else:

                            if not rear_l:

                                rear_l.append(self.lhs[s])

                            else:

                                rear_l.append("+")
                                rear_l.append(self.lhs[s])


                elif (i == "1.0") and (var in self.lhs[s]) and ("^" not in self.lhs[s]):

                    if not is_complex_coeff(self.lhs[s], var):

                        if "-" in self.lhs[s]:

                            if self.lhs[s - 1] == "-":

                                if not rear_l:

                                    temp = self.lhs[s]
                                    temp = temp.replace("-", '')
                                    rear_l.append(temp)

                                else:

                                    rear_l.append("+")
                                    temp = self.lhs[s]
                                    temp = temp.replace("-", '')
                                    rear_l.append(temp)

                            else:

                                if not rear_l:

                                    rear_l.append(self.lhs[s])

                                else:

                                    rear_l.append("-")
                                    temp = self.lhs[s]
                                    temp = temp.replace("-", '')
                                    rear_l.append(temp)

                        else:

                            if self.lhs[s - 1] == "-":

                                if not rear_l:

                                    rear_l.append("-" + self.lhs[s])

                                else:

                                    rear_l.append("-")
                                    rear_l.append(self.lhs[s])

                            else:

                                if not rear_l:

                                    rear_l.append(self.lhs[s])

                                else:

                                    rear_l.append("+")
                                    rear_l.append(self.lhs[s])

                    else:

                        if self.lhs[s - 1] == "-":

                            if not rear_l:

                                rear_l.append("-" + self.lhs[s])

                            else:

                                rear_l.append("-")
                                rear_l.append(self.lhs[s])

                        else:

                            if not rear_l:

                                rear_l.append(self.lhs[s])

                            else:

                                rear_l.append("+")
                                rear_l.append(self.lhs[s])

        rear_l.insert(0, "(1")
        rear_l.append(")1")
        # print(rear_l)
        # l_string = stringify(rear_l)
        # l_string = l_string.replace(".0",'')
        # l_string = l_string.replace("-"," - ")
        # l_string = l_string.replace("+"," + ")
        # print(l_string)
        # Now we combine all similar terms
        for i in l_deg_ordered:

            s = 0
            while s != len(rear_l):

                if var + "^" + i in rear_l[s]:

                    if s != 1:

                        if (rear_l[s - 1] in "+-") and (var + "^" + i in rear_l[s - 2]):

                            term_one = rear_l[s - 2]

                            if not is_complex_coeff(term_one, var):

                                if rear_l[s - 3] == "-":

                                    if "-" not in term_one:
                                        rear_l[s - 3] = "+"
                                        term_one = "-" + term_one

                            op = rear_l[s - 1]
                            term_two = rear_l[s]

                            term_one = term_one.replace(var + "^" + i, '')
                            term_two = term_two.replace(var + "^" + i, '')

                            if term_one == "":

                                term_one = "1.0"

                            elif term_one == "-":

                                term_one = "-1.0"

                            if term_two == "":

                                term_two = "1.0"

                            elif term_two == "-":

                                term_two = "-1.0"

                            if op == "+":

                                new_term = complex(term_one) + complex(term_two)

                            elif op == "-":

                                new_term = complex(term_one) - complex(term_two)

                            else:

                                print("shits broken")

                            if new_term.imag == 0:

                                new_term = str(new_term.real)
                                if "-" in new_term:

                                    if s - 2 == 1:

                                        rear_l[s - 2] = new_term + var + "^" + i
                                        del rear_l[s - 1:s + 1]

                                    else:

                                        if rear_l[s - 3] == "-":

                                            rear_l[s - 3] = "+"
                                            new_term = new_term.replace("-", '')
                                            rear_l[s - 2] = new_term + var + "^" + i
                                            del rear_l[s - 1:s + 1]

                                        else:

                                            rear_l[s - 3] = "-"
                                            new_term = new_term.replace("-", '')
                                            rear_l[s - 2] = new_term + var + "^" + i
                                            del rear_l[s - 1:s + 1]

                                elif new_term == "0.0":

                                    if s - 2 == 1:

                                        del rear_l[s - 2:s + 1]

                                    else:

                                        del rear_l[s - 3:s + 1]

                                elif new_term == "1.0":

                                    rear_l[s - 2] = var + "^" + i
                                    del rear_l[s - 1:s + 1]

                                elif new_term == "-1.0":

                                    if s - 2 == 1:

                                        rear_l[s - 2] = "-" + var + "^" + i
                                        del rear_l[s - 1:s + 1]

                                    else:

                                        if rear_l[s - 3] == "-":

                                            rear_l[s - 3] = "+"
                                            rear_l[s - 2] = var + "^" + i
                                            del rear_l[s - 1:s + 1]

                                        else:

                                            rear_l[s - 3] = "-"
                                            rear_l[s - 2] = var + "^" + i
                                            del rear_l[s - 1:s + 1]

                                else:

                                    rear_l[s - 2] = new_term + var + "^" + i
                                    del rear_l[s - 1:s + 1]

                            else:

                                new_term = str(new_term)
                                rear_l[s - 2] = new_term + var + "^" + i
                                del rear_l[s - 1:s + 1]

                            s = -1

                elif (i == "1.0") and (var in rear_l[s]) and ("^" not in rear_l[s]):

                    if s != 1:

                        if (rear_l[s - 1] in "+-") and (var in rear_l[s - 2]) and ("^" not in rear_l[s - 2]):

                            term_one = rear_l[s - 2]

                            if not is_complex_coeff(term_one, var):

                                if rear_l[s - 3] == "-":

                                    if "-" not in term_one:
                                        rear_l[s - 3] = "+"
                                        term_one = "-" + term_one

                            op = rear_l[s - 1]
                            term_two = rear_l[s]

                            term_one = term_one.replace(var, '')
                            term_two = term_two.replace(var, '')

                            if term_one == "":

                                term_one = "1.0"

                            elif term_one == "-":

                                term_one = "-1.0"

                            if term_two == "":

                                term_two = "1.0"

                            elif term_two == "-":

                                term_two = "-1.0"

                            if op == "+":

                                new_term = complex(term_one) + complex(term_two)

                            elif op == "-":

                                new_term = complex(term_one) - complex(term_two)

                            else:

                                print("shits broken")

                            if new_term.imag == 0:

                                new_term = str(new_term.real)
                                if "-" in new_term:

                                    if s - 2 == 1:

                                        rear_l[s - 2] = new_term + var
                                        del rear_l[s - 1:s + 1]

                                    else:

                                        if rear_l[s - 3] == "-":

                                            rear_l[s - 3] = "+"
                                            rear_l[s - 2] = new_term + var
                                            del rear_l[s - 1:s + 1]

                                        else:

                                            rear_l[s - 3] = "-"
                                            new_term = new_term.replace("-", '')
                                            rear_l[s - 2] = new_term + var
                                            del rear_l[s - 1:s + 1]

                                elif new_term == "0.0":

                                    if s - 2 == 1:

                                        del rear_l[s - 2:s + 1]

                                    else:

                                        del rear_l[s - 3:s + 1]

                                elif new_term == "1.0":

                                    rear_l[s - 2] = var
                                    del rear_l[s - 1:s + 1]

                                elif new_term == "-1.0":

                                    if s - 2 == 1:

                                        rear_l[s - 2] = "-" + var
                                        del rear_l[s - 1:s + 1]

                                    else:

                                        if rear_l[s - 3] == "-":

                                            rear_l[s - 3] = "+"
                                            rear_l[s - 2] = var
                                            del rear_l[s - 1:s + 1]

                                        else:

                                            rear_l[s - 3] = "-"
                                            rear_l[s - 2] = var
                                            del rear_l[s - 1:s + 1]

                                else:

                                    rear_l[s - 2] = new_term + var
                                    del rear_l[s - 1:s + 1]

                            else:

                                new_term = str(new_term)
                                rear_l[s - 2] = new_term + var
                                del rear_l[s - 1:s + 1]

                            s = -1

                s += 1

        # print(rear_l)
        # l_string = stringify(rear_l)
        # print(l_string)

        rear_r = ["(1", "0", ")1"]
        r_string = stringify(self.rhs)
        r_temp = Arithmetic(r_string)
        rear_r[1] = str(r_temp.calculate())
        # print(rear_r)

        # Find the highest deg
        highest_deg = 0.0
        for s in rear_l:

            if var + "^" in s:

                temp = s
                x = ""
                k = 0
                while temp[k] != "^":
                    k += 1

                k += 1
                while k != len(temp):
                    x += temp[k]
                    k += 1

                if float(x) > highest_deg:
                    highest_deg = float(x)

            elif (var in s) and ("^" not in s):

                x = 1.0

                if float(x) > highest_deg:
                    highest_deg = float(x)

        self.lhs = copy.deepcopy(rear_l)
        self.rhs = copy.deepcopy(rear_r)
        self.deg = copy.deepcopy(l_deg_ordered)

    def solver(self) -> List[Union[int, float, complex]]:
        """Function takes LHS and RHS of an equation with all variables on LHS, and single constant on RHS and solves based on highest power term."""
        self.update_attr()
        print(self.deg)
        if self.deg[0] == 1.0:

            # print("yeet", l ,r)
            s = 0
            while s != len(self.lhs):

                if self.var_type[0] in self.lhs[s]:

                    value = self.lhs[s]
                    value = value.replace(self.var_type[0], '')
                    if value == '':

                        value = 1 + 0j

                    else:

                        value = complex(value)

                    if round(value.imag, 6) == 0:
                        value = value.real

                    other_value = complex(self.rhs[1])

                    if round(other_value.imag, 6) == 0:
                        other_value = other_value.real

                    self.rhs[1] = str(other_value / value)
                    self.lhs[s] = self.var_type[0]
                    l_string = stringify(self.lhs)
                    r_string = stringify(self.rhs)
                    print(l_string + " = " + r_string)

                s += 1

            if (len(self.lhs) == 3) and (self.lhs[1] == self.var_type[0]):

                ans = []
                temp = complex(self.rhs[1])

                if round(temp.imag, 6) == 0:
                    temp = temp.real

                ans.append(temp)

        elif self.deg[0] == 2.0:

            if "-" in self.rhs[1]:

                self.rhs[1] = self.rhs[1].replace('-', '')
                self.lhs.insert(-1, "+")
                self.lhs.insert(-1, self.rhs[1])
                self.rhs[1] = "0"

            else:

                self.lhs.insert(-1, "-")
                self.lhs.insert(-1, self.rhs[1])
                self.rhs[1] = "0"

            # Quadratic Formula

            ans = self.quadratic()

            for s in range(0, len(ans)):

                if round(ans[s].imag, 6) == 0:
                    ans[s] = ans[s].real

        # 3rd or polynomial

        elif self.deg[0] == 3.0:

            if "-" in self.rhs[1]:

                self.rhs[1] = self.rhs[1].replace('-', '')
                self.lhs.insert(-1, "+")
                self.lhs.insert(-1, self.rhs[1])
                self.rhs[1] = "0"

            else:

                self.lhs.insert(-1, "-")
                self.lhs.insert(-1, self.rhs[1])
                self.rhs[1] = "0"

            # Cubic Function Formula
            ans = self.cardano()

            for s in range(0, len(ans)):

                if round(ans[s].imag, 6) == 0:
                    ans[s] = ans[s].real

        # Ferrari's Method
        elif self.deg[0] == 4.0:

            if "-" in self.rhs[1]:

                self.rhs[1] = self.rhs[1].replace('-', '')
                self.lhs.insert(-1, "+")
                self.lhs.insert(-1, self.rhs[1])
                self.rhs[1] = "0"

            else:

                self.lhs.insert(-1, "-")
                self.lhs.insert(-1, self.rhs[1])
                self.rhs[1] = "0"

            ans = self.ferrari()

            for s in range(0, len(ans)):

                if round(ans[s].imag, 6) == 0:
                    ans[s] = ans[s].real

        # For any polynomial of nth degree where n>=5
        else:
            from math_core.jenkins_traub import real_poly

            if (self.rhs[1] != "0") and (self.rhs[1] != "0.0"):

                print("we in here", self.rhs)
                if "-" in self.rhs[1]:

                    self.rhs[1] = self.rhs[1].replace('-', '')
                    self.lhs.insert(-1, "+")
                    self.lhs.insert(-1, self.rhs[1])
                    self.rhs[1] = "0"

                else:

                    self.lhs.insert(-1, "-")
                    self.lhs.insert(-1, self.rhs[1])
                    self.rhs[1] = "0"

            # print("coeff before JT",coeff)
            print("Checking if 0 is a root via synthetic division...\n")
            self.solution.append("Checking if 0 is a root via synthetic division...")
            self.solution.append("")
            self.solution.append("")

            test = self.lin_divide([1, 0])
            test_two = self.lin_divide([1, 0])
            remainder = test[-1]

            del test_two[-1]
            test_obj = Algebra()
            test_obj.coeff = copy.deepcopy(test_two)
            test_obj.var_type = copy.deepcopy(self.var_type)
            test_obj.update_params_from_coeff()
            #print(test_obj.eqn_string)

            test_temp = test_obj.eqn_string

            if remainder < 0:

                test_temp += str(remainder) + "/" + self.var_type[0]

            elif remainder > 0:

                test_temp += "+" + str(remainder) + "/" + self.var_type[0]

            print("(" + stringify(self.lhs) + ")/" + self.var_type[0] + " = " + test_temp + "\n")
            self.solution.append("(" + stringify(self.lhs) + ")/" + self.var_type[0] + " = " + test_temp)
            self.solution.append("")
            self.solution.append("")

            if remainder == 0.0:

                success_attempt = False
                ans = []
                i = 1
                while not success_attempt:

                    if len(test) - 2 >= 5:

                        try:
                            del test[-1]
                            from math_core.Calculus import Calculus
                            coeff = Calculus()
                            coeff.coeff = copy.deepcopy(test)
                            coeff.var_type = copy.deepcopy(self.var_type)
                            coeff.update_params_from_coeff()
                            print("AYO!", coeff.coeff, coeff.deg)
                            ans = real_poly(coeff)

                        except ZeroDivisionError:

                            string = self.var_type[0]

                            test = self.lin_divide([1, 0])

                            print("0 might be a repeated root, trying again...\n")
                            self.solution.append("0 might be a repeated root, trying again...")
                            self.solution.append("")
                            self.solution.append("")

                            test_two = self.lin_divide([1, 0])
                            remainder = test[-1]

                            test_obj = Algebra()
                            test_obj.coeff = copy.deepcopy(test_two)
                            test_obj.var_type = copy.deepcopy(self.var_type)
                            test_obj.update_params_from_coeff()
                            # print(test_obj.eqn_string)

                            test_temp = test_obj.eqn_string

                            if remainder < 0:

                                test_temp += str(remainder) + "/" + self.var_type[0]

                            elif remainder > 0:

                                test_temp += "+" + str(remainder) + "/" + self.var_type[0]

                            print("(" + stringify(self.lhs) + ")/" + self.var_type[0] + " = " + test_temp + "\n")
                            self.solution.append("(" + stringify(self.lhs) + ")/" + self.var_type[0] + " = " + test_temp)
                            self.solution.append("")
                            self.solution.append("")
                            i += 1

                        else:

                            success_attempt = True
                            print("Success! 0 is a root\n")
                            self.solution.append("Success! 0 is a root")
                            self.solution.append("")
                            self.solution.append("")

                    elif len(test) - 2 == 4:

                        del test[-1]
                        from math_core.Calculus import Calculus
                        test_eqn = Calculus()
                        test_eqn.coeff = copy.deepcopy(test)
                        test_eqn.var_type = copy.deepcopy(self.var_type)
                        test_eqn.update_params_from_coeff()
                        ans = test_eqn.ferrari()
                        success_attempt = True

                    else:

                        break

                for s in range(1, i + 1):
                    ans.insert(0, 0)


            else:

                print("0 is not a root\n")
                self.solution.append("0 is not a root")
                from math_core.Calculus import Calculus
                coeff = Calculus()
                coeff.coeff = copy.deepcopy(self.coeff)
                coeff.var_type = copy.deepcopy(self.var_type)
                coeff.update_params_from_coeff()
                ans = real_poly(coeff)

            print(ans)

            for i in range(0, len(ans)):

                if round(ans[i].imag, 5) == 0:
                    ans[i] = ans[i].real

        return ans
