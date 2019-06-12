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
       self.assertEqual(ceil(totalCost(G.P)), 41)
       self.assertEqual([x.startTime for x in G.V], [0, 14, 25, 34, 46, 65, 81, 94, 113, 110])
       self.assertEqual([round(x.finishTime) for x in G.V],[14, 25, 34, 46, 65, 81, 94, 113, 131, 129])
       self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ['v1', 'v2', 'v6', 'v3', 'v4', 'v5', 'v9', 'v7', 'v8'])
       self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], [])
       self.assertEqual([processor.val for processor in G.P.processorList[2].taskList], ['NoCostSlot', 'v10'])
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

        self.assertEqual([processor.val for processor in mP.fittestIndividual.P.processorList[0].taskList], [])
        self.assertEqual([processor.val for processor in mP.fittestIndividual.P.processorList[1].taskList], ['NoCostSlot', 'v7', 'v6', 'Slot', 'v8', 'v10'])
        self.assertEqual([processor.val for processor in mP.fittestIndividual.P.processorList[2].taskList], ['v1', 'v4', 'v2', 'v5', 'v9', 'Slot'])
        


if __name__ == "__main__":
    unittest.main()
    input("press close to exit")