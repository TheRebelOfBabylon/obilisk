from parser.lexer import Lexer
from parser.combinator import TreeBuilder
from parser.interpreter import Interpreter


lexer = Lexer("69+((21/3)^8.2)/(3*cos(45))")
list_of_tokens = lexer.obilisk_lex()
if not lexer.vars:
    tokens = TreeBuilder(list_of_tokens)
    tree = tokens.build_tree()
    inter = Interpreter(tree)
    print(inter.solve())

lexer = Lexer("sqrt(-3)+2")
list_of_tokens = lexer.obilisk_lex()
if not lexer.vars:
    tokens = TreeBuilder(list_of_tokens)
    tree = tokens.build_tree()
    inter = Interpreter(tree)
    print(inter.solve())

lexer = Lexer("2-0.7j*cos(45))")
list_of_tokens = lexer.obilisk_lex()
if not lexer.vars:
    tokens = TreeBuilder(list_of_tokens)
    tree = tokens.build_tree()
    inter = Interpreter(tree)
    print(inter.solve())

lexer = Lexer("69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)=x+3")
list_of_tokens = lexer.obilisk_lex()
if not lexer.vars:
    tokens = TreeBuilder(list_of_tokens)
    tree = tokens.build_tree()
    inter = Interpreter(tree)
    print(inter.solve())
