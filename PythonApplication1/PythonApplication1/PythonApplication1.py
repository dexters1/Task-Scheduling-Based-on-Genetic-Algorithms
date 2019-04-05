import sys
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *

if __name__ == "__main__":
    print ("makeGraph()")
    G = makeGraph()
    printGraph(G)
    
    simplifyGraph(G)
    print("Values after preProcessing(): ")
    printGraph(G)

    
