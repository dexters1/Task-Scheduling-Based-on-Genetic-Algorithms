import sys
from GraphPreprocessing import *
from MakeGraphVariations import *

if __name__ == "__main__":
    print ("MakeGraph()")
    G = make_graph()
    print_graph(G)
    
    SimplifyGraph(G)
    print("Values after preProcessing(): ")
    print_graph(G)

    
