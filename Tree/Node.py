class Node:
    def print(self, i):
        raise NotImplementedError("print(self, i) should be implemented in all subclasses")

    def is_bool(self):
        return False

    def is_number(self):
        return False

    def is_string(self):
        return False

    def is_symbol(self):
        return False

    def is_null(self):
        return False

    def is_pair(self):
        return False

    def is_procedure(self):
        return False

    def get_car(self):
        raise Exception("car is not returning a pair")

    def get_cdr(self):
        raise Exception("cdr is not returning a pair")

    def set_car(self, a):
        raise Exception("argument of set_car! is not a pair")

    def set_cdr(self, a):
        raise Exception("argument of set_cdr! is not a pair")

    def get_name(self):
        raise Exception("this node does not have a get_name function")

    def get_value(self):
        raise Exception("this node does not have a get_value function")

    def apply(self, args):
        raise Exception("this node does not have an apply function")

    def eval(self, env):
        raise Exception("this node does not have an eval function")

    @staticmethod
    def same_length_lists(params, args):
        if params.is_null():
            return args.is_null()
        elif args.is_null():
            return not params.is_pair()
        else:
            return Node.same_length_lists(params.get_cdr(), args.get_cdr())

    @staticmethod
    def list_length(args, i=0):
        if args.is_null():
            return i
        else:
            return Node.list_length(args.get_cdr(), i + 1)
