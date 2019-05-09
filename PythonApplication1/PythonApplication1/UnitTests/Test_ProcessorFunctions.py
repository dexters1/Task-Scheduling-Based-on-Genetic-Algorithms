import sys
import os

sys.path.insert(0, os.getcwd())

from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from Processor.ProcessorFunctions import *
from math import ceil
import unittest

class TestProcessorFunctions(unittest.TestCase):
    def testGraphAfterProcessingFunctions1(self):
        G = makeGraph1()
        self.assertEqual(ceil(totalCost(G.P)), 9)
        self.assertEqual([x.startTime for x in G.V], [0, 37])
        self.assertEqual([x.finishTime for x in G.V], [10,45])
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ["v1"])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ["v2"])

    def testGraphAfterProcessingFunctions7(self):
        G = makeGraph7()
        self.assertEqual(ceil(totalCost(G.P)), 176)
        self.assertEqual([x.startTime for x in G.V], [0, 16, 7, 16, 18, 23, 43, 45, 46, 74])
        self.assertEqual([x.finishTime for x in G.V],[7, 19, 16, 23, 30, 30, 52, 49, 57, 79])
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ["v5", "Slot", "v7"])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ["v1", "v2", "v3", "v6", "Slot", "v9"])
        self.assertEqual([processor.val for processor in G.P.processorList[2].taskList], ["v4", "Slot", "v8", "Slot", "v10"])

if __name__ == "__main__":
    unittest.main()
    input("press close to exit")