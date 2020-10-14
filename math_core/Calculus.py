"""All methods related to calculus type problems."""
from math_core.Equation import Equation, stringify_node, check_mono, visit_NUMNode, round_complex
from math_core.Algebra import Algebra, sub_var_dict
from parser.lexer import Token, EXP, DIV, MUL, MINUS, PLUS, NUMBER, FUNC, CONSTANT, VARIABLE
from parser.ast import AST, BINOPNode, FUNCNode, UNIOPNode, VARNode, NUMNode, NumberNode, BinOpNode, UniOpNode, FuncNode, VariableNode
from math_core.algebra_formats import monomial_x

from typing import List, Union, Tuple
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

cos_sine_anti_dict = {
    "cos": "sin",
    "cosh": "sinh",
    "sin": "cos",
    "sinh": "cosh",
    "tan": "sec",
    "tanh": "sech",
    "csc": "cot",
    "csch": "coth",
    "cot": "csc",
    "coth": "csch",
}


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
        if not self.check_for_x_power_x():
            self.compute_low_hanging_fruit()
            if self.type == "derivative":
                self.tree = deepcopy(self.tree.args[0])
                new_tree, _ = self.compute_derivative(self.tree, temp_tree=deepcopy(self.tree))
                self.tree = deepcopy(new_tree)
                self.eqn_string = stringify_node(self.tree, self.var)
                self.compute_low_hanging_fruit(ops_flag=False)
                # print(stringify_node(self.tree, self.var))
            elif self.type == "integral":
                if len(self.tree.args) == 1:
                    self.tree = deepcopy(self.tree.args[0])
                    new_tree, _ = self.compute_integral(self.tree, temp_tree=deepcopy(self.tree))
                    new_tree = BinOpNode(new_tree, Token(("+", PLUS)), NumberNode(Token(("#C", CONSTANT))))
                    self.tree = deepcopy(new_tree)
                    self.eqn_string = stringify_node(self.tree, self.var)
                    self.compute_low_hanging_fruit(ops_flag=False)
                    # print(stringify_node(self.tree, self.var))
                else:
                    print("We have a definite integral")

    def compute_derivative(self, node: AST, temp_tree: AST, verbose: bool = True, tree_path: List[str] = None) -> Tuple[
        AST, List[str]]:
        """Method climbs through AST, finds derivative terms and solves them"""
        if tree_path is None:
            tree_path = []
        if node.type == BINOPNode:
            if node.op.tag == EXP:
                if node.right.type == NUMNode:
                    # d/dx()^a = a*()^(a-1)
                    coeff = round_complex(visit_NUMNode(node.right))
                    if node.left.type == BINOPNode and node.left.op.tag == MUL and node.left.left.type == NUMNode:
                        coeff = round_complex(coeff*visit_NUMNode(node.left.left))
                        inter_node = node.left.right
                        der_expr_node, temp_tree = self.compute_derivative(node.left.right, verbose=False,
                                                                           temp_tree=temp_tree)
                    elif node.left.type == BINOPNode and node.left.op.tag == DIV and node.left.right.type == NUMNode:
                        coeff = round_complex(coeff/visit_NUMNode(node.left.right))
                        inter_node = node.left.left
                        der_expr_node, temp_tree = self.compute_derivative(node.left.left, verbose=False,
                                                                           temp_tree=temp_tree)
                    else:
                        inter_node = node.left
                        der_expr_node, temp_tree = self.compute_derivative(node.left, verbose=False,
                                                                           temp_tree=temp_tree)
                    if coeff < 0:
                        coeff_node = UniOpNode(Token(("-", MINUS)), NumberNode(Token((str(abs(coeff)), NUMBER))))
                    else:
                        coeff_node = NumberNode(Token((str(abs(coeff)), NUMBER)))
                    new_exp = round_complex(visit_NUMNode(node.right) - 1)
                    new_exp_node = NumberNode(Token((str(new_exp), NUMBER)))
                    if new_exp == 1:
                        new_node = BinOpNode(coeff_node, Token(("*", MUL)), inter_node)
                    elif der_expr_node.type == NUMNode:
                        if round_complex(visit_NUMNode(der_expr_node)) == 1:
                            new_node = BinOpNode(coeff_node, Token(("*", MUL)),
                                                 BinOpNode(inter_node, Token(("^", EXP)), new_exp_node))
                        else:
                            coeff = round_complex(visit_NUMNode(coeff_node) * visit_NUMNode(der_expr_node))
                            coeff_node = NumberNode(Token((str(coeff), NUMBER)))
                            if coeff < 0:
                                coeff_node = UniOpNode(Token(("-", MINUS)), coeff_node)
                            new_node = BinOpNode(coeff_node, Token(("*", MUL)),
                                                 BinOpNode(inter_node, Token(("^", EXP)), new_exp_node))
                    else:
                        new_node = BinOpNode(BinOpNode(coeff_node, Token(("*", MUL)),
                                                       BinOpNode(inter_node, Token(("^", EXP)), new_exp_node)),
                                             Token(("*", MUL)), der_expr_node)
                    if verbose:
                        self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                             + stringify_node(new_node, self.var))
                        self.solution.append("------")
                        temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
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
                            temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
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
                            temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                            self.solution.append(stringify_node(temp_tree, self.var))
                            self.solution.append("------")
                        return new_node, temp_tree
            elif node.op.tag == DIV:
                return self.quotient_rule(node, temp_tree=temp_tree, tree_path=tree_path[:], verbose=verbose)
            elif node.op.tag == MUL:
                return self.product_rule(node, temp_tree=temp_tree, tree_path=tree_path[:], verbose=verbose)
            tree_path.append("left")
            new_left, temp_tree = self.compute_derivative(node.left, temp_tree=temp_tree, verbose=verbose,
                                                          tree_path=tree_path[:])
            tree_path[-1] = "right"
            new_right, temp_tree = self.compute_derivative(node.right, temp_tree=temp_tree, verbose=verbose,
                                                           tree_path=tree_path[:])
            return BinOpNode(new_left, node.op, new_right), temp_tree
        elif node.type == UNIOPNode:
            tree_path.append("right")
            new_node, temp_tree = self.compute_derivative(node.right, tree_path=tree_path[:], temp_tree=temp_tree,
                                                          verbose=verbose)
            return UniOpNode(node.op, new_node), temp_tree
        elif node.type == FUNCNode:
            if node.op.value.lower() in ("ln", "abs_ln"):
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
            elif node.op.value.lower() in list_of_trig_func:
                return self.trig_derive(node, temp_tree=temp_tree, tree_path=tree_path[:], verbose=verbose)
            if verbose:
                self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                     + stringify_node(new_node, self.var))
                self.solution.append("------")
                temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, self.var))
                self.solution.append("------")
            return new_node, temp_tree
        elif node.type == VARNode:
            new_node = NumberNode(Token(("1", NUMBER)))
            if verbose:
                self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                     + stringify_node(new_node, self.var))
                self.solution.append("------")
                temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, self.var))
                self.solution.append("------")
            return new_node, temp_tree
        else:
            new_node = NumberNode(Token(("0", NUMBER)))
            if verbose:
                self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                     + stringify_node(new_node, self.var))
                self.solution.append("------")
                temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, self.var))
                self.solution.append("------")
            return new_node, temp_tree

    def quotient_rule(self, node: AST, temp_tree: AST, tree_path: List[str], verbose: bool = True) -> Tuple[
        AST, List[str]]:
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
            temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
            self.solution.append(stringify_node(temp_tree, self.var))
            self.solution.append("------")
        return new_node, temp_tree

    def product_rule(self, node: AST, temp_tree: AST, tree_path: List[str], verbose: bool = True) -> Tuple[
        AST, List[str]]:
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
        if new_node.left.type == NUMNode:
            if round_complex(visit_NUMNode(new_node.left)) == 1:
                new_node = new_node.right
            elif new_node.right.type == BINOPNode and new_node.right.op.tag == MUL and new_node.right.left.type == NUMNode:
                new_coeff = round_complex(visit_NUMNode(new_node.right.left) * visit_NUMNode(new_node.left))
                new_node = BinOpNode(NumberNode(Token((str(new_coeff), NUMBER))), Token(("*", MUL)),
                                     new_node.right.right)
        elif new_node.right.type == NUMNode:
            if round_complex(visit_NUMNode(new_node.right)) == 1:
                new_node = new_node.left
            elif new_node.left.type == BINOPNode and new_node.left.op.tag == MUL and new_node.left.left.type == NUMNode:
                new_coeff = round_complex(visit_NUMNode(new_node.left.left) * visit_NUMNode(new_node.right))
                new_node = BinOpNode(NumberNode(Token((str(new_coeff), NUMBER))), Token(("*", MUL)),
                                     new_node.left.right)
        if verbose:
            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                 + stringify_node(new_node, self.var))
            self.solution.append("------")
            temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
            self.solution.append(stringify_node(temp_tree, self.var))
            self.solution.append("------")
        return new_node, temp_tree

    def trig_derive(self, node: AST, temp_tree: AST, tree_path: List[str], verbose: bool = True) -> Tuple[
        AST, List[str]]:
        """Method computes derivatives for all trig functions"""
        der_exprs, temp_tree = self.compute_derivative(node.args[0], temp_tree=temp_tree, verbose=False)
        if node.op.value.lower() in ("cos", "cosh"):
            if node.op.value.lower() == "cos":
                new_node = UniOpNode(Token(("-", MINUS)),
                                     FuncNode(Token((cos_sine_anti_dict[node.op.value.lower()], FUNC)), node.args))
            else:
                new_node = FuncNode(Token((cos_sine_anti_dict[node.op.value.lower()], FUNC)), node.args)
        elif node.op.value.lower() in ("sin", "sinh"):
            new_node = FuncNode(Token((cos_sine_anti_dict[node.op.value.lower()], FUNC)), node.args)
        elif node.op.value.lower() in ("tan", "tanh"):
            new_node = BinOpNode(FuncNode(Token((cos_sine_anti_dict[node.op.value.lower()], FUNC)), node.args),
                                 Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
        elif node.op.value.lower() == "sec":
            new_node = BinOpNode(FuncNode(Token(("tan", FUNC)), node.args), Token(("*", MUL)),
                                 FuncNode(Token(("sec", FUNC)), node.args))
        elif node.op.value.lower() in ("csc", "csch"):
            new_node = BinOpNode(UniOpNode(Token(("-", MINUS)),
                                           FuncNode(Token((cos_sine_anti_dict[node.op.value.lower()], FUNC)),
                                                    node.args)), Token(("*", MUL)),
                                 FuncNode(Token((node.op.value.lower(), FUNC)), node.args))
        elif node.op.value.lower() in ("cot", "coth"):
            new_node = UniOpNode(Token(("-", MINUS)), BinOpNode(
                FuncNode(Token((cos_sine_anti_dict[node.op.value.lower()], FUNC)), node.args), Token(("^", EXP)),
                NumberNode(Token(("2", NUMBER)))))
        elif node.op.value.lower() == "acos":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = FuncNode(Token(("sqrt", FUNC)),
                             [BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("-", MINUS)), squared_term)])
            new_node = UniOpNode(Token(("-", MINUS)),
                                 BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom))
        elif node.op.value.lower() == "asin":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = FuncNode(Token(("sqrt", FUNC)),
                             [BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("-", MINUS)), squared_term)])
            new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom)
        elif node.op.value.lower() == "atan":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = BinOpNode(squared_term, Token(("+", PLUS)), NumberNode(Token(("1", NUMBER))))
            new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom)
        elif node.op.value.lower() == "asec":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = FuncNode(Token(("sqrt", FUNC)),
                             [BinOpNode(squared_term, Token(("-", MINUS)), NumberNode(Token(("1", NUMBER))))])
            denom = BinOpNode(FuncNode(Token(("abs", FUNC)), node.args), Token(("*", MUL)), denom)
            new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom)
        elif node.op.value.lower() == "acsc":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = FuncNode(Token(("sqrt", FUNC)),
                             [BinOpNode(squared_term, Token(("-", MINUS)), NumberNode(Token(("1", NUMBER))))])
            denom = BinOpNode(FuncNode(Token(("abs", FUNC)), node.args), Token(("*", MUL)), denom)
            new_node = UniOpNode(Token(("-", MINUS)),
                                 BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom))
        elif node.op.value.lower() == "acot":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = BinOpNode(squared_term, Token(("+", PLUS)), NumberNode(Token(("1", NUMBER))))
            new_node = UniOpNode(Token(("-", MINUS)),
                                 BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom))
        elif node.op.value.lower() == "sech":
            new_node = BinOpNode(FuncNode(Token(("tanh", FUNC)), node.args), Token(("*", MUL)),
                                 UniOpNode(Token(("-", MINUS)), FuncNode(Token(("sech", FUNC)), node.args)))
        elif node.op.value.lower() == "acosh":
            denom_left = FuncNode(Token(("sqrt", FUNC)),
                                  [BinOpNode(node.args[0], Token(("-", MINUS)), NumberNode(Token(("1", NUMBER))))])
            denom_right = FuncNode(Token(("sqrt", FUNC)),
                                   [BinOpNode(node.args[0], Token(("+", PLUS)), NumberNode(Token(("1", NUMBER))))])
            denom = BinOpNode(denom_left, Token(("*", MUL)), denom_right)
            new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom)
        elif node.op.value.lower() == "asinh":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = FuncNode(Token(("sqrt", FUNC)),
                             [BinOpNode(squared_term, Token(("+", PLUS)), NumberNode(Token(("1", NUMBER))))])
            new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom)
        elif node.op.value.lower() == "atanh":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("-", MINUS)), squared_term)
            new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom)
        elif node.op.value.lower() == "asech":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = FuncNode(Token(("sqrt", FUNC)),
                             [BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("-", MINUS)), squared_term)])
            denom = BinOpNode(node.args[0], Token(("*", MUL)), denom)
            new_node = UniOpNode(Token(("-", MINUS)),
                                 BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom))
        elif node.op.value.lower() == "acsch":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = FuncNode(Token(("sqrt", FUNC)),
                             [BinOpNode(squared_term, Token(("+", PLUS)), NumberNode(Token(("1", NUMBER))))])
            denom = BinOpNode(node.args[0], Token(("*", MUL)), denom)
            new_node = UniOpNode(Token(("-", MINUS)),
                                 BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom))
        elif node.op.value.lower() == "acoth":
            if node.args[0].type == BINOPNode and node.args[0].op.tag == EXP and node.args[0].right.type == NUMNode:
                exp = round_complex(visit_NUMNode(node.args[0]) * 2)
                squared_term = BinOpNode(node.args[0].left, Token(("^", EXP)), NumberNode(Token((str(exp), NUMBER))))
            else:
                squared_term = BinOpNode(node.args[0], Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
            denom = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("-", MINUS)), squared_term)
            new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), denom)
        if der_exprs.type != NUMNode:
            new_node = BinOpNode(new_node, Token(("*", MUL)), der_exprs)
        else:
            if round_complex(visit_NUMNode(der_exprs)) != 1:
                new_node = BinOpNode(new_node, Token(("*", MUL)), der_exprs)
        if verbose:
            self.solution.append("d/d" + self.var + "(" + stringify_node(node, self.var) + ") = "
                                 + stringify_node(new_node, self.var))
            self.solution.append("------")
            temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
            self.solution.append(stringify_node(temp_tree, self.var))
            self.solution.append("------")
        return new_node, temp_tree

    def compute_integral(self, node: AST, temp_tree: AST, var: str = None, verbose: bool = True, tree_path: List[str] = None) -> Tuple[
        AST, AST]:
        """Method climbs through AST, finds integral terms and solves them"""
        if var is None:
            var = self.var
        if tree_path is None:
            tree_path = []
        if node.type == BINOPNode:
            if node.op.tag == EXP:
                if node.right.type == NUMNode:
                    current_exp = round_complex(visit_NUMNode(node.right))
                    if current_exp != -1:
                        # ∫ ()^a dx = (1/(a+1))*()^(a+1)
                        new_exp = round_complex(current_exp + 1)
                        coeff = 1
                        inter_node = node.left
                        if node.left.type == BINOPNode:
                            if node.left.op.tag == MUL and node.left.left.type == NUMNode:
                                coeff = round_complex(visit_NUMNode(node.left.left))
                                inter_node = node.left.right
                            elif node.left.op.tag == DIV and node.left.right.type == NUMNode:
                                coeff = round_complex(1 / visit_NUMNode(node.left.right))
                                inter_node = node.left.left
                        coeff = round_complex(coeff*1 / new_exp)
                        if coeff < 0:
                            coeff_node = UniOpNode(Token(("-", MINUS)), NumberNode(Token((str(abs(coeff)), NUMBER))))
                        else:
                            coeff_node = NumberNode(Token((str(coeff), NUMBER)))
                        new_exp_node = NumberNode(Token((str(new_exp), NUMBER)))
                        if new_exp == 1:
                            new_node = BinOpNode(coeff_node, Token(("*", MUL)), inter_node)
                        else:
                            new_node = BinOpNode(coeff_node, Token(("*", MUL)), BinOpNode(inter_node, Token(("^", EXP)), new_exp_node))

                        if verbose:
                            self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                                 + stringify_node(new_node, var) + "+C")
                            self.solution.append("------")
                            temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                            self.solution.append(stringify_node(temp_tree, var) + "+C")
                            self.solution.append("------")
                        return new_node, temp_tree
            elif node.op.tag == MUL:
                if node.left.type == NUMNode:
                    new_exp = 2
                    coeff = round_complex(visit_NUMNode(node.left) / new_exp)
                    var_node = node.right
                    if coeff < 0:
                        coeff_node = UniOpNode(Token(("-", MINUS)), NumberNode(Token((str(abs(coeff)), NUMBER))))
                    else:
                        coeff_node = NumberNode(Token((str(coeff), NUMBER)))
                    new_exp_node = NumberNode(Token((str(new_exp), NUMBER)))
                    new_node = BinOpNode(coeff_node, Token(("*", MUL)),
                                         BinOpNode(var_node, Token(("^", EXP)), new_exp_node))
                    if verbose:
                        self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                             + stringify_node(new_node, var) + "+C")
                        self.solution.append("------")
                        temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                        self.solution.append(stringify_node(temp_tree, var) + "+C")
                        self.solution.append("------")
                    return new_node, temp_tree
                elif node.right.type == NUMNode:
                    new_exp = 2
                    coeff = round_complex(visit_NUMNode(node.right) / new_exp)
                    var_node = node.left
                    if coeff < 0:
                        coeff_node = UniOpNode(Token(("-", MINUS)), NumberNode(Token((str(abs(coeff)), NUMBER))))
                    else:
                        coeff_node = NumberNode(Token((str(coeff), NUMBER)))
                    new_exp_node = NumberNode(Token((str(new_exp), NUMBER)))
                    new_node = BinOpNode(coeff_node, Token(("*", MUL)),
                                         BinOpNode(var_node, Token(("^", EXP)), new_exp_node))
                    if verbose:
                        self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                             + stringify_node(new_node, var) + "+C")
                        self.solution.append("------")
                        temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                        self.solution.append(stringify_node(temp_tree, var) + "+C")
                        self.solution.append("------")
                    return new_node, temp_tree
            elif node.op.tag == DIV:
                if node.left.type == NUMNode and round_complex(visit_NUMNode(node.left)) == 1:
                    if node.right.type == BINOPNode and node.right.op.tag == MUL and node.right.left.type == NUMNode and node.right.right.type == VARNode:
                        # ∫ 1/a*x dx = 1/a*ln(x)+c
                        print("Step 3.5.2", node)
                        coeff = round_complex(visit_NUMNode(node.right.left))
                        new_node = FuncNode(Token(("abs_ln", FUNC)), [node.right])
                        if coeff != 1:
                            if coeff == -1:
                                new_node = UniOpNode(Token(("-", MINUS)), new_node)
                            else:
                                coeff_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), NumberNode(Token((str(abs(coeff))))))
                                if coeff < 0:
                                    coeff_node = UniOpNode(Token(("-", MINUS)), coeff_node)
                                new_node = BinOpNode(coeff_node, Token(("*", MUL)), new_node)
                        if verbose:
                            self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                                 + stringify_node(new_node, var) + "+C")
                            self.solution.append("------")
                            temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                            self.solution.append(stringify_node(temp_tree, var) + "+C")
                            self.solution.append("------")
                        return new_node, temp_tree
                new_node, new_var = self.integral_substitution(node, verbose=verbose)
                print("Step 3", new_node)
                if new_node is not None:
                    new_node, _ = self.compute_integral(
                        new_node,
                        var=new_var,
                        temp_tree=deepcopy(new_node),
                        verbose=verbose)
                    print("Step 4", new_node)
                    new_node = self.resub_og_node(new_node)
                    print("Step 5", new_node)
                    if verbose:
                        self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                             + stringify_node(new_node, var) + "+C")
                        self.solution.append("------")
                        temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                        self.solution.append(stringify_node(temp_tree, var) + "+C")
                        self.solution.append("------")
                    return new_node, temp_tree
            tree_path.append("left")
            new_left, temp_tree = self.compute_integral(node.left, var=var, temp_tree=temp_tree, verbose=verbose,
                                                        tree_path=tree_path[:])
            tree_path[-1] = "right"
            new_right, temp_tree = self.compute_integral(node.right, var=var, temp_tree=temp_tree, verbose=verbose,
                                                         tree_path=tree_path[:])
            return BinOpNode(new_left, node.op, new_right), temp_tree
        elif node.type == FUNCNode:
            if node.op.value.lower() == "sin" and hash(node.args[0]) == hash(monomial_x[0]):
                coeff = round_complex(visit_NUMNode(node.args[0].left))
                new_node = FuncNode(Token(("cos", FUNC)), node.args)
                if coeff != -1:
                    if coeff == 1:
                        new_node = UniOpNode(Token(("-", MINUS)), new_node)
                    else:
                        coeff_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), NumberNode(Token((str(abs(coeff))))))
                        if coeff > 0:
                            coeff_node = UniOpNode(Token(("-", MINUS)), coeff_node)
                        new_node = BinOpNode(coeff_node, Token(("*", MUL)), new_node)
            elif node.op.value.lower() == "cos" and hash(node.args[0]) == hash(monomial_x[0]):
                coeff = round_complex(visit_NUMNode(node.args[0].left))
                new_node = FuncNode(Token(("sin", FUNC)), node.args)
                if coeff != 1:
                    if coeff == -1:
                        new_node = UniOpNode(Token(("-", MINUS)), new_node)
                    else:
                        coeff_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)),
                                               NumberNode(Token((str(abs(coeff)), NUMBER))))
                        if coeff < 0:
                            coeff_node = UniOpNode(Token(("-", MINUS)), coeff_node)
                        new_node = BinOpNode(coeff_node, Token(("*", MUL)), new_node)
            elif node.op.value.lower() == "tan" and hash(node.args[0]) == hash(monomial_x[0]):
                new_node = self.trig_identity(node)
                print("Step 1", new_node)
                if verbose:
                    self.solution.append(stringify_node(node, var) + " = " + stringify_node(new_node, var))
                    self.solution.append("------")
                    temp_tree = self.precisely_replace_node(temp_tree, tree_path[:], new_node)
                    self.solution.append(stringify_node(temp_tree, var) + "+C")
                    self.solution.append("------")
                    node = new_node
                print("Step 2", new_node)
                new_node, _ = self.compute_integral(new_node, var=var, temp_tree=temp_tree, tree_path=tree_path[:], verbose=verbose)
                print("YEET", new_node, "\n\n", temp_tree)
                verbose = False
            elif node.op.value.lower() == "sec" and hash(node.args[0]) == hash(monomial_x[0]):
                dummy_node = BinOpNode(deepcopy(node), Token(("+", PLUS)), FuncNode(Token(("tan", FUNC)), deepcopy(node.args)))
                dummy_node = BinOpNode(dummy_node, Token(("/", DIV)), dummy_node)
                new_node_num_right = BinOpNode(deepcopy(node), Token(("^", EXP)), NumberNode(Token(("2", NUMBER))))
                new_node_num_left = BinOpNode(FuncNode(Token(("tan", FUNC)), deepcopy(node.args)), Token(("*", MUL)), deepcopy(node))
                new_node_num = BinOpNode(new_node_num_left, Token(("+", PLUS)), new_node_num_right)
                new_node = BinOpNode(new_node_num, Token(("/", DIV)), dummy_node.right)
                if verbose:
                    self.solution.append("Multiplying " + stringify_node(node, var) + " by " + stringify_node(dummy_node, var)
                                          + " gives " + stringify_node(new_node, var))
                    self.solution.append("------")
                    temp_tree = self.precisely_replace_node(temp_tree, tree_path[:], new_node)
                    self.solution.append(stringify_node(temp_tree, var) + "+C")
                    self.solution.append("------")
                    node = new_node
                new_node, _ = self.compute_integral(new_node, var=var, temp_tree=temp_tree, tree_path=tree_path[:],
                                                    verbose=verbose)
                verbose = False
            if verbose:
                self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                     + stringify_node(new_node, var) + "+C")
                self.solution.append("------")
                temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                print(stringify_node(temp_tree, var), var, tree_path)
                self.solution.append(stringify_node(temp_tree, var) + "+C")
                self.solution.append("------")
            return new_node, temp_tree
        elif node.type == UNIOPNode:
            print("Step 3.5.1")
            tree_path.append("right")
            new_right, temp_tree = self.compute_integral(node.right, var=var, temp_tree=temp_tree, tree_path=tree_path[:], verbose=False)
            del tree_path[-1]
            new_node = UniOpNode(node.op, new_right)
            if new_right.type == UNIOPNode and new_right.op.tag == MINUS:
                new_node = new_right
            print("Step 3.5.3")
            if verbose:
                self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                     + stringify_node(new_node, var) + "+C")
                self.solution.append("------")
                temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, var) + "+C")
                self.solution.append("------")
            return new_node, temp_tree
        elif node.type == VARNode:
            new_exp = 2
            coeff = new_exp
            coeff_node = NumberNode(Token((str(coeff), NUMBER)))
            new_exp_node = NumberNode(Token((str(new_exp), NUMBER)))
            new_node = BinOpNode(BinOpNode(node.left, Token(("^", EXP)), new_exp_node), Token(("/", DIV)), coeff_node)
            if verbose:
                self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                     + stringify_node(new_node, var) + "+C")
                self.solution.append("------")
                temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, var) + "+C")
                self.solution.append("------")
            return new_node, temp_tree
        elif node.type == NUMNode:
            var_node = VariableNode(Token((var, VARIABLE)))
            new_node = BinOpNode(node, Token(("*", MUL)), var_node)
            if verbose:
                self.solution.append("∫ " + stringify_node(node, var) + " d" + var + " = "
                                     + stringify_node(new_node, var) + "+C")
                self.solution.append("------")
                temp_tree = self.precisely_replace_node(temp_tree, tree_path, new_node)
                self.solution.append(stringify_node(temp_tree, var) + "+C")
                self.solution.append("------")
            return new_node, temp_tree

    def trig_identity(self, node: AST) -> AST:
        """Method will replace the node based on trigonometric identities"""
        if node.op.value.lower() == "tan":
            return BinOpNode(FuncNode(Token(("sin", FUNC)), node.args), Token(("/", DIV)), FuncNode(Token(("cos", FUNC)), node.args))

    def integral_substitution(self, node: AST, verbose: bool = True) -> Tuple[Union[AST, None], str]:
        """Method will perform substitution to try and solve the integral"""
        if node.type == BINOPNode and node.op.tag == DIV:
            sub_chk = False
            sub_var = "u"
            if self.var == sub_var:
                sub_var = sub_var_dict[self.var]
            der, _ = self.compute_derivative(node.right, temp_tree=deepcopy(node), verbose=False)
            var_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("*", MUL)), VariableNode(Token((sub_var, VARIABLE))))
            if stringify_node(der, self.var) == stringify_node(node.left, self.var):
                sub_chk = True
                new_node = BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), var_node)
            elif der.type == UNIOPNode:
                if stringify_node(der.right, self.var) == stringify_node(node.left, self.var):
                    sub_chk = True
                    new_node = UniOpNode(Token(("-", MINUS)), BinOpNode(NumberNode(Token(("1", NUMBER))), Token(("/", DIV)), var_node))
            elif der.type == BINOPNode:
                if der.op.tag == MUL and der.left.type == NUMNode:
                    if stringify_node(der.right, self.var) == stringify_node(node.left, self.var):
                        sub_chk = True
                        new_node = BinOpNode(der.left, Token(("/", DIV)), var_node)
            if sub_chk:
                if verbose:
                    self.solution.append("Substituting " + stringify_node(node.right, self.var) + " for " + sub_var)
                    self.solution.append("------")
                    self.solution.append(sub_var + " = " + stringify_node(node.right, self.var))
                    self.solution.append("------")
                    self.solution.append("d"+sub_var+"/d"+self.var+" = "+stringify_node(der, self.var))
                    self.solution.append("------")
                    self.solution.append("d" + self.var + " = d" + sub_var + "/" + stringify_node(der, self.var) + " -> "
                                         + "∫ " + stringify_node(node.left, self.var) + "/" + stringify_node(der, self.var) + "*1/"
                                         + sub_var + " du")
                    self.solution.append("------")
                    if self.subs is None:
                        self.subs = {var_node: node.right}
                    else:
                        self.subs[var_node] = node.right
                return new_node, sub_var
            return None, self.var

    def resub_og_node(self, node: AST) -> AST:
        """Method will climb through tree and resubstitute based on expressions in self.subs"""
        if node in self.subs:
            return self.subs[node]
        if node.type == BINOPNode:
            return BinOpNode(self.resub_og_node(node.left), node.op, self.resub_og_node(node.right))
        elif node.type == UNIOPNode:
            return UniOpNode(node.op, self.resub_og_node(node.right))
        elif node.type == FUNCNode:
            new_args = []
            for arg in node.args:
                new_args.append(self.resub_og_node(arg))
            return FuncNode(node.op, new_args)
        return node

    def precisely_replace_node(self, tree: AST, old_node_path: List[str], new_node: AST) -> AST:
        """Method replaces a specific node based on a given path to it"""
        if not old_node_path:
            return new_node
        else:
            path = old_node_path[0]
            del old_node_path[0]
            for branch in old_node_path:
                path += "." + branch
            rsetattr(tree, path, new_node)
            return tree
