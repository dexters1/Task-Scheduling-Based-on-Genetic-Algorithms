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
        self.cost = None
        self.successors = []
        self.predecessors = []
        self.depth = None
        self.preprocessed = False

class Edge:
    def __init__(self, u, v, weight=None):
        self.first = u
        self.second = v 
        if (weight==None):
            self.weight = random.randint(10,30)
        else:
            self.weight = weight

class Graph:
    def __init__(self, V=[], E=[], P=[]):
        self.V = V
        self.E = E
        self.P = P
        self.fitness = None
        self.totalTime = None
        self.cost = None
        self.selectionNumber = None
 
