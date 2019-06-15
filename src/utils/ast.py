import matplotlib.pyplot as plt
import networkx as nx
from utils.utils import Token

#
# Klasa: ArithmGraph
# ------------------
# konstruuje objekt, reprezentujący graf arytmetyczny skomponowany z objektu klasy DiGraph i paru 
# pomocnych pól (list i słowników)
#    
# pola:
#     1) G: <class 'networkx.classes.digraph.DiGraph'> - objekt klasy DiGraph (graf skierowany)
#     2) labels: <class 'dict'> - nazwy wierzchołku (liczba, zmienna, operator)
#     3) edge_labels: <class 'dict'> - priorytetkość wykonywania operacji (1 lub 2)
#     4) colors: <class 'list'> - kolory wierzchołków
#     5) stack: <class 'list'> - stos tymczasowo przechowujący operandy
#     6) index: <class 'int'> - id każdego wierzchołka, aby uniknąć dublikatów
#
# metody:
#     1) add_operand - dodaje operandy do grafu za pomocą metody add_node i innych (z biblioteki networkx)
#         modyfikuje lub mutuje pola: G, labels, colors, stack, index
#     2) add_operator - dodaje operatory do grafu za pomocą metody add_node i innych (z biblioteki networkx)
#         modyfikuje lub mutuje pola: G, labels, colors, edge_labels, stack index
#
class ArithmGraph:
    def __init__(self):
        self.G = nx.DiGraph()
        self.labels = {}
        self.edge_labels = {}
        self.colors = []
        self.stack = []
        self.index = 0
        
    def add_operand(self, label, color="blue"):
        self.G.add_node(self.index)
        self.labels[self.index] = label
        self.colors.append(color)
        self.stack.append(self.index)
        self.index += 1
    
    def add_operator(self, label, color="green"):
        self.G.add_node(self.index)
        self.labels[self.index] = label
        self.colors.append(color)
        
        op2 = self.stack.pop()
        op1 = self.stack.pop()
        
        self.edge_labels.update({(self.index, op1): 1, (self.index, op2): 2})
        self.G.add_edges_from([(self.index, op1), (self.index, op2)])
        
        self.stack.append(self.index)
        self.index += 1

#
# Funkcja: create_graph
# --------------------
# stwarza graf (objekt klasy DiGraph (Graf skierowany) z biblioteki networkx (https://networkx.github.io/))
# reprezentujący graf arytmetyczny
#    [2, 2, '-'] => <class 'networkx.classes.digraph.DiGraph'> ( https://wmpics.pics/pm-V1E24LUG.html )
#
# argumenty:
#    1) tokens: <class 'list'> - lista symbolów w notacji posfiksowej
#
# zwraca:
#    <class 'networkx.classes.digraph.DiGraph'> - objekt reprezentujący graph arytmetyczny
#
def create_graph(tokens):
    ag = ArithmGraph()
    
    for i in range(0, len(tokens)):
        token = tokens[i]
        
        if token["type"] == Token.NUMBER:
            ag.add_operand(token["value"], color="blue")
        elif token["type"] == Token.VARIABLE:
            ag.add_operand(token["value"], color="red")
        elif token["type"] == Token.OPERATOR:
            if i == len(tokens)-1:
                ag.add_operator(token["value"], color="yellow")
            else:
                ag.add_operator(token["value"], color="green")
    
    return ag