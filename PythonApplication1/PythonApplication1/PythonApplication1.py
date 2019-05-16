import sys
from Graph.GraphPreprocessing import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from GeneticAlgorithm.populationInitialization import *

if __name__ == "__main__":
#   drawAllGraphs(9)

    mP = initialMultiPopulation(mPN, NIND, makeGraph7)

    updateFitness(mP)
    updateSelectionNumber(mP)


 #   drawMpGraph(mP)

   
