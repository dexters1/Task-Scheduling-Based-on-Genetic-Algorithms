import sys
from graph import *
from math import inf

def make_graph():
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")
    g = Vertex("g")
    h = Vertex("h")
    i = Vertex("i")
    j = Vertex("j")

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

    return Graph(vertex, edges)

def get_in_degrees(G, v):
    L = []
    n = 0
    for edge in G.E:
        if edge.second == v:
                L.append(edge.first)
    return L

def get_out_degrees(G, v):
    L = []
    n = 0
    for edge in G.E:
        if edge.first == v:
            L.append(edge.second)
    return L

def get_succesors(node, G, L):
    S = []
    for edge in G.E:
       if edge.first == node:
         if edge.second not in L:
             L.append(edge.second)
             S.append(edge.second)
    for suc in S:
        get_succesors(suc, G, L)
    return L

def get_predecessors(node, G, L):
    S = []
    for edge in G.E:
       if edge.second == node:
           if edge.first not in L:
             L.append(edge.first)
             S.append(edge.first)             
    for pred in S:
        get_predecessors(pred, G, L)
    return L

def preProcessing(G):
    cG = G.V[:]
    for v in cG:
        i = get_in_degrees(G, v)
        o = get_out_degrees(G, v)
        print("in_deg: ", len(i), "out_deg", len(o))
        #if (len(i) <= 1) and (len(o) == 1):
        if (len(o) == 1):
               iChild = get_in_degrees(G, o[0])
               if(len(iChild) == 1):
                   combineNode(v, o[0], G)


def combineNode(v, o, G): 
    iV = get_in_degrees(G, v)
    #if (len(iV) == 1 ):
    #    G.E.append(Edge(iV[0],o))
    for iter in iV:
        G.E.append(Edge(iter,o))
    G.V.remove(v)
    cG = G.E[:]
    for iter in cG:
        if iter.first == v or iter.second == v:
            G.E.remove(iter)
            
       