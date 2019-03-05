from Tree.Node import Node

class IntNode(Node):
    def __init__(self, i):
        self.val = i

    def get_value(self):
        return self.val

    def is_number(self):
        return True

    def print(self, i):
        # no indenting
        print(self.val, end="")

    def eval(self, env):
        return self
