from Special.Special import Special
from Tree.BooleanNode import true_node

class If(Special):
    def eval(self, node, env):
        condition = node.get_cdr().get_car()
        cddr = node.get_cdr().get_cdr()
        return cddr.get_car().eval(env) if condition.eval(env) == true_node \
                else cddr.get_cdr().get_car().eval(env)
