from parser.lexer import Token
from parser.ast import AST

from typing import List, Union


class Equation:
    def __init__(self, eqn_string: str = None, tokens: List[Token] = None, tree: List[Union[AST, Token]] = None):
        self.eqn_string = eqn_string.replace(" ", "")
        self.eqn_tokens = tokens
        self.tree = tree
        self.solution = ["The inputted equation is "+self.eqn_string]
