import sys, os
sys.path.append(os.path.join(sys.path[0], "../interpreted-interpreter"))

from Parser.Parser import Parser
from Tree.TreeBuilder import TreeBuilder
from Tree.Environment import Environment
from Tree.BuiltInNode import BuiltInNode
from Tree.IdentNode import IdentNode

def setup_parser():
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
    return (parser, global_env)

def eval_and_print(s):
    (parser, global_env) = setup_parser()
    parser.feed(s)
    parser.parse().eval(global_env).print(0)

def assert_stripped_output_is(capsys, s):
    (out, err) = capsys.readouterr()
    assert out.strip() == s


import pytest, random

class TestBuiltins(object):
    @pytest.mark.parametrize("v1, v2", [(x, y) for x in range(10) for y in range(5)])
    def test_binary_addition(self, v1, v2, capsys):
        eval_and_print("(b+ %s %s)" % (v1, v2))
        assert_stripped_output_is(capsys, str(v1 + v2))

    @pytest.mark.parametrize("v1, v2", [(x, y) for x in range(10) for y in range(5)])
    def test_binary_subtraction(self, v1, v2, capsys):
        eval_and_print("(b- %s %s)" % (v1, v2))
        assert_stripped_output_is(capsys, str(v1 - v2))

    @pytest.mark.parametrize("numbers", [([int(10 * random.random())
        for _ in range(10)])
            for _ in range(10)])
    def test_cons(self, numbers, capsys):
        # generate cons expression
        s = "".join(["(cons %s" % x for x in numbers])
        # close with (cons 1 ()) and add closing parens
        s = "%s (cons 1 ()) %s" % (s, ")" * len(numbers))
        eval_and_print(s)
        assert_stripped_output_is(capsys, "(%s 1)" % " ".join(str(n) for n in numbers))

    def test_cons_dot(self, capsys):
        eval_and_print("(cons 1 2)")
        assert_stripped_output_is(capsys, "(1 . 2)")

    @pytest.mark.parametrize("numbers", [([int(10 * random.random())
            for _ in range(10)])
                for _ in range(10)])
    def test_car(self, numbers, capsys):
        eval_and_print("(car '(%s))" % " ".join(str(n) for n in numbers))
        assert_stripped_output_is(capsys, str(numbers[0]))

    @pytest.mark.parametrize("numbers", [([int(10 * random.random())
            for _ in range(10)])
                for _ in range(10)])
    def test_cdr(self, numbers, capsys):
        eval_and_print("(cdr '(%s))" % " ".join(str(n) for n in numbers))
        assert_stripped_output_is(capsys, "(%s)" % " ".join(str(n) for n in numbers[1:]))

    @pytest.mark.parametrize("number", [x for x in range(10)])
    def test_set_car(self, number, capsys):
        eval_and_print("(set-car! '(11 2 3 4) %s)" % number)
        assert_stripped_output_is(capsys, "(%s 2 3 4)" % number)

    @pytest.mark.parametrize("numbers", [([int(10 * random.random())
            for _ in range(10)])
                for _ in range(10)])
    def test_set_cdr(self, numbers, capsys):
        nums = " ".join(str(n) for n in numbers)
        eval_and_print("(set-cdr! '(11 2 3 4) '(%s))" % nums)
        assert_stripped_output_is(capsys, "(11 %s)" % nums)
