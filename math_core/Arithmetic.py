from math_core.Equation import Equation, visit_NUMNode, list_of_func
from parser.ast import FuncNode, BinOpNode, AST, UniOpNode, NumberNode
from parser.ast import FUNCNode, BINOPNode, NUMNode, VARNode, UNIOPNode
from parser.lexer import MUL, MINUS, PLUS, EXP, DIV, NUMBER, CONSTANT

import math
import cmath
from typing import Union


def stringify(num: Union[int, float, complex]) -> str:
    """Method takes a number and returns a string"""
    if type(num) == float:
        if num.is_integer():
            return str(int(num))
    return str(num)


class Arithmetic(Equation):
    def calculate(self) -> Union[float, complex, int]:
        """Method calls the method from the Interpreter class to climb the AST and solve"""
        ans = self.solve()
        self.solution.append("The final answer is "+stringify(ans))
        return ans

    def solve(self):
        """Method which initiates tree climbing"""
        return self.climb_tree(self.tree)

    def climb_tree(self, node: AST):
        """Method to climb tree and find answer"""
        if node.type == UNIOPNode:
            return self.visit_UNIOPNode(node)
        elif node.type == BINOPNode:
            return self.visit_BINOPNode(node)
        elif node.type == FUNCNode:
            return self.visit_FUNCNode(node)
        elif node.type == NUMNode:
            return visit_NUMNode(node)
        elif node.type == VARNode:
            return node.value

    def visit_UNIOPNode(self, node: UniOpNode):
        """Method to evaluate UniOpNodes"""
        if node.op.tag == PLUS:
            return +self.climb_tree(node.right)
        elif node.op.tag == MINUS:
            return -self.climb_tree(node.right)

    def visit_BINOPNode(self, node: BinOpNode):
        """Method to evaluate BinOpNodes"""
        left = self.climb_tree(node.left)
        right = self.climb_tree(node.right)
        if node.op.tag == EXP:
            ans = left ** right

            self.solution.append(stringify(left)+"^"+stringify(right)+" = "+stringify(ans))
            self.update_eqn_string(stringify(left)+"^"+stringify(right), stringify(ans))
            return ans
        elif node.op.tag == MUL:
            ans = left * right
            self.solution.append(stringify(left)+"*"+stringify(right) + " = " + stringify(ans))
            self.update_eqn_string(stringify(left)+"*"+stringify(right), stringify(ans))
            return ans
        elif node.op.tag == DIV:
            ans = left / right
            self.solution.append(stringify(left)+"/"+stringify(right) + " = " + stringify(ans))
            self.update_eqn_string(stringify(left)+"/"+stringify(right), stringify(ans))
            return ans
        elif node.op.tag == PLUS:
            ans = left + right
            self.solution.append(stringify(left)+"+"+stringify(right) + " = " + stringify(ans))
            self.update_eqn_string(stringify(left)+"+"+stringify(right), stringify(ans))
            return ans
        elif node.op.tag == MINUS:
            ans = left - right
            self.solution.append(stringify(left)+"-"+stringify(right) + " = " + stringify(ans))
            self.update_eqn_string(stringify(left)+"-"+stringify(right), stringify(ans))
            return ans
        #elif node.op.tag == EQUAL:
            #return left, right

    def visit_FUNCNode(self, node: FuncNode):
        """Method to evaluate FuncNodes"""
        if node.op.value in list_of_func or node.op.value.upper() in list_of_func:
            if node.op.value in ("log", "LOG"):
                if len(node.args) == 2:
                    base = self.climb_tree(node.args[0])
                    exponent = self.climb_tree(node.args[1])
                    ans = math.log(base, exponent)
                    self.solution.append(node.op.value+"("+stringify(base)+","+stringify(exponent)+") = "+stringify(ans))
                    self.update_eqn_string(node.op.value+"("+stringify(base)+","+stringify(exponent)+")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for log function. Args = {}".format(node.args))
            elif node.op.value in ("ln", "LN"):
                if len(node.args) == 1:
                    exponent = self.climb_tree(node.args[0])
                    ans = math.log(exponent)
                    self.solution.append(node.op.value+"("+stringify(exponent)+") = "+stringify(ans))
                    self.update_eqn_string(node.op.value+"("+stringify(exponent)+")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for ln function. Args = {}".format(node.args))
            elif node.op.value in ("sqrt", "SQRT"):
                if len(node.args) == 1:
                    num = self.climb_tree(node.args[0])
                    ans = cmath.sqrt(num)
                    self.solution.append(node.op.value+"("+stringify(num)+") = "+stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(num) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for sqrt function. Args = {}".format(node.args))
            elif node.op.value in ("sin", "SIN", "cos", "COS", "tan", "TAN", "sinh", "SINH", "cosh", "COSH", "tanh", "TANH", "asinh", "ASINH", "acosh", "ACOSH", "atanh", "ATANH"):
                if len(node.args) == 1:
                    num = self.climb_tree(node.args[0])
                    oper = getattr(math, node.op.value.lower())
                    ans = oper(math.radians(num))
                    self.solution.append(node.op.value+"(" + stringify(num) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(num) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("sinh", "SINH", "cosh", "COSH", "tanh", "TANH", "asinh", "ASINH", "acosh", "ACOSH", "atanh", "ATANH"):
                if len(node.args) == 1:
                    num = self.climb_tree(node.args[0])
                    oper = getattr(math, node.op.value.lower())
                    ans = oper(num)
                    self.solution.append(node.op.value + "(" + stringify(num) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(num) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("asin", "ASIN", "acos", "ACOS", "atan", "ATAN"):
                if len(node.args) == 1:
                    num = self.climb_tree(node.args[0])
                    oper = getattr(math, node.op.value.lower())
                    ans = math.degrees(oper(num))
                    self.solution.append(node.op.value + "(" + stringify(num) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(num) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("sinh", "SINH", "cosh", "COSH", "tanh", "TANH"):
                if len(node.args) == 1:
                    num = self.climb_tree(node.args[0])
                    oper = getattr(math, node.op.value.lower())
                    ans = oper(num)
                    self.solution.append(node.op.value + "(" + stringify(num) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(num) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("sec", "SEC"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = 1/math.cos(result)
                    self.solution.append("sec("+stringify(result)+") = 1/cos("+stringify(result)+") = "+stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("csc", "CSC"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = 1 / math.sin(result)
                    self.solution.append("csc(" + stringify(result) + ") = 1/sin(" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("cot", "COT"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = 1 / math.tan(result)
                    self.solution.append("cot(" + stringify(result) + ") = 1/tan(" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("asec", "ASEC"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = math.acos(1/result)
                    self.solution.append("asec(" + stringify(result) + ") = acos(1/" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("acsc", "ACSC"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = math.asin(1/result)
                    self.solution.append("acsc(" + stringify(result) + ") = asin(1/" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("acot", "ACOT"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = math.atan(1/result)
                    self.solution.append("acot(" + stringify(result) + ") = atan(1/" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("sech", "SECH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = 1 / math.cosh(result)
                    self.solution.append("sech(" + stringify(result) + ") = 1/cosh(" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("csch", "CSCH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = 1 / math.sinh(result)
                    self.solution.append("csch(" + stringify(result) + ") = 1/sinh(" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("coth", "COTH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = 1 / math.tanh(result)
                    self.solution.append("coth(" + stringify(result) + ") = 1/tanh(" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("asech", "ASECH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = math.acosh(1/result)
                    self.solution.append("asech(" + stringify(result) + ") = acosh(1/" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("acsch", "ACSCH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = math.asinh(1/result)
                    self.solution.append("acsch(" + stringify(result) + ") = asinh(1/" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("acoth", "ACOTH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        ans = math.inf
                    else:
                        ans = math.atanh(1/result)
                    self.solution.append("acoth(" + stringify(result) + ") = atanh(1/" + stringify(result) + ") = " + stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(result) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("abs", "ABS"):
                if len(node.args) == 1:
                    num = self.climb_tree(node.args[0])
                    ans = abs(num)
                    self.solution.append("abs("+stringify(num)+") = "+stringify(ans))
                    self.update_eqn_string(node.op.value + "(" + stringify(num) + ")", stringify(ans))
                    return ans
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
        else:
            return Exception("Invalid function{}".format(node.op.value))

    @staticmethod
    def div_check(x: Union[int, float, complex], y: Union[int, float, complex]) -> bool:
        """Detects divisions by zero."""
        try:
            x / y
        except ZeroDivisionError:
            return True
        else:
            return False

