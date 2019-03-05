from Tree.Node import Node

class NilNode(Node):
    def is_null(self):
        return True

    def print(self, i):
        # no indenting
        print("()", end="")

    def eval(self, env):
        return nil_node

nil_node = NilNode()
