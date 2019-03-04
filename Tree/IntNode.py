from Tree.Node import Node

class IntNode(Node):
    def __init__(self, i):
        self.val = i

    def is_number():
        return True

    def print(self, i):
        print("%s%s" % (" " * i, self.val))
