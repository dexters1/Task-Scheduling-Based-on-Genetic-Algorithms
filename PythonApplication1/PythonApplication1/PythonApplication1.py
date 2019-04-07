import sys
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from Graph.DrawGraph import *

if __name__ == "__main__":
    print ("makeGraph()")

    for iter in range(1,10):
        funcName = "makeGraph"+str(iter)
        G = globals()[funcName]()
        
        fileName = "slika_" + str(iter) + ".gv"
        drawGraph(G,fileName)

        simplifyGraph(G)
        fileNameSimplified = "slika_" + str(iter) + "_Simplified.gv"	
        drawGraph(G,fileNameSimplified)

   # G = makeGraph7()
   # printGraph(G)
   # drawGraph(G,"slika_7.gv")

    #simplifyGraph(G)
    #print("Values after preProcessing(): ")
    #printGraph(G)	
    #drawGraph(G,"slika_7_Simplified.gv")