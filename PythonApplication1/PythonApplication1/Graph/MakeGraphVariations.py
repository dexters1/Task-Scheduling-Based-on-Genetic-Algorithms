import sys
from Graph.GraphClass import *
from Graph.GraphFunctions import *
from Processor.ProcessorClass import *
from Processor.ProcessorFunctions import *
from Graph.PriorityDefinition import *

# Applies for all makeGraph function Variations

# Input args:
#   No input args
# output args:
#   Graph
# Description:
#   Makes a predefined graph

def makeGraph1():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    P = ProcessorList([p1,p2])

    v1 = Vertex("v1", 10, p1)
    v2 = Vertex("v2", 15, p2)

    p1.taskList = [v1]
    p2.taskList = [v2]

    vertex = [v1, v2]

    edges = []

    edges.append(Edge(v1, v2))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraph2():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p3)
    v2 = Vertex("v2", 24, p2)
    v3 = Vertex("v3", 23, p2)
    v4 = Vertex("v4", 11, p1)

    vertex = [v1, v2, v3, v4]

    edges = []

    edges.append(Edge(v1, v2))
    edges.append(Edge(v1, v3))
    edges.append(Edge(v1, v4))

    G = Graph(vertex, edges, P)
    
    updateGraph(G)

    return G

def makeGraph3():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p1)
    v2 = Vertex("v2", 15, p2)
    v3 = Vertex("v3", 23, p2)
    v4 = Vertex("v4", 11, p1)
    v5 = Vertex("v5", 21, p3)
    v6 = Vertex("v6", 3, p1)
    v7 = Vertex("v7", 17, p2)
    v8 = Vertex("v8", 7, p3)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8]

    edges = []

    edges.append(Edge(v1, v4))
    edges.append(Edge(v2, v4))
    edges.append(Edge(v3, v4))
    edges.append(Edge(v4, v5))
    edges.append(Edge(v5, v6))
    edges.append(Edge(v5, v7))
    edges.append(Edge(v5, v8))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraph4():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p1)
    v2 = Vertex("v2", 15, p2)
    v3 = Vertex("v3", 23, p2)
    v4 = Vertex("v4", 11, p1)
    v5 = Vertex("v5", 21, p2)

    vertex = [v1, v2, v3, v4, v5]

    edges = []

    edges.append(Edge(v1, v2))
    edges.append(Edge(v1, v3))
    edges.append(Edge(v1, v4))
    edges.append(Edge(v2, v5))
    edges.append(Edge(v3, v5))
    edges.append(Edge(v4, v5))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraph5():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p1)
    v2 = Vertex("v2", 15, p3)
    v3 = Vertex("v3", 23, p3)
    v4 = Vertex("v4", 11, p3)
    v5 = Vertex("v5", 21, p1)
    v6 = Vertex("v6", 3, p1)
    v7 = Vertex("v7", 17, p2)
    v8 = Vertex("v8", 7, p3)
    v9 = Vertex("v9", 13, p2)
    v10 = Vertex("v10", 12, p1)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]

    edges = []

    edges.append(Edge(v1, v2))
    edges.append(Edge(v1, v3))
    edges.append(Edge(v1, v4))
    edges.append(Edge(v2, v5))
    edges.append(Edge(v3, v6))
    edges.append(Edge(v4, v7))
    edges.append(Edge(v5, v8))
    edges.append(Edge(v6, v8))
    edges.append(Edge(v7, v8))
    edges.append(Edge(v8, v9))
    edges.append(Edge(v9, v10))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G


def makeGraph6():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p2)
    v2 = Vertex("v2", 15, p3)
    v3 = Vertex("v3", 23, p1)
    v4 = Vertex("v4", 11, p3)
    v5 = Vertex("v5", 21, p2)
    v6 = Vertex("v6", 3, p1)
    v7 = Vertex("v7", 17, p3)
    v8 = Vertex("v8", 7, p3)
    v9 = Vertex("v9", 13, p2)
    v10 = Vertex("v10", 12, p3)
    v11 = Vertex("v11", 15, p2)
    v12 = Vertex("v12", 11, p1)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12]

    edges = []

    edges.append(Edge(v1, v2))
    edges.append(Edge(v1, v3))
    edges.append(Edge(v1, v5))
    edges.append(Edge(v2, v4))
    edges.append(Edge(v3, v4))
    edges.append(Edge(v5, v4))
    edges.append(Edge(v3, v6))
    edges.append(Edge(v5, v8))
    edges.append(Edge(v6, v7))
    edges.append(Edge(v8, v7))
    edges.append(Edge(v4, v7))
    edges.append(Edge(v7, v9))
    edges.append(Edge(v7, v10))
    edges.append(Edge(v10, v11))
    edges.append(Edge(v10, v12))
    edges.append(Edge(v11, v12))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraph7():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 13, p2)
    v2 = Vertex("v2", 17, p2)
    v3 = Vertex("v3", 14, p2)
    v4 = Vertex("v4", 9, p3)
    v5 = Vertex("v5", 12, p1)
    v6 = Vertex("v6", 13, p2)
    v7 = Vertex("v7", 11, p1)
    v8 = Vertex("v8", 10, p3)
    v9 = Vertex("v9", 17, p2)
    v10 = Vertex("v10", 15, p3)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]

    edges = []

    edges.append(Edge(v1, v2, 18))
    edges.append(Edge(v1, v3, 12))
    edges.append(Edge(v1, v4, 9))
    edges.append(Edge(v1, v5, 11))
    edges.append(Edge(v1, v6, 14))
    edges.append(Edge(v2, v8, 19))
    edges.append(Edge(v2, v9, 16))
    edges.append(Edge(v3, v7, 23))
    edges.append(Edge(v4, v8, 27))
    edges.append(Edge(v4, v9, 23))
    edges.append(Edge(v5, v9, 13))
    edges.append(Edge(v6, v8, 15))
    edges.append(Edge(v7, v10, 17))
    edges.append(Edge(v8, v10, 11))
    edges.append(Edge(v9, v10, 13))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraph8():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p3)
    v2 = Vertex("v2", 15, p2)
    v3 = Vertex("v3", 23, p1)
    v4 = Vertex("v4", 11, p3)
    v5 = Vertex("v5", 21, p2)
    v6 = Vertex("v6", 3, p1)
    v7 = Vertex("v7", 17, p2)
    v8 = Vertex("v8", 7, p3)
    v9 = Vertex("v9", 13, p1)
    v10 = Vertex("v10", 12, p2)
    v11 = Vertex("v11", 23, p3)
    v12 = Vertex("v12", 11, p1)
    v13 = Vertex("v13", 21, p3)
    v14 = Vertex("v14", 3, p2)
    v15 = Vertex("v15", 17, p3)
    v16 = Vertex("v16",13, p1)
    v17 = Vertex("v17", 13, p2)
    v18 = Vertex("v18", 12, p3)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18]

    edges = []

    edges.append(Edge(v1, v5))
    edges.append(Edge(v2, v6))
    edges.append(Edge(v3, v7))
    edges.append(Edge(v4, v8))
    edges.append(Edge(v5, v9))
    edges.append(Edge(v6, v9))
    edges.append(Edge(v7, v9))
    edges.append(Edge(v8, v9))
    edges.append(Edge(v9, v10))
    edges.append(Edge(v9, v11))
    edges.append(Edge(v9, v12))
    edges.append(Edge(v9, v13))
    edges.append(Edge(v10, v14))
    edges.append(Edge(v11, v15))
    edges.append(Edge(v12, v16))
    edges.append(Edge(v13, v17))
    edges.append(Edge(v14, v18))
    edges.append(Edge(v15, v18))
    edges.append(Edge(v16, v18))
    edges.append(Edge(v17, v18))


    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraph9():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p1)
    v2 = Vertex("v2", 15, p2)
    v3 = Vertex("v3", 23, p3)
    v4 = Vertex("v4", 11, p2)
    v5 = Vertex("v5", 21, p3)
    v6 = Vertex("v6", 3, p1)
    v7 = Vertex("v7", 17, p2)
    v8 = Vertex("v8", 7, p3)
    v9 = Vertex("v9", 13, p3)
    v10 = Vertex("v10", 12, p2)
    v11 = Vertex("v11", 23, p2)
    v12 = Vertex("v12", 11, p3)
    v13 = Vertex("v13", 21, p2)
    v14 = Vertex("v14", 3, p1)
    v15 = Vertex("v15", 17, p1)
    v16 = Vertex("v16",13, p2)
    v17 = Vertex("v17", 13, p3)
    v18 = Vertex("v18", 12, p1)
    v19 = Vertex("v19", 13, p2)
    v20 = Vertex("v20", 12, p3)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20]

    edges = []

    edges.append(Edge(v1, v5))
    edges.append(Edge(v1, v6))
    edges.append(Edge(v2, v6))
    edges.append(Edge(v2, v7))
    edges.append(Edge(v3, v8))
    edges.append(Edge(v3, v9))
    edges.append(Edge(v4, v9))
    edges.append(Edge(v4, v10))
    edges.append(Edge(v5, v13))
    edges.append(Edge(v5, v11))
    edges.append(Edge(v6, v11))
    edges.append(Edge(v7, v14))
    edges.append(Edge(v7, v11))
    edges.append(Edge(v8, v11))
    edges.append(Edge(v8, v15))
    edges.append(Edge(v9, v11))
    edges.append(Edge(v10, v11))
    edges.append(Edge(v10, v16))
    edges.append(Edge(v11, v12))
    edges.append(Edge(v12, v13))
    edges.append(Edge(v12, v14))
    edges.append(Edge(v12, v15))
    edges.append(Edge(v12, v16))
    edges.append(Edge(v13, v17))
    edges.append(Edge(v14, v17))
    edges.append(Edge(v15, v17))
    edges.append(Edge(v16, v17))
    edges.append(Edge(v17, v18))
    edges.append(Edge(v18, v19))
    edges.append(Edge(v19, v20))


    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraphTest():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p2)
    v2 = Vertex("v2", 15, p2)
    v3 = Vertex("v3", 23, p2)
    v4 = Vertex("v4", 11, p3)
    v5 = Vertex("v5", 21, p1)
    v6 = Vertex("v6", 3, p2)
    v7 = Vertex("v7", 17, p1)
    v8 = Vertex("v8", 7, p3)
    v9 = Vertex("v9", 13, p2)
    v10 = Vertex("v10", 12, p3)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]

    edges = []

    edges.append(Edge(v1, v2))
    edges.append(Edge(v1, v3))
    edges.append(Edge(v1, v4))
    edges.append(Edge(v1, v5))
    edges.append(Edge(v1, v6))
    edges.append(Edge(v2, v8))
    edges.append(Edge(v2, v9))
    edges.append(Edge(v3, v7))
    edges.append(Edge(v4, v8))
    edges.append(Edge(v4, v9))
    edges.append(Edge(v5, v9))
    edges.append(Edge(v6, v8))
    edges.append(Edge(v7, v10))
    edges.append(Edge(v8, v10))
    edges.append(Edge(v9, v10))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G


def makeGraphTest77():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=2, val="p2")
    p3 = Processor(capacity=3, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 13, p1)
    v2 = Vertex("v2", 17, p1)
    v3 = Vertex("v3", 14, p1)
    v4 = Vertex("v4", 9, p1)
    v5 = Vertex("v5", 12, p1)
    v6 = Vertex("v6", 13, p1)
    v7 = Vertex("v7", 11, p1)
    v8 = Vertex("v8", 10, p1)
    v9 = Vertex("v9", 17, p1)
    v10 = Vertex("v10", 15, p1)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]

    edges = []

    edges.append(Edge(v1, v2, 18))
    edges.append(Edge(v1, v3, 12))
    edges.append(Edge(v1, v4, 9))
    edges.append(Edge(v1, v5, 11))
    edges.append(Edge(v1, v6, 14))
    edges.append(Edge(v2, v8, 19))
    edges.append(Edge(v2, v9, 16))
    edges.append(Edge(v3, v7, 23))
    edges.append(Edge(v4, v8, 27))
    edges.append(Edge(v4, v9, 23))
    edges.append(Edge(v5, v9, 13))
    edges.append(Edge(v6, v8, 15))
    edges.append(Edge(v7, v10, 17))
    edges.append(Edge(v8, v10, 11))
    edges.append(Edge(v9, v10, 13))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

