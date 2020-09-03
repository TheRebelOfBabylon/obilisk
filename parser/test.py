from parser.lexer import parse
from parser.combinator import TreeBuilder
from parser.interpreter import Interpreter

list_of_tokens = parse("69+((21/3)^8.2)/(3*cos(45))")
tokens = TreeBuilder(list_of_tokens)
tree = tokens.build_tree()
inter = Interpreter(tree)
print(inter.solve())

list_of_tokens = parse("sqrt(3-6)+2")
tokens = TreeBuilder(list_of_tokens)
tree = tokens.build_tree()
inter = Interpreter(tree)
print(inter.solve())

list_of_tokens = parse("2-0.7j*cos(45))")
tokens = TreeBuilder(list_of_tokens)
tree = tokens.build_tree()
inter = Interpreter(tree)
print(inter.solve())
