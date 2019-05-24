import sys
from Graph.GraphPreprocessing import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from GeneticAlgorithm.PopulationInitialization import *
from GeneticAlgorithm.GeneticOperations import *
from TaskDuplication.TaskDuplicationFunctions import *

if __name__ == "__main__":
#   drawAllGraphs(9)
    G = makeGraphGATheirs()
    totalTime(G)
    G.cost = totalCost(G.P)
    print(G.totalTime)
    print(G.cost)
    drawGraph(G, "theirGraph/graph")
    G = makeGraph7()
    for processor in G.P.processorList:
        print([x.val for x in processor.taskList])
        print([x.finishTime for x in processor.taskList])
    taskDuplication(G)

    drawGraph(G, "taskDuplicationTest/Graf7")


#    exit(0)
    mP = initialMultiPopulation(mPN, NIND, makeGraphGA)

    updateFitness(mP)
    updateSelectionNumber(mP)
    print(mP.fittestIndividual.fitness)       
        
    #newGeneration(mP)

    #for population in mP.populationList:
    #    print("Population: " + str(j))
    #    j = j + 1
    #    print(population.minCost, population.minTime)

    noChange = 0
    for i in range(0, 100):
        lastCost = copy.deepcopy(mP.fittestIndividual.cost)
        fittestGraph = newGeneration(mP)
        if fittestGraph.cost == lastCost:
            noChange = noChange + 1
        else:
            noChange = 0
        if noChange >= 10:
            print("No change for 10 generations")
            break

    taskDuplication(mP.fittestIndividual)
    print(mP.fittestIndividual.totalTime)
    print(mP.fittestIndividual.cost)
    drawGraph(mP.fittestIndividual, "multiPopulationFittest/lastGeneration")

    #print( [x.selectionNumber for x in matingPool(mP[0])])

   # for vertex in mP[0].individualList[0].V:
   #     print(vertex.val + " " + vertex.processor.val)

    #for vertex in mP[0].individualList[1].V:
    #    print(vertex.val + " " + vertex.processor.val)

#    child = crossoverOperation(mP.populationList[0].individualList[0], mP.populationList[0].individualList[1])

#    for processor in child.P.processorList:
#        print(processor)
#
#    for vertex in child.V:
#        print(vertex.val + " " + str(vertex.processor.val))

  #  for vertex in child.V:
  #      print(vertex.val + " " + vertex.processor.val)

  #  verteciasd = [x.val for x in child.V]
  #  for x in verteciasd:
  #      print(int(x.val[1::]))
  #  verteciasd.sort(key=lambda x: int(x[1::]), reverse=True)
  #  print(verteciasd)

#    for processor in mP.populationList[0].individualList[6].P.processorList:
#        print(processor)
#
#    for vertex in mP.populationList[0].individualList[6].V:
#        print(vertex.val + " " + str(vertex.processor.val))

#    for individual in mP.populationList[0].individualList:
#    mutateIndividual(mP.populationList[0], mP.populationList[0].individualList[6])

#    print("AFTER")
#    for processor in mP.populationList[0].individualList[6].P.processorList:
#        print(processor)

#    for vertex in mP.populationList[0].individualList[6].V:
#        print(vertex.val + " " + str(vertex.processor.val))

 #   print(len(mate(mP.populationList[0])))

   # drawMpGraph(mP)

   
