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
    return population

def initialMultiPopulation(multiPopSize, popSize, G):
    multiPopulation = []
    for i in range(0,multiPopSize):
        multiPopulation.append(initialPopulation(popSize, G))
    return multiPopulation
