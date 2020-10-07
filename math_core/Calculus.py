"""All methods related to calculus type problems."""
from math_core.Equation import Equation, stringify_node, check_mono, visit_NUMNode, round_complex
from math_core.Algebra import Algebra
from parser.lexer import Token, EXP, DIV, MUL, MINUS, PLUS, NUMBER, FUNC
from parser.ast import AST, BINOPNode, FUNCNode, UNIOPNode, VARNode, NUMNode, NumberNode, BinOpNode, UniOpNode, FuncNode

from typing import List, Union
import functools
import math
from copy import deepcopy


list_of_trig_func = [
    "cos",
    "sin",
    "tan",
    "sec",
    "csc",
    "cot",
    "acos",
    "asin",
    "atan",
    "asec",
    "acsc",
    "acot",
    "cosh",
    "sinh",
    "tanh",
    "sech",
    "csch",
    "coth",
    "acosh",
    "asinh",
    "atanh",
    "asech",
    "acsch",
    "acoth",
]


def rsetattr(obj, attr, val):
    pre, _, post = attr.rpartition('.')
    return setattr(rgetattr(obj, pre) if pre else obj, post, val)


def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return functools.reduce(_getattr, [obj] + attr.split('.'))


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
            new_tree, _ = self.compute_derivative(self.tree, temp_tree=deepcopy(self.tree))
            self.tree = deepcopy(new_tree)
            self.eqn_string = stringify_node(self.tree, self.var)
            self.compute_low_hanging_fruit(ops_flag=False)
            #print(stringify_node(self.tree, self.var))

    def compute_derivative(self, node: AST, temp_tree: AST, verbose: bool = True, tree_path: List[str] = None) -> AST:
        """Method climbs through AST, finds derivative terms and solves them"""
        if tree_path is None:
            tree_path = []
        if node.type == BINOPNode:
            if node.op.tag == EXP:
                if node.right.type == NUMNode:
                    # d/dx()^a = a*()^(a-1)
                    coeff_node = node.right
                    if round_complex(visit_NUMNode(node.right)) < 0:
                        coeff_node = UniOpNode(Token(("-", MINUS)), coeff_node)
                    new_exp = round_complex(visit_NUMNode(node.right) - 1)
                    new_exp_node = NumberNode(Token((str(new_exp), NUMBER)))
                    der_expr_node, temp_tree = self.compute_derivative(node.left, verbose=False, temp_tree=temp_tree)
                    if new_exp == 1:
                        new_node = BinOpNode(coeff_node, Token(("*", MUL)), node.left)
                    elif der_expr_node.type == NUMNode and round_complex(visit_NUMNode(der_expr_node)) == 1:
                        new_node = BinOpNode(coeff_node, Token(("*", MUL)),
                                             BinOpNode(node.left, Token(("^", EXP)), new_exp_node))
                    else:
                        new_node = BinOpNode(BinOpNode(coeff_node, Token(("*", MUL)),
                                                       BinOpNode(node.left, Token(("^", EXP)), new_exp_node)),
                                             Token(("*", MUL)), der_expr_node)
                    if verbose:
                        self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                             + stringify_node(new_node, self.var))
                        self.solution.append("------")
                        temp_tree = self.calc_replace_node(temp_tree, tree_path, new_node)
                        self.solution.append(stringify_node(temp_tree, self.var))
                        self.solution.append("------")
                    return new_node, temp_tree
                elif node.left.type == NUMNode:
                    if round_complex(visit_NUMNode(node.left)) == math.e:
                        der_expr, temp_tree = self.compute_derivative(node.right, temp_tree=temp_tree, verbose=False)
                        new_node = node
                        if der_expr.type != NUMNode:
                            new_node = BinOpNode(der_expr, Token(("*", MUL)), new_node)
                        else:
                            if round_complex(visit_NUMNode(der_expr)) != 1:
                                new_node = BinOpNode(der_expr, Token(("*", MUL)), new_node)
                        if verbose:
                            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                                 + stringify_node(new_node, self.var))
                            self.solution.append("------")
                            temp_tree = self.calc_replace_node(temp_tree, tree_path, new_node)
                            self.solution.append(stringify_node(temp_tree, self.var))
                            self.solution.append("------")
                        return new_node, temp_tree
                    elif node.right.type == VARNode or check_mono(node.right):
                        der_expr, temp_tree = self.compute_derivative(node.right, temp_tree=temp_tree, verbose=False)
                        new_node = BinOpNode(node, Token(("*", MUL)), FuncNode(Token(("ln", FUNC)), [node.left]))
                        if der_expr.type != NUMNode:
                            new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                        else:
                            if round_complex(visit_NUMNode(der_expr)) != 1:
                                new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                        if verbose:
                            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                                 + stringify_node(new_node, self.var))
                            self.solution.append("------")
                            temp_tree = self.calc_replace_node(temp_tree, tree_path, new_node)
                            self.solution.append(stringify_node(temp_tree, self.var))
                            self.solution.append("------")
                        return new_node, temp_tree
            elif node.op.tag == DIV:
                return self.quotient_rule(node, temp_tree=temp_tree, tree_path=tree_path[:], verbose=verbose)
            elif node.op.tag == MUL:
                return self.product_rule(node, temp_tree=temp_tree, tree_path=tree_path[:], verbose=verbose)
            tree_path.append("left")
            new_left, temp_tree = self.compute_derivative(node.left, temp_tree=temp_tree, verbose=verbose, tree_path=tree_path[:])
            tree_path[-1] = "right"
            new_right, temp_tree = self.compute_derivative(node.right, temp_tree=temp_tree, verbose=verbose, tree_path=tree_path[:])
            return BinOpNode(new_left, node.op, new_right), temp_tree
        elif node.type == UNIOPNode:
            tree_path.append("right")
            return UniOpNode(node.op, self.compute_derivative(node.right, tree_path=tree_path[:], temp_tree=temp_tree, verbose=verbose))
        elif node.type == FUNCNode:
            if node.op.value.lower() in "ln":
                der_expr, temp_tree = self.compute_derivative(node.args[0], temp_tree=temp_tree, verbose=False)
                new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), node.args[0])
                if der_expr.type != NUMNode:
                    new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                else:
                    if round_complex(visit_NUMNode(der_expr)) != 1:
                        new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
            elif node.op.value.lower() in "log":
                der_expr, temp_tree = self.compute_derivative(node.args[0], temp_tree=temp_tree, verbose=False)
                denom_node = BinOpNode(node.args[0], Token(("*", MUL)), FuncNode(Token(("ln", FUNC)), [node.args[1]]))
                new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom_node)
                if der_expr.type != NUMNode:
                    new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                else:
                    if round_complex(visit_NUMNode(der_expr)) != 1:
                        new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
            elif node.op.value.lower() in "sqrt":
                inter_node = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("0.5", NUMBER))))
                new_node, temp_tree = self.compute_derivative(inter_node, temp_tree=temp_tree, verbose=False)
            elif node.op.value.lower() in "abs":
                der_expr, temp_tree = self.compute_derivative(node.args[0], temp_tree=temp_tree, verbose=False)
                new_node = BinOpNode(node.args[0], Token(("/", DIV)), node)
                if der_expr.type != NUMNode:
                    new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
                else:
                    if round_complex(visit_NUMNode(der_expr)) != 1:
                        new_node = BinOpNode(new_node, Token(("*", MUL)), der_expr)
            if verbose:
                self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                     + stringify_node(new_node, self.var))
                self.solution.append("------")
                temp_tree = self.calc_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, self.var))
                self.solution.append("------")
            return new_node, temp_tree
        elif node.type == VARNode:
            new_node = NumberNode(Token(("1", NUMBER)))
            if verbose:
                self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                     + stringify_node(new_node, self.var))
                self.solution.append("------")
                temp_tree = self.calc_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, self.var))
                self.solution.append("------")
            return new_node, temp_tree
        else:
            new_node = NumberNode(Token(("0", NUMBER)))
            if verbose:
                self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                     + stringify_node(new_node, self.var))
                self.solution.append("------")
                temp_tree = self.calc_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, self.var))
                self.solution.append("------")
            return new_node, temp_tree

    def quotient_rule(self, node: AST, temp_tree: AST, tree_path: List[str], verbose: bool = True) -> AST:
        """Computes quotient rule for derivatives"""
        der_top_node, temp_tree = self.compute_derivative(node.left, temp_tree=temp_tree, verbose=False)
        der_bottom_node, temp_tree = self.compute_derivative(node.right, temp_tree=temp_tree, verbose=False)
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
            self.solution.append("------")
            temp_tree = self.calc_replace_node(temp_tree, tree_path, new_node)
            self.solution.append(stringify_node(temp_tree, self.var))
            self.solution.append("------")
        return new_node, temp_tree

    def product_rule(self, node: AST, temp_tree: AST, tree_path: List[str], verbose: bool = True) -> AST:
        """Compute product rule for derivatives"""
        der_left, temp_tree = self.compute_derivative(node.left, temp_tree=temp_tree, verbose=False)
        der_right, temp_tree = self.compute_derivative(node.right, temp_tree=temp_tree, verbose=False)
        if der_left.type == NUMNode and round_complex(
                visit_NUMNode(der_left)) == 1 and der_right.type == NUMNode and round_complex(
            visit_NUMNode(der_right)) == 1:
            new_node_left = NumberNode(Token(("1", NUMBER)))
            new_node_right = NumberNode(Token(("1", NUMBER)))
            new_node = BinOpNode(new_node_left, Token(("+", PLUS)), new_node_right)
        elif der_left.type == NUMNode and round_complex(visit_NUMNode(der_left)) == 1:
            new_node_left = node.right
            new_node_right = BinOpNode(der_right, Token(("*", MUL)), node.left)
            new_node = BinOpNode(new_node_left, Token(("+", PLUS)), new_node_right)
        elif der_left.type == NUMNode and round_complex(visit_NUMNode(der_left)) == 0:
            new_node = BinOpNode(der_right, Token(("*", MUL)), node.left)
        elif der_right.type == NUMNode and round_complex(visit_NUMNode(der_right)) == 1:
            new_node_left = BinOpNode(der_left, Token(("*", MUL)), node.right)
            new_node_right = node.left
            new_node = BinOpNode(new_node_left, Token(("+", PLUS)), new_node_right)
        elif der_right.type == NUMNode and round_complex(visit_NUMNode(der_right)) == 0:
            new_node = BinOpNode(der_left, Token(("*", MUL)), node.right)
        else:
            new_node_left = BinOpNode(der_left, Token(("*", MUL)), node.right)
            new_node_right = BinOpNode(der_right, Token(("*", MUL)), node.left)
            new_node = BinOpNode(new_node_left, Token(("+", PLUS)), new_node_right)
        if new_node.left.type == NUMNode and round_complex(visit_NUMNode(new_node.left)) == 1:
            new_node = new_node.right
        elif new_node.right.type == NUMNode and round_complex(visit_NUMNode(new_node.right)) == 1:
            new_node = new_node.left
        if verbose:
            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                 + stringify_node(new_node, self.var))
            self.solution.append("------")
            temp_tree = self.calc_replace_node(temp_tree, tree_path, new_node)
            self.solution.append(stringify_node(temp_tree, self.var))
            self.solution.append("------")
        return new_node, temp_tree

    def calc_replace_node(self, tree: AST, old_node_path: List[str], new_node: AST) -> AST:
        """Method replaces a specific node based on a given path to it"""
        # TODO - Fix this method
        path = old_node_path[0]
        del old_node_path[0]
        for branch in old_node_path:
            path += "."+branch
        rsetattr(tree, path, new_node)
        return tree
