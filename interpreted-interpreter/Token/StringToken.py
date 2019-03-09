from Token.Token import Token
from Token.TokenTypes import TokenTypes

class StringToken(Token):
    def __init__(self, s):
        super().__init__(TokenTypes.STRING)
        self.val = s

    def get_string_val(self):
        return self.val
