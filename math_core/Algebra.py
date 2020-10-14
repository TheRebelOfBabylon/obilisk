"""
1. Check if equation is already in solvable format
2. Check if equation can be more easily solved by using substitution
3. Order equation into standard polynomial format
4. Solve
"""
from parser.lexer import Lexer, Token
from parser.combinator import TreeBuilder
from math_core.Equation import Equation, stringify_node, Colors, round_complex, visit_NUMNode, check_mono
from parser.ast import AST, BINOPNode, VARNode, UNIOPNode, FUNCNode, UniOpNode, NumberNode, NUMNode, FuncNode, BinOpNode, VariableNode
from parser.lexer import Token, EQUAL, EXP, MUL, PLUS, MINUS, NUMBER, CONSTANT, DIV, FUNC, VARIABLE
from math_core.Arithmetic import list_of_func, Arithmetic, stringify
from math_core.algebra_formats import quadratic_left_full, quadratic_left_no_b, quadratic_left_no_c, \
    quadratic_left_no_bc, \
    quadratic_right_full, quadratic_right_no_b, quadratic_right_no_c, quadratic_right_no_bc, cubic_left_full, \
    cubic_left_no_b, \
    cubic_left_no_bcd, cubic_left_no_bc, cubic_left_no_bd, cubic_left_no_c, cubic_left_no_cd, cubic_left_no_d, \
    cubic_right_full, \
    cubic_right_no_b, cubic_right_no_bc, cubic_right_no_bcd, cubic_right_no_bd, cubic_right_no_c, cubic_right_no_cd, \
    cubic_right_no_d, \
    quartic_left_full, quartic_left_no_bcd, quartic_left_no_b, quartic_left_no_bc, quartic_left_no_bcde, \
    quartic_left_no_bce, \
    quartic_left_no_bd, quartic_left_no_bde, quartic_left_no_be, quartic_left_no_c, quartic_left_no_cd, \
    quartic_left_no_cde, \
    quartic_left_no_ce, quartic_left_no_d, quartic_left_no_de, quartic_left_no_e, quartic_right_full, \
    quartic_right_no_b, \
    quartic_right_no_bcde, quartic_right_no_bc, quartic_right_no_bcd, quartic_right_no_bce, quartic_right_no_bd, \
    quartic_right_no_bde, \
    quartic_right_no_be, quartic_right_no_c, quartic_right_no_cd, quartic_right_no_cde, quartic_right_no_ce, \
    quartic_right_no_d, \
    quartic_right_no_de, quartic_right_no_e, monomial_x, monomial_x_power, poly_regex, poly_power_regex, poly_regex_2

from typing import List, Union, Tuple
from copy import deepcopy
import cmath
import math
import random
import re

list_of_templates = [
    quadratic_left_full,
    quadratic_left_no_b,
    quadratic_left_no_c,
    quadratic_left_no_bc,
    quadratic_right_full,
    quadratic_right_no_b,
    quadratic_right_no_c,
    quadratic_right_no_bc,
    cubic_left_full,
    cubic_left_no_b,
    cubic_left_no_c,
    cubic_left_no_d,
    cubic_left_no_bc,
    cubic_left_no_bd,
    cubic_left_no_cd,
    cubic_left_no_bcd,
    cubic_right_full,
    cubic_right_no_b,
    cubic_right_no_c,
    cubic_right_no_d,
    cubic_right_no_bc,
    cubic_right_no_bd,
    cubic_right_no_cd,
    cubic_right_no_bcd,
    quartic_left_full,
    quartic_left_no_b,
    quartic_left_no_c,
    quartic_left_no_d,
    quartic_left_no_e,
    quartic_left_no_bc,
    quartic_left_no_bd,
    quartic_left_no_be,
    quartic_left_no_cd,
    quartic_left_no_ce,
    quartic_left_no_de,
    quartic_left_no_bcd,
    quartic_left_no_bce,
    quartic_left_no_bde,
    quartic_left_no_cde,
    quartic_left_no_bcde,
    quartic_right_full,
    quartic_right_no_b,
    quartic_right_no_c,
    quartic_right_no_d,
    quartic_right_no_e,
    quartic_right_no_bc,
    quartic_right_no_bd,
    quartic_right_no_be,
    quartic_right_no_cd,
    quartic_right_no_ce,
    quartic_right_no_de,
    quartic_right_no_bcd,
    quartic_right_no_bce,
    quartic_right_no_bde,
    quartic_right_no_cde,
    quartic_right_no_bcde,
]

oper_dict = {
    EQUAL: EQUAL,
    EXP: EXP,
    MUL: (MUL, DIV),
    DIV: (MUL, DIV),
    PLUS: (PLUS, MINUS),
    MINUS: (PLUS, MINUS),
}

trig_op_dict = {
    "cos" : "acos",
    "acos" : "cos",
    "sin" : "asin",
    "asin" : "sin",
    "tan" : "atan",
    "atan" : "tan",
    "sec" : "asec",
    "asec" : "sec",
    "csc" : "acsc",
    "acsc" : "csc",
    "cot" : "acot",
    "acot" : "cot",
    "cosh" : "acosh",
    "acosh" : "cosh",
    "sinh" : "asinh",
    "asinh" : "sinh",
    "tanh" : "atanh",
    "atanh" : "tanh",
    "sech" : "asech",
    "asech" : "sech",
    "csch" : "acsch",
    "acsch" : "csch",
    "coth" : "acoth",
    "acoth" : "coth",
}

sub_var_dict = {

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
    except TypeError:
        return False


def check_for_monomial(node: AST):
    """Method will check if a node is a monomial"""
    if hash(node) == hash(monomial_x[0]):
        return True
    elif hash(node) == hash(monomial_x_power[0]):
        return True
    else:
        return False


class Algebra(Equation):
    def __init__(self, eqn_string: str = None, tokens: List[Token] = None, tree: List[Union[AST, Token]] = None,
                 var: str = None, exprs: List[AST] = None):
        Equation.__init__(self, eqn_string, tokens, tree)  # should this be super()?
        self.var = var
        self.coeff = []
        self.exprs = exprs
        self.subs = None
        self.divisors = None

    def __repr__(self):
        return 'Algebra(%s)' % (self.eqn_string)

    def check_solvability(self) -> Tuple[bool, str]:
        """Method checks if the equation is already in a solvable format"""
        tree_hash = hash(self.tree)
        for template, name in list_of_templates:
            temp_hash = hash(template)
            if temp_hash == tree_hash:
                return True, name
        return False, None

    def isolate(self, verbose: bool = True, rounding: bool = True):
        """Method will take the equation in standard polynomial form and solve it"""
        _, template_name = self.check_solvability()
        if template_name is not None:
            if "right" in template_name:
                self.swap_lhs_and_rhs()
            if "quadratic" in template_name:
                return self.quadratic_formula(verbose=verbose, rounding=rounding)
            elif "cubic" in template_name:
                return self.cardano(verbose=verbose, rounding=rounding)
            elif "quartic" in template_name:
                return self.ferrari(verbose=verbose, rounding=rounding)
        else:
            if not self.check_for_x_power_x():
                self.compute_low_hanging_fruit()
                self.check_for_substitution()
                self.remove_redundant_br()
                self.find_divisors()
                self.multiply_div()
                self.foil_monomials()
                if self.tree.type == BINOPNode and self.tree.op.tag == EQUAL:
                    if self.tree.left.type == NUMNode and self.tree.left.value in ("0", "0.0"):
                        self.swap_lhs_and_rhs()
                if self.tree.right.type == NUMNode and self.tree.right.value in ("0", "0.0"):
                    self.coeff = self.get_coeff(self.tree)
                    if len(self.coeff) >= 7:
                        return self.real_poly(self.coeff)

    def swap_lhs_and_rhs(self):
        """This method takes the LHS and RHS of AST and swaps them"""
        if self.tree.type == BINOPNode and self.tree.op.tag == EQUAL:
            new_left = self.tree.right
            new_right = self.tree.left
            self.tree.left = new_left
            self.tree.right = new_right

    def check_for_x_power_x(self):
        """This method climbs through AST and checks for x^x or any variation"""
        return self.check_for_exp(self.tree)

    def check_for_exp(self, node: AST) -> bool:
        """Method checks if there is an EXP node. If so, checks for variables"""
        if node.type == BINOPNode and node.op.tag != EXP:
            chk = self.check_for_exp(node.left)
            if not chk:
                return self.check_for_exp(node.right)
            return True
        elif node.type == UNIOPNode:
            return self.check_for_exp(node.right)
        elif node.type == BINOPNode and node.op.tag == EXP:
            base = self.check_for_variable(node.left)
            if base:
                exponent = self.check_for_variable(node.right)
                if exponent:
                    return True
            chk = self.check_for_exp(node.left)
            if not chk:
                return self.check_for_exp(node.right)
            return True
        elif node.type in (NUMNode, VARNode):
            return False

    def check_for_variable(self, node: AST) -> bool:
        """Returns True for variables, false for numbers"""
        if node.type == VARNode:
            return True
        elif node.type == NUMNode:
            return False
        elif node.type == UNIOPNode:
            return self.check_for_variable(node.right)
        elif node.type == BINOPNode:
            chk = self.check_for_variable(node.left)
            if not chk:
                return self.check_for_variable(node.right)
            return True

    def compute_low_hanging_fruit(self, ops_flag: bool = True):
        """Method finds any operator with a number of the left and right side and computes it"""
        while self.find_operator(self.tree, ops_flag=ops_flag):
            continue

    def find_operator(self, node: AST, ops_flag: bool = True) -> bool:
        """Method climbs through AST and finds operators"""
        if node.type == BINOPNode:
            if node.left.type == NUMNode and node.op.tag != DIV:
                left = stringify(self.goto_NUMNode(node.left))
                if node.right.type == NUMNode:
                    right = stringify(self.goto_NUMNode(node.right))
                    ans = self.compute(left + node.op.value + right)
                    ans_token = Token((stringify(ans), NUMBER))
                    ans_node = NumberNode(ans_token)
                    new_tree = self.replace_node(self.tree, node, ans_node)
                    if new_tree is None:
                        raise Exception("{} was not replaced by {}.".format(node, ans_node))
                    self.tree = deepcopy(new_tree)
                    return True
            elif node.left.type == BINOPNode and node.left.op.tag in oper_dict[node.op.tag] and node.left.right.type == NUMNode:
                left = stringify(self.goto_NUMNode(node.left.right))
                if node.right.type == NUMNode:
                    if node.left.op.tag == EXP and node.op.tag == EXP:
                        right = stringify(self.goto_NUMNode(node.right))
                        ans_token = Token((str(int(left)*int(right)), NUMBER))
                        ans_node = BinOpNode(node.left.left, node.left.op, NumberNode(ans_token))
                        self.solution.append(stringify_node(node, self.var) + " = " + stringify_node(ans_node, self.var))
                        self.update_eqn_string(stringify_node(node, self.var), stringify_node(ans_node, self.var))
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    else:
                        right = stringify(self.goto_NUMNode(node.right))
                        ans = self.compute(left + node.op.value + right)
                        ans_token = Token((stringify(ans), NUMBER))
                        ans_node = BinOpNode(node.left.left, node.left.op, NumberNode(ans_token))
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
            if node.op.tag in (MUL, DIV):
                num = None
                if node.left.type == NUMNode:
                    num = visit_NUMNode(node.left)
                elif node.right.type == NUMNode:
                    num = visit_NUMNode(node.right)
                if round_complex(num) == 0:
                    node_string = stringify_node(node, self.var)
                    self.solution.append(node_string + " = 0")
                    self.update_eqn_string(node_string, "0")
                    ans_token = Token(("0", NUMBER))
                    ans_node = NumberNode(ans_token)
                    new_tree = self.replace_node(self.tree, node, ans_node)
                    if new_tree is None:
                        raise Exception("{} was not replaced by {}.".format(node, ans_node))
                    self.tree = deepcopy(new_tree)
                    return True
                if node.op.tag == DIV:
                    if hash(node.left) == hash(node.right) and node.left.__repr__() == node.right.__repr__():
                        node_string = stringify_node(node, self.var)
                        self.solution.append(node_string+" = 1")
                        self.update_eqn_string(node_string, "1")
                        ans_token = Token(("1", NUMBER))
                        ans_node = NumberNode(ans_token)
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif node.right.type == NUMNode:
                        num = visit_NUMNode(node.right)
                        if round_complex(num) == 0:
                            raise ZeroDivisionError
                    if self.divisors:
                        for div in self.divisors:
                            if stringify_node(div, self.var) in stringify_node(node.left, self.var) and stringify_node(div, self.var) in stringify_node(node.right, self.var):
                                new_node = self.remove_repeating_div(node, div)
                                node_string = stringify_node(node, self.var)
                                new_node_str = stringify_node(new_node, self.var)
                                self.solution.append(node_string + " = " + new_node_str)
                                self.update_eqn_string(node_string, "(" + new_node_str + ")")
                                new_tree = self.replace_node(self.tree, node, new_node)
                                self.tree = deepcopy(new_tree)
                                return True
                elif node.op.tag == MUL:
                    if node.left.type == NUMNode:
                        num = visit_NUMNode(node.left)
                        if round_complex(num) == 1 and not check_mono(node):
                            node_string = stringify_node(node.right, self.var)
                            if "1*("+node_string+")" in self.eqn_string:
                                self.solution.append("1*("+node_string+") = "+node_string)
                                self.update_eqn_string("1*(" + node_string + ")", node_string)
                            elif "1*"+node_string in self.eqn_string:
                                self.solution.append("1*" + node_string + " = " + node_string)
                                self.update_eqn_string("1*"+node_string, node_string)
                            ans_node = node.right
                            new_tree = self.replace_node(self.tree, node, ans_node)
                            if new_tree is None:
                                raise Exception("{} was not replaced by {}.".format(node, ans_node))
                            self.tree = deepcopy(new_tree)
                            return True
                    elif node.right.type == NUMNode:
                        num = visit_NUMNode(node.right)
                        if round_complex(num) == 1 and not check_mono(node):
                            node_string = stringify_node(node.left, self.var)
                            if "(" + node_string + ")*1" in self.eqn_string:
                                self.solution.append("(" + node_string + ")*1 = " + node_string)
                                self.update_eqn_string("(" + node_string + ")*1", node_string)
                            elif node_string+"*1" in self.eqn_string:
                                self.solution.append(node_string + "*1 = " + node_string)
                                self.update_eqn_string(node_string+"*1", node_string)
                            ans_node = node.left
                            new_tree = self.replace_node(self.tree, node, ans_node)
                            if new_tree is None:
                                raise Exception("{} was not replaced by {}.".format(node, ans_node))
                            self.tree = deepcopy(new_tree)
                            return True
                    elif node.__repr__() == BinOpNode(node.left, Token(("*", MUL)), BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), node.left)).__repr__() \
                        or node.__repr__() == BinOpNode(BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), node.right), Token(("*", MUL)), node.right).__repr__():
                        node_string = stringify_node(node, self.var)
                        self.solution.append(node_string + " = 1")
                        self.update_eqn_string(node_string, "1")
                        ans_token = Token(("1", NUMBER))
                        ans_node = NumberNode(ans_token)
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif node.left.type == BINOPNode and node.left.op.tag == DIV and node.left.left.type == NUMNode \
                        and round_complex(visit_NUMNode(node.left.left)) == 1:
                        node_string = stringify_node(node, self.var)
                        ans_node = BinOpNode(node.right, Token(("/", DIV)), node.left.right)
                        self.solution.append(node_string + " = " + stringify_node(ans_node, self.var))
                        self.update_eqn_string(node_string, "("+stringify_node(ans_node, self.var)+")")
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif node.right.type == BINOPNode and node.right.op.tag == DIV and node.right.left.type == NUMNode \
                        and round_complex(visit_NUMNode(node.right.left)) == 1:
                        node_string = stringify_node(node, self.var)
                        ans_node = BinOpNode(node.left, Token(("/", DIV)), node.right.right)
                        self.solution.append(node_string + " = " + stringify_node(ans_node, self.var))
                        self.update_eqn_string(node_string, "("+stringify_node(ans_node, self.var)+")")
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
            elif node.op.tag in (PLUS, MINUS):
                if node.left.type == NUMNode:
                    num = visit_NUMNode(node.left)
                    if round_complex(num) == 0:
                        node_string = stringify_node(node.right, self.var)
                        if "0" + node.op.value + "(" + node_string + ")" in stringify_node(node, self.var):
                            self.solution.append("0" + node.op.value + "(" + node_string + ") = " + node_string)
                            self.update_eqn_string("0" + node.op.value + "(" + node_string + ")", node_string)
                        else:
                            self.solution.append("0" + node.op.value + node_string + " = " + node_string)
                            self.update_eqn_string("0" + node.op.value + node_string, node_string)
                        ans_node = node.right
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                elif node.right.type == NUMNode and node.right.value != "#C":
                    num = visit_NUMNode(node.right)
                    if round_complex(num) == 0:
                        node_string = stringify_node(node.left, self.var)
                        if "(" + node_string + ")" + node.op.value + "0" in stringify_node(node, self.var):
                            self.solution.append("(" + node_string + ")" + node.op.value + "0 = " + node_string)
                            self.update_eqn_string("(" + node_string + ")" + node.op.value + "0", node_string)
                        else:
                            self.solution.append(node_string + node.op.value + "0 = " + node_string)
                            self.update_eqn_string(node_string + node.op.value + "0", node_string)
                        ans_node = node.left
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                if node.op.tag == PLUS:
                    if stringify_node(node.left, self.var) == "-"+stringify_node(node.right, self.var) or \
                    stringify_node(node.right, self.var) == "-"+stringify_node(node.left, self.var) or \
                    (node.left.type == UNIOPNode and node.left.right.__repr__() == node.right.__repr__()) or (node.right.type == UNIOPNode and node.right.right.__repr__() == node.left.__repr__()):
                        node_string = stringify_node(node, self.var)
                        self.solution.append(node_string + " = 0")
                        self.update_eqn_string(node_string, "0")
                        ans_token = Token(("0", NUMBER))
                        ans_node = NumberNode(ans_token)
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                elif node.op.tag == MINUS:
                    if hash(node.left) == hash(node.right) and node.left.__repr__() == node.right.__repr__():
                        node_string = stringify_node(node, self.var)
                        self.solution.append(node_string + " = 0")
                        self.update_eqn_string(node_string, "0")
                        ans_token = Token(("0", NUMBER))
                        ans_node = NumberNode(ans_token)
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif node.left.type == BINOPNode and node.left.op.tag in (MINUS, PLUS) and hash(node.left.right) == hash(node.right) and node.left.right.__repr__() == node.right.__repr__():
                        node_string = stringify_node(node.right, self.var)
                        if "(" + node_string + ")-(" + node_string + ")" in stringify_node(BinOpNode(node.left.right, Token(("-", MINUS)), node.right)):
                            self.solution.append("(" + node_string + ")-(" + node_string + ") = 0")
                            self.update_eqn_string("(" + node_string + ")-(" + node_string + ")", "0")
                        else:
                            self.solution.append(node_string + "-" + node_string + " = 0")
                            self.update_eqn_string(node_string + "-" + node_string, "0")
                        zero_token = Token(("0", NUMBER))
                        zero_node = NumberNode(zero_token)
                        ans_node = deepcopy(node.left)
                        ans_node.right = zero_node
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
            elif node.op.tag == EXP:
                if node.left.type == NUMNode:
                    num = visit_NUMNode(node.left)
                    if round_complex(num) == 0:
                        node_string = stringify_node(node, self.var)
                        self.solution.append(node_string + " = 0")
                        self.update_eqn_string(node_string, "0")
                        ans_token = Token(("0", NUMBER))
                        ans_node = NumberNode(ans_token)
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif round_complex(num) == math.e and node.right.type == FUNCNode and node.right.op.value.lower() == "ln":
                        node_string = stringify_node(node.right.args[0], self.var)
                        self.solution.append("#e^ln(" + node_string + ") = " + node_string)
                        self.update_eqn_string("#e^ln(" + node_string + ")", node_string)
                        ans_node = node.right.args[0]
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif round_complex(num) == math.e and node.right.type == FUNCNode and node.right.op.value.lower() == "abs_ln":
                        node_string = stringify_node(node.right.args[0], self.var)
                        self.solution.append("#e^ln|" + node_string + "| = " + node_string)
                        self.update_eqn_string("#e^ln|" + node_string + "|", node_string)
                        ans_node = node.right.args[0]
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                elif node.left.type == BINOPNode and node.left.op.tag == EXP and node.left.right.type == NUMNode and node.right.type == BINOPNode and node.right.op.tag == DIV and node.right.left.type == NUMNode and node.right.right.type == NUMNode:
                    numerator = visit_NUMNode(node.right.left)
                    denom = visit_NUMNode(node.right.right)
                    num = visit_NUMNode(node.left.right)
                    if round_complex(num) == round_complex(denom) and round_complex(numerator) == 1:
                        node_string = stringify_node(node.left.left, self.var)
                        self.solution.append("((" + node_string + ")^" + str(round_complex(num)) + ")^(" + str(round_complex(numerator)) + "/" + str(round_complex(denom)) + ") = " + node_string)
                        self.update_eqn_string("((" + node_string + ")^" + str(round_complex(num)) + ")^(" + str(round_complex(numerator)) + "/" + str(round_complex(denom)) + ")", node_string)
                        ans_node = node.left.left
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                elif node.right.type == NUMNode:
                    num = visit_NUMNode(node.right)
                    if round_complex(num) == 1:
                        node_string = stringify_node(node.left, self.var)
                        if "(" + node_string + ")^1" in stringify_node(node, self.var):
                            self.solution.append("(" + node_string + ")^1" + " = " + node_string)
                            self.update_eqn_string("(" + node_string + ")^1", "(" + node_string + ")")
                        else:
                            self.solution.append(node_string + "^1 = " + node_string)
                            self.update_eqn_string(node_string + "^1", "(" + node_string + ")")
                        ans_node = node.left
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif round_complex(num) == 0:
                        node_string = stringify_node(node.left, self.var)
                        if "(" + node_string + ")^0" in stringify_node(node, self.var):
                            self.solution.append("(" + node_string + ")^0" + " = 1")
                            self.update_eqn_string("(" + node_string + ")^0", "1")
                        else:
                            self.solution.append(node_string + "^0" + " = 1")
                            self.update_eqn_string(node_string + "^0", "1")
                        ans_token = Token(("1", NUMBER))
                        ans_node = NumberNode(ans_token)
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif round_complex(num) == 2 and node.left.type == FUNCNode and node.left.op.value.lower() == "sqrt":
                        node_string = stringify_node(node.left.args[0], self.var)
                        self.solution.append("sqrt(" + node_string + ")^2" + " = " + node_string)
                        self.update_eqn_string("sqrt(" + node_string + ")^2", node_string)
                        ans_node = node.left.args[0]
                        new_tree = self.replace_node(self.tree, node, ans_node)
                        if new_tree is None:
                            raise Exception("{} was not replaced by {}.".format(node, ans_node))
                        self.tree = deepcopy(new_tree)
                        return True
                    elif node.left.type == BINOPNode and node.left.op.tag == EXP and node.left.right.type == BINOPNode and node.left.right.op.tag == DIV and node.left.right.left.type == NUMNode and node.left.right.right.type == NUMNode:
                        numerator = visit_NUMNode(node.left.right.left)
                        left = visit_NUMNode(node.left.right.right)
                        if round_complex(num) == round_complex(left) and round_complex(numerator) == 1:
                            node_string = stringify_node(node.left.left, self.var)
                            self.solution.append("((" + node_string + ")^(" + str(round_complex(numerator)) + "/" + str(round_complex(left)) + "))^" + str(round_complex(num)) + " = " + node_string)
                            self.update_eqn_string("((" + node_string + ")^(" + str(round_complex(numerator)) + "/" + str(round_complex(left)) + "))^" + str(round_complex(num)), node_string)
                            ans_node = node.left.left
                            new_tree = self.replace_node(self.tree, node, ans_node)
                            if new_tree is None:
                                raise Exception("{} was not replaced by {}.".format(node, ans_node))
                            self.tree = deepcopy(new_tree)
                            return True
                if node.right.type == FUNCNode and node.right.op.value.lower() in "log" and hash(node.left) == hash(node.right.args[1]) and node.left.__repr__() == node.right.args[1].__repr__():
                    node_string = stringify_node(node.right.args[0], self.var)
                    base_string = stringify_node(node.left, self.var)
                    if "(" + base_string + ")^log(" in stringify_node(node, self.var):
                        self.solution.append("(" + base_string + ")^log(" + node_string + "," + base_string + ") = " + node_string)
                        self.update_eqn_string("(" + base_string + ")^log(" + node_string + "," + base_string + ")", node_string)
                    else:
                        self.solution.append(base_string + "^log(" + node_string + "," + base_string + ") = " + node_string)
                        self.update_eqn_string(base_string + "^log(" + node_string + "," + base_string + ")", node_string)
                    ans_node = node.right.args[0]
                    new_tree = self.replace_node(self.tree, node, ans_node)
                    if new_tree is None:
                        raise Exception("{} was not replaced by {}.".format(node, ans_node))
                    self.tree = deepcopy(new_tree)
                    return True
            chk = self.find_operator(node.left, ops_flag=ops_flag)
            if not chk:
                chk = self.find_operator(node.right, ops_flag=ops_flag)
            return chk
        elif node.type == FUNCNode and node.op.value.lower() in list_of_func and ops_flag:
            if node.op.value.lower() == "sqrt" and node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                num = visit_NUMNode(node.args[0].right)
                if round_complex(num) == 2:
                    node_string = stringify_node(node.args[0].left, self.var)
                    if "sqrt((" + node_string + ")^2)" in stringify_node(node, self.var):
                        self.solution.append("sqrt((" + node_string + ")^2)" + " = abs(" + node_string + ")")
                        self.update_eqn_string("sqrt((" + node_string + ")^2)", "abs(" + node_string + ")")
                    else:
                        self.solution.append("sqrt(" + node_string + "^2)" + " = abs(" + node_string + ")")
                        self.update_eqn_string("sqrt(" + node_string + "^2)", "abs(" + node_string + ")")
                    ans_node = FuncNode(Token(("abs", FUNC)), [node.args[0].left])
                    new_tree = self.replace_node(self.tree, node, ans_node)
                    if new_tree is None:
                        raise Exception("{} was not replaced by {}.".format(node, ans_node))
                    self.tree = deepcopy(new_tree)
                    return True
            elif node.op.value.lower() in trig_op_dict and node.args[0].type == FUNCNode and node.args[0].op.value.lower() == trig_op_dict[node.op.value.lower()]:
                node_string = stringify_node(node.args[0].args[0], self.var)
                self.solution.append(node.op.value.lower() + "(" + node.args[0].op.value.lower() + "(" + node_string + ")) = " + node_string)
                self.update_eqn_string(node.op.value.lower() + "(" + node.args[0].op.value.lower() + "(" + node_string + "))", node_string)
                ans_node = node.args[0].args[0]
                new_tree = self.replace_node(self.tree, node, ans_node)
                if new_tree is None:
                    raise Exception("{} was not replaced by {}.".format(node, ans_node))
                self.tree = deepcopy(new_tree)
                return True
            elif node.op.value.lower() == "ln" and node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].left.type == NUMNode:
                num = visit_NUMNode(node.args[0].left)
                if round_complex(num) == math.e:
                    node_string = stringify_node(node.args[0].right, self.var)
                    if "ln(#e^(" + node_string + "))" in stringify_node(node, self.var):
                        self.solution.append("ln(#e^(" + node_string + ")) = " + node_string)
                        self.update_eqn_string("ln(#e^(" + node_string + "))", node_string)
                    else:
                        self.solution.append("ln(#e^" + node_string + ") = " + node_string)
                        self.update_eqn_string("ln(#e^" + node_string + ")", node_string)
                    ans_node = node.args[0].right
                    new_tree = self.replace_node(self.tree, node, ans_node)
                    if new_tree is None:
                        raise Exception("{} was not replaced by {}.".format(node, ans_node))
                    self.tree = deepcopy(new_tree)
                    return True
            elif node.op.value.lower() == "abs_ln" and node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].left.type == NUMNode:
                num = visit_NUMNode(node.args[0].left)
                if round_complex(num) == math.e:
                    node_string = stringify_node(node.args[0].right, self.var)
                    if "ln|#e^(" + node_string + ")|" in stringify_node(node, self.var):
                        self.solution.append("ln|#e^(" + node_string + ")| = " + node_string)
                        self.update_eqn_string("ln|#e^(" + node_string + ")|", node_string)
                    else:
                        self.solution.append("ln|#e^" + node_string + "| = " + node_string)
                        self.update_eqn_string("ln|#e^" + node_string + "|", node_string)
                    ans_node = node.args[0].right
                    new_tree = self.replace_node(self.tree, node, ans_node)
                    if new_tree is None:
                        raise Exception("{} was not replaced by {}.".format(node, ans_node))
                    self.tree = deepcopy(new_tree)
                    return True
            elif node.op.value.lower() == "log" and node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and \
            hash(node.args[1]) == hash(node.args[0].left) and node.args[1].__repr__() == node.args[0].left.__repr__():
                node_string = stringify_node(node.args[0].right, self.var)
                base_string = stringify_node(node.args[1], self.var)
                if "log((" + base_string + ")^(" + node_string + ")," + base_string + ")" in stringify_node(node, self.var):
                    self.solution.append(
                        "log((" + base_string + ")^(" + node_string + ")," + base_string + ") = " + node_string)
                    self.update_eqn_string("log((" + base_string + ")^(" + node_string + ")," + base_string + ")",
                                           node_string)
                elif "log(" + base_string + "^(" + node_string + ")," + base_string + ")" in stringify_node(node, self.var):
                    self.solution.append("log(" + base_string + "^(" + node_string + ")," + base_string + ") = " + node_string)
                    self.update_eqn_string("log(" + base_string + "^(" + node_string + ")," + base_string + ")", node_string)
                elif "log((" + base_string + ")^" + node_string + "," + base_string + ")" in stringify_node(node, self.var):
                    self.solution.append("log((" + base_string + ")^" + node_string + "," + base_string + ") = " + node_string)
                    self.update_eqn_string("log((" + base_string + ")^" + node_string + "," + base_string + ")", node_string)
                else:
                    self.solution.append(
                        "log(" + base_string + "^" + node_string + "," + base_string + ") = " + node_string)
                    self.update_eqn_string("log(" + base_string + "^" + node_string + "," + base_string + ")",
                                           node_string)
                ans_node = node.args[0].right
                new_tree = self.replace_node(self.tree, node, ans_node)
                if new_tree is None:
                    raise Exception("{} was not replaced by {}.".format(node, ans_node))
                self.tree = deepcopy(new_tree)
                return True
            new_args = []
            num_chk = True
            for arg in node.args:
                temp = None
                if arg.type == NUMNode:
                    temp = stringify(self.goto_NUMNode(arg))
                if not is_number(temp):
                    num_chk = False
                    break
                else:
                    new_args.append(temp)
            if num_chk:
                if node.op.value.lower() == "log":
                    eqn_string = "log("+new_args[0]+","+new_args[1]+")"
                else:
                    eqn_string = node.op.value.lower()+"("+new_args[0]+")"
                ans = self.compute(eqn_string)
                ans_token = Token((stringify(ans), NUMBER))
                ans_node = NumberNode(ans_token)
                new_tree = self.replace_node(self.tree, node, ans_node)
                if new_tree is None:
                    raise Exception("{} was not replaced by {}.".format(node, ans_node))
                self.tree = deepcopy(new_tree)
                return True
            for arg in node.args:
                chk = self.find_operator(arg, ops_flag=ops_flag)
                if chk:
                    break
            return chk
        elif node.type == UNIOPNode:
            right = None
            if node.right.type == UNIOPNode:
                minus_cnt, ans_node = self.reduce_uni_ops(node)
                if minus_cnt % 2 != 0:
                    ans_node = UniOpNode(Token(("-", MINUS)), ans_node)
                self.solution.append(stringify_node(node, self.var) + " = " + stringify_node(ans_node, self.var))
                self.update_eqn_string(stringify_node(node, self.var), stringify_node(ans_node, self.var))
                new_tree = self.replace_node(self.tree, node, ans_node)
                if new_tree is None:
                    raise Exception("{} was not replaced by {}.".format(node, ans_node))
                self.tree = deepcopy(new_tree)
                return True
            elif node.right.type == NUMNode:
                right = stringify(visit_NUMNode(node.right))
            if is_number(right):
                ans = self.compute(node.op.value+right)
                ans_token = Token((stringify(ans), NUMBER))
                ans_node = NumberNode(ans_token)
                new_tree = self.replace_node(self.tree, node, ans_node)
                if new_tree is None:
                    raise Exception("{} was not replaced by {}.".format(node, ans_node))
                self.tree = deepcopy(new_tree)
                return True
            return self.find_operator(node.right, ops_flag=ops_flag)
        else:
            return False

    def reduce_uni_ops(self, node: AST, minus_cnt : int = 0) -> Tuple[int, AST]:
        """Method is meant to reduce the amount of uniops in an equation"""
        if node.type == UNIOPNode:
            if node.op.tag == "-":
                return self.reduce_uni_ops(node.right, minus_cnt=minus_cnt+1)
            return self.reduce_uni_ops(node.right, minus_cnt=minus_cnt)
        return minus_cnt, node

    def compute(self, eqn_string: str) -> Union[int, complex, float]:
        """Method computes values using Arithmetic class and returns answer"""
        lexer = Lexer(eqn_string)
        tokens = lexer.obilisk_lex()
        combinator = TreeBuilder(tokens)
        tree,_ = combinator.build_tree()
        arithmetic = Arithmetic(eqn_string, tokens, tree)
        ans = arithmetic.calculate()
        ans = round_complex(ans)
        if "The final answer" not in arithmetic.solution[1]:
            self.solution.append(arithmetic.solution[1])
            self.update_eqn_string(eqn_string, stringify(ans))
        return ans

    def replace_node(self, node: AST, old_node: AST, new_node: AST) -> AST:
        """Replaces old node from the self.tree with new node"""
        if hash(node) == hash(old_node) and node.__repr__() == old_node.__repr__():
            return new_node
        elif node.type == BINOPNode:
            new_left = self.replace_node(node.left, old_node, new_node)
            new_right = self.replace_node(node.right, old_node, new_node)
            return BinOpNode(new_left, node.op, new_right)
        elif node.type == UNIOPNode:
            new_right = self.replace_node(node.right, old_node, new_node)
            return UniOpNode(node.op, new_right)
        elif node.type == FUNCNode:
            new_args = []
            for arg in node.args:
                new_args.append(self.replace_node(arg, old_node, new_node))
            return FuncNode(node.op, new_args)
        elif node.type in (NUMNode, VARNode):
            return node

    def check_for_substitution(self):
        """This method checks if it's possible to substitute an expression to simplify the problem"""
        i = len(self.exprs) - 1
        while i != -1:
            if stringify_node(self.exprs[i], self.var) != self.var:
                if self.expr_on_both_sides(self.tree, self.exprs[i]):
                    print("{} is on both sides. Look {}".format(stringify_node(self.exprs[i], self.var), self.eqn_string))
                    sub_var = sub_var_dict[self.var]
                    sub_var_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("*", MUL)),VariableNode(Token((sub_var, VARIABLE))))
                    og_eqn_string = self.eqn_string
                    expr_string = stringify_node(self.exprs[i], self.var)
                    if "(" + expr_string + ")" in self.eqn_string:
                        self.solution.append("(" + expr_string + ") = " + sub_var)
                        self.update_eqn_string("(" + expr_string + ")", sub_var)
                    if expr_string in self.eqn_string:
                        self.solution.append(expr_string + " = " + sub_var)
                        self.update_eqn_string(expr_string, sub_var)
                    if self.var in self.eqn_string:
                        k = 0
                        while k != len(self.solution):
                            if sub_var in self.solution[k]:
                                if self.solution[k-1] == "------" and self.solution[k+1] == "------":
                                    del self.solution[k-1:k+2]
                                    k -= 2
                                else:
                                    del self.solution[k]
                                    k -= 1
                            k += 1
                        self.eqn_string = og_eqn_string
                    else:
                        if self.subs is None:
                            self.subs = {sub_var_node: self.exprs[i]}
                        else:
                            self.subs[sub_var_node] = self.exprs[i]
                        new_tree = self.replace_node(self.tree, self.exprs[i], sub_var_node)
                        self.tree = deepcopy(new_tree)
                        self.var = sub_var
                        lexer = Lexer(self.eqn_string)
                        self.eqn_tokens = lexer.obilisk_lex()
                        combinator = TreeBuilder(self.eqn_tokens, has_var=True)
                        _, self.exprs = combinator.build_tree()
                        i = len(self.exprs)
            i -= 1


    def expr_on_both_sides(self, node: AST, expr: AST) -> bool:
        """Goes through AST to check if an AST appears consistently on either side of the equation"""
        if node.__repr__() == expr.__repr__():
            return True
        elif node.type == BINOPNode:
            if node.op.tag == EQUAL:
                chk = self.expr_on_both_sides(node.left, expr)
                if chk:
                    return self.expr_on_both_sides(node.right, expr)
                return chk
            elif node.op.tag in (PLUS, MINUS):
                return self.expr_on_both_sides(node.left, expr) and self.expr_on_both_sides(node.right, expr)
            else:
                return self.expr_on_both_sides(node.left, expr) or self.expr_on_both_sides(node.right, expr)
        elif node.type == UNIOPNode:
            return self.expr_on_both_sides(node.right, expr)
        elif node.type == FUNCNode:
            for arg in node.args:
                chk = self.expr_on_both_sides(arg, expr)
                if chk:
                    return True
            return False
        else:
            return False

    def remove_redundant_br(self):
        """Remove redundant expressions"""
        while self.redundant_exp_br(self.tree):
            continue

    def redundant_exp_br(self, node: AST) -> bool:
        """Climbs AST and expands exponent expressions if possible"""
        if node.type == BINOPNode:
            if node.op.tag == EXP and node.left.type == BINOPNode and node.left.op.tag in (MUL, DIV):
                if not check_mono(node):
                    if node.right.type == NUMNode:
                        exponent = str(round_complex(visit_NUMNode(node.right)))
                    else:
                        exponent = stringify_node(node.right, self.var)
                    numer_node = BinOpNode(node.left.left, Token(("^", EXP)), node.right)
                    denom_node = BinOpNode(node.left.right, Token(("^", EXP)), node.right)
                    ans_node = BinOpNode(numer_node, node.left.op, denom_node)
                    self.solution.append("("+stringify_node(node.left, self.var) + ")^" + exponent + " = (" + stringify_node(ans_node, self.var) + ")")
                    self.update_eqn_string("("+stringify_node(node.left, self.var) + ")^" + exponent, "(" + stringify_node(ans_node, self.var) + ")")
                    new_tree = self.replace_node(self.tree, node, ans_node)
                    if new_tree is None:
                        raise Exception("{} was not replaced by {}.".format(node, ans_node))
                    self.tree = deepcopy(new_tree)
                    return True
            elif node.op.tag in (PLUS, MINUS) and node.left.type == BINOPNode and node.right.type == BINOPNode and \
            node.left.op.tag == DIV and node.right.op.tag == DIV:
                left_numer = stringify_node(node.left.left, self.var)
                left_denom = stringify_node(node.left.right, self.var)
                right_numer = stringify_node(node.right.left, self.var)
                right_denom = stringify_node(node.right.right, self.var)
                self.solution.append("(" + left_numer + "/" + left_denom + ")" + node.op.value + "(" + right_numer
                                         + "/" + right_denom + ") = ((" + left_numer + "*" + right_denom + ")" +
                                         node.op.value + "(" + right_numer + "*" + left_denom + "))/(" + left_denom
                                         + "*" + right_denom + ")")
                self.update_eqn_string(
                    "(" + left_numer + "/" + left_denom + ")" + node.op.value + "(" + right_numer
                    + "/" + right_denom + ")", "((" + left_numer + "*" + right_denom + ")" +
                    node.op.value + "(" + right_numer + "*" + left_denom + "))/(" + left_denom
                    + "*" + right_denom + ")")
                numer_left_node = BinOpNode(node.left.left, Token(("*", MUL)), node.right.right)
                numer_right_node = BinOpNode(node.right.left, Token(("*", MUL)), node.left.right)
                numer_node = BinOpNode(numer_left_node, node.op, numer_right_node)
                denom_node = BinOpNode(node.left.right, Token(("*", MUL)), node.right.right)
                ans_node = BinOpNode(numer_node, Token(("/", DIV)), denom_node)
                new_tree = self.replace_node(self.tree, node, ans_node)
                if new_tree is None:
                    raise Exception("{} was not replaced by {}.".format(node, ans_node))
                self.tree = deepcopy(new_tree)
                lexer = Lexer(self.eqn_string)
                self.eqn_tokens = lexer.obilisk_lex()
                combinator = TreeBuilder(self.eqn_tokens, has_var=True)
                _, self.exprs = combinator.build_tree()
                return True
            chk = self.redundant_exp_br(node.left)
            if not chk:
                chk = self.redundant_exp_br(node.right)
            return chk
        elif node.type == FUNCNode:
            for arg in node.args:
                chk = self.redundant_exp_br(arg)
                if chk:
                    break
            return chk
        elif node.type == UNIOPNode:
            return self.redundant_exp_br(node.right)
        else:
            return False

    def find_divisors(self):
        while self.find_divisor(self.tree):
            continue

    def find_divisor(self, node: AST) -> bool:
        """Method climbs AST and find any divisors. Stores them in asymptotes attribute."""
        if node.type == BINOPNode:
            if node.op.tag == DIV:
                if self.divisors is None:
                    self.divisors = [node.right]
                    return True
                else:
                    div_chk = False
                    for div in self.divisors:
                        if div.__repr__() == node.right.__repr__():
                            div_chk = True
                    if not div_chk:
                        self.divisors.append(node.right)
                        return True
            return self.find_divisor(node.left) or self.find_divisor(node.right)
        elif node.type == FUNCNode:
            for arg in node.args:
                chk = self.find_divisor(arg)
                if chk:
                    return True
        elif node.type == UNIOPNode:
            return self.find_divisor(node.right)
        return False

    def multiply_div(self):
        """Method finds the divisions in the AST and adds to the numerator the divisor"""
        if self.divisors:
            for div in self.divisors:
                while True:
                    new_tree = self.propogate_div(self.tree, div)
                    if stringify_node(new_tree, self.var) == stringify_node(self.tree, self.var):
                        break
                    self.tree = deepcopy(new_tree)
                self.solution.append("Multiply the equation by " + stringify_node(div, self.var))
                self.update_eqn_string(self.eqn_string, stringify_node(new_tree, self.var))
                self.compute_low_hanging_fruit()

    # TODO - Deal with cases where divisor was in a function.
    def propogate_div(self, node: AST, div: AST, exponent=NumberNode(Token(("1", NUMBER)))) -> AST:
        """Method climbs AST and propogates the given divisor"""
        if self.push_div_deeper(node, div):
            if node.type == BINOPNode:
                if node.op.tag == EXP:
                    match = re.search(poly_regex, stringify_node(node, self.var))
                    if match is None:
                        return BinOpNode(self.propogate_div(node.left, div, exponent=self.find_operator(BinOpNode(BinOpNode(NumberNode(Token(("1"
                                            , NUMBER))), Token(("/", DIV)), exponent), Token(("*", MUL)), node.right))), node.op, node.right)
                    return node
                elif node.op.tag in (MUL, DIV):
                    if "/"+stringify_node(div, self.var) in stringify_node(node, self.var) and stringify_node(div, self.var)+"*" not in stringify_node(node, self.var):
                        if "/"+stringify_node(div, self.var) in stringify_node(node.left, self.var):
                            return BinOpNode(self.propogate_div(node.left, div, exponent=exponent), node.op, node.right)
                        return BinOpNode(node.left, node.op, self.propogate_div(node.right, div, exponent=exponent))
                    elif "/("+stringify_node(div, self.var) in stringify_node(node, self.var) and stringify_node(div, self.var)+")*" not in stringify_node(node, self.var):
                        if "/("+stringify_node(div, self.var) in stringify_node(node.left, self.var):
                            return BinOpNode(self.propogate_div(node.left, div, exponent=exponent), node.op, node.right)
                        return BinOpNode(node.left, node.op, self.propogate_div(node.right, div, exponent=exponent))
            return BinOpNode(self.propogate_div(node.left, div, exponent=exponent), node.op, self.propogate_div(node.right, div, exponent=exponent))
        if stringify_node(div, self.var)+"*" in stringify_node(node, self.var) or stringify_node(div, self.var)+")*" in stringify_node(node, self.var):
            return node
        if exponent.type == NUMNode:
            exp = round_complex(visit_NUMNode(exponent))
            if exp < 1:
                raise Exception("exponent is less than 1. Cannot foil out this term.")
            elif exp == 1:
                pass
            else:
                div = BinOpNode(div, Token(("^", EXP)), exponent)
        else:
            div = BinOpNode(div, Token(("^", EXP)), exponent)
        if node.type == BINOPNode:
            if stringify_node(div, self.var) in stringify_node(node.left, self.var):
                return node
            elif node.op.tag == DIV and stringify_node(div, self.var) not in stringify_node(node.left, self.var):
                numer_node = BinOpNode(div, Token(("*", MUL)), node.left)
                ans_node = BinOpNode(numer_node, Token(("/", DIV)), node.right)
                return ans_node
        ans_node = BinOpNode(div, Token(("*", MUL)), node)
        return ans_node

    def push_div_deeper(self, node: AST, div: AST) -> bool:
        """Method checks if divisor should be multiplied at this top level node or deeper"""
        if node.type == BINOPNode:
            if node.op.tag == DIV and stringify_node(div, self.var) in stringify_node(node.right, self.var):
                return False
            elif node.op.tag == MUL and stringify_node(div, self.var) in stringify_node(node, self.var):
                if "/"+stringify_node(div, self.var) in stringify_node(node, self.var) and stringify_node(div, self.var)+"*" not in stringify_node(node, self.var):
                    return True
                elif "/("+stringify_node(div, self.var) in stringify_node(node, self.var) and stringify_node(div, self.var)+")*" not in stringify_node(node, self.var):
                    return True
                return False
            elif node.op.tag in (MUL, DIV):
                match = re.search(poly_regex, stringify_node(node, self.var))
                if match is not None:
                    return False
                return self.push_div_deeper(node.left, div) or self.push_div_deeper(node.right, div)
            elif node.op.tag == EXP:
                match = re.search(poly_regex, stringify_node(node, self.var))
                if match is not None:
                    return False
            return True
        return False

    def remove_repeating_div(self, node: AST, div: AST) -> AST:
        """Method takes a node, removes the div in the numerator and denominator, returns a new node"""
        if node.type == BINOPNode:
            if node.left.__repr__() == div.__repr__():
                left_chk = True
            else:
                left_chk = False
                new_left = self.remove_repeating_div(node.left, div)
            if node.right.__repr__() == div.__repr__():
                right_chk = True
            else:
                right_chk = False
                new_right = self.remove_repeating_div(node.right, div)
            if left_chk and right_chk:
                return NumberNode(Token(("1", NUMBER)))
            elif left_chk and not right_chk:
                return new_right
            elif not left_chk and right_chk:
                return new_left
            else:
                return BinOpNode(new_left, node.op, new_right)
        elif node.type == FUNCNode:
            new_args = []
            for arg in node.args:
                new_args.append(self.remove_repeating_div(arg, div))
            return FuncNode(node.op, new_args)
        elif node.type == UNIOPNode:
            return UniOpNode(node.op, self.remove_repeating_div(node.right, div))
        else:
            return node

    def foil_monomials(self):
        """Method will foil out all monomial terms."""
        while self.compute_monomial_ops(self.tree):
            # print(stringify_node(self.tree, self.var),"\n")
            continue
        new_rhs = NumberNode(Token(("0", NUMBER)))
        if new_rhs.__repr__() != self.tree.right.__repr__():
            new_lhs = BinOpNode(self.tree.left, Token(("-", MINUS)), self.tree.right)
            new_tree = BinOpNode(new_lhs, Token(("=", EQUAL)), new_rhs)
            self.solution.append("Moving right hand side of the equation to the left hand side...")
            self.solution.append("------")
            self.eqn_string = "("+stringify_node(self.tree.left, self.var)+")-("+stringify_node(self.tree.right, self.var)+")=0"
            self.solution.append(self.eqn_string)
            self.solution.append("------")
            self.tree = deepcopy(new_tree)
            for i in self.solution:
                print(i)
            self.compute_low_hanging_fruit()
        while self.compute_monomial_ops(self.tree):
            # print(stringify_node(self.tree, self.var),"\n")
            continue

    def compute_monomial_ops(self, node: AST):
        """Method defining specific monomial operations"""
        if node.type == BINOPNode:
            if node.op.tag == EXP:
                if node.right.type == NUMNode:
                    if re.match(poly_power_regex, stringify_node(node, self.var)) is not None:
                        node_string = stringify_node(node, self.var)
                        new_node = self.exp_foiling(node)
                        self.exprs.append(new_node)
                        new_string = stringify_node(new_node, self.var)
                        # new_string = new_string.replace("(", '')
                        # new_string = new_string.replace(")", '')
                        new_string = "(" + new_string + ")"
                        self.update_eqn_string(node_string, new_string)
                        new_tree = self.replace_node(self.tree, node, new_node)
                        self.tree = deepcopy(new_tree)
                        return True
            elif node.op.tag == MUL and not check_mono(node):
                if not self.lg_poly_add(node):
                    left_string = stringify_node(node.left, self.var)
                    if re.search(poly_power_regex, left_string) is None and "*" not in left_string:
                        left_string = "(" + left_string + ")"
                        right_string = stringify_node(node.right, self.var)
                        if re.search(poly_power_regex, right_string) is None and "*" not in right_string:
                            right_string = "(" + right_string + ")"
                            left_match = re.match(poly_regex_2, left_string)
                            right_match = re.match(poly_regex_2, right_string)
                            if left_match is not None and right_match is not None:
                                node_string = stringify_node(node, self.var)
                                new_node = self.foiling(node.left, node.right)
                                self.exprs.append(new_node)
                                new_string = stringify_node(new_node, self.var)
                                new_string = "(" + new_string + ")"
                                self.update_eqn_string(node_string, new_string)
                                new_tree = self.replace_node(self.tree, node, new_node)
                                self.tree = deepcopy(new_tree)
                                return True
            elif node.op.tag in (PLUS, MINUS):
                if node.left.type != NUMNode and node.right.type != NUMNode and not check_mono(node.left) and not check_mono(node.right):
                    left_string = stringify_node(node.left, self.var)
                    if re.search(poly_power_regex, left_string) is None and "*" not in left_string:
                        left_string = "(" + left_string + ")"
                        right_string = stringify_node(node.right, self.var)
                        if re.search(poly_power_regex, right_string) is None and "*" not in right_string:
                            right_string = "(" + right_string + ")"
                            left_match = re.match(poly_regex_2, left_string)
                            right_match = re.match(poly_regex_2, right_string)
                            if left_match is not None and right_match is not None:
                                #print(left_string, node.op.value, right_string)
                                new_node = self.poly_add(node.left, node.right, node.op.value)
                                self.exprs.append(new_node)
                                new_string = stringify_node(new_node, self.var)
                                # new_string = "(" + new_string + ")"
                                #print("HERE", left_string+node.op.value+right_string)
                                self.update_eqn_string(left_string+node.op.value+right_string, new_string, br_override=True)
                                new_tree = self.replace_node(self.tree, node, new_node)
                                self.tree = deepcopy(new_tree)
                                return True
            return self.compute_monomial_ops(node.left) or self.compute_monomial_ops(node.right)
        return False

    def lg_poly_add(self, node: AST) -> bool:
        """Method checks if a node contains the addition of two large polynomials"""
        lg_poly_chk = False
        if node.left.type == BINOPNode and node.left.op.tag in (PLUS, MINUS):
            l_c = False
            r_c = False
            for e in self.exprs:
                if stringify_node(e, self.var) == stringify_node(node.left.left, self.var):
                    l_c = True
                elif stringify_node(e, self.var) == stringify_node(node.left.right, self.var):
                    r_c = True
            if l_c and r_c:
                lg_poly_chk = True
        if node.right.type == BINOPNode and node.right.op.tag in (PLUS, MINUS):
            l_c = False
            r_c = False
            for e in self.exprs:
                if stringify_node(e, self.var) == stringify_node(node.right.left, self.var):
                    l_c = True
                elif stringify_node(e, self.var) == stringify_node(node.right.right, self.var):
                    r_c = True
            if l_c and r_c:
                lg_poly_chk = True
        return lg_poly_chk

    def exp_foiling(self, node: AST) -> AST:
        """Method foils out monomials with exponents"""
        exponent = round_complex(visit_NUMNode(node.right))
        if exponent%2 == 0 and exponent > 2:
            # it's even
            node_string = stringify_node(node.left, self.var)
            node_string = node_string.replace("(", '')
            node_string = node_string.replace(")", '')
            node_string = "(" + node_string + ")^" + str(exponent)
            self.solution.append("\nFoiling " + node_string + " ->")
            new_exp = int(exponent/2)
            if new_exp > 1:
                inter_node = BinOpNode(self.foiling(node.left, node.left), node.op, NumberNode(Token((str(new_exp), NUMBER))))
            else:
                inter_node = self.foiling(node.left, node.left)
            inter_string = stringify_node(inter_node.left, self.var)
            inter_string = inter_string.replace("(", '')
            inter_string = inter_string.replace(")", '')
            inter_string = "(" + inter_string + ")^" + str(new_exp)
            self.solution.append(node_string + " = " + inter_string)
            #self.update_eqn_string(node_string, inter_string)
            if new_exp > 1:
                return self.exp_foiling(inter_node)
            return inter_node
        elif exponent == 2:
            node_string = stringify_node(node.left, self.var)
            node_string = node_string.replace("(", '')
            node_string = node_string.replace(")", '')
            node_string = "(" + node_string + ")^" + str(exponent)
            self.solution.append("\nFoiling " + node_string + " ->")
            return self.foiling(node.left, node.left)
        else:
            #it's odd
            left_node = node.left
            node_string = stringify_node(node.left, self.var)
            node_string = node_string.replace("(", '')
            node_string = node_string.replace(")", '')
            node_string = "(" + node_string + ")^" + str(exponent)
            self.solution.append("\nFoiling " + node_string + " ->")
            right_node = BinOpNode(node.left, node.op, NumberNode(Token((str(exponent-1), NUMBER))))
            inter = self.exp_foiling(right_node)
            return self.foiling(left_node, inter)

    def foiling(self, left_node: AST, right_node: AST, verbose: bool = True) -> AST:
        """Method multiplies two polynomials"""
        left_string = stringify_node(left_node, self.var)
        left_string = "(" + left_string + ")"
        right_string = stringify_node(right_node, self.var)
        right_string = "(" + right_string + ")"
        #print(f"{left_string}*{right_string}")
        left_coeff = self.get_coeff(left_node)
        right_coeff = self.get_coeff(right_node)
        ans_coeff = []
        for coeff_l, deg_l in left_coeff:
            for coeff_r, deg_r in right_coeff:
                new_coeff = coeff_l*coeff_r
                if new_coeff != 0:
                    ans_coeff.append((new_coeff, deg_l+deg_r))
        if not ans_coeff:
            return NumberNode(Token(("0", NUMBER)))
        highest_deg = ans_coeff[0][1]
        new_ans = []
        for i in range(highest_deg, -1, -1):
            temp = 0
            for c, d in ans_coeff:
                if i == d:
                    temp += c
            if temp != 0:
                new_ans.append((temp, i))
        ans_node = self.build_node_from_coeff(new_ans)
        ans_string = stringify_node(ans_node, self.var)
        if verbose:
            self.solution.append(left_string + "*" + right_string + " = " + ans_string)
        return ans_node

    def build_node_from_coeff(self, new_ans: List[Tuple[Union[int, complex, float], int]]) -> AST:
        """This method takes a coeff list and returns an AST"""
        ans_node = None
        for coeff, deg in new_ans:
            if deg == 0:
                if ans_node is None:
                    ans_node = NumberNode(Token((str(coeff), NUMBER)))
                else:
                    if type(coeff) is complex:
                        right_term = NumberNode(Token((str(coeff), NUMBER)))
                        ans_node = BinOpNode(ans_node, Token(("+", PLUS)), right_term)
                    else:
                        right_term = NumberNode(Token((str(abs(coeff)), NUMBER)))
                        if coeff < 0:
                            ans_node = BinOpNode(ans_node, Token(("-", MINUS)), right_term)
                        else:
                            ans_node = BinOpNode(ans_node, Token(("+", PLUS)), right_term)
            elif deg == 1:
                if ans_node is None:
                    ans_node = BinOpNode(NumberNode(Token((str(coeff), NUMBER))), Token(("*", MUL)),
                                         VariableNode(Token((self.var, VARIABLE))))
                else:
                    if type(coeff) is complex:
                        right_term = BinOpNode(NumberNode(Token((str(coeff), NUMBER))), Token(("*", MUL)),
                                               VariableNode(Token((self.var, VARIABLE))))
                        ans_node = BinOpNode(ans_node, Token(("+", PLUS)), right_term)
                    else:
                        right_term = BinOpNode(NumberNode(Token((str(abs(coeff)), NUMBER))), Token(("*", MUL)),
                                               VariableNode(Token((self.var, VARIABLE))))
                        if coeff < 0:
                            ans_node = BinOpNode(ans_node, Token(("-", MINUS)), right_term)
                        else:
                            ans_node = BinOpNode(ans_node, Token(("+", PLUS)), right_term)
            else:
                if ans_node is None:
                    base = BinOpNode(NumberNode(Token((str(coeff), NUMBER))), Token(("*", MUL)),
                                     VariableNode(Token((self.var, VARIABLE))))
                    exponent = NumberNode(Token((str(deg), NUMBER)))
                    ans_node = BinOpNode(base, Token(("^", EXP)), exponent)
                else:
                    exponent = NumberNode(Token((str(deg), NUMBER)))
                    if type(coeff) is complex:
                        base = BinOpNode(NumberNode(Token((str(coeff), NUMBER))), Token(("*", MUL)),
                                         VariableNode(Token((self.var, VARIABLE))))
                        right_term = BinOpNode(base, Token(("^", EXP)), exponent)
                        ans_node = BinOpNode(ans_node, Token(("+", PLUS)), right_term)
                    else:
                        base = BinOpNode(NumberNode(Token((str(abs(coeff)), NUMBER))), Token(("*", MUL)),
                                         VariableNode(Token((self.var, VARIABLE))))
                        right_term = BinOpNode(base, Token(("^", EXP)), exponent)
                        if coeff < 0:
                            ans_node = BinOpNode(ans_node, Token(("-", MINUS)), right_term)
                        else:
                            ans_node = BinOpNode(ans_node, Token(("+", PLUS)), right_term)
        return ans_node

    def poly_add(self, left_node: AST, right_node: AST, op: str, verbose: bool = True):
        """This method performs polynomial addition"""
        left_string = stringify_node(left_node, self.var)
        left_string = "(" + left_string + ")"
        right_string = stringify_node(right_node, self.var)
        right_string = "(" + right_string + ")"
        left_coeff = self.get_coeff(left_node)
        right_coeff = self.get_coeff(right_node)
        highest_deg_l = self.get_highest_deg(left_coeff)
        highest_deg_r = self.get_highest_deg(right_coeff)
        ans_coeff = []
        indexes_to_skip = []
        if highest_deg_l >= highest_deg_r:
            for k in range(len(left_coeff)):
                if indexes_to_skip and k in indexes_to_skip:
                    pass
                else:
                    temp = left_coeff[k][0]
                    for i in range(len(left_coeff)):
                        if left_coeff[k][1] == left_coeff[i][1] and i != k:
                            temp = self.add_coeff(temp, "+", left_coeff[i][0])
                            indexes_to_skip.append(i)
                    for coeff_r, deg_r in right_coeff:
                        if left_coeff[k][1] == deg_r:
                            temp = self.add_coeff(temp, op, coeff_r)
                    if temp != 0:
                        ans_coeff.append((temp, left_coeff[k][1]))
        else:
            for k in range(len(right_coeff)):
                if indexes_to_skip and k in indexes_to_skip:
                    pass
                else:
                    if op == "-":
                        temp = -1*right_coeff[k][0]
                    else:
                        temp = right_coeff[k][0]
                    for i in range(len(right_coeff)):
                        if right_coeff[k][1] == right_coeff[i][1] and i != k:
                            if op == "-":
                                temp = self.add_coeff(temp, "+", -1*right_coeff[i][0])
                            else:
                                temp = self.add_coeff(temp, "+", right_coeff[i][0])
                            indexes_to_skip.append(i)
                    for coeff_l, deg_l in left_coeff:
                        if right_coeff[k][1] == deg_l:
                            temp = self.add_coeff(coeff_l, "+", temp)
                    if temp != 0:
                        ans_coeff.append((temp, right_coeff[k][1]))
        ans_coeff = self.reorder_terms(ans_coeff)
        ans_node = self.build_node_from_coeff(ans_coeff)
        ans_string = stringify_node(ans_node, self.var)
        ans_string = ans_string.replace("(", '')
        ans_string = ans_string.replace(")", '')
        if verbose:
            self.solution.append(left_string + op + right_string + " = " + ans_string)
        return ans_node

    def add_coeff(self, left: Union[int, complex, float], op: str, right: Union[int, complex, float]):
        """Add or subtracts two coefficients"""
        if op == "+":
            return left+right
        elif op == "-":
            return left-right

    def get_highest_deg(self, coeff: List[Tuple[Union[int, float, complex], int]]) -> int:
        highest_deg = coeff[0][1]
        for _, deg in coeff:
            if deg > highest_deg:
                highest_deg = deg
        return highest_deg

    def reorder_terms(self, coeff: List[Tuple[Union[int, float, complex], int]]) -> List[Tuple[Union[int, float, complex], int]]:
        """Method will reorder terms in descending order from largest power to constants"""
        highest_deg = 0
        for _, deg in coeff:
            if deg > highest_deg:
                highest_deg = deg
        new_coeff = []
        for i in range(highest_deg, -1, -1):
            for k in range(len(coeff)):
                if coeff[k][1] == i:
                    new_coeff.append((coeff[k][0], coeff[k][1]))
        return new_coeff

    def basic_algebraic_solving(self, node: AST = None, rounding: bool = True) -> List[Union[int, float, complex]]:
        """Method solves equations where the highest degree in the polynomial is one"""
        if node is None:
            coeff = self.get_coeff(self.tree)
        else:
            coeff = self.get_coeff(node)
        #ax + b = 0
        if coeff[0][1] == 1:
            a = coeff[0][0]
        else:
            raise ValueError("Polynomial must be linear")
        if coeff[1][1] == 0:
            b = -coeff[1][0]
        else:
            raise ValueError("Polynomial must be linear")
        if rounding:
            return [round_complex(b/a)]
        return [b/a]

    def quadratic_formula(
            self,
            node: AST = None,
            verbose: bool = True,
            rounding: bool = True
    ) -> List[Union[int, float, complex]]:
        """Method solves a quadratic using the quadratic formula"""
        if node is None:
            coeff = self.get_coeff(self.tree)
        else:
            coeff = self.get_coeff(node)
        if len(coeff) != 4:
            raise ValueError("Quadratics must have 3 terms.")
        if coeff[-1] != 0.0:
            # TODO - We need to move all numerical values from RHS to LHS. RHS must be equal to 0
            pass
        if verbose:
            self.solution.append("")
            print("\n-- Using the quadratic formula --")
            self.solution.append("-- Using the quadratic formula --")
            print("ax^2 + bx + c = 0")
            self.solution.append("ax^2 + bx + c = 0")
            print("x = (-b +/- √(b^2 - 4ac))/2a\n")
            self.solution.append("x = (-b +/- √(b^2 - 4ac))/2a")

        a = coeff[0][0]
        b = coeff[1][0]
        c = coeff[2][0]
        if verbose:
            self.solution.append("")
            print("a = " + str(a))
            self.solution.append("a = " + str(a))
            print("b = " + str(b))
            self.solution.append("b = " + str(b))
            print("c = " + str(c))
            self.solution.append("c = " + str(c))
            print("")

        ans = [0, 0]
        ans[0] = ((-1 * b) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        ans[-1] = ((-1 * b) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

        if verbose:
            self.solution.append("\nThe final answers are:")
        for i in range(len(ans)):
            if rounding:
                ans[i] = round_complex(ans[i])
            if verbose:
                self.solution.append(str(ans[i]))

        return ans

    def cardano(
            self,
            node: AST = None,
            verbose: bool = True,
            rounding: bool = True
    ) -> List[Union[int, float, complex]]:
        """Root finding formula for cubic polynomials."""
        if node is None:
            coeff = self.get_coeff(self.tree)
        else:
            coeff = self.get_coeff(node)
        if len(coeff) != 5:
            raise ValueError("Cubics must have 4 terms.")
        if coeff[-1] != 0.0:
            # TODO - We need to move all numerical values from RHS to LHS. RHS must be equal to 0
            pass
        a = coeff[0][0]
        b = coeff[1][0]
        c = coeff[2][0]
        d = coeff[3][0]
        # depressed cubic
        p = ((3 * a * c) - (b ** 2)) / (9 * (a ** 2))
        q = ((9 * a * b * c) - (27 * (a ** 2) * d) - (2 * (b ** 3))) / (54 * (a ** 3))
        s = cube_root((q) + (((p) ** 3) + ((q) ** 2)) ** (1 / 2))
        t = cube_root((q) - (((p) ** 3) + ((q) ** 2)) ** (1 / 2))
        if verbose:
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
            print("a = " + str(a))
            self.solution.append("a = " + str(a))
            print("b = " + str(b))
            self.solution.append("b = " + str(b))
            print("c = " + str(c))
            self.solution.append("c = " + str(c))
            print("d = " + str(d))
            self.solution.append("d = " + str(d))
            print("")
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
            self.solution.append("")
            print("s = (q + √(p^3 + q^2))^(1/3) = " + str(s))
            self.solution.append("s = (q + √(p^3 + q^2))^(1/3) = " + str(s))
            print("t = (q - √(p^3 + q^2))^(1/3) = " + str(t) + "\n")
            self.solution.append("t = (q - √(p^3 + q^2))^(1/3) = " + str(t))
        ans = [0] * 3
        ans[0] = s + t - (b / (3 * a))
        ans[1] = (-1 * ((s + t) / 2)) - (b / (3 * a)) + (((1j * (3 ** 0.5)) / 2) * (s - t))
        ans[-1] = (-1 * ((s + t) / 2)) - (b / (3 * a)) - (((1j * (3 ** 0.5)) / 2) * (s - t))
        if verbose:
            self.solution.append("\nThe final answers are:")
        for i in range(len(ans)):
            if rounding:
                ans[i] = round_complex(ans[i])
            if verbose:
                self.solution.append(str(ans[i]))
        return ans

    def ferrari(
            self,
            node: AST = None,
            verbose: bool = True,
            rounding: bool = True,
    ) -> List[Union[int, float, complex]]:
        """Root finding formula for quartic polynomials."""
        if node is None:
            coeff = self.get_coeff(self.tree)
        else:
            coeff = self.get_coeff(node)
        if len(coeff) != 6:
            raise ValueError("Quartics must have 5 terms.")
        if coeff[-1] != 0.0:
            # TODO - We need to move all numerical values from RHS to LHS. RHS must be equal to 0
            pass
        a = coeff[0][0]
        b = coeff[1][0]
        c = coeff[2][0]
        d = coeff[3][0]
        e = coeff[4][0]
        # depressed quartic
        p = (c / a) - ((3 * b ** 2) / (8 * a ** 2))
        q = (d / a) - ((b * c) / (2 * a ** 2)) + (b ** 3 / (8 * a ** 3))
        r = (e / a) - ((b * d) / (4 * a ** 2)) + (((b ** 2) * c) / (16 * a ** 3)) - ((3 * b ** 4) / (256 * a ** 4))
        depressed = "y^4+" + str(p) + "y^2+" + str(q) + "y+" + str(r) + "=0"
        #resolvent cubic
        resolvent = "8z^3+" + str(-4 * p) + "z^2+" + str(-8 * r) + "z+" + str((4 * p * r) - (q ** 2)) + "=0"
        if verbose:
            self.solution.append("")
            print("\n-- Using Ferrari's Method: --")
            self.solution.append("-- Using Ferrari's Method: --")
            print("ax^4 + bx^3 + cx^2 + dx + e = 0\n")
            self.solution.append("ax^4 + bx^3 + cx^2 + dx + e = 0")
            self.solution.append("")
            print("a = " + str(a))
            self.solution.append("a = " + str(a))
            print("b = " + str(b))
            self.solution.append("b = " + str(b))
            print("c = " + str(c))
            self.solution.append("c = " + str(c))
            print("d = " + str(d))
            self.solution.append("d = " + str(d))
            print("e = " + str(e))
            self.solution.append("e = " + str(e))
            print("")
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
            self.solution.append("")
            print("p = ((c/a) - 3b^2)/8a^2 = " + str(p))
            self.solution.append("p = ((c/a) - 3b^2)/8a^2 = " + str(p))
            print("q = ((d/a) - bc/(2a^2) + b^3)/8a^3 = " + str(q))
            self.solution.append("q = ((d/a) - bc/(2a^2) + b^3)/8a^3 = " + str(q))
            print("r = ((e/a) - bd/(4a^2) + b^2c/16a^3 - 3b^4)/256a^4 = " + str(q) + "\n")
            self.solution.append("r = ((e/a) - bd/(4a^2) + b^2c/16a^3 - 3b^4)/256a^4 = " + str(q))
            self.solution.append("")
            print("Depressed quartic is " + depressed + "\n")
            self.solution.append("Depressed quartic is " + depressed)
            self.solution.append("")
            # resolvent cubic
            print("Resolvent cubic: 8z^3 - 4pz^2 - 8rz + (4pr - q^2) = 0")
            self.solution.append("Resolvent cubic: 8z^3 - 4pz^2 - 8rz + (4pr - q^2) = 0")
            print(resolvent)
            self.solution.append(resolvent)
            self.solution.append("")
            print("the values of z of " + resolvent + " are")
            self.solution.append("the values of z of " + resolvent + " are")

        lexer = Lexer(resolvent)
        tokens = lexer.obilisk_lex()
        tree_build = TreeBuilder(tokens, has_var=True)
        tree, _ = tree_build.build_tree()
        cubic = Algebra(resolvent, tokens, tree, lexer.vars[0])
        cubic_ans = cubic.isolate(verbose=verbose, rounding=rounding)
        if verbose:
            for i in cubic.solution:
                self.solution.append(i)
            for i in cubic_ans:
                print(i)
                self.solution.append(str(i))
        for i in cubic_ans:
            try:
                if verbose:
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
                if verbose:
                    print("attempt failed...")
                    self.solution.append("attempt failed...")
            else:
                break
        if verbose:
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
        ans[1] = y_two - (b / (4 * a))
        ans[2] = y_three - (b / (4 * a))
        ans[-1] = y_four - (b / (4 * a))
        if verbose:
            self.solution.append("x = " + str(y_one) + "-(" + str(b) + "/(4*" + str(a) + "))")
            self.solution.append("x = " + str(y_two) + "-(" + str(b) + "/(4*" + str(a) + "))")
            self.solution.append("x = " + str(y_three) + "-(" + str(b) + "/(4*" + str(a) + "))")
            self.solution.append("x = " + str(y_four) + "-(" + str(b) + "/(4*" + str(a) + "))")
            self.solution.append("\nThe final answers are:")
        for i in range(len(ans)):
            if rounding:
                ans[i] = round_complex(ans[i])
            if verbose:
                self.solution.append(str(ans[i]))
        return ans

    def lg_poly_root_finding(self):
        """This method solves polynomials of power 5 or greater using the Jenkins-Traub algorithm"""
        self.solution.append("Checking if 0 is a root via synthetic division...")
        coeff = self.get_coeff(self.tree)
        test = self.lin_divide(coeff, [(1, 1), (0, 0)])
        test_node = self.build_node_from_coeff(test[:-1])
        test_node_string = stringify_node(test_node, self.var)
        if test[-1][1] == -1:
            remainder = test[-1][0]
        else:
            raise ValueError(f"Linear division returned a polynomial with last term not power of -1 {test}")
        if remainder < 0:
            test_node_string += "-" + str(abs(remainder)) + "/" + self.var
        elif remainder > 0:
            test_node_string += "+" + str(remainder) + "/" + self.var
        print("(" + stringify_node(self.tree.lhs, self.var) + ")/" + self.var + " = " + test_node_string + "\n")
        self.solution.append("(" + stringify_node(self.tree.lhs, self.var) + ")/" + self.var + " = " + test_node_string)
        if remainder == 0:
            success_attempt = False
            ans = []
            i = 1
            while not success_attempt:
                if len(test) - 2 >= 5:
                    try:
                        del test[-1]
                        ans = self.real_poly(test)
                    except ZeroDivisionError:
                        string = self.var
                        test = self.lin_divide(test, [(1, 1), (0, 0)])
                        print("0 might be a repeated root, trying again...\n")
                        self.solution.append("0 might be a repeated root, trying again...")
                        self.solution.append("")
                        self.solution.append("")

                        remainder = test[-1][0]
                        test_node = self.build_node_from_coeff(test[:-1])
                        test_node_string = stringify_node(test_node, self.var)
                        if test[-1][1] == -1:
                            remainder = test[-1][0]
                        else:
                            raise ValueError(
                                f"Linear division returned a polynomial with last term not power of -1 {test}")
                        if remainder < 0:
                            test_node_string += "-" + str(abs(remainder)) + "/" + self.var
                        elif remainder > 0:
                            test_node_string += "+" + str(remainder) + "/" + self.var
                        print("(" + stringify_node(self.tree.lhs,
                                                   self.var) + ")/" + self.var + " = " + test_node_string + "\n")
                        self.solution.append(
                            "(" + stringify_node(self.tree.lhs, self.var) + ")/" + self.var + " = " + test_node_string)
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
                    ans = self.ferrari(test_node)
                    success_attempt = True
                else:
                    break
            for s in range(1, i + 1):
                ans.insert(0, 0)
        else:
            print("0 is not a root\n")
            self.solution.append("0 is not a root")
            ans = self.real_poly(coeff)
        print(ans)
        for i in range(0, len(ans)):
            if round(ans[i].imag, 5) == 0:
                ans[i] = ans[i].real
        return ans

    def lin_divide(
            self,
            dividend: List[Tuple[Union[int, float, complex], int]],
            divisor: List[Tuple[Union[int, float, complex], int]],
            rounding: bool = True
    ) -> List[Tuple[Union[int, float, complex], int]]:
        """Function does synthetic division of a polynomial. Divisor can only be a linear polynomial."""
        #print(f"\ndividend is {dividend}")
        highest_deg_denom = self.get_highest_deg(divisor)
        if highest_deg_denom == 1:
            denom_root = self.basic_algebraic_solving(self.build_node_from_coeff(divisor), rounding=rounding)
        elif highest_deg_denom == 2:
            denom_root = self.quadratic_formula(self.build_node_from_coeff(divisor), verbose=False, rounding=rounding)
        elif highest_deg_denom == 3:
            denom_root = self.cardano(self.build_node_from_coeff(divisor), verbose=False, rounding=rounding)
        elif highest_deg_denom == 4:
            denom_root = self.ferrari(self.build_node_from_coeff(divisor), verbose=False, rounding=rounding)
        # else:
        for root in denom_root:
            a = root
            #print(f"root is in lin_divide {root}")
            b = 0
            ans = []
            rng = 0
            if len(dividend) == self.get_highest_deg(dividend)+2:
                rng = 1
            for i in range(len(dividend)-rng):
                if rounding:
                    ans.append((round_complex(dividend[i][0] + b), dividend[i][1]-1))
                    b = round_complex(ans[-1][0] * a)
                else:
                    ans.append((dividend[i][0]+b, dividend[i][1]-1))
                    b = ans[-1][0] * a
                #print(f"ans is now {ans} b is now {b}")
            dividend = ans
        return ans

    def normalize(
            self,
            eqn: List[Tuple[Union[int, float, complex], int]],
            rounding: bool = True
    ) -> List[Tuple[Union[int, float, complex], int]]:
        """Method will normalize a polynomial or divide by the coefficient of the highest order term"""
        eqn = self.reorder_terms(eqn)
        print(f"eqn to normalze {eqn}")
        while eqn[0][0] == 0 and len(eqn) > 1:
            if eqn[0][0] == 0:
                del eqn[0]
                print(eqn)
        if len(eqn) == 1:
            return eqn
        c = eqn[0][0]
        new_eqn = []
        for i in range(len(eqn)):
            if rounding:
                new_eqn.append((round_complex(eqn[i][0]/c), eqn[i][1]))
            else:
                new_eqn.append((eqn[i][0]/c, eqn[i][1]))
        return new_eqn

    def poly_coeff_derivative(
            self,
            eqn: List[Tuple[Union[int, float, complex], int]],
            rounding: bool = True
    ) -> List[Tuple[Union[int, float, complex], int]]:
        """Method takes derivative of a polynomial in coeff form"""
        d_eqn = []
        rng = 1
        if eqn[-1] == (0, 0):
            rng = 2
        for i in range(len(eqn)-rng):
            if rounding:
                d_eqn.append((round_complex(eqn[i][0]*eqn[i][1]), eqn[i][1]-1))
            else:
                d_eqn.append((eqn[i][0]*eqn[i][1], eqn[i][1]-1))
        d_eqn.append((0, 0))
        return d_eqn

    def evaluate(
            self,
            eqn: List[Tuple[Union[int, float, complex], int]],
            value: Union[int, complex, float]
    ) -> Union[int, complex, float]:
        """Method evaluates a polynomial in coeff form at a given value"""
        ans = 0
        for coeff, deg in eqn:
            ans += coeff*(value**deg)
        print(f"the answer of {eqn} evaluated at {value} is {ans}")
        return ans

    def cauchy_poly(
            self,
            eqn: List[Tuple[Union[int, float, complex], int]],
            rounding: bool = True
    ) -> List[Tuple[Union[int, float, complex], int]]:
        """Normalizes polynomial and takes the absolute value of each coefficient."""
        cauchy = []
        norm = self.normalize(eqn, rounding=rounding)
        rng = 1
        if norm[-1] == (0, 0):
            rng = 2
        for i in range(len(norm)-rng):
            cauchy.append((abs(norm[i][0]), norm[i][1]))
        cauchy.append((-1 * abs(norm[i + 1][0]), norm[i + 1][1]))
        return cauchy

    # TODO - Add argument to turn off rounding
    def real_poly(self, eqn: List[Tuple[Union[int, float, complex], int]]) -> List[Union[int, float, complex]]:
        """Top level function which calls the rpoly, Jenkins-Traub algorithm."""
        num_roots = self.get_highest_deg(eqn)
        print(f"Num of roots is {num_roots}")
        ans = []
        # Fundamental theorem of algebra says number of highest exponent is the number of roots
        i = 0
        while i != num_roots - 1:
            ans.append(self.rpoly(eqn))
            #print(f"WE GOT A ROOT IT {ans[-1]}")
            divisor = [(1, 1), (-ans[-1], 0)]
            eqn = self.lin_divide(eqn, divisor, rounding=False)
            if round_complex(eqn[-1][0], decimal_place=8) == 0:
                del eqn[-1]
            #print("Now eqn is ", eqn)
            i += 1
        ans.append(self.basic_algebraic_solving(self.build_node_from_coeff(eqn)))
        return ans

    def rpoly(self, eqn: List[Tuple[Union[int, float, complex], int]]) -> Union[int, float, complex]:
        """RPOLY Jenkins-Traub algorithm for polynomial root finding."""
        eqn_norm = self.normalize(eqn, rounding=False)
        #print(f"Normalized eqn = {eqn_norm}")
        # Stage 1: No-shift process. Assuming M = 5
        K = self.poly_coeff_derivative(eqn_norm, rounding=False)
        #print(f"Der of norm (K) is {K}")
        for i in range(0, 5):
            constant = -1 * self.evaluate(K, 0) / self.evaluate(eqn_norm, 0)
            P_z = self.foiling(
                self.build_node_from_coeff(eqn_norm),
                self.build_node_from_coeff([(constant, 0)]),
                verbose=False
            )
            #print(stringify_node(P_z, self.var))
            K_prime = self.poly_add(self.build_node_from_coeff(K), P_z, "+", verbose=False)
            #print(stringify_node(K_prime, self.var))
            divisor = [(1, 1), (0, 0)]
            K = self.lin_divide(self.get_coeff(K_prime), divisor, rounding=False)
            #print(f"K is now {K}")
            if round_complex(K[-1][0], decimal_place=8) == 0 and K[-1][1] == -1:
                del K[-1]
            #print(K)
        # Stage 2: Fixed-shift Process
        #print("Stage 2 Baby")
        t_curr = t_old = t_new = None
        stage_two_success = False
        root_found = False
        while not root_found:
            while not stage_two_success:
                s = self.get_random_root(eqn_norm)
                # print("s",s)
                for i in range(0, 100):
                    constant = -1 * self.evaluate(K, s) / self.evaluate(eqn_norm, s)
                    P_z = self.foiling(
                        self.build_node_from_coeff(eqn_norm),
                        self.build_node_from_coeff([(constant, 0)]),
                        verbose=False
                    )
                    K_prime = self.poly_add(self.build_node_from_coeff(K), P_z, "+", verbose=False)
                    divisor = [(1, 1), (-1 * s, 0)]
                    new_K = self.lin_divide(self.get_coeff(K_prime), divisor, rounding=False)
                    if round_complex(new_K[-1][0] == 0, decimal_place=8) and new_K[-1][1] == -1:
                        del new_K[-1]
                    K_bar = self.normalize(K, rounding=False)
                    new_K_bar = self.normalize(new_K, rounding=False)
                    t_curr = s - self.evaluate(eqn_norm, s) / (1.0*self.evaluate(K_bar, s))
                    t_new = s - self.evaluate(eqn_norm, s) / (1.0*self.evaluate(new_K_bar, s))
                    if i > 0 and abs(t_curr - t_old) <= 0.5 * abs(t_old) and abs(t_new - t_curr) <= 0.5 * abs(t_curr):
                        stage_two_success = True
                        break
                    t_old = t_curr
                    K = new_K
                if not stage_two_success:
                    print("Retrying Stage 2")
            # Stage 3: Variable-shift process
            #print("Stage 3")
            old_err = self.evaluate(eqn_norm, s)
            curr_err = 1
            K_bar = self.normalize(K, rounding=False)
            s = s - (self.evaluate(eqn_norm, s) / self.evaluate(K_bar, s))
            old_s = 0
            stage_three_success = False
            for i in range(0, 10000):
                if abs(self.evaluate(eqn_norm, s)) < abs(10 ** (-5)):
                    stage_three_success = True
                    break
                constant = -1 * self.evaluate(K, s) / self.evaluate(eqn_norm, s)
                P_z = self.foiling(
                    self.build_node_from_coeff(eqn_norm),
                    self.build_node_from_coeff([(constant, 0)]),
                    verbose=False
                )
                K_prime = self.poly_add(self.build_node_from_coeff(K), P_z, "+", verbose=False)
                divisor = [(1, 1), (-1 * s, 0)]
                new_K = self.lin_divide(self.get_coeff(K_prime), divisor, rounding=False)
                if round_complex(new_K[-1][0] == 0, decimal_place=8) and new_K[-1][1] == -1:
                    del new_K[-1]
                new_K_bar = self.normalize(new_K, rounding=False)
                s = s - (self.evaluate(eqn_norm, s) / self.evaluate(new_K_bar, s))
                curr_err = self.evaluate(eqn_norm, s)
                K = new_K
                if math.isnan(s.imag) and math.isnan(s.real):
                    stage_three_success = False
                    break
            if stage_three_success:
                # print("Root is",s)
                root_found = True
            else:
                stage_two_success = False
        return s

    def get_random_root(self, eqn: List[Tuple[Union[int, float, complex], int]]) -> Union[int, float, complex]:
        """Function for finding random roots."""
        cauchy_eqn = self.cauchy_poly(eqn, rounding=False)
        beta = self.newton_raphson(cauchy_eqn)
        # print("beta",beta)
        rand = random.uniform(0, 1) * 2 * math.pi
        root = abs(beta) * cmath.exp(1j * rand)
        return root

    def newton_raphson(
            self,
            eqn: List[Tuple[Union[int, float, complex], int]],
            err: Union[int, float] = 1e-5
    ) -> Union[int, float, complex]:
        """Finds roots of polynomial using Newton-Raphson method."""
        der = self.poly_coeff_derivative(eqn, rounding=False)
        x = random.uniform(0, 1)
        while abs(self.evaluate(eqn, x)) > abs(err):
            x = x - ((self.evaluate(eqn, x)) / (self.evaluate(der, x)))
        return x

    def get_coeff(self, node: AST) -> List[Tuple[int, int]]:
        """This method will get all coefficients from a polynomial in standard form"""
        coeff = []
        coeff = self.goto_next_node(node, coeff)
        highest_deg = coeff[0][1]
        k = 0
        if len(coeff) == 1:
            coeff.append((0, 0))
        else:
            for i in range(highest_deg, -1, -1):
                if k < len(coeff):
                    if i != coeff[k][1]:
                        coeff.insert(k, (0, i))
                    if i == 0:
                        if coeff[-1][1] == 0 and coeff[-2][1] != 0:
                            coeff.append((0, 0))
                elif i == 0:
                    if coeff[-1][1] == 0 and coeff[-2][1] != 0:
                        coeff.append((0, 0))
                k += 1
        return coeff

    def goto_next_node(self, node: AST, coeff: List[Tuple[int, int]], multiplier=1, exponent=0):
        """Method to go through the AST of a standard polynomial"""
        num = None
        if node.type == BINOPNode:
            if node.op.tag in (PLUS, EQUAL):
                coeff = self.goto_next_node(node.left, coeff, multiplier=multiplier, exponent=exponent)
                #print(coeff, stringify_node(node, self.var))
                return self.goto_next_node(node.right, coeff, multiplier=multiplier, exponent=exponent)
            elif node.op.tag == MINUS:
                coeff = self.goto_next_node(node.left, coeff, multiplier=multiplier, exponent=exponent)
                return self.goto_next_node(node.right, coeff, multiplier=multiplier * -1, exponent=exponent)
            elif node.op.tag == MUL and node.left.type in (NUMNode, UNIOPNode):
                if node.right.type == VARNode:
                    return self.goto_next_node(node.left, coeff, multiplier=multiplier, exponent=1)
                elif node.right.type == BINOPNode and node.right.op.tag == EXP:
                    if node.right.right.type == NUMNode:
                        return self.goto_next_node(node.left, coeff, multiplier=multiplier,
                                            exponent=self.goto_NUMNode(node.right.right))
            elif node.op.tag == EXP:
                if node.left.type == BINOPNode and node.left.op.tag == MUL and node.left.left.type == NUMNode and node.left.right.type == VARNode:
                    return self.goto_next_node(node.left.left, coeff, multiplier=multiplier,
                                               exponent=self.goto_NUMNode(node.right))
        elif node.type == NUMNode:
            num = self.goto_NUMNode(node)
        elif node.type == UNIOPNode:
            if node.op.tag == PLUS:
                return self.goto_next_node(node.right, coeff, multiplier=multiplier * 1, exponent=exponent)
            elif node.op.tag == MINUS:
                return self.goto_next_node(node.right, coeff, multiplier=multiplier * -1, exponent=exponent)
        if num is not None:
            coeff.append((num * multiplier, exponent))
            return coeff

    def goto_NUMNode(self, node: NumberNode) -> Union[int, float, complex]:
        """Extract coefficients"""
        num = 0.0
        if node.tag == NUMBER:
            try:
                num = float(node.value)
            except ValueError:
                num = complex(node.value)
        elif node.tag == CONSTANT:
            if node.value in ("#pi", "#PI"):
                num = math.pi
            elif node.value in ("#e", "#E"):
                num = math.e
            elif node.value == "#C":
                num = 1
            else:
                raise ValueError("Constant {} is not recognized".format(node.value))
        if type(num) == float:
            if num.is_integer():
                return int(num)
        return num
