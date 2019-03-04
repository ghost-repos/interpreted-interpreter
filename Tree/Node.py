class Node:
    def print(self, i):
        raise NotImplementedError("print(self, i) should be implemented in all subclasses")

    def is_bool():
        return false

    def is_number():
        return false

    def is_string():
        return false

    def is_symbol():
        return false

    def is_null():
        return false

    def is_pair():
        return false

    def is_procedure():
        return false

    def get_car():
        raise Exception("car is not returning a pair")

    def get_cdr():
        raise Exception("cdr is not returning a pair")

    def set_car():
        raise Exception("argument of set_car! is not a pair")

    def set_cdr():
        raise Exception("argument of set_cdr! is not a pair")

    def get_name():
        return ""

    def apply(self, args):
        raise Exception("this node does not have an apply function")

    def eval(self, env):
        raise Exception("this node does not have an eval function")

    def same_length_lists(self, params, args):
        if (params.is_null()):
            return args.is_null()
        elif args.is_null():
            return params.is_null() or not params.is_pair()
        elif not param.is_pair():
            return true
        else:
            return same_length_lists(params.get_cdr(), args.get_cdr())
