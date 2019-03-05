from Tree.Node import Node
from Special.Regular import Regular
from Special.Begin import Begin
from Special.If import If
from Special.Let import Let
from Special.Lambda import Lambda
from Special.Cond import Cond
from Special.Set import Set
from Special.Define import Define
from Special.Quote import Quote

class ConsNode(Node):
    def __init__(self, h, t):
        self.car = h
        self.cdr = t
        if not self.car.is_symbol():
            self.form = Regular()
        else:
            name = self.car.get_name()
            if name == "quote":
                self.form = Quote()
            elif name == "begin":
                self.form = Begin()
            elif name == "if":
                self.form = If()
            elif name == "let":
                self.form = Let()
            elif name == "lambda":
                self.form = Lambda()
            elif name == "cond":
                self.form = Cond()
            elif name == "set":
                self.form = Set()
            elif name == "define":
                self.form = Define()
            else:
                self.form = Regular()

    def is_pair(self):
        return True

    def print(self, i):
        self.form.print(self, i, False)

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
            return self.form.eval(self, env)
