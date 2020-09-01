from parser.lexer import Token

from typing import List, Union


class AST:
    pass

class FuncNode(AST):
    def __init__(self, op: Token, args: List[Token]):
        self.op = op.value
        self.args = [tok.value for tok in args]

    def __repr__(self):
        return 'MultiFuncNode(%s, %s)' % (self.op, self.args)


class BinOpNode(AST):
    def __init__(self, left: Token, op: Token, right: Token):
        self.left = left.value
        self.op = op.value
        self.right = right.value

    def __repr__(self):
        return 'BinOpNode(%s, %s, %s)' % (self.left, self.op, self.right)


class NumberNode(AST):
    def __init__(self, token: Token):
        self.value = token.value
        self.tag = token.tag

    def __repr__(self):
        return 'NumberNode(%s, %s)' % (self.value, self.tag)


class VariableNode(AST):
    def __init__(self, token: Token):
        self.value = token.value
        self.tag = token.tag

    def __repr__(self):
        return 'VariableNode(%s, %s)' % (self.value, self.tag)


class ConstantNode(AST):
    def __init__(self, token: Token):
        self.value = token.value
        self.tag = token.tag

    def __repr__(self):
        return 'ConstantNode(%s, %s)' % (self.value, self.tag)


class EquationNode(AST):
    """Central node is EQUAL, children are Expressions"""
    def __init__(self, token: Token, children: List[Union[Token, AST]]):
        self.value = token.value
        self.tag = token.tag
        self.children = children

    def __repr__(self):
        return 'EquationNode(%s, %s, %s)' % (self.value, self.tag, self.children)


class ExpressionNode(AST):
    """Parents are Equation, children are terms"""
    def __init__(self, token: Token, children: List[Union[Token, AST]]):
        self.value = token.value
        self.tag = token.tag
        self.children = children

    def __repr__(self):
        return 'ExpressionNode(%s, %s, %s)' % (self.value, self.tag, self.children)


class TermNode(AST):
    """Parents are Expressions, children are Factors"""
    def __init__(self, token: Token, children: List[Union[Token, AST]]):
        self.value = token.value
        self.tag = token.tag
        self.children = children

    def __repr__(self):
        return 'TermNode(%s, %s, %s)' % (self.value, self.tag, self.children)


class FactorNode(AST):
    """Parents are Terms, children are Atoms"""
    def __init__(self, token: Token, children: List[Union[Token, AST]]):
        self.value = token.value
        self.tag = token.tag
        self.children = children

    def __repr__(self):
        return 'FactorNode(%s, %s, %s)' % (self.value, self.tag, self.children)