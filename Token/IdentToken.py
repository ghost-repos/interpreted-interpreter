from Token.Token import Token
from Token.TokenTypes import TokenTypes

class IdentToken(Token):
    def __init__(self, s):
        super().__init__(TokenTypes.IDENT)
        self.name = s

    def get_name(self):
        return self.name
