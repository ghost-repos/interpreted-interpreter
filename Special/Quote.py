from Special.Special import Special

class Quote(Special):
    def eval(self, node, env):
        return node.get_cdr().get_car()
