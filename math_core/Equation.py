from parser.lexer import Token, EXP, EQUAL
from parser.ast import AST, BINOPNode, FUNCNode, UNIOPNode, VARNode, NUMNode

from typing import List, Union
import re


def stringify_node(node: AST, var: str) -> str:
    """Function will take a node and turn it into a string"""
    if node.type == BINOPNode:
        temp = node.op.value
        if node.op.tag != EQUAL:
            if node.left.type == BINOPNode and node.left.op.tag != EXP:
                if node.left.type not in (NUMNode, VARNode):
                    temp = ")" + temp
            elif node.op.tag == EXP and node.left.type == BINOPNode and node.left.op.tag == EXP:
                temp = ")" + temp
            if node.right.type == BINOPNode and node.right.op.tag != EXP:
                if node.right.type not in (NUMNode, VARNode):
                    temp += "("
        left = stringify_node(node.left, var)
        if ")"+node.op.value in temp:
            left = "("+left
        right = stringify_node(node.right, var)
        if node.op.value+"(" in temp:
            right += ")"
        return inference_string(left+temp+right, var)
    elif node.type == UNIOPNode:
        temp = node.op.value
        if node.right.type == BINOPNode:
            temp += "("
        right = stringify_node(node.right, var)
        if "(" in temp:
            right += ")"
        return inference_string(temp+right, var)
    elif node.type == FUNCNode:
        temp = node.op.value+"("
        for i in range(len(node.args)):
            if i < 1:
                temp += stringify_node(node.args[i], var)
            else:
                temp += ","+stringify_node(node.args[i], var)
        temp += ")"
        return inference_string(temp, var)
    elif node.type in (VARNode, NUMNode):
        return inference_string(node.value, var)


def inference_string(eqn_string: str, var: str) -> str:
    """Method will remove some parts of an equation which are redundant"""
    regex = r'\-?\(\-?[0-9]+(\.[0-9]*)?\*[a-zA-Z_]\)'
    match = re.search(regex, eqn_string)
    if match is not None:
        match_wo_br_or_mul = match.group().replace("(", '')
        match_wo_br_or_mul = match_wo_br_or_mul.replace(")",'')
        match_wo_br_or_mul = match_wo_br_or_mul.replace("*", '')
        if match_wo_br_or_mul == "1"+var:
            match_wo_br_or_mul = match_wo_br_or_mul.replace("1", '')
        elif match_wo_br_or_mul == "-1"+var:
            match_wo_br_or_mul = match_wo_br_or_mul.replace("-1", '')
        eqn_string = eqn_string.replace(match.group(), match_wo_br_or_mul)
        match = re.search(regex, eqn_string)
    if match is not None:
        return inference_string(eqn_string, var)
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
        if "("+section_to_replace+")" in self.eqn_string and "("+section_to_replace+")^" not in self.eqn_string:
            self.eqn_string = self.eqn_string.replace("("+section_to_replace+")", new_section)
        else:
            self.eqn_string = self.eqn_string.replace(section_to_replace, new_section)
        self.solution.append(self.eqn_string)
        self.solution.append("------")
