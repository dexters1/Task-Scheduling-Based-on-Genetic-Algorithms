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
        print(totalCost(G.P))
        self.assertEqual(ceil(totalCost(G.P)), 9)
        self.assertEqual([x.startTime for x in G.V], [0, 32])
        self.assertEqual([x.finishTime for x in G.V], [5,47])
        self.assertEqual([processor.val for processor in G.P.processorList[0].taskList], ["v1"])
        self.assertEqual([processor.val for processor in G.P.processorList[1].taskList], ["v2"])


if __name__ == "__main__":
    unittest.main()
    input("press close to exit")