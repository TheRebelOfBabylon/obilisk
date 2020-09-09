from math_core.Equation import Equation
from math_core.Arithmetic import Arithmetic
from math_core.Algebra import Algebra
from math_core.algebra_formats import quadratic
from parser.lexer import Lexer
from parser.combinator import TreeBuilder

from typing import List, Tuple, Union
from copy import deepcopy


class Obilisk:
    def __init__(self, eqn_string: str):
        self.eqn_string = eqn_string
        self.tokens = None
        self.tree = None
        self.vars = None
        self.parse()

    def parse(self):
        """This method takes the inputted equation in string format, tokenizes it and creates an AST"""
        lexer = Lexer(self.eqn_string)
        self.tokens = lexer.obilisk_lex()
        self.vars = deepcopy(lexer.vars)
        tokens = TreeBuilder(self.tokens)
        self.tree = tokens.build_tree()


def decode(input_eqn: str) -> Union[List[str], int, float, complex]:
    """Function creates an Obilisk object, parses the function and then decides how to solve it."""
    obi = Obilisk(input_eqn)
    if not obi.vars:
        arithmetic = Arithmetic(obi.eqn_string, obi.tokens, obi.tree)
        return arithmetic.calculate(), arithmetic.solution
    elif len(obi.vars) == 1:
        algebra = Algebra(obi.eqn_string, obi.tokens, obi.tree, obi.vars[0])
        print(algebra.tree)
        return algebra.check_solvability(quadratic)
    else:
        eqn = Equation()
        eqn.solution.append("Multivariable problems are not yet supported.")
        return eqn.solution
