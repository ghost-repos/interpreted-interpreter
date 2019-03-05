from Special.Special import Special
from Tree.NilNode import nil_node

class Set(Special):
    def eval(self, node, env):
        ident = node.get_cdr().get_car()
        val = node.get_cdr().get_cdr().get_car().eval(env)
        if env.lookup(ident) != None:
            env.assign(ident, val)
        else:
            raise Exception("tried setting a nonexistant var")
        return nil_node
