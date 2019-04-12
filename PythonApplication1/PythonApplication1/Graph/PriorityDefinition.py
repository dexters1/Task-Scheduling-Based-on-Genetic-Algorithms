import sys
from Graph.GraphClass import * 
from Graph.GraphFunctions import *
from math import inf

# Input args:
#   Graph
# output args:
#   No output
# Description: 
#   Defines priortiy based on the priority definition formula for each vertex
#   and sorts the vertices in graph based on descending priority 
# Issues/Bugs:
#   No error handling if Graph isn't correct
def priorityDefinition(G):
    alpha = 1
    beta = 1
    for vertex in G.V:
        vertex.priority = alpha*len(vertex.predecessors)*priorityDefinitionHeft(G, vertex)+beta*communicationCostOfSuccesors(G, vertex)

    # if there is a vertex in graph with no predecessors asign it priority of inf,
    # and if there is a vertex in graph with no successors asign it priority of 0
    for vertex in G.V:
        if len(vertex.predecessors) == 0:
            vertex.priority = inf
        if len(vertex.successors) == 0:
            vertex.priority = 0
 
    sortGraphByPriority(G)

# Input args:
#   Graph, Vertex
# output args:
#   int
# Description: 
#   Returns Heft priortiy based on the heft priority formula
# Issues/Bugs:
#   No error handling if Graph isn't correct
def priorityDefinitionHeft(G, vertex):
    return vertex.weight + max(heftHelperFunction(G,vertex))

# Input args:
#   Graph, Vertex
# output args:
#   List
# Description: 
#   Helper function for priorityDefinitionHeft, not to be used outside
#   the priorityDefinitionHeft function
# Issues/Bugs:
#   No error handling if Graph isn't correct
def heftHelperFunction(G, vertex):
    L = []
    if len(vertex.successors) == 0:
        L = [0]
        return L
    for successor in vertex.successors:
        L.append(getEdgeWeight(G, vertex, successor) + priorityDefinitionHeft(G, successor))
    return L

# Input args:
#   Graph, Vertex
# output args:
#   int
# Description: 
#   Returns the sum of communication costs between a vertex and all it's
#   successors
# Issues/Bugs:
#   No error handling if args aren't correct
def communicationCostOfSuccesors(G, vertex):
    n = 0
    for successor in vertex.successors[::-1]:
        n += getEdgeWeight(G, vertex, successor)
    return n

# Input args:
#   Graph
# output args:
#   No output
# Description: 
#   Sorts the list of vertices inside of the Graph function based on priority
# Issues/Bugs:
#   No error handling if Graph isn't correct
def sortGraphByPriority(G):
    G.V.sort(key=lambda x: x.priority, reverse=True)
    