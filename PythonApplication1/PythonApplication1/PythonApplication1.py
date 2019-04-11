import sys
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*

if __name__ == "__main__":
    G = makeGraphTest()
    drawGraph(G, "testingProccesingFunction.gv")

    for task in G.V[1].processor.taskList:
        print(str(task.startTime) + " " + str(task.finishTime))
        if isinstance(task, Slot):
            print("SLOT!")

    #drawAllGraphs(9)
