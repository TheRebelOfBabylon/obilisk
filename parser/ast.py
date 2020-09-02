from parser.lexer import Token

from typing import List, Union


class AST:
    pass

class FuncNode(AST):
    def __init__(self, op: Token, args: List[Union[AST, Token]]):
        self.op = op.value
        self.args = args

    def __repr__(self):
        return 'FuncNode(%s, %s)' % (self.op, self.args)


class BinOpNode(AST):
    def __init__(self, left: List[Union[AST, Token]], op: Token, right: List[Union[AST, Token]]):
        self.left = left
        self.op = op.value
        self.right = right

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

class MatrixNode(AST):
    def __init__(self, indices: List[Union[Token, AST]]):
        self.rows = len(indices)
        self.columns = len(indices[0])

    def __repr__(self):
        return 'MatrixNode(%s, %s)' % (self.rows, self.columns)

class ConstantNode(AST):
    def __init__(self, token: Token):
        self.value = token.value
        self.tag = token.tag

    def __repr__(self):
        return 'ConstantNode(%s, %s)' % (self.value, self.tag)


class EquationNode(AST):
    """Central node is EQUAL, children are Expressions"""
    def __init__(self, children: List[Union[Token, AST]]):
        self.children = children

    def __repr__(self):
        return 'EquationNode(%s)' % self.children


class ExpressionNode(AST):
    """Parents are Equation, children are terms"""
    def __init__(self, children: List[Union[Token, AST]]):
        self.children = children

    def __repr__(self):
        return 'ExpressionNode(%s)' % self.children


class TermNode(AST):
    """Parents are Expressions, children are Factors"""
    def __init__(self, children: List[Union[Token, AST]]):
        self.children = children

    def __repr__(self):
        return 'TermNode(%s)' % self.children


class FactorNode(AST):
    """Parents are Terms, children are Atoms"""
    def __init__(self, children: List[Union[Token, AST]]):
        self.children = children

    def __repr__(self):
        return 'FactorNode(%s)' % self.children
