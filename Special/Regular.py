from Special.Special import Special

class Regular(Special):
    def eval(self, node, env):
        fun = node.get_car().eval(env)
        params = Special.eval_list(node.get_cdr(), env)
        return fun.apply(params)

    def print(self, node, i, p=True):
        if not p: # if a parenthesis wasnt opened yet
            print()
            print("%s" % (" " * i), end="") # indent
            print("(", end="")
            i += 4 # also indent
        while not node.is_null():
            node.get_car().print(i)
            node = node.get_cdr()
            if node.is_pair():
                print(" ", end="")
            else:
                if not node.is_null(): # in the case of something like (a b . c)
                    print(" . ", end="")
                    node.print(0)
                break
        if not p:
            print(")", end="")
