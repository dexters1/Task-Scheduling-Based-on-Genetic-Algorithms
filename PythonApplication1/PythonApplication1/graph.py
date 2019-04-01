import sys
from math import inf

class Vertex:
    def __init__(self, val):
        self.val = val

class Edge:
    def __init__(self, u, v):
        self.first = u
        self.second = v

class Graph:
    def __init__(self, V=[], E=[]):
        self.V = V
        self.E = E
 
