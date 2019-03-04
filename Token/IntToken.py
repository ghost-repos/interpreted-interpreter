from Token.Token import Token
from Token.TokenTypes import TokenTypes

class IntToken(Token):
    def __init__(self, i):
        super().__init__(TokenTypes.INT)
        self.val = i

    def get_int_val(self):
        return self.val
