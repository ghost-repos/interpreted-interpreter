class Environment:
    def __init__(self, env=None):
        self.parent_env = env
        self.frame = {}

    def find(self, node):
        var = node.get_name()
        if var in self.frame:
            return self.frame[var]
        else:
            return None

    def lookup(self, node):
        result = self.find(node)
        if result != None:
            return result
        elif self.parent_env != None:
            return self.parent_env.lookup(node)
        else:
            raise Exception("undefined variable " + node.get_name())

    def define(self, node, val):
        self.frame[node.get_name()] = val

    def assign(self, node, val):
        result = self.find(node)
        if result != None:
            self.frame[node.get_name()] = val
        elif self.parent_env != None:
            self.parent_env.assign(node, val)
        else:
            raise Exception("undefined variable " + node.get_name())
