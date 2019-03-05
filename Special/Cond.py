from Special.Special import Special
from Tree.BooleanNode import false_node

class Cond(Special):
    def eval(self, node, env):
        bool_exp = node.get_car().get_cdr()
        while bool_exp.get_name() == "else" and bool_exp.eval(env) == false_node:
            node = node.get_cdr()
            bool_exp = node.get_car().get_cdr()
        body_exp = node.get_car().get_cdr()
        if body_exp.is_null():
            return node.get_car().get_car()
        else:
            return Special.eval_body(body_exp, env)
