import sys
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
import copy

def createIndividual(G):
    individual = copy.deepcopy(G)
    for vertex in individual.V:
        vertex.processor = random.choice(individual.P.processorList)
    updateProcessorInfo(individual)
    return individual

def initialPopulation(popSize, G):
    population = []
    for i in range(0, popSize):
        population.append(createIndividual(G))
    return population

def initialMultiPopulation(multiPopSize, popSize, G):
    multiPopulation = []
    for i in range(0,multiPopSize):
        multiPopulation.append(initialPopulation(popSize, G))
    return multiPopulation