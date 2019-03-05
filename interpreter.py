import sys

from Parser.Parser import Parser
from Tree.TreeBuilder import TreeBuilder
from Tree.Environment import Environment
from Tree.BuiltInNode import BuiltInNode
from Tree.IdentNode import IdentNode

parser = Parser()
builder = TreeBuilder()
built_in_env = Environment()
built_ins = ["newline", "write", "car", "cdr", "null?", "pair?", "procedure?", \
        "symbol?", "number?", "display", "b-", "b+", "b*", "b/", "b=", "b<", \
        "eq?", "cons", "apply", "eval", "set-car!", "set-cdr!"]

for built_in in built_ins:
    built_in_env.define(IdentNode(built_in), BuiltInNode(built_in))

global_env = Environment(built_in_env)

try:
    while True:
        parser.feed(input())
        root = parser.parse()
        root.eval(global_env).print(0)
except KeyboardInterrupt:
    sys.exit(0)
