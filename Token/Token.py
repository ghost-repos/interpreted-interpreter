class Token:
    def __init__(self, t):
        self.type = t

    def get_type(self):
        return self.type

    def get_int_val(self):
        raise Exception("this token does not have an int value")

    def get_string_val(self):
        raise Exception("this token does not have a string value")

    def get_name(self):
        raise Exception("this token does not have a name")
