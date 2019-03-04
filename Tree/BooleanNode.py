from Node import Node

class BooleanNode(Node):
    def __init__ (self, val):
        self.bool_val = val

    def is_bool():
        return True

true_node = BooleanNode(True)
false_node = BooleanNode(False)
