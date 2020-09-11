"""
1. Check if equation is already in solvable format
2. Check if equation can be more easily solved by using substitution
3. Order equation into standard polynomial format
4. Solve
"""
from parser.lexer import Lexer
from parser.combinator import TreeBuilder
from math_core.Equation import Equation
from parser.ast import AST, BINOPNode, VARNode, UNIOPNode, FUNCNode, UniOpNode, NumberNode, NUMNode
from parser.lexer import Token, EQUAL, EXP, MUL, PLUS, MINUS, NUMBER, CONSTANT
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
    quartic_right_no_de, quartic_right_no_e

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


def round_complex(num: complex) -> Union[complex, float]:
    """Function will take a complex number and round its real and imaginary parts if they're extremely small"""
    if type(num) == complex:
        if num.real == -0.0 or num.real == 0 or pytest.approx(num.real) == 0.0:
            if num.imag == -0.0 or num.imag == 0 or pytest.approx(num.imag) == 0.0:
                return 0.0
            num = num.imag * 1j
            if num.real == -0 or num.real == -0.0:
                num = 0 + num.imag * 1j
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


def cube_root(x: Union[int, float, complex]) -> Union[int, float, complex]:
    """Function takes the cubic root of a number. Created to ensure proper sign of answer is given."""
    if isinstance(x, complex):
        return x ** (1 / 3)
    else:
        if x >= 0.0:
            return x ** (1 / 3)
        else:
            return -(-x) ** (1 / 3)


class Algebra(Equation):
    def __init__(self, eqn_string: str = None, tokens: List[Token] = None, tree: List[Union[AST, Token]] = None,
                 var: str = None):
        Equation.__init__(self, eqn_string, tokens, tree)  # should this be super()?
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
        print("Tree hash ", tree_hash)
        print(self.tree)
        for template, name in list_of_templates:
            temp_hash = hash(template)
            if temp_hash == tree_hash:
                print("temp_hash ", temp_hash, name)
                return True, name
        return False, None

    def isolate(self):
        """Method will take the equation in standard polynomial form and solve it"""
        _, template_name = self.check_solvability()
        if template_name is not None:
            print(template_name)
            if "quadratic_left" in template_name:
                return self.quadratic_formula()
            elif "quadratic_right" in template_name:
                # TODO - We need to move all numerical values from RHS to LHS and all vars from RHS to LHS
                pass
            elif "cubic_left" in template_name:
                return self.cardano()
            elif "quartic_left" in template_name:
                return self.ferrari()

    def quadratic_formula(self) -> List[Union[int, float, complex]]:
        """Method solves a quadratic using the quadratic formula"""
        self.get_coeff()
        if len(self.coeff) != 4:
            raise ValueError("Quadratics must have 3 terms.")
        if self.coeff[-1] != 0.0:
            # TODO - We need to move all numerical values from RHS to LHS. RHS must be equal to 0
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

    def cardano(self) -> List[Union[int, float, complex]]:
        """Root finding formula for cubic polynomials."""
        self.get_coeff()
        if len(self.coeff) != 5:
            raise ValueError("Cubics must have 4 terms.")
        if self.coeff[-1] != 0.0:
            # TODO - We need to move all numerical values from RHS to LHS. RHS must be equal to 0
            pass
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
        a = self.coeff[0][0]
        print("a = " + str(a))
        self.solution.append("a = " + str(a))
        b = self.coeff[1][0]
        print("b = " + str(b))
        self.solution.append("b = " + str(b))
        c = self.coeff[2][0]
        print("c = " + str(c))
        self.solution.append("c = " + str(c))
        d = self.coeff[3][0]
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

        ans = [0] * 3
        ans[0] = s + t - (b / (3 * a))
        ans[1] = (-1 * ((s + t) / 2)) - (b / (3 * a)) + (((1j * (3 ** 0.5)) / 2) * (s - t))
        ans[-1] = (-1 * ((s + t) / 2)) - (b / (3 * a)) - (((1j * (3 ** 0.5)) / 2) * (s - t))

        self.solution.append("\nThe final answers are:")
        for i in range(len(ans)):
            ans[i] = round_complex(ans[i])
            self.solution.append(str(ans[i]))

        return ans

    def ferrari(self) -> List[Union[int, float, complex]]:
        """Root finding formula for quartic polynomials."""
        self.get_coeff()
        if len(self.coeff) != 6:
            raise ValueError("Quartics must have 5 terms.")
        if self.coeff[-1] != 0.0:
            # TODO - We need to move all numerical values from RHS to LHS. RHS must be equal to 0
            pass
        self.solution.append("")
        print("\n-- Using Ferrari's Method: --")
        self.solution.append("-- Using Ferrari's Method: --")
        print("ax^4 + bx^3 + cx^2 + dx + e = 0\n")
        self.solution.append("ax^4 + bx^3 + cx^2 + dx + e = 0")

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
        d = self.coeff[3][0]
        print("d = " + str(d))
        self.solution.append("d = " + str(d))
        e = self.coeff[4][0]
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
        resolvent = "8z^3+" + str(-4 * p) + "z^2+" + str(-8 * r) + "z+" + str((4 * p * r) - (q ** 2)) + "=0"
        print(resolvent)
        self.solution.append(resolvent)

        lexer = Lexer(resolvent)
        tokens = lexer.obilisk_lex()
        tree_build = TreeBuilder(tokens)
        tree = tree_build.build_tree()
        cubic = Algebra(resolvent, tokens, tree, lexer.vars[0])
        print("do we get here?")
        cubic_ans = cubic.isolate()
        print(cubic_ans)

        for i in cubic.solution:
            self.solution.append(i)

        self.solution.append("")
        print("the values of z of " + resolvent + " are")
        self.solution.append("the values of z of " + resolvent + " are")

        for i in cubic_ans:
            print(i)
            self.solution.append(str(i))

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
                self.goto_next_node(node.right, multiplier=multiplier * -1, exponent=exponent)
            elif node.op.tag == MUL and node.left.type in (NUMNode, UNIOPNode):
                if node.right.type == VARNode:
                    self.goto_next_node(node.left, multiplier=multiplier, exponent=1)
                elif node.right.type == BINOPNode and node.right.op.tag == EXP:
                    if node.right.right.type == NUMNode:
                        self.goto_next_node(node.left, multiplier=multiplier,
                                            exponent=self.goto_NUMNode(node.right.right))
        elif node.type == NUMNode:
            num = self.goto_NUMNode(node)
        elif node.type == UNIOPNode:
            if node.op.tag == PLUS:
                self.goto_next_node(node.right, multiplier=multiplier * 1, exponent=exponent)
            elif node.op.tag == MINUS:
                self.goto_next_node(node.right, multiplier=multiplier * -1, exponent=exponent)
        if num is not None:
            self.coeff.append((num * multiplier, exponent))

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
