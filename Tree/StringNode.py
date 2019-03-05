from Tree.Node import Node

class StringNode(Node):
    def __init__(self, s):
        self.val = s

    def is_string(self):
        return True

    def print(self, i):
        # no indenting
        print(self.val, end="")

    def eval(self, env):
        return self
