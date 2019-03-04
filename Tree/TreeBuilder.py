import IntNode, StringNode, IdentNode, ConsNode
from NilNode import nil_node
from BooleanNode import true_node, false_node

class TreeBuilder:
    def build_boolean_node(self, b):
        if b:
            return true_node
        else:
            return false_node

    def build_int_node(self, i):
        return IntNode(i)

    def build_string_node(self, string):
        return StringNode(string)

    def build_ident_node(self, ident):
        return IdentNode(ident)

    def build_nil_node(self):
        return nil_node

    def build_cons_node(self, a, b):
        return ConsNode(a, b)
