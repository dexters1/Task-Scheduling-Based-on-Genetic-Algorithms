import sys
import random

random.seed(30)

class Vertex:
    def __init__(self, val, weight, processor=None):
        self.val = val
        self.weight = weight
        self.processor = processor
        self.startTime = None
        self.finishTime = None
        self.priority = None
        self.successors = []
        self.predecessors = []
        self.depth = None

class Edge:
    def __init__(self, u, v):
        self.first = u
        self.second = v 
        self.weight = random.randint(10,30)

class Graph:
    def __init__(self, V=[], E=[], P=[]):
        self.V = V
        self.E = E
        self.P = P
 
