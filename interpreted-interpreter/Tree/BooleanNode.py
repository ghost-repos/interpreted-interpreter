from Tree.Node import Node

class BooleanNode(Node):
    def __init__ (self, val):
        self.bool_val = val

    def is_bool(self):
        return True

    def print(self, i, p=False):
        # no indenting
        print("#t", end="") if self.bool_val else print("#f", end="")

    def eval(self, env):
        return self

true_node = BooleanNode(True)
false_node = BooleanNode(False)
