import sys
import os

sys.path.insert(0, os.getcwd())

from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariationsTest import *
import unittest

class TestGraphPreprocessing(unittest.TestCase):

    #Prolog: -> doc: slika 1
    #Epilog: -> doc: slika 1-simplified
    #      Vertex v1 se sjedinjuje sa vertexom v2 pod nazivom vertexa v2
     def testPreprocessingGraph1(self):
         G = makeGraph1()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v2'])
         self.assertEqual([x.first.val for x in G.E], [])
         self.assertEqual([x.second.val for x in G.E], [])
     
    #Prolog: -> doc: slika 2
    #Epilog: -> doc: slika 2-simplified
    #      Vertexi ostaju isti kao i pre poziva funkcije simplifyGraph()
     def testPreprocessingGraph2(self):
         G = makeGraph2()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v1','v2','v3','v4'])
         self.assertEqual([x.first.val for x in G.E], ['v1','v1','v1'])
         self.assertEqual([x.second.val for x in G.E], ['v2','v3','v4'])
    
    #Prolog: -> doc: slika 3
    #Epilog: -> doc: slika 3-simplified
    #      Vertex v4 se sjedinjuje sa vertexom v5 pod nazivom vertexa v5
     def testPreprocessingGraph3(self):
         G = makeGraph3()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v1','v2','v3','v5', 'v6', 'v7', 'v8'])
         self.assertEqual([x.first.val for x in G.E], ['v5','v5','v5','v1','v2','v3'])
         self.assertEqual([x.second.val for x in G.E], ['v6','v7','v8','v5','v5','v5'])
    
    #Prolog: -> doc: slika 4
    #Epilog: -> doc: slika 4-simplified
    #      Vertexi ostaju isti kao i pre poziva funkcije simplifyGraph()
     def testPreprocessingGraph4(self):
         G = makeGraph4()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v1','v2','v3','v4','v5'])
         self.assertEqual([x.first.val for x in G.E], ['v1','v1','v1','v2','v3','v4'])
         self.assertEqual([x.second.val for x in G.E], ['v2','v3','v4','v5','v5','v5'])
  
    #Prolog: -> doc: slika 5
    #Epilog: -> doc: slika 5-simplified
    #      Vertex v2 se sjedinjuje sa vertexom v5 pod nazivom vertexa v5,
    #      Vertex v3 se sjedinjuje sa vertexom v6 pod nazivom vertexa v6,
    #      Vertex v4 se sjedinjuje sa vertexom v7 pod nazivom vertexa v7,
    #      Vertexi v8 i v9 se sjedinjuju sa vertexom v10 pod nazivom vertexa v10
     def testPreprocessingGraph5(self):
         G = makeGraph5()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v1','v5','v6','v7','v10'])
         self.assertEqual([x.first.val for x in G.E], ['v1','v1','v1','v5','v6','v7'])
         self.assertEqual([x.second.val for x in G.E], ['v5','v6','v7','v10','v10','v10'])

    #Prolog: -> doc: slika 6
    #Epilog: -> doc: slika 6-simplified
    #      Nema promene
     def testPreprocessingGraph6(self):
         G = makeGraph6()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12'])

    #Prolog: -> doc: slika 7
    #Epilog: -> doc: slika 7-simplified
    #      Vertex v3 se sjedinjuje sa vertexom v7 pod nazivom vertexa v7
     def testPreprocessingGraph7(self):
         G = makeGraph7()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v1','v2','v4','v5','v6','v7','v8','v9','v10'])
         self.assertEqual([x.first.val for x in G.E], ['v1','v1','v1','v1','v2','v2','v4','v4','v5','v6','v7','v8','v9','v1'])
         self.assertEqual([x.second.val for x in G.E], ['v2','v4','v5','v6','v8','v9','v8','v9','v9','v8','v10','v10','v10','v7'])

    #Prolog: -> doc: slika 8
    #Epilog: -> doc: slika 8-simplified
    #      Vertex v1 se sjedinjuje sa vertexom v5 pod nazivom vertexa v5,
    #      Vertex v2 se sjedinjuje sa vertexom v6 pod nazivom vertexa v6,
    #      Vertex v3 se sjedinjuje sa vertexom v7 pod nazivom vertexa v7,
    #      Vertex v4 se sjedinjuje sa vertexom v8 pod nazivom vertexa v8,
    #      Vertex v10 se sjedinjuje sa vertexom v14 pod nazivom vertexa v14,
    #      Vertex v11 se sjedinjuje sa vertexom v15 pod nazivom vertexa v15,
    #      Vertex v12 se sjedinjuje sa vertexom v16 pod nazivom vertexa v16,
    #      Vertex v13 se sjedinjuje sa vertexom v17 pod nazivom vertexa v17
     def testPreprocessingGraph8(self):
         G = makeGraph8()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v5','v6','v7','v8','v9','v14','v15','v16','v17','v18'])
         self.assertEqual([x.first.val for x in G.E], ['v5','v6','v7','v8','v14','v15','v16','v17','v9','v9','v9','v9'])
         self.assertEqual([x.second.val for x in G.E], ['v9','v9','v9','v9','v18','v18','v18','v18','v14','v15','v16','v17'])

    #Prolog: -> doc: slika 9
    #Epilog: -> doc: slika 9-simplified
    #      Vertex v11 se sjedinjuje sa vertexom v12 pod nazivom vertexa v12,
    #      Vertexi v17, v18 i v19 se sjedinjuju sa vertexom v20 pod nazivom vertexa v20
     def testPreprocessingGraph9(self):
         G = makeGraph9()
         simplifyGraph(G)
         self.assertEqual([x.val for x in G.V], ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v12','v13','v14','v15','v16','v20'])
         self.assertEqual([x.first.val for x in G.E], ['v1','v1','v2','v2','v3','v3','v4','v4', 'v5', 'v7', 'v8', 'v10','v12','v12','v12','v12','v5', 'v6', 'v7', 'v8', 'v9','v10','v13', 'v14', 'v15','v16'])
         self.assertEqual([x.second.val for x in G.E],['v5','v6','v6','v7','v8','v9','v9','v10','v13','v14','v15','v16','v13','v14','v15','v16','v12','v12','v12','v12','v12','v12','v20', 'v20', 'v20','v20'])

if __name__ == "__main__":
    unittest.main()
    input("press close to exit")