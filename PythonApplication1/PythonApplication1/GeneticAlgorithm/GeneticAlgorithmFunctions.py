import sys
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from GeneticAlgorithm.GeneticAlgorithmClasses import *
import copy

# Input args:
#   Population
# output args:
#   No output
# Description: 
#   updates minTime, maxTime, minCost and maxCost for a population 
def updatePopulationInfo(population):
    for individual in population.individualList:
        if individual.totalTime < population.minTime:
            population.minTime = copy.deepcopy(individual.totalTime)
        if individual.totalTime > population.maxTime:
            population.maxTime = copy.deepcopy(individual.totalTime)
        if individual.cost < population.minCost:
            population.minCost = copy.deepcopy(individual.cost)
        if individual.cost > population.maxCost:
            population.maxCost = copy.deepcopy(individual.cost)

# Input args:
#   MultiPopulation
# output args:
#   No output
# Description: 
#   updates minTime, maxTime, minCost and maxCost for the MultiPopulation 
def updateMultiPopulationInfo(mP):
    for population in mP.populationList:
        if population.minTime < mP.minTime:
            mP.minTime = copy.deepcopy(population.minTime)
        if population.maxTime > mP.maxTime:
            mP.maxTime = copy.deepcopy(population.maxTime)
        if population.minCost < mP.minCost:
            mP.minCost = copy.deepcopy(population.minCost)
        if population.maxCost > mP.maxCost:
            mP.maxCost = copy.deepcopy(population.maxCost)

def returnFittestIndividual(mP):
    L = []
    for population in mP.populationList:
        L.append(copy.deepcopy(population.fittestIndividual))
    for individual in L:
        fitnessFunction(mP, individual)
    L.sort(key=lambda x: x.fitness, reverse=True)
    print([x.fitness for x in L])
    mP.fittestIndividual = L[0]
    return L[0]

# Input args:
#   Population, Graph(Individual)
# output args:
#   float(fitness)
# Description: 
#   Returns value of fitness function for an indvidiaul from a population
def fitnessFunction(population, individual):
    fitness = Omega*((population.maxTime - individual.totalTime)/(population.maxTime - population.minTime)) + (1 - Omega)*((population.maxCost - individual.cost)/(population.maxCost - population.minCost))
    individual.fitness = fitness
    return fitness

# Input args:
#   MultiPopulation
# output args:
#   No output
# Description: 
#   Updates fitness for all members of a MultiPopulation including the fittest
#   individual
def updateFitness(mP):
    for population in mP.populationList:
        for individual in population.individualList:
            fitnessFunction(population, individual)
        population.fitnessSum = 0
        population.fittestIndividual.fitness = fitnessFunction(population, population.fittestIndividual)
        for individual in population.individualList:
            if individual.fitness > population.fittestIndividual.fitness:
                population.fittestIndividual = copy.deepcopy(individual)
            population.fitnessSum += individual.fitness
        population.fitnessAverage = population.fitnessSum/NIND
        if  population.fittestIndividual.fitness > mP.fittestIndividual.fitness:
            mP.fittestIndividual = population.fittestIndividual #Problem je sto sad kad imam return fittestIndividual ovo je nepotrebno

# Input args:
#   MultiPopulation
# output args:
#   No output
# Description: 
#   Updates selectionNumber for all members of a MultiPopulation including the fittest
#   individual
def updateSelectionNumber(mP):
    for population in mP.populationList:
        if(population.fitnessSum != 0):
            population.fittestIndividual.selectionNumber = NIND*(population.fittestIndividual.fitness/population.fitnessSum)
            for individual in population.individualList:
                individual.selectionNumber = NIND*(individual.fitness/population.fitnessSum)

# Input args:
#   Population
# output args:
#   int(numberOfSelectedIndividuals)
# Description: 
#   Returns an int with selected number of individuals to be crossed over to the
#   next generation
def numberOfSelectionIndividualsForPopulation(population):
    sumN = 0
    for i in range(0, len(population.individualList)):
        if(population.individualList[i].selectionNumber < 1):
            sumN += population.individualList[i].selectionNumber
        else:
            sumN += (population.individualList[i].selectionNumber % 1)
    return round(sumN)

# Input args:
#   Population
# output args:
#   List(selectedIndividuals)
# Description: 
#   Returns a List with selected invididuals for the next generation. Also every
#   fifth generation add the fittest Individual from the multiPopulation to the
#   list
def matingPool(mP, population):
    population.individualList.sort(key=lambda x: x.selectionNumber, reverse=True)
    L = []
    selectionNum = numberOfSelectionIndividualsForPopulation(population)
    for i in range(0,selectionNum):
        L.append(population.individualList[i])
    if not(mP.numberOfGenerations % 7):
        L.append(copy.deepcopy(mP.fittestIndividual))
    return L