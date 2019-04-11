import sys
from math import exp
from Processor.ProcessorClass import *
from Graph.DrawGraph import *

# ToDo:
# - Ceil-uj na vise
# - Sredi unit testing za ProcessorFunctions
# - https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

vmBasePrice = 0.0475
vmBaseSpeed = 1.0

# Input args:
#   Graph, Vertex
# output args:
#   int
# Description: 
#   Calculates the start time of processing of a task. It determines the time 
#   when all the predecessor tasks it depends on have been finished and the 
#   time it can start on it's assigned processor and returns the maximum value
# Issues:
#   - No error handling if input isn't correct
def startTime(G, vertex):
    return max(availableProcessorForTask(G, vertex),max(predecessorTime(G, vertex)))

# Input args:
#   Graph, Vertex
# output args:
#   List of int
# Description: 
#   Calculates the finish time + communicationCost of all immediate predecessors
#   of a vertex and appends it to the output list. In case there are no 
#   predecessors returns a list with 0.
# Issues:
#   - No error handling if input isn't correct
def predecessorTime(G, vertex):
    if (len(vertex.predecessors) == 0):
        return [0]
    L = []
    inDegree = getInDegrees(G, vertex)
    for pred in inDegree:
        L.append((finishTime(G, pred) + communicationCost(G, pred, vertex)))
    return L

# Input args:
#   Graph, Vertex
# output args:
#   int
# Description: 
#   Calculates the finish time of a task by summing it's start time and
#   estimated time of completion 
# Issues:
#   - No error handling if input isn't correct
def finishTime(G, vertex):
    return startTime(G, vertex) + calculateETC(vertex.weight, vertex.processor)

# Input args:
#   Int, Int
# output args:
#   int?
# Description: 
#   Calculates the estimated time of completion for a task
# Issues:
#   - Treba videti da li treba broj zaokruziti navise sa ceil-om
def calculateETC(time, processor):
    return time//processor.capacity 

# Input args:
#   Graph, Vertex, Vertex
# output args:
#   int
# Description: 
#   Calculates the communication cost between tasks. If the tasks are on the 
#   same processor returns 0, if not returns the weight of their edge
# Issues:
#   - No error hadling if input isn't correct. vertex1 has to be the
#   outgoing edge and vertex2 has to be on the input side of the edge
def communicationCost(G, vertex1, vertex2):
    if (vertex1.processor == vertex2.processor):
        return 0
    for edge in G.E:
        if edge.first == vertex1 and edge.second == vertex2:
            return edge.weight
    exit(1)

# Input args:
#   Graph, Vertex
# output args:
#   int
# Description: 
#   Calculates the finish time of the last task allocated to the processor
#   before the task in the function call
# Issues:
#   - No error hadling if input isn't correct
def availableProcessorForTask(G, vertex):
    n = 0
    for iter in vertex.processor.taskList:
        if iter == vertex:
            return n
        n = finishTime(G, iter)
    return n

# Input args:
#   Graph
# output args:
#   No output args
# Description: 
#   Updates the startTime for all the vertexes in the graph
def updateStartTime(G):
    for vertex in G.V:
        vertex.startTime = startTime(G,vertex)

# Input args:
#   Graph
# output args:
#   No output args
# Description: 
#   Updates the finishTime for all the vertexes in the graph
def updateFinishTime(G):
    for vertex in G.V:
        vertex.finishTime = finishTime(G,vertex)

# Input args:
#   Processor
# output args:
#   No output args
# Description: 
#   Calculates the cost of the virtual machine per unit of time
def vmCost(processor):
    return vmBase*exp(processor.capacity/vmBaseSpeed)

#def cost(processor):
#    n = 0
#    for task in len(processor.taskList):
#        n += vmCost(processor)*calculateETC()

