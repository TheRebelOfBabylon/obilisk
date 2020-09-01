from parser.ast import UniFuncNode, MultiFuncNode, BinOpNode, VariableNode, NumberNode, EquationNode, ExpressionNode, TermNode, FactorNode, ConstantNode
from parser.combinator import Parser
from parser.lexer import Token, PLUS, MINUS, ENDL, EQUAL, EXP, MUL, DIV, L_MATRIX_BR, L_BRACKET, NUMBER, FUNC, VARIABLE, R_MATRIX_BR, R_BRACKET, COMMA, CONSTANT

from typing import List

#Equation ::= Expression|(Expression EQUAL Expression)
#An equation is either an expression or an Expression equal to another Expression

#Expression ::= FUNC L_BRACKET (Term|(Term COMMA Term)) R_BRACKET|Term|(Term(PLUS|MINUS)Term)+
#An Expression can be a term or a series of terms seperated by + or - signs

#Term ::= Factor|(Factor(MUL|DIV)Factor)+
#Term can be a an expression, a term, a matrix or factors multiplied by expressions, terms, matrices, factors and or raised to powers of expressions, terms or factors, seperated by commas or semi-colons or surrounded by paratheses, or a func and parathenses, and if there is a paranthesis, raised to the power of a Expression, Term or Factor

#Factor ::= Atom|(Atom EXP Atom)

#Atom ::= Matrix|NUMBER|VARIABLE|CONSTANT|LPAR Expression RPAR

#Matrix ::= LBRACK Expression|(Expression(COMMA|ENDL)Expression) RBRACK

#Func ::= Trig, Calculus, Log, LN, SQRT, ABS

class Parser():
    def __init__(self, list_of_tokens: List[Token], pos: int = 0):
        self.tokens = list_of_tokens
        self.pos = pos

    def consume_token(self, tag):
        """Compares current token tag to given tag"""
        if self.tokens[self.pos].tag == tag:
            self.pos += 1
        else:
            raise Exception('Invalid syntax')

    def Equation(self):
        """Equation ::= Expression|Expression EQUAL Expression"""
        LHS = self.Expression()

        current_token = self.tokens[self.pos]
        if current_token.tag == EQUAL:
            self.consume_token(EQUAL)
            RHS = self.Expression()
            return EquationNode(current_token, [LHS, RHS])
        return EquationNode(current_token, [LHS])

    def Expression(self):
        """Expression ::= Term|(Term(PLUS|MINUS)Term)+"""
        result = []
        left = self.Term()
        current_token = self.tokens[self.pos]
        while current_token.tag in (PLUS, MINUS):
            if current_token.type == PLUS:
                bin_op = current_token
                self.consume_token(PLUS)
                right = self.Term() #BinaryOpASTNode needs to be added here somehow
            elif current_token.tag == MINUS:
                bin_op = current_token
                self.consume_token(MINUS)
                right = self.Term()
            result.append(BinOpNode(left, bin_op, right))
            left = right
            current_token = self.tokens[self.pos]
        return ExpressionNode(current_token, result)

    def Term(self):
        """Term ::= (Factor|(Factor(MUL|DIV)Factor)+)|FUNC L_BRACKET Factor R_BRACKET"""
        current_token = self.tokens[self.pos]
        if current_token.tag == FUNC:
            self.consume_token(FUNC)
            current_token = self.tokens[self.pos]
            if current_token.tag == L_BRACKET:
                result = []
                result.append(self.Factor()) #This might need to be self.Expression(). I think it goes to atom then loops. Not sure

                current_token = self.tokens[self.pos]
                if current_token.tag == COMMA:
                    while current_token.tag == COMMA:
                        self.consume_token(COMMA)
                        result.append(self.Factor()) #This to
                if current_token.tag == R_BRACKET:
                    self.consume_token(R_BRACKET)
                    return TermNode(current_token, result)
        else:
            result = []
            left = self.Factor()
            current_token = self.tokens[self.pos]
            while current_token.tag in (MUL, DIV):
                if current_token.type == MUL:
                    bin_op = current_token
                    self.consume_token(MUL)
                    right = self.Factor()
                elif current_token.tag == DIV:
                    bin_op = current_token
                    self.consume_token(DIV)
                    right = self.Factor()
                result.append(BinOpNode(left, bin_op, right))
                left = right
                current_token = self.tokens[self.pos]

            return TermNode(current_token, result)

    def Factor(self):
        """Factor ::= Atom|(Atom EXP Atom)+"""
        result = []
        base = self.Atom()

        current_token = self.tokens[self.pos]
        while current_token.tag == EXP:
            self.consume_token(EXP)
            exponent = self.Atom()
            result.append(BinOpNode(base, current_token, exponent))
            current_token = self.tokens[self.pos]


        return FactorNode(current_token, result)

    def Atom(self):
        """Atom ::= Matrix|NUMBER|VARIABLE|CONSTANT|L_BRACKET Expression R_BRACKET"""
        current_token = self.tokens[self.pos]
        if current_token.tag == NUMBER:
            self.consume_token(NUMBER)
            return NumberNode(current_token)
        elif current_token.tag == VARIABLE:
            self.consume_token(VARIABLE)
            return VariableNode(current_token)
        elif current_token.tag == CONSTANT:
            self.consume_token(CONSTANT)
            return ConstantNode(current_token)
        elif current_token.tag == L_BRACKET:
            self.consume_token(L_BRACKET)
            result = self.Expression() #There's the recursion
            self.consume_token(R_BRACKET)
            return result
        elif current_token.tag == L_MATRIX_BR:
            self.consume_token(L_MATRIX_BR)
            #result = []
            #result.append(self.Expression())

            # current_token = self.token
            #if current_token.tag in (COMMA, ENDL):
                #while current_token.tag in (COMMA, ENDL)"
                    #if current_token.tag == COMMA:
                        #EAT COMMA
                        #result.append(self.Expression())
                    #elif current_token.tag == ENDL:
                        #EAT ENDL
                        #current_token = self.token
                        #if current_token.tag != R_MATRIX_BR:
                            #Insert new column in result
                            #result.append(self.Expression())
                #if current_token.tag == R_MATRIX_BR:
                    #EAT R_MATRIX_BR
                    #return result

    def Matrix(self):
        """Matrix ::= L_MATRIX_BR (Expression|Expression(COMMA|ENDL)Expression+ R_MATRIX_BR"""


