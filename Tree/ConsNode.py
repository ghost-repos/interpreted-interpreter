from Tree.Node import Node
from Special.Regular import Regular

class ConsNode(Node):
    def __init__(self, h, t):
        self.car = h
        self.cdr = t

    def is_pair(self):
        return True

    def print(self, i):
        print("cons")
        self.car.print(i)
        self.cdr.print(i + 4)

    def get_car(self):
        return self.car

    def get_cdr(self):
        return self.cdr

    def set_car(self, node):
        self.car = node

    def set_cdr(self, node):
        self.cdr = node

    def eval(self, env):
        if self.car.is_procedure():
            return self
        else:
            return Regular().eval(self, env)
