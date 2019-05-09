import sys
import os

sys.path.insert(0, os.getcwd())

from Graph.MakeGraphVariations import *
from Graph.DrawGraph import *
import unittest

class TestPriorityDefinition(unittest.TestCase):
    def testPriorityDefinition(self):
        G = makeGraphTest()
        # Testirano racunanje prioriteta za graf sa slike u test-output folderu,
        # pod nazivom slike testPriorityDefinition.gv.pdf. Takodje testirano i
        # odredjivanje dubine vertexa grafa
        drawGraph(G, "testPriorityDefinition.gv")
        self.assertEqual([vertex.priority for vertex in G.V], [114, 126, 115, 114, 102, 94, 171, 105, 57, 36])
        self.assertEqual([vertex.depth for vertex in G.V], [0, 1, 1, 1, 1, 1, 2, 2, 2, 3])



if __name__ == "__main__":
    unittest.main()
    input("press close to exit")