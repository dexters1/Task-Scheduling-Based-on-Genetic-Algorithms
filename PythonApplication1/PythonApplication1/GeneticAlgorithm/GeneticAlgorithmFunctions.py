import sys
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from GeneticAlgorithm.GeneticAlgorithmClasses import *
import copy

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

def fitnessFunction(population, individual):
    fitness = Omega*((population.maxTime - individual.totalTime)/(population.maxTime - population.minTime)) + (1 - Omega)*((population.maxCost - individual.cost)/(population.maxCost - population.minCost))
    individual.fitness = fitness
    return fitness

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
            mP.fittestIndividual = population.fittestIndividual #skinuo sam odavde deep copy

def updateSelectionNumber(mP):
    for population in mP.populationList:
        for individual in population.individualList:
            individual.selectionNumber = NIND*(individual.fitness/population.fitnessSum)

def numberOfSelectionIndividualsForPopulation(population):
    sumN = 0
    for i in range(0, len(population.individualList)):
        if(population.individualList[i].selectionNumber < 1):
            sumN += population.individualList[i].selectionNumber
        else:
            sumN += (population.individualList[i].selectionNumber % 1)
    return round(sumN)

def matingPool(population):
    population.individualList.sort(key=lambda x: x.selectionNumber, reverse=True)
    L = []
    selectionNum = numberOfSelectionIndividualsForPopulation(population)
    for i in range(0,selectionNum):
        L.append(population.individualList[i])
    return L






