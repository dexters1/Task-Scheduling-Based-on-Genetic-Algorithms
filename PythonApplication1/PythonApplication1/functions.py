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

def get_in_degrees(G):
    L = []
    for v in G.V:
        n = 0
        for edge in G.E:
            if edge.second == v:
                n += 1
        L.append(n)
    return L

def get_out_degrees(G):
    L = []
    for v in G.V:
        n = 0
        for edge in G.E:
            if edge.first == v:
                n += 1
        L.append(n)
    return L

def get_succesors(node, G):
    L = []
    for edge in G.E:
       if edge.first == node:
         L.append(edge.second.val)
    return L

def get_predecessors(node, G):
    L = []
    for edge in G.E:
       if edge.second == node:
         L.append(edge.first.val)
    return L
