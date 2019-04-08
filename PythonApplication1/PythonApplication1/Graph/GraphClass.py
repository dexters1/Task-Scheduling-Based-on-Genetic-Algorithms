import sys
import random

random.seed(30)

class Vertex:
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight
        self.successors = []
        self.predecessors = []

class Edge:
    def __init__(self, u, v):
        self.first = u
        self.second = v
        self.weight = random.randint(10,30)

class Graph:
    def __init__(self, V=[], E=[]):
        self.V = V
        self.E = E
 