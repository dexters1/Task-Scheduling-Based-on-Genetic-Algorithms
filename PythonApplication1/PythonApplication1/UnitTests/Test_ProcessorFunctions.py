import sys
import os

sys.path.insert(0, os.getcwd())

from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from Processor.ProcessorFunctions import *
from Graph.DrawGraph import *
from math import ceil
import unittest

class TestProcessorFunctions(unittest.TestCase):
    def testGraphAfterProcessingFunctions1(self):
        G = makeGraph1()
        self.assertEqual(ceil(totalCost(G.P)), 9)
        self.assertEqual([x.startTime for x in G.V], [0, 37])
        self.assertEqual([x.finishTime for x in G.V], [10,44.5])
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ["v1"])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ["NoCostSlot","v2"])

    def testGraphAfterProcessingFunctions7(self):
        G = makeGraph7()
        drawGraph(G, "testGraphAfterProcessingFunctions7.gv")
        # Testiramo da li graf 7 ima dobro izracunatu totalnu cenu, vreme
        # pocetka i kraja obrade svih vertexa i da li je dobra raspodela
        # taskova po procesorima. Raspored taskova je prethodno odredjen 
        # sortiranjem pomocu prioriteta taskova u odnosu na dubinu.
        # Slika grafa 7 na kojim je vrsena analiza se nalazi u test-output
        # folderu pod imenom testGraphAfterProcessingFunctions7.gv.pdf
        self.assertEqual(ceil(totalCost(G.P)), 179)
        self.assertEqual([x.startTime for x in G.V], [0, 15.5, 6.5, 15, 17.5, 22, 42.5, 43.5, 45, 73])
        self.assertEqual([x.finishTime for x in G.V],[6.5, 18.5, 15.0, 22.0, 29.5, 28.5, 51.0, 46.833333333333336, 56.0, 78.0])
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ["NoCostSlot", "v5", "Slot", "v7"])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ["v1", "v2", "v3", "v6", "Slot", "v9"])
        self.assertEqual([processor.val for processor in G.P.processorList[2].taskList], ["NoCostSlot", "v4", "Slot", "v8", "Slot", "v10"])


    def testGraphAfterProcessingFunctions6(self):
        G = makeGraph6()
        drawGraph(G, "testGraphAfterProcessingFunctions6.gv")
        # Testiramo da li graf 6 ima dobro izracunatu totalnu cenu, vreme
        # pocetka i kraja obrade svih vertexa i da li je dobra raspodela
        # taskova po procesorima. Raspored taskova je prethodno odredjen 
        # sortiranjem pomocu prioriteta taskova u odnosu na dubinu.
        # Slika grafa 6 na kojim je vrsena analiza se nalazi u test-output
        # folderu pod imenom testGraphAfterProcessingFunctions6.gv.pdf
        self.assertEqual(ceil(totalCost(G.P)), 300)
        self.assertEqual([x.startTime for x in G.V], [0, 34, 24, 5, 87, 90.66666666666667, 57, 93, 98.66666666666667, 112.66666666666667, 126.66666666666667, 160.16666666666669])
        self.assertEqual([x.finishTime for x in G.V],[5.0, 57.0, 29.0, 15.5, 90.66666666666667, 93, 60, 98.66666666666667, 102.66666666666667, 119.16666666666667, 134.16666666666669, 171.16666666666669])
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ["NoCostSlot", "v3", "v6", "Slot", "v12"])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ["v1", "v5", "Slot", "v9", "Slot", "v11"])
        self.assertEqual([processor.val for processor in G.P.processorList[2].taskList], ["NoCostSlot", "v2", "Slot", "v4", "v8", "v7", "v10"])

if __name__ == "__main__":
    unittest.main()
    input("press close to exit")