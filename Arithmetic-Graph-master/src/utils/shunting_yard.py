from utils.utils import *

# converts infix notation to RPN
# using https://en.wikipedia.org/wiki/Shunting-yard_algorithm

#
# Funkcja: convert
# ----------------
# tłumaczy notację infiksową na ODP (https://pl.wikipedia.org/wiki/Odwrotna_notacja_polska)
#    [2, '-', 2] => [2, 2, '-']
#
# argumenty:
#    1) tokens: <class 'list'> - lista symbolów w notacji infiksowej
#
# zwraca:
#    <class 'list'> - lista symbolów w notacji posfiksowej
#
def convert(tokens):
    op_stack = []
    output = []

    for token in tokens:
        if token["type"] == Token.NUMBER or token["type"] == Token.VARIABLE:
            output.append(token)
        elif token["type"] == Token.OPERATOR:
            while (  # TODO: define function with this condition
                    (top(op_stack) and top(op_stack)["type"] != Token.LEFT_PARENTH) and
                    ((top(op_stack) and top(op_stack)["precedence"] < token["precedence"]) or
                     (top(op_stack) and top(op_stack)["precedence"] == token["precedence"] and
                      token["associativity"] == "left"))
            ):
                output.append(op_stack.pop())
                if top(op_stack) and top(op_stack)["type"] == Token.LEFT_PARENTH:
                    break

            op_stack.append(token)
        elif token["type"] == Token.LEFT_PARENTH:
            op_stack.append(token)
        elif token["type"] == Token.RIGHT_PARENTH:
            while top(op_stack)["type"] != Token.LEFT_PARENTH:
                output.append(op_stack.pop())
            op_stack.pop()  # deleting left parenth

    while len(op_stack):  # TODO: reverse method
        output.append(op_stack.pop())

    return output
