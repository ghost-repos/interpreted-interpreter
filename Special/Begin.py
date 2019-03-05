from Special.Special import Special

class Begin(Special):
    def eval(self, node, env):
        return Special.eval_body(node.get_cdr(), env)
