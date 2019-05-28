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
        self.assertEqual(ceil(totalCost(G.P)), 155)
        self.assertEqual([x.startTime for x in G.V], [0, 6.5, 15.5, 17.5, 13.5, 22.0, 42.5, 43.5, 36.5, 64.5])
        self.assertEqual([round(x.finishTime) for x in G.V],[6, 14, 18, 30, 22, 28, 51, 47, 48, 70])
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ["NoCostSlot", "v5", "Slot", "v7"])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ["v1", "v3",  "v2", "v6", "Slot", "v9"])
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
        self.assertEqual(ceil(totalCost(G.P)), 295)
        self.assertEqual([round(x.startTime) for x in G.V], [0, 34, 5, 24, 87, 57, 91, 93, 99, 113, 127, 160])
        self.assertEqual([round(x.finishTime) for x in G.V],[5, 57, 16, 29, 91, 60, 93, 99, 103, 119, 134, 171])
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ["NoCostSlot", "v3", "v6", "Slot", "v12"])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ["v1", "v5", "Slot", "v9", "Slot", "v11"])
        self.assertEqual([processor.val for processor in G.P.processorList[2].taskList], ["NoCostSlot", "v2", "Slot", "v4", "v8", "v7", "v10"])

if __name__ == "__main__":
    unittest.main()
    input("press close to exit")