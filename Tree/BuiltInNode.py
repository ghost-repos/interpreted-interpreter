from Tree.Node import Node
from Tree.IntNode import IntNode
from Tree.ConsNode import ConsNode
from Tree.NilNode import nil_node
from Tree.BooleanNode import true_node, false_node

class BuiltInNode(Node):
    def __init__(self, s):
        self.symbol = s

    def get_name(self):
        return self.symbol

    def is_procedure(self):
        return True

    def apply(self, args):
        built_in = self.symbol
        args_length = Node.list_length(args)
        if args_length == 0:
            if build_in == "newline":
                print()
                return nil_node
            else:
                raise Exception("unknown builtin function with 0 params")

        arg1 = args.get_car()
        if args_length == 1:
            if built_in == "write":
                arg1.print(0)
                return nil_node
            elif built_in == "car":
                return arg1.get_car()
            elif built_in == "cdr":
                return arg1.get_cdr()
            elif built_in == "null?":
                return true_node if arg1.is_null() else false_node
            elif built_in == "pair?":
                return true_node if arg1.is_pair() else false_node
            elif built_in == "procedure?":
                return true_node if arg1.is_procedure() else false_node
            elif built_in == "symbol?":
                return true_node if arg1.is_symbol() else false_node
            elif built_in == "number?":
                return true_node if arg1.is_number() else false_node
            elif built_in == "display":
                return arg1
            else:
                raise Exception("unknown builtin function with 1 param")

        arg2 = args.get_cdr().get_car()
        if args_length == 2:
            if built_in == "b-":
                return IntNode(arg1.get_value() - arg2.get_value())
            elif built_in == "b+":
                return IntNode(arg1.get_value() + arg2.get_value())
            elif built_in == "b*":
                return IntNode(arg1.get_value() * arg2.get_value())
            elif built_in == "b/":
                return IntNode(arg1.get_value() / arg2.get_value())
            elif built_in == "b=":
                return true_node if arg1.get_value() == arg2.get_value() else false_node
            elif built_in == "b<":
                return true_node if arg1.get_value() < arg2.get_value() else false_node
            elif built_in == "eq?":
                return true_node if arg1 == arg2 else false_node
            elif built_in == "cons":
                return ConsNode(arg1, arg2)
            elif built_in == "apply":
                return arg1.apply(arg2)
            elif built_in == "eval":
                return arg1.eval(arg2)
            elif built_in == "set-car!":
                arg1.set_car(arg2)
                return arg1
            elif built_in == "set-cdr!":
                arg1.set_cdr(arg2)
                return arg1
            else:
                raise Exception("unknown builtin function with 2 params")

        raise Exception("unknown builtin function")





























