import sys
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from GeneticAlgorithm.GeneticAlgorithmFunctions import *
from Graph.DrawGraph import drawGraph
import copy

# Input args:
#   Population, Graph(Parent1), Graph(Parent2)
# output args:
#   Graph(Child)
# Description: 
#   sorts both parents by vertex value and then crossesovers at crossoverPoint by crossoverLength
#   and then updates the child by prioritey, processorInfo, totalTime, cost and fitness
def crossoverOperation(population, parent1, parent2):
    child = copy.deepcopy(parent1)

    crossoverLenght = random.randint(0, round(len(child.V)/2))
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
    fitnessFunction(population, child)
    return child

# Input args:
#   Graph(Child), Graph(Parent)
# output args:
#   Processor(ChildProcessor)
# Description: 
#   Finds Child's processor by value of Parent's processor.
#   Meant to be used as a helper function for crossoverOperation
def findProcessorByVal(childGraph, parentProcessor):
    for processor in childGraph.P.processorList:
        if processor.val == parentProcessor.val:
            return processor
    exit(1)

# Input args:
#   Population, Graph(individual)
# output args:
#   float(probabilityOfMutation)
# Description: 
#   Calculates probability of Mutation for given individual
def probabilityOfMutation(population, individual):
    if individual.fitness >= population.fitnessAverage:
        return k3*(population.fittestIndividual.fitness - individual.fitness)/(population.fittestIndividual.fitness - population.fitnessAverage)
    else:
        return k4

# Input args:
#   Population, Graph(parent1), Graph(parent2)
# output args:
#   float(probabilityOfCrossover)
# Description: 
#   Calculates probability of Crossover for given parent combination
def probabilityOfCrossover(population, parent1, parent2):
    highestParentFitness = max(parent1.fitness, parent2.fitness)
    if highestParentFitness >= population.fitnessAverage:
        return k1*(population.fittestIndividual.fitness - highestParentFitness)/(population.fittestIndividual.fitness - population.fitnessAverage)
    else:
        return k2

# Input args:
#   Population, Graph(individual)
# output args:
#   No output
# Description: 
#   Calculates probabilityOfMutation for Graph(individual) then for each vertex
#   in Graph(individual) creates a randomNum between 0 and 1, if the number is
#   less than the probabilityOfMutation mutate individual ( mutation in this 
#   function means change the processor assigned to the particular vertex randomly )
def mutateIndividual(population, individual):
    pM = probabilityOfMutation(population, individual)
    for vertex in individual.V:
        randomNum = random.uniform(0,1)
        if randomNum <= pM:
            oldProcessor = vertex.processor
            while vertex.processor == oldProcessor:
                vertex.processor = random.choice(individual.P.processorList)


# Input args:
#   MultiPopulation, Population
# output args:
#   List(ChildList)
# Description: 
#   Finds the matePool based on selectionNum with the help of the matingPool 
#   function. Calculates the number of needed children and then fills the list
#   of children by crossover with the individuals from the matingPool. If 
#   the matingPool only has 2 or less unique individuals returns an empty list
#   because the population has converged 
def mate(mP, population):
    matePool = matingPool(mP, population)
    #matePool = population.individualList
    numberOfChildrenNeeded = NIND - numberOfSelectionIndividualsForPopulation(population) 
    numberOfChildren = 0
    childList = []
    while numberOfChildren != numberOfChildrenNeeded:
        fitnessValueList = list(set([x.fitness for x in matePool]))
        if mP.numberOfGenerations>2 and len(fitnessValueList) <= 2:
            return childList       
        parentList = random.sample(matePool, 2)      
        randomNum = random.uniform(0,1)
        pC = probabilityOfCrossover(population, parentList[0], parentList[1])
        if pC > randomNum:
            numberOfChildren = numberOfChildren + 1
            child = crossoverOperation(population, parentList[0], parentList[1])
            childList.append(child)
    return childList


# Input args:
#   MultiPopulation
# output args:
#   No output
# Description: 
#   Creates a newGeneration of multiPopulation. Transferes the selected individuals
#   from the previous generation to the new generation with the matingPoolList.
#   Makes a list of children with the mate function and then mutates the children.
#   In the end update all the individuals with regrads to priority, processorInfo,
#   totalTime, cost, PopulationInfo, fitness and selectionNumber.
def newGeneration(mP):
    for population in mP.populationList:
        matingPoolList = matingPool(mP, population)
        childrenList = mate(mP,population) 
        for individual in childrenList:
            mutateIndividual(population, individual)

        population.individualList = []
        population.individualList.extend(matingPoolList)
        population.individualList.extend(childrenList)
        if mP.numberOfGenerations > 2 and len(childrenList) == 0:
            population.individualList = []

        for individual in population.individualList:
            priorityDefinition(individual)
            updateProcessorInfo(individual)
            totalTime(individual)
            individual.cost = totalCost(individual.P)
        updatePopulationInfo(population)

    updateFitness(mP)
    updateSelectionNumber(mP)
    updateMultiPopulationInfo(mP)
    fittestIndividual = returnFittestIndividual(mP)


    mP.numberOfGenerations = mP.numberOfGenerations + 1
    print("Generation: " + str(mP.numberOfGenerations))
    print("Max fitness: " + str(fittestIndividual.fitness))
    print("Min Cost: " + str(mP.minCost))
    print("Max Cost: " + str(mP.maxCost))
    print("Min Time: " + str(mP.minTime))
    print("Max Time: " + str(mP.maxTime))
    print("Fittest Individual Cost: " + str(fittestIndividual.cost))
    print("Fittest Individual Time: " + str(fittestIndividual.totalTime))
    print("\n")

    return fittestIndividual