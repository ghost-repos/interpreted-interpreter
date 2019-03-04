from Tree.Node import Node

class ConsNode(Node):
    def __init__(self, h, t):
        self.car = h
        self.cdr = t

    def is_pair():
        return True

    def print(self, i):
        self.car.print(i)
        self.cdr.print(i + 4)
