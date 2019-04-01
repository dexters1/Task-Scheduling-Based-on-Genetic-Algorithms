import sys
from functions import *

if __name__ == "__main__":
    print ("\nMakeGraph()")
    G = make_graph()
    print([x.val for x in G.V])
    print([x.first.val for x in G.E])
    print([x.second.val for x in G.E])

    Lin = get_in_degrees(G)
    Lout = get_out_degrees(G)
    Lsuc = []
    get_succesors(G.V[0], G, Lsuc)
    Lpred = []
    get_predecessors(G.V[8], G, Lpred)

    for i in range(len(G.V)):
        print("Node:", G.V[i].val, "In degrees:", Lin[i], "Out degrees:", Lout[i])
    print("Succesors: ", Lsuc)
    print("Predecessors: ", Lpred)
    
