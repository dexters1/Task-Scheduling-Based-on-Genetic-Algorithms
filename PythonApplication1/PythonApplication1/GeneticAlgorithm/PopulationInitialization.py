import sys
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from GeneticAlgorithm.GeneticAlgorithmClasses import *
from GeneticAlgorithm.GeneticAlgorithmFunctions import *
import copy

# Input args:
#   function(makeGraph)
# output args:
#   Graph(individual)
# Description: 
#   Makes a Graph(individual) from the makeGraph function and randomizes it's
#   processsors and recalculates priority, processorInfo, totalTime anc cost then
#   returns the Graph(individual) as output
def createIndividual(makeGraphSent):
    individual = makeGraphSent()
    for vertex in individual.V:
        vertex.processor = random.choice(individual.P.processorList)
    priorityDefinition(individual)
    updateProcessorInfo(individual)
    totalTime(individual)
    individual.cost = totalCost(individual.P)
    return individual

# Input args:
#   int(populationSize), function(makeGraph)
# output args:
#   Population
# Description: 
#   Makes an initial population with random processor assignment for individuals
#   (Graphs) 
def initialPopulation(popSize, makeGraphSent):
    population = Population([])
    for i in range(0, popSize):
        population.individualList.append(createIndividual(makeGraphSent))
    updatePopulationInfo(population)
    population.fittestIndividual = population.individualList[0]
    return population

# Input args:
#   int(multiPopulationSize), int(populationSize), function(makeGraph)
# output args:
#   MultiPopulation
# Description: 
#   Makes an initial MultiPopulation with random processor assignment for individuals (Graphs) 
#   in all populations
def initialMultiPopulation(multiPopSize, popSize, makeGraphSent):
    multiPopulation = MultiPopulation([])
    for i in range(0,multiPopSize):
        multiPopulation.populationList.append(initialPopulation(popSize, makeGraphSent))
    multiPopulation.fittestIndividual = multiPopulation.populationList[0].individualList[0]
    multiPopulation.fittestIndividual.fitness = fitnessFunction(multiPopulation.populationList[0], multiPopulation.populationList[0].individualList[0])
    return multiPopulation
