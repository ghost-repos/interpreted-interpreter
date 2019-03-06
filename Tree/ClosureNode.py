from Tree.Node import Node
from Tree.Environment import Environment
from Tree.IdentNode import IdentNode
from Tree.NilNode import nil_node

class ClosureNode(Node):
    def __init__(self, lambd, env):
        self.f = lambd
        self.env = env

    def is_procedure(self):
        return True

    def print(self, i, p=False):
        # no indenting
        print("%s#{Procedure" % (" " * i), end="")
        if self.f != None:
            self.f.print(i + 4)
            print()
        print("%s}" % (" " * i))

    def apply(self, args):
        from Tree.ConsNode import ConsNode
        params = self.f.get_cdr().get_car()
        if not Node.same_length_lists(params, args):
            raise Exception("params and argument count don't match")
        head = nil_node
        env = Environment(self.env)

        while not params.is_null():
            if not params.is_pair(): # n-ary function ?
                env.define(params, args)
                break
            else:
                env.define(params.get_car(), args.get_car())
                params = params.get_cdr()
                args = args.get_cdr()

        body = self.f.get_cdr().get_cdr()
        return ConsNode(IdentNode("begin"), body).eval(env)
