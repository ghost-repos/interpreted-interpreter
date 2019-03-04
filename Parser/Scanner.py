class Scanner:
    special_id_chars = {"!", "$", "%", "&", "*", "+", "-", ".", "/",
            ":", "<", "=", ">", "?", "@", "^"}

    @staticmethod
    def is_valid_id_character(self, c):
        c_val = ord(c)
        ((c_val >= ord("A") and c_val <= ord("Z")) or \
                (c_val >= ord("a") and c_val <= ord("z"))) or \
                c_val in special_id_chars

    def __init__(self):
        self.buf = []

    def get_next_token(self):
        self.buf += list(input())
        print(self.buf)
