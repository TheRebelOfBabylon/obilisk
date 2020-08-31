from parser.lexer import Token

from typing import List


class ASTExpr:
    pass

class Func(ASTExpr):
    def __init__(self, op: Token, args: List[Token]):
        self.op = op.value
        self.args = [tok.value for tok in args]

    def __repr__(self):
        return 'MultiFuncNode(%s, %s)' % (self.op, self.args)


class BinOp(ASTExpr):
    def __init__(self, left: Token, op: Token, right: Token):
        self.left = left.value
        self.op = op.value
        self.right = right.value

    def __repr__(self):
        return 'BinOpNode(%s, %s, %s)' % (self.left, self.op, self.right)


class Number(ASTExpr):
    def __init__(self, token: Token):
        self.value = token.value

    def __repr__(self):
        return 'NumberNode(%s)' % self.value


class Variable(ASTExpr):
    def __init__(self, token: Token):
        self.value = token.value

    def __repr__(self):
        return 'VariableNode(%s)' % self.value

class Constant(ASTExpr):
    def __init__(self, token: Token):
        self.value = token.value

    def __repr__(self):
        return 'ConstantNode(%s)' % self.value