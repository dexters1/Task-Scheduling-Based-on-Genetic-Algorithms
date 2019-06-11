import sys
from Graph.GraphClass import *
from Graph.GraphFunctions import *

# Input args:
#   Graph
# output args:
#   No output
# Description: 
#   For every vertex in the graph check if the vertex has only one outward edge, 
#   if it does check if the outward vertex it's pointing to has only one inward edge, 
#   if it does combine them into one vertex. Update successors and predecessors for 
#    all the vertexes in the graph in the end
# Issues/Bugs:
#   No error handling if Graph isn't correct
def simplifyGraph(G):
    cG = G.V[:]
    for vertex in cG: 
        outwardOfVertex = getOutDegrees(G, vertex) 
        if (len(outwardOfVertex) == 1): 
               inwardOfChild = getInDegrees(G, outwardOfVertex[0]) 
               if(len(inwardOfChild) == 1):
                   combineVertex(vertex, outwardOfVertex[0], G)
    updateSuccessors(G)
    updatePredecessors(G)
    
# Input args:
#   Vertex, Vertex, Graph
# Output args:
#   No output
# Description:
#   Connect the inward edges of the first vertex to the second vertex, add the
#   first vertex processing time ( weight ) to the second vertex and delete the 
#   first vertex and it's edges from the graph
# Issues/Bugs:
#   - Not to be used outside the simplifyGraph() function, it's only made to 
#   help with simplifying of Graphs. 
#   - It assumes the first vertex has only one output and the second vertex
#   only one input due to it being the prerequisite of being called inside 
#   the simplifyGraph() function

def combineVertex(vertex, outwardOfVertex, G): 
    inwardOfVertex = getInDegrees(G, vertex)
    for iter in inwardOfVertex:
        edge = Edge(iter,outwardOfVertex)
        edge.weight = getEdgeWeight(G, iter, vertex)
        G.E.append(edge)
    outwardOfVertex.weight = outwardOfVertex.weight + vertex.weight
    outwardOfVertex.preprocessed = True
    outwardOfVertex.appendedVertexList.append(vertex.val)
    G.V.remove(vertex)
    cG = G.E[:]
    for iter in cG:
        if iter.first == vertex or iter.second == vertex:
            G.E.remove(iter)
            
