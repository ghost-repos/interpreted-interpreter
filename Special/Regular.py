from Special.Special import Special

class Regular(Special):
    def eval(self, node, env):
        fun = node.get_car().eval(env)
        params = Special.eval_list(node.get_cdr(), env)
        return fun.apply(params)
