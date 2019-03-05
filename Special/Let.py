from Special.Special import Special
from Tree.Environment import Environment

class Let(Special):
    def eval(self, node, env):
        env = Environment(env)
        Let.add_defs(node, env)

    @staticmethod
    def add_defs(node, env):
        if node.is_null():
            return
        ident = node.get_car().get_car()
        val = node.get_car().get_cdr().get_car()
        env.define(ident, val.eval(env))
        Let.add_defs(node.get_cdr(), env)
