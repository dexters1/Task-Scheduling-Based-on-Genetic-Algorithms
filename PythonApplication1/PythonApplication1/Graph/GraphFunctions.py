import sys
from Graph.GraphClass import *

# Input args:
#   Graph, Vertex
# output args:
#   List
# Description: 
#   Returns a list of all inward edges of a vertex
def getInDegrees(G, vertex):
    L = []
    for edge in G.E:
        if edge.second == vertex:
                L.append(edge.first)
    return L

# Input args:
#   Graph, Vertex
# output args:
#   List
# Description: 
#   Returns a list of all outward edges of a vertex
def getOutDegrees(G, vertex):
    L = []
    for edge in G.E:
        if edge.first == vertex:
            L.append(edge.second)
    return L

# Input args:
#   Graph, Vertex, Vertex
# output args:
#   List
# Description: 
#   Returns weight of edge between first and second vertex sent, if there is
#   no edge exits application
def getEdgeWeight(G, first, second):
    for edge in G.E:
        if edge.first == first and edge.second == second:
            return edge.weight
    exit(1)


# Input args:
#   Vertex, Graph, List
# output args:
#   List
# Description: 
#   Returns a list of all successors of a vertex 
# Issues/Bugs:
#  - An empty list must be sent as a parameter of the function call or it will
#   not work proprely
def getAllSuccessors(vertex, G, L):
    S = []
    for edge in G.E:
       if edge.first == vertex:
         if edge.second not in L:
             L.append(edge.second)
             S.append(edge.second)
    for suc in S:
        getAllSuccessors(suc, G, L)
    return L

# Input args:
#   Vertex, Graph, List
# output args:
#   List
# Description: 
#   Returns a list of all predecessors of a vertex 
# Issues/Bugs:
#   - An empty list must be sent as a parameter of the function call or it will
#   not work proprely
def getAllPredecessors(vertex, G, L):
    S = []
    for edge in G.E:
       if edge.second == vertex:
           if edge.first not in L:
             L.append(edge.first)
             S.append(edge.first)             
    for pred in S:
        getAllPredecessors(pred, G, L)
    return L

# Input args:
#   Graph
# output args:
#   No output args
# Description: 
#   Updates the successors for all the vertexes in the graph
def updateSuccessors(G):
    for vertex in G.V:
        vertex.successors[:] = []
        vertex.successors = getOutDegrees(G, vertex)

# Input args:
#   Graph
# output args:
#   No output args
# Description: 
#   Updates the predecessors for all the vertexes in the graph
def updatePredecessors(G):
    for vertex in G.V:
        vertex.predecessors[:] = []
        vertex.predecessors = getInDegrees(G, vertex)

# Input args:
#   Graph
# output args:
#   No output args
# Description: 
#   Prints the graph, the names of it's vertices, weight of vertices and how they
#   are connected regarding Edges
# Issues/Bugs:
#   - No error handling if Graph isn't correct
def printGraph(G):
    print("\n")
    print("Vertices names:  ", [x.val for x in G.V])
    print("Vertices weights:","[", ",   ".join([str(x.weight) for x in G.V]),"]")
    print("First edge: ", [x.first.val for x in G.E])
    print("Second edge:", [x.second.val for x in G.E])
    print("\n")
       

def updateGraph(G):
    import Processor.ProcessorFunctions
    import Graph.PriorityDefinition
    updateSuccessors(G)
    updatePredecessors(G)
    Graph.PriorityDefinition.priorityDefinition(G)
    print([x.val for x in G.V])
    Processor.ProcessorFunctions.updateProcessorTaskList(G)
    Processor.ProcessorFunctions.updateStartTime(G)
    Processor.ProcessorFunctions.updateFinishTime(G)
    Processor.ProcessorFunctions.addSlot(G)