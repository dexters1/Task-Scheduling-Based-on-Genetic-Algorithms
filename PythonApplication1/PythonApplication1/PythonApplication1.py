import sys
from Graph.GraphPreprocessing import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from GeneticAlgorithm.PopulationInitialization import *
from GeneticAlgorithm.GeneticOperations import *
from TaskDuplication.TaskDuplicationFunctions import *
import time

if __name__ == "__main__":

    start_time = time.time()
    #Fali mi neki ReadMe ili opis main-a, raspitaj se oko toga sta da stavis
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

    drawGraph(mP.fittestIndividual, "taskDuplicationTest/PreDuplicationLastGenerationSimplified")

    print("GA code: %s seconds" % (time.time() - start_time))

    taskDuplication(mP.fittestIndividual)
    print(mP.fittestIndividual.totalTime)
    print(totalCost(mP.fittestIndividual.P))
    drawGraph(mP.fittestIndividual, "taskDuplicationTest/lastGenerationSimplified")

    print("Full code: %s seconds" % (time.time() - start_time))


   
