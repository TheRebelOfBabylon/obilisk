"""
1. Check if equation is already in solvable format
2. Check if equation can be more easily solved by using substitution
3. Order equation into standard polynomial format
4. Solve
"""
from math_core.Equation import Equation
from parser.ast import AST, BINOPNode, VARNode, UNIOPNode, FUNCNode
from parser.lexer import Token, EQUAL, EXP
from math_core.algebra_formats import quadratic, NUM_OR_CONST, PLUS_MINUS

from typing import List, Union
from copy import deepcopy

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

    def check_solvability(self, format: AST) -> bool:
        """Method checks if the equation is already in a solvable format"""
        return self.climb_tree(self.tree, format)

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
