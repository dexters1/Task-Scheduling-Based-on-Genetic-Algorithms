from graphviz import Digraph
from Graph.GraphClass import *
import os
pathDirectory = os.path.dirname(os.path.dirname(__file__)) + "\\Graphviz\\bin"
os.environ["PATH"] += os.pathsep + pathDirectory

# Input args:
#   Graph, String
# output args:
#   No output args
# Description: 
#   Draws the graph, the names of it's vertices and how they are connected
#   regarding Edges. It saves the drawn graph as a pdf file as fileName.gv.pdf
#   in the test-output directory which inside the directory of the source code
# Issues/Bugs:
#   - No error handling if Graph isn't correct
def drawGraph(G, fileName):

    dot = Digraph(comment=fileName)
    for vertex in G.V:
        dot.node(vertex.val, vertex.val)
    for edge in G.E:
        dot.edge(edge.first.val, edge.second.val, constraint='true')
    fileDirectory = "test-output/" + fileName
    dot.render(fileDirectory, view=False)