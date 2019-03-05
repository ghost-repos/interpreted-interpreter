from Tree.Node import Node

class BooleanNode(Node):
    def __init__ (self, val):
        self.bool_val = val

    def is_bool(self):
        return True

    def print(self, i):
        # no indenting
        print("#t") if self.bool_val else print("#f")

    def eval(self, env):
        return self

true_node = BooleanNode(True)
false_node = BooleanNode(False)
