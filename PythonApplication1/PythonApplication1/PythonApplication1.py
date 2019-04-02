import sys
from functions import *

if __name__ == "__main__":
    print ("\nMakeGraph()")
    G = make_graph()
    print([x.val for x in G.V])
    print([x.first.val for x in G.E])
    print([x.second.val for x in G.E])

    Lin = get_in_degrees(G, G.V[0])
    Lout = get_out_degrees(G, G.V[0])
    Lsuc = []
    get_succesors(G.V[7], G, Lsuc)
    Lpred = []
    get_predecessors(G.V[1], G, Lpred)

    print("Succesors: ", [x.val for x in Lsuc])
    print("Predecessors: ", [x.val for x in Lpred])
    print("In degrees: ", [x.val for x in Lin])
    print("Out degrees: ", [x.val for x in Lout])
    
    preProcessing(G)
    print("\nValues after preProcessing(): \n")
    print([x.val for x in G.V])
    print([x.first.val for x in G.E])
    print([x.second.val for x in G.E])
    
