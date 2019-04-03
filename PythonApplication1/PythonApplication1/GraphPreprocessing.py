import sys
from Graph import *
from GraphFunctions import *


# For every vertex in the graph check if the vertex has only one outward edge, if it does check if the outward vertex it's pointing to has only one inward edge, 
# if it does combine them into one vertex. Update successors and predecessors for all the vertexes in the graph in the end
def SimplifyGraph(G):
    cG = G.V[:]
    for vertex in cG: 
        o = get_out_degrees(G, vertex) 
        if (len(o) == 1): 
               iChild = get_in_degrees(G, o[0]) 
               if(len(iChild) == 1):
                   combineVertex(vertex, o[0], G)
    update_successors(G)
    update_predecessors(G)                

# Connect the inward edges of the parent vertex to the child vertex, add the parent processing time ( weight ) to the child vertex and delete the parent vertex and it's edges from the graph
# ( Not to be used outside the SimplifyGraph() function ) 
def combineVertex(v, o, G): 
    iV = get_in_degrees(G, v)
    for iter in iV:
        G.E.append(Edge(iter,o))
    o.weight = o.weight + v.weight
    G.V.remove(v)
    cG = G.E[:]
    for iter in cG:
        if iter.first == v or iter.second == v:
            G.E.remove(iter)
            