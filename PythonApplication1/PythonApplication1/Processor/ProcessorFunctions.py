import sys
from math import exp
from math import ceil
from Processor.ProcessorClass import *
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *

# ToDo:
# - Sredi unit testing za ProcessorFunctions

vmBasePrice = 0.1 
#0.0475
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
    return ceil(max(availableProcessorForTask(G, vertex),max(predecessorTime(G, vertex))))

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
    for pred in vertex.predecessors:
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
    if vertex.startTime == None:
        return startTime(G, vertex) + calculateETC(vertex.weight, vertex.processor)
    return vertex.startTime + calculateETC(vertex.weight, vertex.processor)

# Input args:
#   Int, Int
# output args:
#   int?
# Description: 
#   Calculates the estimated time of completion for a task
# Issues:
#   - Treba videti da li treba broj zaokruziti navise sa ceil-om
def calculateETC(time, processor):
    return ceil(time/processor.capacity) 

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
        if not (isinstance(iter, Slot)): #if not idle time
            #n = finishTime(G, iter)
            if iter.finishTime == None:
                n = finishTime(G, iter)
            else:
                n = iter.finishTime
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
    return vmBasePrice*exp(processor.capacity/vmBaseSpeed)

# Input args:
#   Processor
# output args:
#   No output args
# Description: 
#   Adds an element of type slot in processor.taskList to denote processor 
#   idle-time if no tasks are being processed
def addSlot(G):
    for processor in G.P.processorList:
        for i in range(0,len(processor.taskList)-1):
            if processor.taskList[i].finishTime != processor.taskList[i+1].startTime:
                processor.taskList.insert(i+1,Slot(processor.taskList[i].finishTime,processor.taskList[i+1].startTime))

# Input args:
#   Processor, Vertex
# output args:
#   No output args
# Description: 
#   Calculates the total cost of task execution on processor. In case of idle
#   time it just multiplies the price per unit of time with the idle time
def cost(processor, vertex):
    if not isinstance(vertex,Slot):
        return vmCost(processor)*calculateETC(vertex.weight, processor)
    return vmCost(processor)*(vertex.finishTime - vertex.startTime)

# Input args:
#   ProcessorList
# output args:
#   double
# Description: 
#   Calculates the total cost of task execution on processor. In case of idle
#   time it just multiplies the price per unit of time with the idle time
def totalCost(processorList):
    n = 0.0
    for processor in processorList.processorList:
        for task in processor.taskList:
            n += cost(processor,task)
    return n 

# Input args:
#   Graph
# output args:
#   No output args
# Description: 
#    Updates process taskList after Graph has been sorted by priority
def updateProcessorTaskList(G):
    for process in G.P.processorList:
        process.taskList = []
    for vertex in G.V:
        vertex.processor.taskList.append(vertex)