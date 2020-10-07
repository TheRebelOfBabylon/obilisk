"""All methods related to calculus type problems."""
from math_core.Equation import Equation, stringify_node, check_mono, visit_NUMNode, round_complex
from math_core.Algebra import Algebra
from parser.lexer import Token, EXP, DIV, MUL, MINUS, PLUS, NUMBER, FUNC
from parser.ast import AST, BINOPNode, FUNCNode, UNIOPNode, VARNode, NUMNode, NumberNode, BinOpNode, UniOpNode, FuncNode

from typing import List, Tuple, Union
import math
from copy import deepcopy


class Calculus(Algebra):
    def __init__(
            self,
            eqn_string: str = None,
            tokens: List[Token] = None,
            tree: List[Union[AST, Token]] = None,
            var: str = None,
            exprs: List[AST] = None,
            type: str = None
    ):
        Algebra.__init__(self, eqn_string, tokens, tree, var, exprs)
        self.type = type
        self.eqn_string = stringify_node(self.tree, self.var)

    def __repr__(self):
        return f'Calculus({self.eqn_string})'

    def derive(self):
        """Method solves calculus problems"""
        self.compute_low_hanging_fruit()
        if self.type == "derivative":
            new_tree = self.compute_derivative(self.tree)
            self.tree = deepcopy(new_tree)
            self.compute_low_hanging_fruit(ops_flag=False)
            print(stringify_node(self.tree, self.var))

    def compute_derivative(self, node: AST, verbose: bool = True) -> AST:
        """Method climbs through AST, finds derivative terms and solves them"""
        if node.type == BINOPNode:
            if node.op.tag == EXP:
                if node.right.type == NUMNode:
                    # d/dx()^a = a*()^(a-1)
                    coeff_node = node.right
                    if round_complex(visit_NUMNode(node.right)) < 0:
                        coeff_node = UniOpNode(Token(("-", MINUS)), coeff_node)
                    new_exp = round_complex(visit_NUMNode(node.right) - 1)
                    new_exp_node = NumberNode(Token((str(new_exp), NUMBER)))
                    der_expr_node = self.compute_derivative(node.left, verbose=verbose)
                    if der_expr_node.type == NUMNode and round_complex(visit_NUMNode(der_expr_node)) == 1:
                        new_node = BinOpNode(coeff_node, Token(("*", MUL)),
                                             BinOpNode(node.left, Token(("^", EXP)), new_exp_node))
                    else:
                        new_node = BinOpNode(BinOpNode(coeff_node, Token(("*", MUL)),
                                                       BinOpNode(node.left, Token(("^", EXP)), new_exp_node)),
                                             Token(("*", MUL)), der_expr_node)
                    if verbose:
                        self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                             + stringify_node(new_node, self.var))
                        #self.update_eqn_string(stringify_node(node, self.var), stringify_node(new_node, self.var))
                    return new_node
                elif node.left.type == NUMNode:
                    if round_complex(visit_NUMNode(node.left)) == math.e:
                        der_expr = self.compute_derivative(node.right)
                        new_node = node
                        if der_expr.type != NUMNode:
                            new_node = BinOpNode(der_expr, Token(("*", MUL)), new_node)
                        else:
                            if round_complex(visit_NUMNode(der_expr)) != 1:
                                new_node = BinOpNode(der_expr, Token(("*", MUL)), new_node)
                        if verbose:
                            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                                 + stringify_node(new_node, self.var))
                            self.update_eqn_string(stringify_node(node, self.var), stringify_node(new_node, self.var))
                        return new_node
                    elif node.right.type == VARNode or check_mono(node.right):
                        der_expr = self.compute_derivative(node.right)
                        new_node = BinOpNode(node, Token(("*", MUL)), FuncNode(Token(("ln", FUNC)), [node.left]))
                        if der_expr.type != NUMNode:
                            new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                        else:
                            if round_complex(visit_NUMNode(der_expr)) != 1:
                                new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                        if verbose:
                            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                                 + stringify_node(new_node, self.var))
                            self.update_eqn_string(stringify_node(node, self.var), stringify_node(new_node, self.var))
                        return new_node
            elif node.op.tag == DIV:
                return self.quotient_rule(node, verbose=verbose)
            elif node.op.tag == MUL:
                return self.product_rule(node, verbose=verbose)
            new_left = self.compute_derivative(node.left, verbose=verbose)
            new_right = self.compute_derivative(node.right, verbose=verbose)
            return BinOpNode(new_left, node.op, new_right)
        elif node.type == UNIOPNode:
            return UniOpNode(node.op, self.compute_derivative(node.right))
        elif node.type == FUNCNode:
            if node.op.value.lower() in "ln":
                der_expr = self.compute_derivative(node.args[0])
                new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), node.args[0])
                if der_expr.type != NUMNode:
                    new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                else:
                    if round_complex(visit_NUMNode(der_expr)) == 1:
                        new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
            elif node.op.value.lower() in "log":
                der_expr = self.compute_derivative(node.args[0])
                denom_node = BinOpNode(node.args[0], Token(("*", MUL)), FuncNode(Token(("ln", FUNC)), [node.args[1]]))
                new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom_node)
                if der_expr.type != NUMNode:
                    new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                else:
                    if round_complex(visit_NUMNode(der_expr)) == 1:
                        new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
            elif node.op.value.lower() in "sqrt":
                inter_node = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("0.5", NUMBER))))
                new_node = self.compute_derivative(inter_node, verbose=False)
            if verbose:
                self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                     + stringify_node(new_node, self.var))
                self.update_eqn_string(stringify_node(node, self.var), stringify_node(new_node, self.var))
            return new_node
        elif node.type == VARNode:
            return NumberNode(Token(("1", NUMBER)))
        else:
            return NumberNode(Token(("0", NUMBER)))

    def quotient_rule(self, node: AST, verbose: bool = True) -> AST:
        """Computes quotient rule for derivatives"""
        der_top_node = self.compute_derivative(node.left)
        der_bottom_node = self.compute_derivative(node.right)
        if der_top_node.type == NUMNode and round_complex(
                visit_NUMNode(der_top_node)) == 1 and der_bottom_node.type == NUMNode and round_complex(
                visit_NUMNode(der_bottom_node)) == 1:
            num_node_left = NumberNode(Token(("1", NUMBER)))
            num_node_right = NumberNode(Token(("1", NUMBER)))
        elif der_top_node.type == NUMNode and round_complex(visit_NUMNode(der_top_node)) == 1:
            num_node_left = node.right
            num_node_right = BinOpNode(der_bottom_node, Token(("*", MUL)), node.left)
        elif der_bottom_node.type == NUMNode and round_complex(visit_NUMNode(der_bottom_node)) == 1:
            num_node_left = BinOpNode(der_top_node, Token(("*", MUL)), node.right)
            num_node_right = node.left
        else:
            num_node_left = BinOpNode(der_top_node, Token(("*", MUL)), node.right)
            num_node_right = BinOpNode(der_bottom_node, Token(("*", MUL)), node.left)
        if node.right.type == BINOPNode and node.right.op.tag == EXP and node.right.right.type == NUMNode:
            new_exp = round_complex(visit_NUMNode(node.right.right) * 2)
            denom_node = BinOpNode(node.right.left, Token(("^", EXP)), NumberNode(Token((str(new_exp), NUMBER))))
        else:
            denom_node = BinOpNode(node.right, Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
        num_node = BinOpNode(num_node_left, Token(("-", MINUS)), num_node_right)
        new_node = BinOpNode(num_node, Token(("/", DIV)), denom_node)
        if verbose:
            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                 + stringify_node(new_node, self.var))
            self.update_eqn_string(stringify_node(node, self.var), stringify_node(new_node, self.var))
        return new_node

    def product_rule(self, node: AST, verbose: bool = True) -> AST:
        """Compute product rule for derivatives"""
        der_left = self.compute_derivative(node.left)
        der_right = self.compute_derivative(node.right)
        if der_left.type == NUMNode and round_complex(
                visit_NUMNode(der_left)) == 1 and der_right.type == NUMNode and round_complex(
            visit_NUMNode(der_right)) == 1:
            new_node_left = NumberNode(Token(("1", NUMBER)))
            new_node_right = NumberNode(Token(("1", NUMBER)))
        elif der_left.type == NUMNode and round_complex(visit_NUMNode(der_left)) == 1:
            new_node_left = node.right
            new_node_right = BinOpNode(der_right, Token(("*", MUL)), node.left)
        elif der_right.type == NUMNode and round_complex(visit_NUMNode(der_right)) == 1:
            new_node_left = BinOpNode(der_left, Token(("*", MUL)), node.right)
            new_node_right = node.left
        else:
            new_node_left = BinOpNode(der_left, Token(("*", MUL)), node.right)
            new_node_right = BinOpNode(der_right, Token(("*", MUL)), node.left)
        new_node = BinOpNode(new_node_left, Token(("+", PLUS)), new_node_right)
        if verbose:
            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                 + stringify_node(new_node, self.var))
            self.update_eqn_string(stringify_node(node, self.var), stringify_node(new_node, self.var))
        return new_node