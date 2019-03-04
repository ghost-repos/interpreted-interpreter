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
# modified rest to get rid of common lhs:
# rest2 -> )
#        | exp again
# again -> rest
#        | . exp )

from Parser.Scanner import Scanner

class Parser:
    def __init__(self):
        self.scanner = Scanner()

    def parse(self):
        self.scanner.get_next_token()
