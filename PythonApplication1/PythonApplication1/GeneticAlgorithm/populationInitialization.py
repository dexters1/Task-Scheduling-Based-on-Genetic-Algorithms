import sys
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from GeneticAlgorithm.GeneticAlgorithmClasses import *
from GeneticAlgorithm.GeneticAlgorithmFunctions import *
import copy

def createIndividual(makeGraphSent):
    individual = makeGraphSent()
    for vertex in individual.V:
        vertex.processor = random.choice(individual.P.processorList)
    priorityDefinition(individual)
    updateProcessorInfo(individual)
    totalTime(individual)
    individual.cost = totalCost(individual.P)
    return individual

def initialPopulation(popSize, G):
    population = Population([])
    for i in range(0, popSize):
        population.individualList.append(createIndividual(G))
    updatePopulationInfo(population)
    population.fittestIndividual = population.individualList[0]
    return population

def initialMultiPopulation(multiPopSize, popSize, G):
    multiPopulation = MultiPopulation([])
    for i in range(0,multiPopSize):
        multiPopulation.populationList.append(initialPopulation(popSize, G))
    multiPopulation.fittestIndividual = multiPopulation.populationList[0].individualList[0]
    multiPopulation.fittestIndividual.fitness = fitnessFunction(multiPopulation.populationList[0], multiPopulation.populationList[0].individualList[0])
    return multiPopulation
