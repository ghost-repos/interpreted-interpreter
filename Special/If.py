from Special.Special import Special
from Tree.BooleanNode import true_node

class If(Special):
    def eval(self, node, env):
        condition = node.get_cdr().get_car()
        cddr = node.get_cdr().get_cdr()
        return cddr.get_car().eval(env) if condition.eval(env) == true_node \
                else cddr.get_cdr().get_car().eval(env)

    def print(self, node, i, p=True):
        print("if ", end="") # print if statement
        node.get_cdr().get_car().print(i) # print the condition (regular)
        print(" ", end="")
        cddr = node.get_cdr().get_cdr()
        t = cddr.get_car()
        t.print(i) # print true body (regular or node)
        print(" ", end="")
        f = cddr.get_cdr().get_car()
        f.print(i + 4) # print false body (regular or node)
