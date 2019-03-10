import sys, os
sys.path.append(os.path.join(sys.path[0], "../interpreted-interpreter"))

from Parser.Parser import Parser
from Tree.TreeBuilder import TreeBuilder
from Tree.Environment import Environment
from Tree.BuiltInNode import BuiltInNode
from Tree.IdentNode import IdentNode

parser = Parser()
builder = TreeBuilder()
built_in_env = Environment()
built_ins = ["newline", "write", "car", "cdr", "null?", "pair?", "procedure?",
        "symbol?", "number?", "display", "b-", "b+", "b*", "b/", "b=", "b<",
        "eq?", "cons", "apply", "eval", "set-car!", "set-cdr!", "builtin-env",
        "global-env"]
for built_in in built_ins:
    built_in_env.define(IdentNode(built_in), BuiltInNode(built_in))
global_env = Environment(built_in_env)
BuiltInNode.set_starting_env(built_in_env, global_env)

def get_parser(new_global=False):
    global global_env
    if new_global:
        global_env = Environment(built_in_env)
    return (parser, global_env)

def eval_and_print(s, new_global=False):
    (parser, global_env) = get_parser(new_global)
    parser.feed(s)
    parser.parse().eval(global_env).print(0)

def assert_stripped_output_is(capsys, s):
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out.strip() == s
