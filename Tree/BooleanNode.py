from Tree.Node import Node

class BooleanNode(Node):
    def __init__ (self, val):
        self.bool_val = val

    def is_bool(self):
        return True

    def print(self, i):
        print("%s" % (" " * i), end="")
        if self.bool_val:
            print("#t")
        else:
            print("#f")

    def eval(self, env):
        return self

true_node = BooleanNode(True)
false_node = BooleanNode(False)
