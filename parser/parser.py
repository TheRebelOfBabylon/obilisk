from parser.ast import UniFunc, MultiFunc, BinOp, Variable, Number
from parser.combinator import Parser
from parser.lexer import Token, PLUS, MINUS, ENDL, EQUAL, EXP, MUL, DIV, L_MATRIX_BR, L_BRACKET, NUMBER, FUNC, VARIABLE, R_MATRIX_BR, R_BRACKET, COMMA, CONSTANT

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

class Interpreter():
    def __init__(self, token: Token, pos: int):
        self.token = token
        self.pos = pos

    def Equation(self):
        """Equation ::= Expression|Expression EQUAL Expression"""
        LHS = self.Expression()

        current_token = self.token
        if current_token.tag == "EQUAL":
            #EAT EQUAL
            #RHS = self.Expression()
            #return (LHS, RHS)
        #return result = LHS

    def Expression(self):
        """Expression ::= FUNC L_BRACKET (Term|(Term COMMA Term)+) R_BRACKET|Term|(Term(PLUS|MINUS)Term)+"""
        current_token = self.token
        if current_token.tag == FUNC:
            # EAT FUNC
            # current_token = self.token
            # If current_token.tag == L_BRACKET:
                # result = []
                # result.append(self.Term())

                # current_token = self.token
                # if current_token.tag == COMMA:
                    # while current_token.tag == COMMA:
                        # EAT COMMA
                        # result.append(self.Term())
                # if current_token.tag == R_BRACKET:
                    # EAT R_BRACKET:
                    # return result
        else:
            result = self.Term()

            current_token = self.token
            while current_token.tag in (PLUS, MINUS):
                current_token = self.token
                if current_token.type == PLUS:
                    # EAT PLUS
                    # result = result + self.Term()
                elif current_token.tag == MINUS:
                    # Eat MINUS
                    # result = result + self.Term()

            return result

    def Term(self):
        """Term ::= Factor|(Factor(MUL|DIV)Factor)+"""
        result = self.Factor()

        current_token = self.token
        while current_token.tag in (MUL, DIV):
            current_token = self.token
            if current_token.type == MUL:
                #EAT MUL
                #result = result * self.Factor()
            elif current_token.tag == DIV:
                #Eat DIV
                #result = result / self.Factor()

        return result

    def Factor(self):
        """Factor ::= Atom|(Atom EXP Atom)+"""
        result = self.Atom()

        current_token = self.token
        while current_token.tag == EXP:
            current_token = self.token
            #EAT EXP
            #result = result ** self.Atom()

        return result

    def Atom(self):
        """
        Atom ::= Matrix|NUMBER|VARIABLE|CONSTANT|L_BRACKET Expression R_BRACKET
        Matrix ::= L_MATRIX_BR (Expression|Expression(COMMA|ENDL)Expression+ R_MATRIX_BR
        """

        current_token = self.token
        if current_token.tag == NUMBER:
            #Eat token
            #return current_token.value
            pass
        elif current_token.tag == VARIABLE:
            #Eat token
            #return current_token.value
            pass
        elif current_token.tag == CONSTANT:
            #Eat token
            #return current_token.value
            pass
        elif current_token.tag == L_BRACKET:
            #Eat L_BRACKET
            #result = self.expression() #There's the recursion
            #Eat R_BRACKET
            #return result
            pass
        elif current_token.tag == L_MATRIX_BR:
            #EAT L_MATRIX_BR
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

