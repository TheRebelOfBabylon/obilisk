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
            return num.imag*1j
        elif num.imag == -0.0 or num.imag == 0 or pytest.approx(num.imag) == 0.0:
            return num.real
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
        for template, name in list_of_templates:
            temp_hash = hash(template)
            tree_hash = hash(self.tree)
            if temp_hash == tree_hash:
                return True, name
        return False, None

    def isolate(self, template: Tuple[AST, str]):
        """Method will take the equation in standard polynomial form and solve it"""
        if "quadratic" in template[1]:
            return self.quadratic_formula()

    def quadratic_formula(self) -> List[Union[int, float, complex]]:
        """Method solves a quadratic using the quadratic formula"""
        self.get_coeff(self.tree)
        if len(self.coeff) != 4 and self.coeff[-1] != 0.0:
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
        for i in range(len(ans)):
            ans[i] = round_complex(ans[i])
            self.solution.append(str(ans[i]))

        return ans

    def get_coeff(self):
        """This method will get all coefficients from a polynomial in standard form"""
        self.goto_next_node(self.tree)

    def goto_next_node(self, node: AST, multiplier=1):
        """Method to go through the AST of a standard polynomial"""
        # TODO - self.coeff should be a list of tuples: [0] is coeff, [1] is power
        num = None
        if node.type == BINOPNode:
            if node.op.tag in (PLUS, MINUS, EQUAL):
                self.goto_next_node(node.left, multiplier)
                self.goto_next_node(node.right, multiplier)
            elif node.op.tag == MUL and node.left.type in (NUMNode, UNIOPNode):
                if node.right.type == VARNode or node.right.op.tag == EXP:
                    self.goto_next_node(node.left, multiplier)
        elif node.type == NUMNode:
            num = self.goto_NUMNode(node)
        elif node.type == UNIOPNode:
            if node.op.tag == PLUS:
                self.goto_next_node(node.right, multiplier=multiplier*1)
            elif node.op.tag == MINUS:
                self.goto_next_node(node.right, multiplier=multiplier*-1)
        if num is not None:
            self.coeff.append(num*multiplier)

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
        return num

