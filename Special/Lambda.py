from Special.Special import Special
from Tree.ClosureNode import ClosureNode

class Lambda(Special):
    def eval(self, node, env):
        return ClosureNode(node, env)
