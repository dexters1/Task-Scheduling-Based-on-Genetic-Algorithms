import sys
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from GeneticAlgorithm.GeneticAlgorithmClasses import *

def updatePopulationInfo(population):
    for individual in population.individualList:
        if individual.totalTime < population.minTime:
            population.minTime = individual.totalTime
        if individual.totalTime > population.maxTime:
            population.maxTime = individual.totalTime
        if individual.cost < population.minCost:
            population.minCost = individual.cost
        if individual.cost > population.maxCost:
            population.maxCost = individual.cost

def fitnessFunction(population, individual):
    fitness = Omega*((population.maxTime - individual.totalTime)/(population.maxTime - population.minTime)) + (1 - Omega)*((population.maxCost - individual.cost)/(population.maxCost - population.minCost))
    individual.fitness = fitness
    return fitness

def updateFitness(mP):
    for population in mP:
        for individual in population.individualList:
            fitnessFunction(population, individual)
        population.fitnessSum = 0
        for individual in population.individualList:
            population.fitnessSum += individual.fitness
        population.fitnessAverage = population.fitnessSum/NIND

def updateSelectionNumber(mP):
    for population in mP:
        for individual in population.individualList:
            individual.selectionNumber = NIND*(individual.fitness/population.fitnessSum)


