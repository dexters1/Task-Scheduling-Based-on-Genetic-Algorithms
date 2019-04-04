import sys
from Graph.GraphClass import *
from Graph.GraphFunctions import *


# For every vertex in the graph check if the vertex has only one outward edge, if it does check if the outward vertex it's pointing to has only one inward edge, 
# if it does combine them into one vertex. Update successors and predecessors for all the vertexes in the graph in the end
def SimplifyGraph(G):
    cG = G.V[:]
    for vertex in cG: 
        outwardOfVertex = get_out_degrees(G, vertex) 
        if (len(outwardOfVertex) == 1): 
               inwardOfChild = get_in_degrees(G, outwardOfVertex[0]) 
               if(len(inwardOfChild) == 1):
                   combineVertex(vertex, outwardOfVertex[0], G)
    update_successors(G)
    update_predecessors(G)                

# Connect the inward edges of the parent vertex to the child vertex, add the parent processing time ( weight ) to the child vertex and delete the parent vertex and it's edges from the graph
# ( Not to be used outside the SimplifyGraph() function ) 
def combineVertex(vertex, outwardOfVertex, G): 
    inwardOfVertex = get_in_degrees(G, vertex)
    for iter in inwardOfVertex:
        G.E.append(Edge(iter,outwardOfVertex))
    outwardOfVertex.weight = outwardOfVertex.weight + vertex.weight
    G.V.remove(vertex)
    cG = G.E[:]
    for iter in cG:
        if iter.first == vertex or iter.second == vertex:
            G.E.remove(iter)
            