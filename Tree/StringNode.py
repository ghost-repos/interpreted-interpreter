from Tree.Node import Node

class StringNode(Node):
    def __init__(self, s):
        self.val = s

    def is_string():
        return True

    def print(self, i):
        print("%s%s" % (" " * i, self.val))
