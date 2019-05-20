import sys
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from GeneticAlgorithm.GeneticAlgorithmFunctions import *
from Graph.DrawGraph import drawGraph
import copy

#sorts both parents by vertex value and then crossesover and then updates the child
def crossoverOperation(parent1, parent2):
    child = copy.deepcopy(parent1)

    crossoverLenght = random.randint(0, len(child.V)/2)
    crossoverPoint = random.randint(0, len(child.V)-crossoverLenght)

    vertexSortedByValChild = [x for x in child.V]
    vertexSortedByValChild.sort(key=lambda x: int(x.val[1::]), reverse=False)

    vertexSortedByValP2 = [x for x in parent2.V]
    vertexSortedByValP2.sort(key=lambda x: int(x.val[1::]), reverse=False)

    for i in range(crossoverPoint,crossoverPoint+crossoverLenght):
        vertexSortedByValChild[i].processor = findProcessorByVal(child, vertexSortedByValP2[i].processor)

    priorityDefinition(child)
    updateProcessorInfo(child)
    totalTime(child)
    child.cost = totalCost(child.P)
    return child


def findProcessorByVal(childGraph, parentProcessor):
    for processor in childGraph.P.processorList:
        if processor.val == parentProcessor.val:
            return processor
    exit(1)

def probabilityOfMutation(population, individual):
    if individual.fitness >= population.fitnessAverage:
        return k3*(population.fittestIndividual.fitness - individual.fitness)/(population.fittestIndividual.fitness - population.fitnessAverage)
    else:
        return k4

def probabilityOfCrossover(population, parent1, parent2):
    highestParentFitness = max(parent1.fitness, parent2.fitness)
    if highestParentFitness >= population.fitnessAverage:
        return k1*(population.fittestIndividual.fitness - highestParentFitness)/(population.fittestIndividual.fitness - population.fitnessAverage)
    else:
        return k2

def mutateIndividual(population, individual):
    pM = probabilityOfMutation(population, individual)
    for vertex in individual.V:
        randomNum = random.uniform(0,1)
        if randomNum <= pM:
            oldProcessor = vertex.processor
            while vertex.processor == oldProcessor:
                vertex.processor = random.choice(individual.P.processorList)

def mate(mP, population):
    matePool = matingPool(population)
    numberOfChildrenNeeded = NIND - numberOfSelectionIndividualsForPopulation(population) #ovde ce rasti na svakih par generacija malo
    numberOfChildren = 0
    childList = []
    while numberOfChildren != numberOfChildrenNeeded:
        parentList = random.sample(matePool, 2)
        randomNum = random.uniform(0,1)
        pC = probabilityOfCrossover(population, parentList[0], parentList[1])
        if pC > randomNum:
            numberOfChildren = numberOfChildren + 1
            child = crossoverOperation(parentList[0], parentList[1])
            childList.append(child)
    if not(mP.numberOfGenerations % 5):
        childList.append(copy.deepcopy(mP.fittestIndividual))
    return childList

def newGeneration(mP):
    for population in mP.populationList:
        matingPoolList = matingPool(population)
        childrenList = mate(mP,population) 
        for individual in childrenList:
            mutateIndividual(population, individual)

        population.individualList = []
        population.individualList.extend(matingPoolList)
        population.individualList.extend(childrenList)

        for individual in population.individualList:
            priorityDefinition(individual)
            updateProcessorInfo(individual)
            totalTime(individual)
            individual.cost = totalCost(individual.P)
        updatePopulationInfo(population)

    updateFitness(mP)
    updateSelectionNumber(mP)


    mP.numberOfGenerations = mP.numberOfGenerations + 1
    print("Generation: " + str(mP.numberOfGenerations))
    print("Max fitness: " + str(mP.fittestIndividual.fitness))
    print("Min Cost: " + str(mP.populationList[0].minCost))
    print("Max Cost: " + str(mP.populationList[0].maxCost))
    print("Min Time: " + str(mP.populationList[0].minTime))
    print("Max Time: " + str(mP.populationList[0].maxTime))
    print("Fittest Individual Cost: " + str(mP.fittestIndividual.cost))
    print("Fittest Individual Time: " + str(mP.fittestIndividual.totalTime))
    print("\n")