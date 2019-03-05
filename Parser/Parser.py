# grammar:
# exp   -> ( rest
#        | #f
#        | #t
#        | ' exp
#        | int
#        | str
#        | ident
# rest  -> )
#        | exp rest
#        | exp . exp )
#
# modified rest to get rid of common left factor:
# rest1 -> )
#        | exp rest2
# rest2 -> rest1
#        | . exp )

from Parser.Scanner import Scanner
from Token.TokenTypes import TokenTypes
from Tree.NilNode import nil_node
from Tree.BooleanNode import true_node, false_node
from Tree.ConsNode import ConsNode
from Tree.IdentNode import IdentNode
from Tree.IntNode import IntNode
from Tree.StringNode import StringNode
from Tree.ConsNode import ConsNode

class Parser:
    def __init__(self):
        self.scanner = Scanner()

    def feed(self, s):
        self.scanner.feed(s)

    def parse(self):
        token = self.scanner.get_next_token()
        if token == None:
            return None
        else:
            return self.parse_exp(token)

    def parse_exp(self, token):
        if token.get_type() == TokenTypes.LPAREN:
            return self.parse_rest1(self.scanner.get_next_token())
        elif token.get_type() == TokenTypes.STRING:
            return StringNode(token.get_string_val())
        elif token.get_type() == TokenTypes.IDENT:
            return IdentNode(token.get_name())
        elif token.get_type() == TokenTypes.INT:
            return IntNode(token.get_int_val())
        elif token.get_type() == TokenTypes.QUOTE:
            return ConsNode(IdentNode("quote"), ConsNode( \
                    self.parse_exp(self.scanner.get_next_token()) \
                    , nil_node))
        elif token.get_type() == TokenTypes.TRUE:
            return true_node
        elif token.get_type() == TokenTypes.FALSE:
            return false_node
        else:
            raise Exception("unrecognized token received")

    def parse_rest1(self, token):
        if token.get_type() == TokenTypes.RPAREN:
            return nil_node
        else:
            return ConsNode(self.parse_exp(token), self.parse_rest2( \
                    self.scanner.get_next_token()))

    def parse_rest2(self, token):
        if token.get_type() == TokenTypes.DOT:
            ret = self.parse_exp(self.scanner.get_next_token())
            ty = self.scanner.get_next_token().get_type()
            if ty != TokenTypes.RPAREN:
                raise Exception("expected RPAREN got %s" % ty)
            return ret
        else:
            return self.parse_rest1(token)
