from graphviz import Digraph
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
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

    dot = Digraph()
    for vertex in G.V:
        nodeName = vertex.val + "\n" + "w:" + str(vertex.weight) + "|"+"st:"+str(vertex.startTime)+"|"+"ft:"+str(vertex.finishTime)+"|"+str(vertex.processor.val)
        dot.node(vertex.val, nodeName, fontsize=str(8.0))
    for edge in G.E:
        dot.edge(edge.first.val, edge.second.val,label=str(edge.weight), fontsize=str(6.0),constraint='true')
    fileDirectory = "test-output/" + fileName
    dot.render(fileDirectory, view=False)

# Input args:
#   int
# output args:
#   No output args
# Description: 
#   Goes through all the different graphs in the MakeGraphVariations module and
#   calls the drawGraph fucntion for the regular graph and it's simplified 
#   counterpart. The input argument i is used to denote the number of different 
#   graphs in the MakeGraphVariations module  
# Issues/Bugs:
#   - No error handling if input argument i is larger than the number of Graphs
#   in MakeGraphVariations
def drawAllGraphs(i):
    for iter in range(1,i+1):
           funcName = "makeGraph"+str(iter)
           G = globals()[funcName]()

           fileName = "slika_" + str(iter) + ".gv"
           drawGraph(G,fileName)

           simplifyGraph(G)

           fileNameSimplified = "slika_" + str(iter) + "_Simplified.gv"	
           drawGraph(G,fileNameSimplified)