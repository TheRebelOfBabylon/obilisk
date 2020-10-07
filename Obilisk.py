from math_core.Equation import Equation
from math_core.Arithmetic import Arithmetic
from math_core.Algebra import Algebra
from math_core.Calculus import Calculus
from parser.lexer import Lexer
from parser.combinator import TreeBuilder
from parser.ast import FUNCNode, AST, BINOPNode, UNIOPNode

from typing import List, Tuple, Union
from copy import deepcopy

ALGEBRA = "algebra"
CALCULUS = "calculus"
DERIVATIVE = "derivative"
INTEGRAL = "integral"

class Obilisk:
    def __init__(self, eqn_string: str):
        self.eqn_string = eqn_string
        self.tokens = None
        self.tree = None
        self.type = None
        self.vars = None
        self.exprs = None
        self.parse()

    def parse(self):
        """This method takes the inputted equation in string format, tokenizes it and creates an AST"""
        lexer = Lexer(self.eqn_string)
        self.tokens = lexer.obilisk_lex()
        self.vars = deepcopy(lexer.vars)
        if self.vars:
            tokens = TreeBuilder(self.tokens, has_var=True)
        else:
            tokens = TreeBuilder(self.tokens)
        self.tree, self.exprs = tokens.build_tree()

    def identify_type_of_eqn(self) -> str:
        """This method will check if the first node in the tree is a function or look in the tree for derivative operations"""
        list_of_alg_funcs = ["solve", "isolate", "roots"]
        list_of_calc_funcs = ["integral", "derivative", "limit"]
        if self.tree.type == FUNCNode:
            if self.tree.op.value in list_of_alg_funcs:
                self.tree = deepcopy(self.tree.args[0])
                return ALGEBRA
            elif self.tree.op.value in list_of_calc_funcs:
                self.type = self.tree.op.value
                self.tree = deepcopy(self.tree.args[0])
                return CALCULUS
        if self.check_for_ddx(self.tree):
            return CALCULUS
        return ALGEBRA

    def check_for_ddx(self, node: AST) -> bool:
        """Method climbs tree checking for d/dx operators"""
        if node.type == BINOPNode:
            return self.check_for_ddx(node.left) or self.check_for_ddx(node.right)
        elif node.type == UNIOPNode:
            return self.check_for_ddx(node.right)
        elif node.type == FUNCNode:
            if "d/d" in node.op.value:
                return True
            for arg in node.args:
                if self.check_for_ddx(arg):
                    return True
        return False


def decode(input_eqn: str) -> Tuple[Union[int, float, complex, None], List[str]]:
    """Function creates an Obilisk object, parses the function and then decides how to solve it."""
    obi = Obilisk(input_eqn)
    if not obi.vars:
        arithmetic = Arithmetic(obi.eqn_string, obi.tokens, obi.tree)
        return arithmetic.calculate(), arithmetic.solution
    else:
        if obi.identify_type_of_eqn() == ALGEBRA:
            if len(obi.vars) > 1:
                eqn = Equation()
                eqn.solution.append("Multivariable problems are not yet supported.")
                return None, eqn.solution
            algebra = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs)
            return algebra.isolate(), algebra.solution
        elif obi.identify_type_of_eqn() == CALCULUS:
            if len(obi.vars) > 1:
                eqn = Equation()
                eqn.solution.append("Multivariable problems are not yet supported.")
                return None, eqn.solution
            calculus = Calculus(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0], obi.exprs, obi.type)
            return calculus.derive(), calculus.solution
