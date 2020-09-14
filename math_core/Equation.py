from parser.lexer import Token
from parser.ast import AST

from typing import List, Union


class Equation:
    def __init__(self, eqn_string: str = None, tokens: List[Token] = None, tree: List[Union[AST, Token]] = None):
        self.eqn_string = eqn_string.replace(" ", "")
        self.eqn_tokens = tokens
        self.tree = tree
        self.solution = ["The inputted equation is "+self.eqn_string]

    def update_eqn_string(self, section_to_replace: str, new_section: str):
        """Method which updates the eqn string based on recent ops"""
        self.solution.append("------")
        if "("+section_to_replace+")" in self.eqn_string:
            self.eqn_string = self.eqn_string.replace("("+section_to_replace+")", new_section)
        else:
            self.eqn_string = self.eqn_string.replace(section_to_replace, new_section)
        self.solution.append(self.eqn_string)
        self.solution.append("------")
