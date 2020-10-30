from parser.lexer import Token, EXP, EQUAL, PLUS, MINUS, NUMBER, CONSTANT, MUL, DIV
from parser.ast import AST, BINOPNode, FUNCNode, UNIOPNode, VARNode, NUMNode, NumberNode
from math_core.algebra_formats import monomial_x_power, monomial_x, build_monomial_template

from typing import List, Union, Any
import re
from fractions import Fraction
import pytest
import math


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
]


class Colors:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"


def stringify_node(node: AST, var: Union[str, List[str]]) -> str:
    """Function will take a node and turn it into a string"""
    if node.type == BINOPNode:
        temp = node.op.value
        if node.op.tag != EQUAL:
            if node.left.type == BINOPNode and node.left.op.tag != EXP:
                if node.op.tag not in (EXP, DIV, PLUS, MINUS) or node.left.op.tag not in (PLUS, MINUS) and not check_mono(node.left):
                    temp = ")" + temp
            elif node.op.tag == EXP and node.left.type == BINOPNode and node.left.op.tag == EXP and check_mono(node.right):
                temp = ")" + temp
            if node.right.type == BINOPNode and node.right.op.tag != EXP:
                if node.op.tag not in (PLUS, MINUS) or node.right.op.tag not in (PLUS, MINUS) and not check_mono(node.right):
                    temp += "("
        left = stringify_node(node.left, var)
        if ")"+node.op.value in temp:
            left = "("+left
        right = stringify_node(node.right, var)
        if node.op.value+"(" in temp:
            right += ")"
        return inference_string(left+temp+right, var)
    elif node.type == UNIOPNode:
        temp = node.op.value
        if node.right.type == BINOPNode:
            temp += "("
        right = stringify_node(node.right, var)
        if "(" in temp:
            right += ")"
        return inference_string(temp+right, var)
    elif node.type == FUNCNode:
        if node.op.value.lower() not in ("abs", "abs_ln"):
            temp = node.op.value.lower()+"("
            for i in range(len(node.args)):
                if i < 1:
                    temp += stringify_node(node.args[i], var)
                else:
                    temp += ","+stringify_node(node.args[i], var)
            temp += ")"
        else:
            temp = "|"
            if node.op.value.lower() == "abs_ln":
                temp = "ln" + temp
            temp += stringify_node(node.args[0], var)
            temp += "|"
        return inference_string(temp, var)
    elif node.type == VARNode:
        return inference_string(node.value, var)
    elif node.type == NUMNode:
        if type(round_complex(visit_NUMNode(node))) == float and node.tag == NUMBER:
            return inference_string(str(Fraction(node.value).limit_denominator(1000)), var)
        return inference_string(node.value, var)


def inference_string(eqn_string: str, var: Union[str, List[str]]) -> str:
    """Method will remove some parts of an equation which are redundant"""
    regex = r'\-?\(?\(?\-?[0-9]+(\.[0-9]*)?([\-\+][0-9]+(\.[0-9]*)?j)?\)?\*[a-zA-Z_](\^[-]?[0-9]+(\.[0-9]*)?)?\)?'
    if isinstance(var, str):
        var = [var]
    for var in var:
        match = re.search(regex, eqn_string)
        if match is not None:
            if "((" in match.group():
                match_wo_br_or_mul = match.group().replace("((", '(')
                match_wo_br_or_mul = match_wo_br_or_mul.replace(var+")",var)
            else:
                match_wo_br_or_mul = match.group().replace("(", '')
                match_wo_br_or_mul = match_wo_br_or_mul.replace(")",'')
            match_wo_br_or_mul = match_wo_br_or_mul.replace("*", '')
            if "1"+var in match_wo_br_or_mul:
                match_wo_br_or_mul = match_wo_br_or_mul.replace("1", '')
            elif "-1"+var in match_wo_br_or_mul:
                match_wo_br_or_mul = match_wo_br_or_mul.replace("-1", '-')
            eqn_string = eqn_string.replace(match.group(), match_wo_br_or_mul)
            match = re.search(regex, eqn_string)
        if match is not None:
            return inference_string(eqn_string, var)
        if eqn_string in "1*"+var:
            eqn_string = eqn_string.replace("1*"+var, var)
        elif eqn_string in "-1*"+var:
            eqn_string = eqn_string.replace("-1*"+var, "-"+var)
        if eqn_string in "1"+var:
            eqn_string = eqn_string.replace("1"+var, var)
        elif eqn_string in "-1" + var:
            eqn_string = eqn_string.replace("-1"+var, "-"+var)
        if "#" in eqn_string:
            eqn_string = eqn_string.replace("#", "")
    return eqn_string.replace('(' + var + ')', var) if not check_for_func(eqn_string) else eqn_string


def check_for_func(eqn: str):
    """Method checks if there are functions in the string"""
    for func in list_of_func:
        if func in eqn:
            return True
    return False


def round_complex(num: Any, decimal_place: int = 6) -> Union[complex, float]:
    """Function will take a complex number and round its real and imaginary parts if they're extremely small"""
    if type(num) == complex:
        if round(num.real, decimal_place).is_integer() and not round(num.imag, decimal_place).is_integer():
            num = int(round(num.real, decimal_place)) + num.imag * 1j
        elif round(num.real, decimal_place).is_integer() and round(num.imag, decimal_place).is_integer():
            num = int(round(num.real, decimal_place)) + int(round(num.imag, decimal_place)) * 1j
        elif not round(num.real, decimal_place).is_integer() and round(num.imag, decimal_place).is_integer():
            num = num.real + int(round(num.imag, decimal_place)) * 1j
        if num.real == 0:
            num = num.imag * 1j
        if num.imag == 0:
            num = num.real
    if type(num) == float:
        if round(num, decimal_place).is_integer():
            num = int(num)
    return num


def visit_NUMNode(node: NumberNode):
    """This method takes a CONSTNode and returns the constant if it exits"""
    if node.tag == NUMBER:
        try:
            num = float(node.value)
        except ValueError:
            num = complex(node.value)
        return num
    elif node.tag == CONSTANT:
        if node.value in ("#pi", "#PI"):
            return math.pi
        elif node.value in ("#e", "#E"):
            return math.e
        elif node.value == "#C":
            return 1
        else:
            raise ValueError(f"Constant {node.value} is not recognized")


def check_mono(node: AST):
    """This method checks if a node is a monomial that isn't part of the standard templates"""
    if hash(node) == hash(monomial_x[0]) or hash(node) == hash(monomial_x_power[0]):
        return True
    if node.type == BINOPNode:
        mono_template = None
        if node.op.tag == EXP and node.right.type == NUMNode:
            exponent = round_complex(visit_NUMNode(node.right))
            mono_template = build_monomial_template(exponent, EXP)
        elif node.op.tag == MUL and node.right.type == BINOPNode and node.right.op.tag == EXP and node.right.right.type == NUMNode:
            exponent = round_complex(visit_NUMNode(node.right.right))
            mono_template = build_monomial_template(exponent, MUL)
        if mono_template is not None:
            if hash(node) == hash(mono_template[0]):
                return True
    return False


class Equation:
    def __init__(self, eqn_string: str = None, tokens: List[Token] = None, tree: List[Union[AST, Token]] = None):
        self.solution = ["The inputted equation is " + eqn_string]
        self.eqn_string = eqn_string.replace(" ", "")
        self.eqn_tokens = tokens
        self.tree = tree

    def update_eqn_string(self, section_to_replace: str, new_section: str, br_override: bool = False):
        """Method which updates the eqn string based on recent ops"""
        self.solution.append("------")
        if not br_override:
            if "("+section_to_replace+")" in self.eqn_string and "("+section_to_replace+")^" not in self.eqn_string:
                self.eqn_string = self.eqn_string.replace("("+section_to_replace+")", new_section)
            else:
                self.eqn_string = self.eqn_string.replace(section_to_replace, new_section)
        else:
            self.eqn_string = self.eqn_string.replace(section_to_replace, new_section)
        self.solution.append(self.eqn_string)
        self.solution.append("------")

