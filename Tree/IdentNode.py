from Tree.Node import Node

class IdentNode(Node):
    def __init__(self, n):
        self.name = n

    def is_symbol():
        return True

    def print(self, i):
        print("%s%s" % (" " * i, self.name))
