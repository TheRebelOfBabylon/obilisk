"""
1. Check if equation is already in solvable format
2. Check if equation can be more easily solved by using substitution
3. Order equation into standard polynomial format
4. Solve
"""
from math_core.Equation import Equation
from parser.ast import AST, BINOPNode, VARNode, UNIOPNode, FUNCNode, UniOpNode, NumberNode, NUMNode
from parser.lexer import Token, EQUAL, EXP, MUL, PLUS, MINUS, NUMBER, CONSTANT
from math_core.algebra_formats import quadratic_left_full, quadratic_left_no_b, quadratic_left_no_c, quadratic_left_no_bc, \
     quadratic_right_full, quadratic_right_no_b, quadratic_right_no_c, quadratic_right_no_bc

from typing import List, Union, Tuple
from copy import deepcopy
import math
import pytest

list_of_templates = [
    quadratic_left_full,
    quadratic_left_no_b,
    quadratic_left_no_c,
    quadratic_left_no_bc,
    quadratic_right_full,
    quadratic_right_no_b,
    quadratic_right_no_c,
    quadratic_right_no_bc,
]


def round_complex(num: complex) -> Union[complex, float]:
    """Function will take a complex number and round its real and imaginary parts if they're extremely small"""
    if type(num) == complex:
        if num.real == -0.0 or num.real == 0 or pytest.approx(num.real) == 0.0:
            if num.imag == -0.0 or num.imag == 0 or pytest.approx(num.imag) == 0.0:
                return 0.0
            num = num.imag*1j
            if num.real == -0 or num.real == -0.0:
                num = 0+num.imag*1j
            return num
        elif num.imag == -0.0 or num.imag == 0 or pytest.approx(num.imag) == 0.0:
            num = num.real
            if num == -0 or num == -0.0:
                num = 0
            return num
    if type(num) == float:
        if num == -0.0:
            num = 0.0
    return num


class Algebra(Equation):
    def __init__(self, eqn_string: str = None, tokens: List[Token] = None, tree: List[Union[AST, Token]] = None, var: str = None):
        Equation.__init__(self, eqn_string, tokens, tree) #should this be super()?
        self.var = var
        self.lhs = None
        self.rhs = None
        self.coeff = []
        self.seperate_lhs_rhs()

    def __repr__(self):
        return 'Algebra(%s, %s)' % (self.lhs, self.rhs)

    def seperate_lhs_rhs(self):
        """Method takes the lhs and rhs of the AST and splits them"""
        if self.tree.type == BINOPNode:
            if self.tree.op.tag == EQUAL:
                self.lhs = deepcopy(self.tree.left)
                self.rhs = deepcopy(self.tree.right)
        elif self.tree.type == FUNCNode:
            if self.tree.op.value in ("solve", "isolate", "roots"):
                self.tree = deepcopy(self.tree.args[0])
                self.lhs = deepcopy(self.tree.left)
                self.rhs = deepcopy(self.tree.right)

    def check_solvability(self) -> Tuple[bool, str]:
        """Method checks if the equation is already in a solvable format"""
        tree_hash = hash(self.tree)
        for template, name in list_of_templates:
            temp_hash = hash(template)
            if temp_hash == tree_hash:
                return True, name
        return False, None

    def isolate(self):
        """Method will take the equation in standard polynomial form and solve it"""
        _, template_name = self.check_solvability()
        if template_name is not None:
            if "quadratic" in template_name:
                return self.quadratic_formula()

    def quadratic_formula(self) -> List[Union[int, float, complex]]:
        """Method solves a quadratic using the quadratic formula"""
        self.get_coeff()
        if len(self.coeff) != 4:
            raise ValueError("Quadratics must have 3 terms.")
        if self.coeff[-1] != 0.0:
            #TODO - We need to move all numerical values from RHS to LHS. RHS must be equal to 0
            pass
        self.solution.append("")
        print("\n-- Using the quadratic formula --")
        self.solution.append("-- Using the quadratic formula --")
        print("ax^2 + bx + c = 0")
        self.solution.append("ax^2 + bx + c = 0")
        print("x = (-b +/- √(b^2 - 4ac))/2a\n")
        self.solution.append("x = (-b +/- √(b^2 - 4ac))/2a")

        self.solution.append("")
        a = self.coeff[0][0]
        print("a = " + str(a))
        self.solution.append("a = " + str(a))
        b = self.coeff[1][0]
        print("b = " + str(b))
        self.solution.append("b = " + str(b))
        c = self.coeff[2][0]
        print("c = " + str(c))
        self.solution.append("c = " + str(c))
        print("")

        ans = [0, 0]
        ans[0] = ((-1 * b) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        ans[-1] = ((-1 * b) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

        self.solution.append("\nThe final answers are:")
        for i in range(len(ans)):
            ans[i] = round_complex(ans[i])
            self.solution.append(str(ans[i]))

        return ans

    def get_coeff(self):
        """This method will get all coefficients from a polynomial in standard form"""
        self.goto_next_node(self.tree)
        highest_deg = self.coeff[0][1]
        k = 0
        for i in range(highest_deg, -1, -1):
            if i != self.coeff[k][1]:
                self.coeff.insert(k, (0, i))
            if i == 0:
                if self.coeff[-1][1] == 0 and self.coeff[-2][1] != 0:
                    self.coeff.append((0, 0))
            k += 1

    def goto_next_node(self, node: AST, multiplier=1, exponent=0):
        """Method to go through the AST of a standard polynomial"""
        num = None
        if node.type == BINOPNode:
            if node.op.tag in (PLUS, EQUAL):
                self.goto_next_node(node.left, multiplier=multiplier, exponent=exponent)
                self.goto_next_node(node.right, multiplier=multiplier, exponent=exponent)
            elif node.op.tag == MINUS:
                self.goto_next_node(node.left, multiplier=multiplier, exponent=exponent)
                self.goto_next_node(node.right, multiplier=multiplier*-1, exponent=exponent)
            elif node.op.tag == MUL and node.left.type in (NUMNode, UNIOPNode):
                if node.right.type == VARNode:
                    self.goto_next_node(node.left, multiplier=multiplier, exponent=1)
                elif node.right.type == BINOPNode and node.right.op.tag == EXP:
                    if node.right.right.type == NUMNode:
                        self.goto_next_node(node.left, multiplier=multiplier, exponent=self.goto_NUMNode(node.right.right))
        elif node.type == NUMNode:
            num = self.goto_NUMNode(node)
        elif node.type == UNIOPNode:
            if node.op.tag == PLUS:
                self.goto_next_node(node.right, multiplier=multiplier*1, exponent=exponent)
            elif node.op.tag == MINUS:
                self.goto_next_node(node.right, multiplier=multiplier*-1, exponent=exponent)
        if num is not None:
            self.coeff.append((num*multiplier, exponent))

    def goto_NUMNode(self, node: NumberNode):
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
            else:
                raise ValueError("Constant {} is not recognized".format(node.value))
        if type(num) == float:
            if num.is_integer():
                return int(num)
        return num

