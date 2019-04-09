import sys
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*

if __name__ == "__main__":
    G = makeGraphTest()
    print(startTime(G, G.V[0]))
    print(finishTime(G, G.V[0]))
    print("\n")

    print(startTime(G, G.V[1]))
    print(finishTime(G, G.V[1]))
    print("\n")

    print(startTime(G, G.V[2]))
    print(finishTime(G, G.V[2]))
    print("\n")

    print(startTime(G, G.V[3]))
    print(finishTime(G, G.V[3]))
    print("\n")

    print(startTime(G, G.V[4]))
    print(finishTime(G, G.V[4]))
    print("\n")

    #drawAllGraphs(9)
