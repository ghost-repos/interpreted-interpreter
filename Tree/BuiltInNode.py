from Tree.Node import Node
from Tree.IntNode import IntNode
from Tree.NilNode import nil_node

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
            pass
        arg1 = args.get_car()
        if args_length == 1:
            pass
        arg2 = args.get_cdr().get_car()
        if args_length == 2:
            if built_in == "b+":
                return IntNode(arg1.get_value() + arg2.get_value())
