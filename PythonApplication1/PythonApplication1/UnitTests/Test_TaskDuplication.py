import sys
import os

sys.path.insert(0, os.getcwd())

from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from Processor.ProcessorFunctions import *
from Graph.DrawGraph import *
from TaskDuplication.TaskDuplicationFunctions import *
from PythonApplication1 import *
import unittest

class TestTaskDuplication(unittest.TestCase):
    def testTaskDuplication(self):
       G = makeGraphDuplicateTest()
       taskDuplication(G)
       self.assertEqual(ceil(totalCost(G.P)), 39)
       self.assertEqual([x.startTime for x in G.V], [0, 14, 27, 40, 51, 64, 56, 76, 94, 101, 76])
       self.assertEqual([round(x.finishTime) for x in G.V],[14, 27, 40, 51, 64, 76, 76, 94, 101, 106, 92])
       self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ['v1', 'v6', 'v2', 'v3', 'v4', 'v5', 'v9', 'v7', 'v8'])
       self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], [])
       self.assertEqual([processor.val for processor in G.P.processorList[2].taskList], ['NoCostSlot', 'v9.3', 'v10'])
       drawGraph(G, "testDuplication/DuplicateTest")


    def testTaskDuplication3(self):
        G = makeGraph3()
        drawGraph(G,"testDuplication/beforeDuplicationGraph3")
        taskDuplication(G)
        drawGraph(G,"testDuplication/afterDuplicationGraph3")
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ['v1', 'v2.1', 'Slot', 'v4', 'v5.1', 'v6'])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ['v3', 'v2', 'Slot', 'v4.2', 'v5.2', 'v7'])
        self.assertEqual([processor.val for processor in G.P.processorList[2].taskList], ['NoCostSlot', 'v4.3', 'v5', 'v8'])

    def testTaskDuplicationAfterGA(self):
        #Ako se ukljuci predprocessiranje pre GA ne dolazi do dupliciranja taska jer nije korisno
        #Duplicirani taskovi dobijaju svoju ocenu prioriteta i sortiraju se po tome u raspored 
        #sto nekad izaziva da graf traje duze i da bude skuplji ( ti slucajevi se ne uzimaju kao koristni )
        #mislim da treba videti sto se tice te raspodele tasko mislim da nesto potencijalno nisam dobro razumeo
        #ili uradio i da to pravi sitne probleme sa algoritmom. 
        #
        #Also ne racunam u cenu kada se zavrsi poslednja obrada podataka na procesoru i on salje edge-om podatke
        #nekom drugom  vertexu!!!!!!!! Nisam 100% siguran da li je to dobro
        G = makeGraphGA()
        drawGraph(G, "testDuplication/MakeGraphGA")
        mP = initialMultiPopulation(mPN, NIND, makeGraphGA)

        updateFitness(mP)
        updateSelectionNumber(mP)
        print(mP.fittestIndividual.fitness)

        noChange = 0
        for i in range(0, 100):
            lastCost = copy.deepcopy(mP.fittestIndividual.cost)
            fittestGraph = newGeneration(mP)
            if fittestGraph.cost == lastCost:
                noChange = noChange + 1
            else:
                noChange = 0
            if noChange >= 10:
                print("No change for 10 generations")
                break

        drawGraph(mP.fittestIndividual, "testDuplication/FittestIndividualBeforeTaskDuplication")
        print(totalCost(mP.fittestIndividual.P))
        taskDuplication(mP.fittestIndividual)
        print(totalCost(mP.fittestIndividual.P))
        drawGraph(mP.fittestIndividual, "testDuplication/FittestIndividualAfterDuplication")

        self.assertEqual([processor.val for processor in mP.fittestIndividual.P.processorList[0].taskList], ['v1.1', 'v2', 'v3', 'v7'])
        self.assertEqual([processor.val for processor in mP.fittestIndividual.P.processorList[1].taskList], ['NoCostSlot', 'v9', 'v8', 'v10'])
        self.assertEqual([processor.val for processor in mP.fittestIndividual.P.processorList[2].taskList], ['v1', 'v4', 'v5', 'v6'])
        


if __name__ == "__main__":
    unittest.main()
    input("press close to exit")