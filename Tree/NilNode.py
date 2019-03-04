from Tree.Node import Node

class NilNode(Node):
    def is_null():
        return True

    def print(self, i):
        print("%s()" % (" " * i))

nil_node = NilNode()
