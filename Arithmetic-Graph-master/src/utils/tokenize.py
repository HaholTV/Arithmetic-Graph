from utils.utils import *

#
# Funkcja: tokenize
# -----------------
# przetwarza tekstowe wyrarzenie arytmetyczne w listę (tablicę) symbolów (liczby, zmięnna, operator)
#    "2 + 2" => [2, '-', 2]
#
# argumenty:
#    1) expr: <class 'str'> - tekstowe wyrarzenie arytmetyczne
#
# zwraca:
#    <class 'list'> - listę symbolów (notacja infiksowa, tak jak wprowadził użytkownik)
#
def tokenize(expr):
    tokens = []
    buffer = []
    
    for c in expr:
        if c.isdigit() or c == '.':
            buffer.append(c)
        else:
            if len(buffer):
                tokens.append(new_token(Token.NUMBER, to_number(buffer)))
            
            if c.isspace():
                continue
            elif c.isalpha():
                tokens.append(new_token(Token.VARIABLE, c))
            elif isoperator(c):
                tokens.append(new_token(Token.OPERATOR, c))
            elif c == '(':
                tokens.append(new_token(Token.LEFT_PARENTH, c))
            elif c == ')':
                tokens.append(new_token(Token.RIGHT_PARENTH, c))
            else:
                throw_error("Unknown token: " + c)
                
    if len(buffer):
        tokens.append(new_token(Token.NUMBER, to_number(buffer)))
                
    return tokens