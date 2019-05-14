import sys
from Graph.GraphPreprocessing import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from GeneticAlgorithm.populationInitialization import *

if __name__ == "__main__":
#   drawAllGraphs(9)
   G = makeGraph7()
   mP = initialMultiPopulation(2, 10, G)
   drawGraph(mP[0][0], "multiPopulationTest/mp0-0")
   drawGraph(mP[0][1], "multiPopulationTest/mp0-1")
   drawGraph(mP[1][0], "multiPopulationTest/mp1-0")
