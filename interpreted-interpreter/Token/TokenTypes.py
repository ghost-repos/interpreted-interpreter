from enum import Enum, auto

class TokenTypes(Enum):
    QUOTE = auto()
    LPAREN = auto()
    RPAREN = auto()
    DOT = auto()
    TRUE = auto()
    FALSE = auto()
    INT = auto()
    STRING = auto()
    IDENT = auto()
