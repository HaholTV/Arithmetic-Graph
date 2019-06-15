import sys

#
# Klasa: Token
# ------------
# przeztrzeń nazw dla konstant reprezentujacyh typy tokenów
#
class Token:
    NUMBER = 0  # liczba
    VARIABLE = 1  # zmienna
    OPERATOR = 2  # operator
    LEFT_PARENTH = 4  # otwierający nawias
    RIGHT_PARENTH = 5  # zamykający nawias

#
# Funkcja: isoperator
# -------------------
# sprawdza czy argument jest operatorem
#     '*' => True
#
# argumenty:
#     1) c: <class 'str'> - ascii symbol
#
# zwraca:
#     <class 'bool'> - symbol był operatorem lub nie
#
def isoperator(c):
    return c in ('+', '-', '*', '/', '%')

#
# Funkcja: to_number
# ------------------
# konwertuje liste cyfer w liczbę
#     ['2, '3'] => 23
#
# argumenty:
#     1) buffer: <class 'list'> - lista z cyframi
#
# zwraca:
#     <class 'int'> | <class 'float'> - liczbe całkowitą lub zmiennopozycyjną zależnie od tego 
#     czy w liście była znaleziona kropka
#
def to_number(buffer):
    number = "".join(buffer)
    buffer.clear()
    
    if ('.' in number):
        return float(number)
    else:
        return int(number)

#
# Funkcja: new_token
# ------------------
# Fabrykuje słownik mieszczący dane o tokenie
#     (2, '/') => {"type": 2, "value": '/', "precedence": 2, "associativity": "left"}
#
# argumenty:
#     1) token_type: <class 'int'> - typ tokenu (z przeztrzeni nazw Token)
#     2) token_value: <class 'str'> - znaczenie tokenu
#
# zwraca:
#     <class 'dict'> - informacje o tokenie
#
def new_token(token_type, token_value):
    if token_type == Token.OPERATOR:
        if token_value in ('*', '/', '%'):
            precedence = 2
            associativity = 'left'
        elif token_value in ('+', '-'):
            precedence = 3
            associativity = 'left'
        return {
            "type": token_type,
            "value": token_value,
            "precedence": precedence,
            "associativity": associativity
        }
    else:
        return {"type": token_type, "value": token_value}

#
# Funkcja: top
# ------------
# funckcja pomocnicza przy pracy ze stosami - pokazuje element z samej góry 
# (nie usuwając jak standardowa funkcja pop)
#     [1, 2, 3, 4] => 4 a[-1]
#
# argumenty:
#     1) stack: <class 'int'> - stos
#
# zwraca:
#     <class 'int'> - ostatni element stosu
#
def top(stack):
    return stack[len(stack)-1] if len(stack) else None
    
#
# Funkcja: throw_error
# --------------------
# funkcja pomocnicza - wyrzuca pomyłkę i terminuje skrypt
#     "Internall error has occured" => None (standardowe wyjście << "Error: Internal error has occured")
#
# argumenty:
#     1) message <class 'str'> - powiadomienie z pomyłką
#
# zwraca:
#     None
#
def throw_error(message):
    print("Error:", message)
    sys.exit()
    