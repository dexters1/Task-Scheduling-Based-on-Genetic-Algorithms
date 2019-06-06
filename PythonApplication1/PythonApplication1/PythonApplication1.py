import sys
from Graph.GraphPreprocessing import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from GeneticAlgorithm.PopulationInitialization import *
from GeneticAlgorithm.GeneticOperations import *
from TaskDuplication.TaskDuplicationFunctions import *

if __name__ == "__main__":
#    drawAllGraphs(9);
    #I dalje ne kapiram sta je edge weight i ko se njime bavi
    #jer je procesor i dalje slobodan za obradu taskova dok prenosi
    #task na drugi procesor
    mP = initialMultiPopulation(mPN, NIND, makeGraphGA)

    updateFitness(mP)
    updateSelectionNumber(mP)
    print(mP.fittestIndividual.fitness)

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
    print(totalCost(mP.fittestIndividual.P))
    drawGraph(mP.fittestIndividual, "taskDuplicationTest/lastGeneration")

   
