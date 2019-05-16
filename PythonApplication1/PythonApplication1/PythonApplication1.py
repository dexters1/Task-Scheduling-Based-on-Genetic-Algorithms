import sys
from Graph.GraphPreprocessing import *
from Graph.DrawGraph import *
from Processor.ProcessorFunctions import*
from GeneticAlgorithm.populationInitialization import *
from GeneticAlgorithm.GeneticOperations import *

if __name__ == "__main__":
#   drawAllGraphs(9)

    mP = initialMultiPopulation(mPN, NIND, makeGraph7)

    updateFitness(mP)
    updateSelectionNumber(mP)

    #print( [x.selectionNumber for x in matingPool(mP[0])])

   # for vertex in mP[0].individualList[0].V:
   #     print(vertex.val + " " + vertex.processor.val)

    #for vertex in mP[0].individualList[1].V:
    #    print(vertex.val + " " + vertex.processor.val)

    child = crossoverOperation(mP[0].individualList[0], mP[0].individualList[1])

    for processor in child.P.processorList:
        print(processor)

    for vertex in child.V:
        print(vertex.val + " " + str(vertex.processor.val))

  #  for vertex in child.V:
  #      print(vertex.val + " " + vertex.processor.val)

  #  verteciasd = [x.val for x in child.V]
  #  for x in verteciasd:
  #      print(int(x.val[1::]))
  #  verteciasd.sort(key=lambda x: int(x[1::]), reverse=True)
  #  print(verteciasd)
 #   for i in range(0, len(mP[0].individualList)):
 #       print(mP[0].individualList[i].fitness)
 #   print(mP[0].fitnessSum)


   # drawMpGraph(mP)

   
