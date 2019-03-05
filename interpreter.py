import sys

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
        "eq?", "cons", "apply", "eval", "set-car!", "set-cdr!"]

for built_in in built_ins:
    built_in_env.define(IdentNode(built_in), BuiltInNode(built_in))

# some more builtins for ease
parser.feed("""
            (define (b>= x y)
                (if (b< x y) #f #t))
            (define (b> x y)
                (if (b>= x y)
                    (if (b= x y) #f #t) #f))
            (define (b<= x y)
                (if (b> x y) #f #t))
            (define (+ x . z)
                (if (null? z) x
                    (b+ x (apply + z))))
            """)
root = parser.parse()
while root != None:
    root.eval(built_in_env)
    root = parser.parse()

global_env = Environment(built_in_env)

while True:
    try:
        parser.feed(input())
        root = parser.parse()
        while root != None:
            root.eval(global_env).print(0)
            root = parser.parse()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)
