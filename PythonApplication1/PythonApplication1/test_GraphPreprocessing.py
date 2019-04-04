import sys
from GraphPreprocessing import *
from MakeGraphVariations import *
import unittest

class TestGraphPreprocessing(unittest.TestCase):
     def test_preprocessingGraph1(self):
         G = make_graph1()
         SimplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['b'])
         self.assertEqual([x.first.val for x in G.E], [])
         self.assertEqual([x.second.val for x in G.E], [])
     def test_preprocessingGraph2(self):
         G = make_graph2()
         SimplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['a','b','c','d'])
         self.assertEqual([x.first.val for x in G.E], ['a','a','a'])
         self.assertEqual([x.second.val for x in G.E], ['b','c','d'])
     def test_preprocessingGraph3(self):
         G = make_graph3()
         SimplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['a','b','c','e', 'f', 'g', 'h'])
         self.assertEqual([x.first.val for x in G.E], ['e','e','e','a','b','c'])
         self.assertEqual([x.second.val for x in G.E], ['f','g','h','e','e','e'])
     def test_preprocessingGraph4(self):
         G = make_graph4()
         SimplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['a','b','c','d','e'])
         self.assertEqual([x.first.val for x in G.E], ['a','a','a','b','c','d'])
         self.assertEqual([x.second.val for x in G.E], ['b','c','d','e','e','e'])
     def test_preprocessingGraph5(self):
         G = make_graph5()
         SimplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['a','e','f','g','j'])
         self.assertEqual([x.first.val for x in G.E], ['a','a','a','e','f','g'])
         self.assertEqual([x.second.val for x in G.E], ['e','f','g','j','j','j'])
     def test_preprocessingGraph6(self):
         G = make_graph6()
         SimplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['b','c','e','f','g','h','i','j','k','l'])
         self.assertEqual([x.first.val for x in G.E], ['c','e','g','g','j','j','b','c','e'])
         self.assertEqual([x.second.val for x in G.E], ['f','h','i','j','k','l','g','g','g'])
     def test_preprocessingGraph7(self):
         G = make_graph7()
         SimplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['a','b','d','e','f','g','h','i','j'])
         self.assertEqual([x.first.val for x in G.E], ['a','a','a','a','b','b','d','d','e','f','g','h','i','a'])
         self.assertEqual([x.second.val for x in G.E], ['b','d','e','f','h','i','h','i','i','h','j','j','j','g'])

if __name__ == "__main__":
    unittest.main()
    input("press close to exit")