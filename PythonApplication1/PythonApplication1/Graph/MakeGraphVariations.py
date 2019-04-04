import sys
from Graph.GraphClass import *
from Graph.GraphFunctions import *

def make_graph1():
    a = Vertex("a", 10)
    b = Vertex("b", 15)

    vertex = [a, b]

    edges = []

    edges.append(Edge(a, b))

    G = Graph(vertex, edges)

    update_successors(G)
    update_predecessors(G)

    return G

def make_graph2():
    a = Vertex("a", 10)
    b = Vertex("b", 15)
    c = Vertex("c", 23)
    d = Vertex("d", 11)

    vertex = [a, b, c, d]

    edges = []

    edges.append(Edge(a, b))
    edges.append(Edge(a, c))
    edges.append(Edge(a, d))

    G = Graph(vertex, edges)

    update_successors(G)
    update_predecessors(G)

    return G

def make_graph3():
    a = Vertex("a", 10)
    b = Vertex("b", 15)
    c = Vertex("c", 23)
    d = Vertex("d", 11)
    e = Vertex("e", 21)
    f = Vertex("f", 3)
    g = Vertex("g", 17)
    h = Vertex("h", 7)

    vertex = [a, b, c, d, e, f, g, h]

    edges = []

    edges.append(Edge(a, d))
    edges.append(Edge(b, d))
    edges.append(Edge(c, d))
    edges.append(Edge(d, e))
    edges.append(Edge(e, f))
    edges.append(Edge(e, g))
    edges.append(Edge(e, h))

    G = Graph(vertex, edges)

    update_successors(G)
    update_predecessors(G)

    return G

def make_graph4():
    a = Vertex("a", 10)
    b = Vertex("b", 15)
    c = Vertex("c", 23)
    d = Vertex("d", 11)
    e = Vertex("e", 21)

    vertex = [a, b, c, d, e]

    edges = []

    edges.append(Edge(a, b))
    edges.append(Edge(a, c))
    edges.append(Edge(a, d))
    edges.append(Edge(b, e))
    edges.append(Edge(c, e))
    edges.append(Edge(d, e))

    G = Graph(vertex, edges)

    update_successors(G)
    update_predecessors(G)

    return G

def make_graph5():
    a = Vertex("a", 10)
    b = Vertex("b", 15)
    c = Vertex("c", 23)
    d = Vertex("d", 11)
    e = Vertex("e", 21)
    f = Vertex("f", 3)
    g = Vertex("g", 17)
    h = Vertex("h", 7)
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


def make_graph6():
    a = Vertex("a", 10)
    b = Vertex("b", 15)
    c = Vertex("c", 23)
    d = Vertex("d", 11)
    e = Vertex("e", 21)
    f = Vertex("f", 3)
    g = Vertex("g", 17)
    h = Vertex("h", 7)
    i = Vertex("i", 13)
    j = Vertex("j", 12)
    k = Vertex("k", 15)
    l = Vertex("l", 11)

    vertex = [a, b, c, d, e, f, g, h, i, j, k, l]

    edges = []

    edges.append(Edge(a, b))
    edges.append(Edge(b, d))
    edges.append(Edge(c, d))
    edges.append(Edge(e, d))
    edges.append(Edge(c, f))
    edges.append(Edge(e, h))
    edges.append(Edge(d, g))
    edges.append(Edge(g, i))
    edges.append(Edge(g, j))
    edges.append(Edge(j, k))
    edges.append(Edge(j, l))

    G = Graph(vertex, edges)

    update_successors(G)
    update_predecessors(G)

    return G

def make_graph7():
    a = Vertex("a", 10)
    b = Vertex("b", 15)
    c = Vertex("c", 23)
    d = Vertex("d", 11)
    e = Vertex("e", 21)
    f = Vertex("f", 3)
    g = Vertex("g", 17)
    h = Vertex("h", 7)
    i = Vertex("i", 13)
    j = Vertex("j", 12)

    vertex = [a, b, c, d, e, f, g, h, i, j]

    edges = []

    edges.append(Edge(a, b))
    edges.append(Edge(a, c))
    edges.append(Edge(a, d))
    edges.append(Edge(a, e))
    edges.append(Edge(a, f))
    edges.append(Edge(b, h))
    edges.append(Edge(b, i))
    edges.append(Edge(c, g))
    edges.append(Edge(d, h))
    edges.append(Edge(d, i))
    edges.append(Edge(e, i))
    edges.append(Edge(f, h))
    edges.append(Edge(g, j))
    edges.append(Edge(h, j))
    edges.append(Edge(i, j))

    G = Graph(vertex, edges)

    update_successors(G)
    update_predecessors(G)

    return G