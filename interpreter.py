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
        "eq?", "cons", "apply", "eval", "set-car!", "set-cdr!", "builtin-env",
        "global-env"]

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
            """
            # example of n-ary addition
            """
            (define (+ x . z)
                (if (null? z) x
                    (b+ x (apply + z))))
            """
            # a few higher order functions
            """
            (define (map f l)
                (if (null? l) ()
                    (cons (f (car l)) (map f (cdr l)))))
            (define (fold f l ac)
                (if (null? l) ac
                    (fold f (cdr l) (f (car l) ac))))
            """
            # sort that takes n-ary amount of numbers
            # (sort 1 9 28 1 3)
            # (apply sort '(1 99 71 53))
            """
            (define (sort . z)
                (define (bmerge a b)
                    (if (null? b) a
                        (if (null? a) b
                            (if (b< (car a) (car b))
                                (cons (car a) (bmerge (cdr a) b))
                                (cons (car b) (bmerge a (cdr b)))))))
                (define (merge a . z)
                    (if (null? z) a
                        (apply merge (cons (bmerge a (car z)) (cdr z)))))
                (apply merge (map (lambda (x) (cons x ())) z)))
            """)
root = parser.parse()
while root != None:
    root.eval(built_in_env)
    root = parser.parse()

global_env = Environment(built_in_env)

BuiltInNode.set_starting_env(built_in_env, global_env)

while True:
    try:
        parser.feed(input())
        root = parser.parse()
        while root != None:
            root.eval(global_env).print(0)
            print()
            root = parser.parse()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)
