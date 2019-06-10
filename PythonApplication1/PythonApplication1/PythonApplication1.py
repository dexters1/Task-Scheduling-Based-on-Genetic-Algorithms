import sys
from Graph.GraphPreprocessing import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from GeneticAlgorithm.PopulationInitialization import *
from GeneticAlgorithm.GeneticOperations import *
from TaskDuplication.TaskDuplicationFunctions import *

if __name__ == "__main__":
    mP = initialMultiPopulation(mPN, NIND, makeGraphGA)

    updateFitness(mP)
    updateSelectionNumber(mP)
    print(mP.fittestIndividual.fitness)
    #Izmerim vreme od pocetka do posle GA i od GA do kraja
    #Trebaju slike pre i posle dupliciranja za sve te grafove od 10 20 30 40 i 50 taskova na 8 procesora
    #Trebam slike raspodele posle GA i pre i posle dupliciranja
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

    drawGraph(mP.fittestIndividual, "taskDuplicationTest/PreDuplicationLastGeneration")
    taskDuplication(mP.fittestIndividual)
    print(mP.fittestIndividual.totalTime)
    print(totalCost(mP.fittestIndividual.P))
    drawGraph(mP.fittestIndividual, "taskDuplicationTest/lastGeneration")


   
