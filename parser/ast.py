from parser.lexer import Token, EXP, MUL

from typing import List, Union

FUNCNode = 'FUNCNode'
BINOPNode = 'BINOPNode'
NUMNode = 'NUMNode'
VARNode = 'VARNode'
UNIOPNode = 'UNIOPNode'

class AST:
    pass

class FuncNode(AST):
    def __init__(self, op: Token, args: List[Union[AST, Token]]):
        self.op = op
        self.args = args
        self.type = FUNCNode

    def __repr__(self):
        return 'FuncNode(%s, %s)' % (self.op.value, self.args)


class UniOpNode(AST):
    def __init__(self, op: Token, right: Union[AST, Token]):
        self.right = right
        self.op = op
        self.type = UNIOPNode

    def __repr__(self):
        return 'UniOpNode(%s, %s)' % (self.op.value, self.right)

    def __hash__(self):
        return hash(self.go_down_node(node=self))

    def go_down_node(self, node):
        # TODO - probably gonna need to add to this code to deal with unary ops acting on expressions
        if node.right.type == UNIOPNode:
            return self.go_down_node(node.right)
        elif node.right.type == NUMNode:
            return node.right


class BinOpNode(AST):
    def __init__(self, left: Union[AST, Token], op: Token, right: Union[AST, Token]):
        self.left = left
        self.op = op
        self.right = right
        self.type = BINOPNode

    def __repr__(self):
        return 'BinOpNode(%s, %s, %s)' % (self.left, self.op.value, self.right)

    def __hash__(self):
        if self.op.tag == EXP:
            if self.right.type == NUMNode:
                return hash((self.left, self.right.value))
        return hash((self.left, self.right))

class NumberNode(AST):
    def __init__(self, token: Token):
        self.value = token.value
        self.tag = token.tag
        self.type = NUMNode

    def __repr__(self):
        return 'NumberNode(%s, %s)' % (self.value, self.tag)

    def __hash__(self):
        return hash(self.type)


class VariableNode(AST):
    def __init__(self, token: Token):
        self.value = token.value
        self.tag = token.tag
        self.type = VARNode

    def __repr__(self):
        return 'VariableNode(%s, %s)' % (self.value, self.tag)

    def __hash__(self):
        return hash(self.type)

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
        self.type = CONSTNode

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
