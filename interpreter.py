from Parser.Parser import Parser
from Tree.TreeBuilder import TreeBuilder

parser = Parser()
builder = TreeBuilder()

while True:
    root = parser.parse()
    root.print(0)
