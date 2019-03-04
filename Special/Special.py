from Tree.NilNode import nil_node

class Special:
    @staticmethod
    def eval_list(l, env):
        from Tree.ConsNode import ConsNode

        if l.is_null():
            return nil_node
        else:
            return ConsNode(l.get_car().eval(env), Special.eval_list(l.get_cdr(), env))
