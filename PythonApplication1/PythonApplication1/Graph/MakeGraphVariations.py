import sys
from Graph.GraphClass import *
from Graph.GraphFunctions import *
from Processor.ProcessorClass import *
from Processor.ProcessorFunctions import *
from Graph.PriorityDefinition import *
import copy

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

def makeGraphGA():

    p1 = Processor(capacity=0.9, val="p1") #1/3 # 2*(1/3) # 4*(1/3)
    p2 = Processor(capacity=0.9, val="p2")
    p3 = Processor(capacity=0.9, val="p3")
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
    #simplifyGraph(G)

    updateGraph(G)

    return G

def makeGraphGATheirs():

    p1 = Processor(capacity=0.9, val="p1")
    p2 = Processor(capacity=0.9, val="p2")
    p3 = Processor(capacity=0.9, val="p3")
    P = ProcessorList([p1,p2,p3])

    v11 = Vertex("v1.1", 13, p1)
    v12 = Vertex("v1.2", 13, p2)
    v13 = Vertex("v1.3", 13, p3)
    #v11 = Vertex("v1", 13, p1)

    v2 = Vertex("v2", 17, p1)
    v3 = Vertex("v3", 14, p2)
    v4 = Vertex("v4", 9, p3)
    v5 = Vertex("v5", 12, p3)
    v6 = Vertex("v6", 13, p1)
    v7 = Vertex("v7", 11, p2)
    v8 = Vertex("v8", 10, p1)
    v9 = Vertex("v9", 17, p2)
    v10 = Vertex("v10", 15, p2)

    vertex = [v11, v12, v13, v2, v3, v4, v5, v6, v7, v8, v9, v10]
    #vertex = [v11, v2, v3, v4, v5, v6, v7, v8, v9, v10]

    edges = []

    edges.append(Edge(v11, v2, 18))
    edges.append(Edge(v12, v3, 12))
    edges.append(Edge(v13, v4, 9))
    #edges.append(Edge(v11, v3, 12))
    #edges.append(Edge(v11, v4, 9))
    #edges.append(Edge(v11, v5, 11))
    edges.append(Edge(v13, v5, 11))
    edges.append(Edge(v11, v6, 14))
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
     
    #print(G.P.processorList[0].taskList[1])
    #G.P.processorList[0].taskList = [G.V[0], G.V[1], G.V[5], Slot(startTime=G.V[5].finishTime, finishTime=G.V[7].startTime), G.V[7]]
    #vertex1OnProcessor2 = copy.deepcopy(G.V[0])
    #vertex1OnProcessor2.startTime = 0
    #vertex1OnProcessor2.finishTime = finishTime(vertex1OnProcessor2)
    #G.P.processorList[1].taskList = [, G.V[2],G.V[6], G.V[8], Slot(G.V[8].finishTime, G.V[9].startTime), G.V[9]]

    #G.P.processorList[2].taskList = [copy.deepcopy(G.V[0]), G.V[3],G.V[4]]



    return G


def makeGraphDuplicateTest():

    p1 = Processor(capacity=1, val="p1")
    p2 = Processor(capacity=1, val="p2")
    p3 = Processor(capacity=1, val="p3")
    P = ProcessorList([p1,p2,p3])

    v1 = Vertex("v1", 10, p1)
    v2 = Vertex("v2", 15, p1)
    v3 = Vertex("v3", 15, p1)
    v4 = Vertex("v4", 15, p1)
    v5 = Vertex("v5", 15, p1)
    v6 = Vertex("v6", 15, p1)
    v7 = Vertex("v7", 15, p1)
    v8 = Vertex("v8", 15, p1)
    v9 = Vertex("v9", 15, p1)
    v10 = Vertex("v10", 15, p3)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]

    edges = []

    edges.append(Edge(v1, v2, weight=5))
    edges.append(Edge(v1, v3))
    edges.append(Edge(v1, v4))
    edges.append(Edge(v1, v5))
    edges.append(Edge(v1, v6, 3))
    edges.append(Edge(v6, v7))
    edges.append(Edge(v6, v9))
    edges.append(Edge(v3, v8))
    edges.append(Edge(v2, v9, 3))
    edges.append(Edge(v9, v10))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraphGA10():

    p1 = Processor(capacity=0.9, val="p1")
    p2 = Processor(capacity=0.9, val="p2")
    p3 = Processor(capacity=0.9, val="p3")
    p4 = Processor(capacity=0.9, val="p4")
    p5 = Processor(capacity=0.9, val="p5")
    p6 = Processor(capacity=0.9, val="p6")
    p7 = Processor(capacity=0.9, val="p7")
    p8 = Processor(capacity=0.9, val="p8")
    P = ProcessorList([p1,p2,p3,p4,p5,p6,p7,p8])

    v1 = Vertex("v1", 13, p3)
    v2 = Vertex("v2", 17, p4)
    v3 = Vertex("v3", 14, p6)
    v4 = Vertex("v4", 9, p3)
    v5 = Vertex("v5", 12, p1)
    v6 = Vertex("v6", 13, p7)
    v7 = Vertex("v7", 11, p1)
    v8 = Vertex("v8", 10, p3)
    v9 = Vertex("v9", 17, p8)
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

def makeGraphGA20():
    p1 = Processor(capacity=0.9, val="p1")
    p2 = Processor(capacity=0.9, val="p2")
    p3 = Processor(capacity=0.9, val="p3")
    p4 = Processor(capacity=0.9, val="p4")
    p5 = Processor(capacity=0.9, val="p5")
    p6 = Processor(capacity=0.9, val="p6")
    p7 = Processor(capacity=0.9, val="p7")
    p8 = Processor(capacity=0.9, val="p8")
    P = ProcessorList([p1,p2,p3,p4,p5,p6,p7,p8])

    v1 = Vertex("v1", 13, p2)
    v2 = Vertex("v2", 17, p2)
    v3 = Vertex("v3", 14, p2)
    v4 = Vertex("v4", 9, p3)
    v5 = Vertex("v5", 12, p1)
    v6 = Vertex("v6", 13, p2)
    v7 = Vertex("v7", 11, p1)
    v8 = Vertex("v8", 10, p3)
    v9 = Vertex("v9", 17, p2)
    v10 = Vertex("v10", 15, p4)
    v11 = Vertex("v11", 13, p5)
    v12 = Vertex("v12", 17, p6)
    v13 = Vertex("v13", 14, p7)
    v14 = Vertex("v14", 9, p8)
    v15 = Vertex("v15", 12, p3)
    v16 = Vertex("v16", 13, p2)
    v17 = Vertex("v17", 11, p1)
    v18 = Vertex("v18", 10, p5)
    v19 = Vertex("v19", 17, p2)
    v20 = Vertex("v20", 15, p8)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20]

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
    edges.append(Edge(v7, v11, 18))
    edges.append(Edge(v8, v11, 12))
    edges.append(Edge(v9, v12, 9))
    edges.append(Edge(v11, v13, 11))
    edges.append(Edge(v10, v14, 14))
    edges.append(Edge(v10, v15, 19))
    edges.append(Edge(v10, v16, 16))
    edges.append(Edge(v12, v17, 23))
    edges.append(Edge(v14, v18, 27))
    edges.append(Edge(v15, v18, 23))
    edges.append(Edge(v15, v19, 13))
    edges.append(Edge(v16, v19, 15))
    edges.append(Edge(v18, v20, 17))
    edges.append(Edge(v19, v20, 11))
    edges.append(Edge(v12, v16, 13))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraphGA30():
    p1 = Processor(capacity=0.9, val="p1")
    p2 = Processor(capacity=0.9, val="p2")
    p3 = Processor(capacity=0.9, val="p3")
    p4 = Processor(capacity=0.9, val="p4")
    p5 = Processor(capacity=0.9, val="p5")
    p6 = Processor(capacity=0.9, val="p6")
    p7 = Processor(capacity=0.9, val="p7")
    p8 = Processor(capacity=0.9, val="p8")
    P = ProcessorList([p1,p2,p3,p4,p5,p6,p7,p8])

    v1 = Vertex("v1", 13, p2)
    v2 = Vertex("v2", 17, p2)
    v3 = Vertex("v3", 14, p2)
    v4 = Vertex("v4", 9, p3)
    v5 = Vertex("v5", 12, p1)
    v6 = Vertex("v6", 13, p2)
    v7 = Vertex("v7", 11, p1)
    v8 = Vertex("v8", 10, p3)
    v9 = Vertex("v9", 17, p2)
    v10 = Vertex("v10", 15, p4)
    v11 = Vertex("v11", 13, p5)
    v12 = Vertex("v12", 17, p6)
    v13 = Vertex("v13", 14, p7)
    v14 = Vertex("v14", 9, p8)
    v15 = Vertex("v15", 12, p3)
    v16 = Vertex("v16", 13, p2)
    v17 = Vertex("v17", 11, p1)
    v18 = Vertex("v18", 10, p5)
    v19 = Vertex("v19", 17, p2)
    v20 = Vertex("v20", 15, p8)
    v21 = Vertex("v21", 13, p5)
    v22 = Vertex("v22", 17, p6)
    v23 = Vertex("v23", 14, p7)
    v24 = Vertex("v24", 9, p8)
    v25 = Vertex("v25", 12, p3)
    v26 = Vertex("v26", 13, p2)
    v27 = Vertex("v27", 11, p1)
    v28 = Vertex("v28", 10, p5)
    v29 = Vertex("v29", 17, p2)
    v30 = Vertex("v30", 15, p8)

    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30]

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
    edges.append(Edge(v7, v11, 18))
    edges.append(Edge(v8, v11, 12))
    edges.append(Edge(v9, v12, 9))
    edges.append(Edge(v11, v13, 11))
    edges.append(Edge(v10, v14, 14))
    edges.append(Edge(v10, v15, 19))
    edges.append(Edge(v10, v16, 16))
    edges.append(Edge(v12, v17, 23))
    edges.append(Edge(v14, v18, 27))
    edges.append(Edge(v15, v18, 23))
    edges.append(Edge(v15, v19, 13))
    edges.append(Edge(v16, v19, 15))
    edges.append(Edge(v18, v20, 17))
    edges.append(Edge(v19, v20, 11))
    edges.append(Edge(v12, v16, 13))
    edges.append(Edge(v18, v21, 18))
    edges.append(Edge(v19, v22, 12))
    edges.append(Edge(v20, v24, 9))
    edges.append(Edge(v20, v25, 11))
    edges.append(Edge(v21, v23, 14))
    edges.append(Edge(v21, v24, 19))
    edges.append(Edge(v22, v25, 16))
    edges.append(Edge(v22, v26, 23))
    edges.append(Edge(v22, v27, 27))
    edges.append(Edge(v24, v28, 23))
    edges.append(Edge(v25, v28, 13))
    edges.append(Edge(v25, v29, 15))
    edges.append(Edge(v26, v29, 17))
    edges.append(Edge(v28, v30, 11))
    edges.append(Edge(v29, v30, 13))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

def makeGraphGA40():
    p1 = Processor(capacity=0.9, val="p1")
    p2 = Processor(capacity=0.9, val="p2")
    p3 = Processor(capacity=0.9, val="p3")
    p4 = Processor(capacity=0.9, val="p4")
    p5 = Processor(capacity=0.9, val="p5")
    p6 = Processor(capacity=0.9, val="p6")
    p7 = Processor(capacity=0.9, val="p7")
    p8 = Processor(capacity=0.9, val="p8")
    P = ProcessorList([p1,p2,p3,p4,p5,p6,p7,p8])

    v1 = Vertex("v1", 13, p2)
    v2 = Vertex("v2", 17, p2)
    v3 = Vertex("v3", 14, p2)
    v4 = Vertex("v4", 9, p3)
    v5 = Vertex("v5", 12, p1)
    v6 = Vertex("v6", 13, p2)
    v7 = Vertex("v7", 11, p1)
    v8 = Vertex("v8", 10, p3)
    v9 = Vertex("v9", 17, p2)
    v10 = Vertex("v10", 15, p4)
    v11 = Vertex("v11", 13, p5)
    v12 = Vertex("v12", 17, p6)
    v13 = Vertex("v13", 14, p7)
    v14 = Vertex("v14", 9, p8)
    v15 = Vertex("v15", 12, p3)
    v16 = Vertex("v16", 13, p2)
    v17 = Vertex("v17", 11, p1)
    v18 = Vertex("v18", 10, p5)
    v19 = Vertex("v19", 17, p2)
    v20 = Vertex("v20", 15, p8)
    v21 = Vertex("v21", 13, p5)
    v22 = Vertex("v22", 17, p6)
    v23 = Vertex("v23", 14, p7)
    v24 = Vertex("v24", 9, p8)
    v25 = Vertex("v25", 12, p3)
    v26 = Vertex("v26", 13, p2)
    v27 = Vertex("v27", 11, p1)
    v28 = Vertex("v28", 10, p5)
    v29 = Vertex("v29", 17, p2)
    v30 = Vertex("v30", 15, p8)
    v31 = Vertex("v31", 13, p5)
    v32 = Vertex("v32", 17, p6)
    v33 = Vertex("v33", 14, p7)
    v34 = Vertex("v34", 9, p8)
    v35 = Vertex("v35", 12, p3)
    v36 = Vertex("v36", 13, p2)
    v37 = Vertex("v37", 11, p1)
    v38 = Vertex("v38", 10, p5)
    v39 = Vertex("v39", 17, p2)
    v40 = Vertex("v40", 15, p8)


    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40]

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
    edges.append(Edge(v7, v11, 18))
    edges.append(Edge(v8, v11, 12))
    edges.append(Edge(v9, v12, 9))
    edges.append(Edge(v11, v13, 11))
    edges.append(Edge(v10, v14, 14))
    edges.append(Edge(v10, v15, 19))
    edges.append(Edge(v10, v16, 16))
    edges.append(Edge(v12, v17, 23))
    edges.append(Edge(v14, v18, 27))
    edges.append(Edge(v15, v18, 23))
    edges.append(Edge(v15, v19, 13))
    edges.append(Edge(v16, v19, 15))
    edges.append(Edge(v18, v20, 17))
    edges.append(Edge(v19, v20, 11))
    edges.append(Edge(v12, v16, 13))
    edges.append(Edge(v18, v21, 18))
    edges.append(Edge(v19, v22, 12))
    edges.append(Edge(v20, v24, 9))
    edges.append(Edge(v20, v25, 11))
    edges.append(Edge(v21, v23, 14))
    edges.append(Edge(v21, v24, 19))
    edges.append(Edge(v22, v25, 16))
    edges.append(Edge(v22, v26, 23))
    edges.append(Edge(v22, v27, 27))
    edges.append(Edge(v24, v28, 23))
    edges.append(Edge(v25, v28, 13))
    edges.append(Edge(v25, v29, 15))
    edges.append(Edge(v26, v29, 17))
    edges.append(Edge(v28, v30, 11))
    edges.append(Edge(v29, v30, 13))

    edges.append(Edge(v28, v31, 18))
    edges.append(Edge(v29, v32, 12))
    edges.append(Edge(v30, v34, 9))
    edges.append(Edge(v30, v35, 11))
    edges.append(Edge(v31, v33, 14))
    edges.append(Edge(v31, v34, 19))
    edges.append(Edge(v32, v35, 16))
    edges.append(Edge(v32, v36, 23))
    edges.append(Edge(v32, v37, 27))
    edges.append(Edge(v34, v38, 23))
    edges.append(Edge(v35, v38, 13))
    edges.append(Edge(v35, v39, 15))
    edges.append(Edge(v36, v39, 17))
    edges.append(Edge(v38, v40, 11))
    edges.append(Edge(v39, v40, 13))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G


def makeGraphGA50():
    p1 = Processor(capacity=0.9, val="p1")
    p2 = Processor(capacity=0.9, val="p2")
    p3 = Processor(capacity=0.9, val="p3")
    p4 = Processor(capacity=0.9, val="p4")
    p5 = Processor(capacity=0.9, val="p5")
    p6 = Processor(capacity=0.9, val="p6")
    p7 = Processor(capacity=0.9, val="p7")
    p8 = Processor(capacity=0.9, val="p8")
    P = ProcessorList([p1,p2,p3,p4,p5,p6,p7,p8])

    v1 = Vertex("v1", 13, p2)
    v2 = Vertex("v2", 17, p2)
    v3 = Vertex("v3", 14, p2)
    v4 = Vertex("v4", 9, p3)
    v5 = Vertex("v5", 12, p1)
    v6 = Vertex("v6", 13, p2)
    v7 = Vertex("v7", 11, p1)
    v8 = Vertex("v8", 10, p3)
    v9 = Vertex("v9", 17, p2)
    v10 = Vertex("v10", 15, p4)
    v11 = Vertex("v11", 13, p5)
    v12 = Vertex("v12", 17, p6)
    v13 = Vertex("v13", 14, p7)
    v14 = Vertex("v14", 9, p8)
    v15 = Vertex("v15", 12, p3)
    v16 = Vertex("v16", 13, p2)
    v17 = Vertex("v17", 11, p1)
    v18 = Vertex("v18", 10, p5)
    v19 = Vertex("v19", 17, p2)
    v20 = Vertex("v20", 15, p8)
    v21 = Vertex("v21", 13, p5)
    v22 = Vertex("v22", 17, p6)
    v23 = Vertex("v23", 14, p7)
    v24 = Vertex("v24", 9, p8)
    v25 = Vertex("v25", 12, p3)
    v26 = Vertex("v26", 13, p2)
    v27 = Vertex("v27", 11, p1)
    v28 = Vertex("v28", 10, p5)
    v29 = Vertex("v29", 17, p2)
    v30 = Vertex("v30", 15, p8)
    v31 = Vertex("v31", 13, p5)
    v32 = Vertex("v32", 17, p6)
    v33 = Vertex("v33", 14, p7)
    v34 = Vertex("v34", 9, p8)
    v35 = Vertex("v35", 12, p3)
    v36 = Vertex("v36", 13, p2)
    v37 = Vertex("v37", 11, p1)
    v38 = Vertex("v38", 10, p5)
    v39 = Vertex("v39", 17, p2)
    v40 = Vertex("v40", 15, p8)
    v41 = Vertex("v41", 13, p5)
    v42 = Vertex("v42", 17, p6)
    v43 = Vertex("v43", 14, p7)
    v44 = Vertex("v44", 9, p8)
    v45 = Vertex("v45", 12, p3)
    v46 = Vertex("v46", 13, p2)
    v47 = Vertex("v47", 11, p1)
    v48 = Vertex("v48", 10, p5)
    v49 = Vertex("v49", 17, p2)
    v50 = Vertex("v50", 15, p8)


    vertex = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45, v46, v47, v48, v49, v50]

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
    edges.append(Edge(v7, v11, 18))
    edges.append(Edge(v8, v11, 12))
    edges.append(Edge(v9, v12, 9))
    edges.append(Edge(v11, v13, 11))
    edges.append(Edge(v10, v14, 14))
    edges.append(Edge(v10, v15, 19))
    edges.append(Edge(v10, v16, 16))
    edges.append(Edge(v12, v17, 23))
    edges.append(Edge(v14, v18, 27))
    edges.append(Edge(v15, v18, 23))
    edges.append(Edge(v15, v19, 13))
    edges.append(Edge(v16, v19, 15))
    edges.append(Edge(v18, v20, 17))
    edges.append(Edge(v19, v20, 11))
    edges.append(Edge(v12, v16, 13))
    edges.append(Edge(v18, v21, 18))
    edges.append(Edge(v19, v22, 12))
    edges.append(Edge(v20, v24, 9))
    edges.append(Edge(v20, v25, 11))
    edges.append(Edge(v21, v23, 14))
    edges.append(Edge(v21, v24, 19))
    edges.append(Edge(v22, v25, 16))
    edges.append(Edge(v22, v26, 23))
    edges.append(Edge(v22, v27, 27))
    edges.append(Edge(v24, v28, 23))
    edges.append(Edge(v25, v28, 13))
    edges.append(Edge(v25, v29, 15))
    edges.append(Edge(v26, v29, 17))
    edges.append(Edge(v28, v30, 11))
    edges.append(Edge(v29, v30, 13))
    edges.append(Edge(v28, v31, 18))
    edges.append(Edge(v29, v32, 12))
    edges.append(Edge(v30, v34, 9))
    edges.append(Edge(v30, v35, 11))
    edges.append(Edge(v31, v33, 14))
    edges.append(Edge(v31, v34, 19))
    edges.append(Edge(v32, v35, 16))
    edges.append(Edge(v32, v36, 23))
    edges.append(Edge(v32, v37, 27))
    edges.append(Edge(v34, v38, 23))
    edges.append(Edge(v35, v38, 13))
    edges.append(Edge(v35, v39, 15))
    edges.append(Edge(v36, v39, 17))
    edges.append(Edge(v38, v40, 11))
    edges.append(Edge(v39, v40, 13))
    edges.append(Edge(v38, v41, 18))
    edges.append(Edge(v39, v42, 12))
    edges.append(Edge(v40, v44, 9))
    edges.append(Edge(v40, v45, 11))
    edges.append(Edge(v41, v43, 14))
    edges.append(Edge(v41, v44, 19))
    edges.append(Edge(v42, v45, 16))
    edges.append(Edge(v42, v46, 23))
    edges.append(Edge(v42, v47, 27))
    edges.append(Edge(v44, v48, 23))
    edges.append(Edge(v45, v48, 13))
    edges.append(Edge(v45, v49, 15))
    edges.append(Edge(v46, v49, 17))
    edges.append(Edge(v48, v50, 11))
    edges.append(Edge(v49, v50, 13))

    G = Graph(vertex, edges, P)

    updateGraph(G)

    return G

