import sys
from Processor.ProcessorFunctions import*
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from GeneticAlgorithm.GeneticAlgorithmFunctions import *
import copy

#sorts both parents by vertex value and then crossesover and then updates the child
def crossoverOperation(parent1, parent2):
    child = copy.deepcopy(parent1)
    crossoverPoint = round(len(child.V)/2)

    vertexSortedByValChild = [x for x in child.V]
    vertexSortedByValChild.sort(key=lambda x: int(x.val[1::]), reverse=False)

    vertexSortedByValP2 = [x for x in parent2.V]
    vertexSortedByValP2.sort(key=lambda x: int(x.val[1::]), reverse=False)

    for i in range(0,crossoverPoint):
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
