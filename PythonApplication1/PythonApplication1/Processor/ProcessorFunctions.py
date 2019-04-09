import sys
from math import exp
from Processor.ProcessorClass import *
from Graph.DrawGraph import *

vmBasePrice = 0.0475
vmBaseSpeed = 1.0

def startTime(G, vertex):
    return max(availableProcessorForTask(G, vertex),max(predecessorTime(G, vertex)))

def predecessorTime(G, vertex):
    if (len(vertex.predecessors) == 0):
        return [0]
    L = []
    inDegree = getInDegrees(G, vertex)
    for pred in inDegree:
        L.append((finishTime(G, pred) + communicationCost(G, pred, vertex)))
    return L

def finishTime(G, vertex):
    return startTime(G, vertex) + calculateETC(vertex.weight, vertex.processor)

#Treba videti da li treba broj zaokruziti navise sa ceil-om
def calculateETC(time, processor):
    return time//processor.capacity 

def communicationCost(G, vertex1, vertex2):
    if (vertex1.processor == vertex2.processor):
        return 0
    for edge in G.E:
        if edge.first == vertex1 and edge.second == vertex2:
            return edge.weight
    exit(1)

def availableProcessorForTask(G, vertex):
    n = 0
    for iter in vertex.processor.taskList:
        if iter == vertex:
            return n
        n = finishTime(G, iter)
    return n
#def vmCost(processor):
#    return vmBase*exp(processor.capacity/vmBaseSpeed)
#def cost(processor):
#    n = 0
#    for task in len(processor.taskList):
#        n += vmCost(processor)*calculateETC()

