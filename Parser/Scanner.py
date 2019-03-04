from Token.Token import Token
from Token.TokenTypes import TokenTypes
from Token.IdentToken import IdentToken
from Token.IntToken import IntToken
from Token.StringToken import StringToken

class Scanner:
    special_id_chars = {"!", "$", "%", "&", "*", "+", "-", ".", "/",
            ":", "<", "=", ">", "?", "@", "^"}
    whitespace_chars = {" ", "\r", "\f", "\n"}

    @staticmethod
    def is_valid_id_character(c):
        return c.isalpha() or c in Scanner.special_id_chars

    def __init__(self):
        self.buf = []

    def shift_buffer(self):
        tmp = self.buf[0]
        self.buf = self.buf[1:]
        return tmp

    def peek_buffer(self):
        return self.buf[0]

    def unshift_buffer(self, s):
        self.buf = [s] + self.buf

    def feed(self, s):
        self.buf += list(s)

    def get_next_token(self):
        ch = self.shift_buffer()
        while ch in Scanner.whitespace_chars:
            ch = self.shift_buffer()

        if ch == "'": # special characters
            return Token(TokenTypes.QUOTE)
        elif ch == "(":
            return Token(TokenTypes.LPAREN)
        elif ch == ")":
            return Token(TokenTypes.RPAREN)
        elif ch == ".":
            return Token(TokenTypes.DOT)
        elif ch == "#": # booleans
            ch = self.shift_buffer()
            if ch == "f":
                return Token(TokenTypes.FALSE)
            elif ch == "t":
                return Token(TokenTypes.TRUE)
            else:
                raise Exception("unexpected character for boolean literal (%s)" % ch)
        elif ch == "\"": # strings
            s = ""
            while len(self.buf) > 0 and self.peek_buffer() != "\"":
                s += self.shift_buffer()
            return StringToken(s)
        elif ch.isnumeric(): # int literals
            v = int(ch)
            while len(self.buf) > 0 and self.peek_buffer().isnumeric():
                v = v * 10 + int(self.shift_buffer())
            return IntToken(v)
        elif Scanner.is_valid_id_character(ch):
            s = ch
            while len(self.buf) > 0 and Scanner.is_valid_id_character(self.peek_buffer()):
                s += self.shift_buffer()
            return IdentToken(s)
        else:
            raise Exception("illegal character received (%s)" % ch)

