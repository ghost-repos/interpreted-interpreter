import sys

from Parser.Parser import Parser
from Tree.TreeBuilder import TreeBuilder
from Tree.Environment import Environment
from Tree.BuiltInNode import BuiltInNode
from Tree.IdentNode import IdentNode

parser = Parser()
builder = TreeBuilder()
built_in_env = Environment()
built_in_env.define(IdentNode("b+"), BuiltInNode("b+"))
global_env = Environment(built_in_env)

# example code, b+ is binary +
# parser.feed("(b+ 1 (b+ 3 4))")
# root = parser.parse()
# root.eval(global_env).print(0)

try:
    while True:
        parser.feed(input())
        root = parser.parse()
        root.eval(global_env).print(0)
except KeyboardInterrupt:
    sys.exit(0)
