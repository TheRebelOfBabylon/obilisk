from parser.lexer import Token, EXP, EQUAL
from parser.ast import AST, BINOPNode, FUNCNode, UNIOPNode, VARNode, NUMNode

from typing import List, Union


def stringify_node(node: AST) -> str:
    """Function will take a node and turn it into a string"""
    if node.type == BINOPNode:
        temp = node.op.value
        if node.op.tag != EQUAL:
            if node.left.type == BINOPNode and node.left.op.tag != EXP:
                if node.left.type not in (NUMNode, VARNode):
                    temp = ")" + temp
            if node.right.type == BINOPNode and node.right.op.tag != EXP:
                if node.right.type not in (NUMNode, VARNode):
                    temp += "("
        left = stringify_node(node.left)
        if ")"+node.op.value in temp:
            left = "("+left
        right = stringify_node(node.right)
        if node.op.value+"(" in temp:
            right += ")"
        return left+temp+right
    elif node.type == UNIOPNode:
        right = stringify_node(node.right)
        return node.op.value+right
    elif node.type == FUNCNode:
        temp = node.op.value+"("
        for i in range(len(node.args)):
            if i < 1:
                temp += stringify_node(node.args[i])
            else:
                temp += ","+stringify_node(node.args[i])
        temp += ")"
        return temp
    elif node.type in (VARNode, NUMNode):
        return node.value


def inference_string(eqn_string: str, var: str) -> str:
    """Method will remove some parts of an equation which are redundant"""
    eqn_string = eqn_string.replace('1*' + var, var)
    return eqn_string.replace('(' + var + ')', var)


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
