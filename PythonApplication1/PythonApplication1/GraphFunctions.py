import sys
from Graph import *

#Makes a user defined graph
def make_graph():
    a = Vertex("a", 10)
    b = Vertex("b", 15)
    c = Vertex("c", 23)
    d = Vertex("d", 11)
    e = Vertex("e", 21)
    f = Vertex("f", 23)
    g = Vertex("g", 17)
    h = Vertex("h", 17)
    i = Vertex("i", 13)
    j = Vertex("j", 12)

    vertex = [a, b, c, d, e, f, g, h, i, j]

    edges = []

    edges.append(Edge(a, b))
    edges.append(Edge(a, c))
    edges.append(Edge(a, d))
    edges.append(Edge(b, e))
    edges.append(Edge(c, f))
    edges.append(Edge(d, g))
    edges.append(Edge(e, h))
    edges.append(Edge(f, h))
    edges.append(Edge(g, h))
    edges.append(Edge(h, i))
    edges.append(Edge(i, j))

    G = Graph(vertex, edges)

    update_successors(G)
    update_predecessors(G)

    return G

#Returns a list of all inward edges of a vertex
def get_in_degrees(G, vertex):
    L = []
    n = 0
    for edge in G.E:
        if edge.second == vertex:
                L.append(edge.first)
    return L

#Returns a list of all outward edges of a vertex
def get_out_degrees(G, vertex):
    L = []
    n = 0
    for edge in G.E:
        if edge.first == vertex:
            L.append(edge.second)
    return L

#Returns a list of all successors of a vertex (an empty list must be sent as a parameter of the function call)
def get_successors(vertex, G, L):
    S = []
    for edge in G.E:
       if edge.first == vertex:
         if edge.second not in L:
             L.append(edge.second)
             S.append(edge.second)
    for suc in S:
        get_successors(suc, G, L)
    return L

#Returns a list of all predecessors of a vertex (an empty list must be sent as a parameter of the function call)
def get_predecessors(vertex, G, L):
    S = []
    for edge in G.E:
       if edge.second == vertex:
           if edge.first not in L:
             L.append(edge.first)
             S.append(edge.first)             
    for pred in S:
        get_predecessors(pred, G, L)
    return L

#Updates the successors for all the vertexes in the graph
def update_successors(G):
    for vertex in G.V:
        vertex.successors[:] = []
        vertex.successors = get_successors(vertex, G, vertex.successors)

#Updates the predecessors for all the vertexes in the graph
def update_predecessors(G):
    for vertex in G.V:
        vertex.predecessors[:] = []
        vertex.predecessors = get_predecessors(vertex, G, vertex.predecessors)

def print_graph(G):
    print("\n")
    print("Vertices names:   ", [x.val for x in G.V])
    print("Vertices weights:","[", ",  ".join([str(x.weight) for x in G.V]),"]")
    print("First edge:  ", [x.first.val for x in G.E])
    print("Second edge: ", [x.second.val for x in G.E])
    print("\n")
    
       