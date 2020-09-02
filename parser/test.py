from parser.lexer import parse
from parser.combinator import TreeBuilder

list_of_tokens = parse("69+((21/3)^8.2)/(3*cos(45))")
tokens = TreeBuilder(list_of_tokens)
tree = tokens.build_tree()
print(tree)

list_of_tokens = parse("69+((21/3)^8.2)/(3*cos(45))+23")
tokens = TreeBuilder(list_of_tokens)
tree = tokens.build_tree()
print(tree)