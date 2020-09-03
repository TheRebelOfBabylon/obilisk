from parser.ast import FuncNode, BinOpNode, NumberNode, ConstantNode, VariableNode, AST
from parser.ast import FUNCNode, BINOPNode, NUMNode, CONSTNode, VARNode
from parser.lexer import EQUAL, MUL, MINUS, PLUS, EXP, DIV

import math
import cmath
from typing import Union

list_of_func = [
    "cos",
    "sin",
    "tan",
    "abs",
    "log",
    "ln",
    "sqrt",
    "sec",
    "csc",
    "cot",
    "acos",
    "asin",
    "atan",
    "asec",
    "acsc",
    "acot",
    "cosh",
    "sinh",
    "tanh",
    "sech",
    "csch",
    "coth",
    "acosh",
    "asinh",
    "atanh",
    "asech",
    "acsch",
    "acoth",
    "derivative",
    "integral",
]


class Interpreter:
    has_vars = False

    def __init__(self, tree):
        self.tree = tree
        self.vars = []

    def solve(self):
        """Method which initiates tree climbing"""
        return self.climb_tree(self.tree)

    def climb_tree(self, node: AST):
        """Method to climb tree and find answer"""
        if node.type == BINOPNode:
            return self.visit_BINOPNode(node)
        elif node.type == FUNCNode:
            return self.visit_FUNCNode(node)
        elif node.type == NUMNode:
            try:
                num = float(node.value)
            except:
                num = complex(node.value)
            return num
        elif node.type == VARNode:
            return node.value
        elif node.type == CONSTNode:
            return self.vist_CONSTNode(node)

    def visit_BINOPNode(self, node: BinOpNode):
        """Method to evaluate BinOpNodes"""
        if node.op.tag == EXP:
            return self.climb_tree(node.left) ** self.climb_tree(node.right)
        elif node.op.tag == MUL:
            return self.climb_tree(node.left) * self.climb_tree(node.right)
        elif node.op.tag == DIV:
            return self.climb_tree(node.left) / self.climb_tree(node.right)
        elif node.op.tag == PLUS:
            return self.climb_tree(node.left) + self.climb_tree(node.right)
        elif node.op.tag == MINUS:
            return self.climb_tree(node.left) - self.climb_tree(node.right)
        elif node.op.tag == EQUAL:
            return self.climb_tree(node.left), self.climb_tree(node.right)

    def visit_FUNCNode(self, node: FuncNode):
        """Method to evaluate FuncNodes"""
        if node.op.value in list_of_func or node.op.value.upper() in list_of_func:
            if node.op.value in ("log", "LOG"):
                if len(node.args) == 2:
                    return math.log(self.climb_tree(node.args[0]), self.climb_tree(node.args[1]))
                return ValueError("Too few or too many arguments for log function. Args = {}".format(node.args))
            elif node.op.value in ("ln", "LN"):
                if len(node.args) == 1:
                    return math.log(self.climb_tree(node.args[0]))
                return ValueError("Too few or too many arguments for ln function. Args = {}".format(node.args))
            elif node.op.value in ("sqrt", "SQRT"):
                if len(node.args) == 1:
                    return cmath.sqrt(self.climb_tree(node.args[0]))
                return ValueError("Too few or too many arguments for sqrt function. Args = {}".format(node.args))
            elif node.op.value in ("sin", "SIN", "cos", "COS", "tan", "TAN", "sinh", "SINH", "cosh", "COSH", "tanh", "TANH", "asinh", "ASINH", "acosh", "ACOSH", "atanh", "ATANH"):
                if len(node.args) == 1:
                    oper = getattr(math, node.op.value.lower())
                    return oper(math.radians(self.climb_tree(node.args[0])))
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("sinh", "SINH", "cosh", "COSH", "tanh", "TANH", "asinh", "ASINH", "acosh", "ACOSH", "atanh", "ATANH"):
                if len(node.args) == 1:
                    oper = getattr(math, node.op.value.lower())
                    return oper(self.climb_tree(node.args[0]))
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("asin", "ASIN", "acos", "ACOS", "atan", "ATAN"):
                if len(node.args) == 1:
                    oper = getattr(math, node.op.value.lower())
                    return math.degrees(oper(self.climb_tree(node.args[0])))
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("sinh", "SINH", "cosh", "COSH", "tanh", "TANH"):
                if len(node.args) == 1:
                    oper = getattr(math, node.op.value.lower())
                    return oper(self.climb_tree(node.args[0]))
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("sec", "SEC"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return 1/math.cos(result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("csc", "CSC"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return 1/math.sin(result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("cot", "COT"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return 1/math.tan(result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("asec", "ASEC"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return math.acos(1/result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("acsc", "ACSC"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return math.asin(1/result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("acot", "ACOT"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return math.atan(1/result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("sech", "SECH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return 1/math.cosh(result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("csch", "CSCH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return 1/math.sinh(result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("coth", "COTH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return 1/math.tanh(result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("asech", "ASECH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return math.acosh(1/result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("acsch", "ACSCH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return math.asinh(1/result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("acoth", "ACOTH"):
                if len(node.args) == 1:
                    result = self.climb_tree(node.args[0])
                    if self.div_check(1, result):
                        return math.inf
                    else:
                        return math.atanh(1/result)
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
            elif node.op.value in ("abs", "ABS"):
                if len(node.args) == 1:
                    return abs(self.climb_tree(node.args[0]))
                return ValueError("Too few or too many arguments for {} function. Args = {}".format(node.op.value, node.args))
        else:
            return Exception("Invalid function{}".format(node.op.value))

    def vist_CONSTNode(self, node: CONSTNode):
        """This method takes a CONSTNode and returns the constant if it exits"""
        if node.value in ("#pi", "#PI"):
            return math.pi
        elif node.value in ("#e", "#E"):
            return math.e
        else:
            raise ValueError("Constant {} is not recognized".format(node.value))

    @staticmethod
    def div_check(x: Union[int, float, complex], y: Union[int, float, complex]) -> bool:
        """Detects divisions by zero."""
        try:
            x / y
        except ZeroDivisionError:
            return True
        else:
            return False


