"""
1. Check if equation is already in solvable format
2. Check if equation can be more easily solved by using substitution
3. Order equation into standard polynomial format
4. Solve
"""
from math_core.Equation import Equation
from parser.ast import AST, BINOPNode, VARNode, UNIOPNode, FUNCNode, UniOpNode, NumberNode, NUMNode, CONSTNode
from parser.lexer import Token, EQUAL, EXP, MUL, PLUS, MINUS
from math_core.algebra_formats import quadratic_left_full, quadratic_left_no_b, quadratic_left_no_c, quadratic_left_no_bc, \
    NUM_OR_CONST, quadratic_right_full, quadratic_right_no_b, quadratic_right_no_c, quadratic_right_no_bc

from typing import List, Union, Tuple
from copy import deepcopy
import math

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

class Algebra(Equation):
    def __init__(self, eqn_string: str = None, tokens: List[Token] = None, tree: List[Union[AST, Token]] = None, var: str = None):
        Equation.__init__(self, eqn_string, tokens, tree) #should this be super()?
        self.var = var
        self.lhs = None
        self.rhs = None
        self.coeff = None
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
            check = self.climb_tree(self.tree, template)
            if check:
                return True, name
        return False, None

    def climb_tree(self, actual_tree: AST, template: AST) -> bool:
        """Method climbs the tree if the corresponding nodes are the same"""
        if actual_tree.type == BINOPNode and template.type == BINOPNode:
            #checking to see if it's the right power
            if actual_tree.op.tag == EXP:
                if actual_tree.right.value == template.right.value:
                    return True
            else:
                if actual_tree.op.tag in template.op.tag:
                    check_left = self.climb_tree(actual_tree.left, template.left)
                    if check_left:
                        return self.climb_tree(actual_tree.right, template.right)
        elif actual_tree.type == UNIOPNode:
            return self.climb_tree(actual_tree.right, template)
        elif actual_tree.type in NUM_OR_CONST and template.type in NUM_OR_CONST:
            if actual_tree.type in template.type:
                return True
        elif actual_tree.type == VARNode and template.type == VARNode:
            if actual_tree.type == template.type:
                return True
        return False

    def isolate(self, template: Tuple[AST, str]):
        """Method will take the equation in standard polynomial form and solve it"""
        if "quadratic" in template[1]:
            return self.quadratic_formula(template[0])

    def quadratic_formula(self, template: AST):
        """Method solves a quadratic using the quadratic formula"""
        self.coeff = [0]*4
        self.find_coeffs(self.tree, template)

    def find_coeffs(self, actual_tree: AST, template: AST):
        if actual_tree.type == BINOPNode and template.type == BINOPNode:
            if actual_tree.op.tag in template.op.tag:
                self.find_coeffs(actual_tree.left, template.left)
                self.find_coeffs(actual_tree.right, template.right)
        # elif actual_tree.type == UNIOPNode:
        #     self.resolve_UNIOPNode(actual_tree, template)
        elif actual_tree.type in NUM_OR_CONST and template.type in NUM_OR_CONST:
            self.resolve_NumberNode(actual_tree, template)

    # def resolve_UNIOPNode(self, node: UniOpNode, template: AST):
    #     """Method to evaluate UniOpNodes"""
    #     if node.op.tag == PLUS:
    #         return self.find_coeffs(+node.right, template)
    #     elif node.op.tag == MINUS:
    #         return self.find_coeffs(-node.right, template)

    def resolve_NumberNode(self, node: NumberNode, template: NumberNode):
        """Method to evaluate NumberNodes"""
        if node.type == NUMNode:
            try:
                num = float(node.value)
            except ValueError:
                num = complex(node.value)
        elif node.type == CONSTNode:
            if node.value in ("#pi", "#PI"):
                num = math.pi
            elif node.value in ("#e", "#E"):
                num = math.e
            else:
                raise ValueError("Constant {} is not recognized".format(node.value))
        if template.value == 'a':
            self.coeff[0] = num
        elif template.value == 'b':
            self.coeff[1] = num
        elif template.value == 'c':
            self.coeff[2] = num
        elif template.value == 'd':
            self.coeff[3] = num
