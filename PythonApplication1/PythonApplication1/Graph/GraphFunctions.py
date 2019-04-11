import sys
from Graph.GraphClass import *

# Input args:
#   No input args
# output args:
#   Graph
# Description:
#   Makes a predefined graph
def makeGraph():
    v1 = Vertex("v1", 10)
    v2 = Vertex("v2", 15)
    v3 = Vertex("v3", 23)
    v4 = Vertex("v4", 11)
    v5 = Vertex("v5", 21)
    v6 = Vertex("v6", 3)
    v7 = Vertex("v7", 17)
    v8 = Vertex("v8", 7)
    v9 = Vertex("v9", 13)
    v10 = Vertex("v10", 12)

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

    G = Graph(vertex, edges)

    updateSuccessors(G)
    updatePredecessors(G)

    return G

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
    
       