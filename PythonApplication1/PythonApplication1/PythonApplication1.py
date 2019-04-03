import sys
from GraphPreprocessing import *
from MakeGraphVariations import *

if __name__ == "__main__":
    print ("\nMakeGraph()")
    G = make_graph()
    print([x.val for x in G.V])
    print([x.weight for x in G.V])
    print([x.first.val for x in G.E])
    print([x.second.val for x in G.E])
    print([x.val for x in G.V[0].successors])
    print([x.val for x in G.V[4].successors])
    print([x.val for x in G.V[4].predecessors])
    print([x.val for x in G.V[1].predecessors])
    
    SimplifyGraph(G)
    print("\nValues after preProcessing(): \n")
    print([x.val for x in G.V])
    print([x.weight for x in G.V])
    print([x.first.val for x in G.E])
    print([x.second.val for x in G.E])
    print([x.val for x in G.V[0].successors])
    print([x.val for x in G.V[1].successors])
    print([x.val for x in G.V[0].predecessors])
    print([x.val for x in G.V[1].predecessors])

    
