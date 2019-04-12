import sys
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*

if __name__ == "__main__":
    G = makeGraphTest()
    drawGraph(G, "testingProccesingFunction.gv")


    print(totalCost(G.P))
    #drawAllGraphs(9)
