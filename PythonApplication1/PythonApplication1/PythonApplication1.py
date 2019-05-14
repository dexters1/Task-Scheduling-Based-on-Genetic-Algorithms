import sys
from Graph.GraphPreprocessing import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from GeneticAlgorithm.populationInitialization import *

if __name__ == "__main__":
#   drawAllGraphs(9)

    mP = initialMultiPopulation(2, 10, makeGraph7)

    updateFitness(mP)

    for i in range(0,1):
        for j in range(0,10):
            print("info: " + str(i) + " " + str(j))
            print(mP[i].individualList[j].fitness)

    for i in range(0,10):
        print("individual number: " + str(i))
        print(mP[0].individualList[i].cost)
        print(mP[0].individualList[i].totalTime)
        print("\n")

    print("Population info")
    print(mP[0].maxCost)
    print(mP[0].minCost)
    print(mP[0].maxTime)
    print(mP[0].minTime)

    print([processor.val for processor in mP[0].individualList[0].P.processorList[0].taskList])
    print([processor.val for processor in mP[0].individualList[0].P.processorList[1].taskList])
    print([processor.val for processor in mP[0].individualList[0].P.processorList[2].taskList])

    drawMpGraph(mP)

   
