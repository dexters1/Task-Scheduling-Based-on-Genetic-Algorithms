import sys
from math import exp
from math import ceil
from Processor.ProcessorClass import *
from Graph.GraphPreprocessing import *
from Graph.MakeGraphVariations import *
from Graph.PriorityDefinition import getWeight

from os import path


vmBasePrice = 0.1 
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
    if vertex.startTime == None:
        return max(availableProcessorForTask(G, vertex),max(predecessorTime(G, vertex)))
    else:
        return vertex.startTime


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
    if vertex.finishTime == None:
        return startTime(G, vertex) + calculateRealETC(vertex, vertex.processor)
    else:
        return vertex.finishTime

# Input args:
#   Int, Int
# output args:
#   double
# Description: 
#   Calculates the estimated time of completion for a task
def calculateETC(time, processor):
    return time/processor.capacity 

# Input args:
#   Int, Int
# output args:
#   int
# Description: 
#   Calculates the estimated time of completion for a task using ETC table.
#   First it checks if the main module is a processor function test module so 
#   it calls a different realization of the function. If it's not a processor
#   function test module and the task is not preprocessed task then it lookups
#   the value from the ETC table by transforming
#   task and processor names into numbers. ( For example: V1 transforms into row 1 and 
#   P2 transforms into columnn 2 for the lookup table ) if the vertex is a duplicated vertex
#   it has a name that denotes the task number and the processor it's been duplicated on
#   For example ( V1.2 - means task V1 has been duplicated for processor 2 ) so we need to
#   split it's string name to the . and make it's name from V1.2 for example to V1 and then
#   we lookup the ETC table as previously stated.
#   If the task was preprocessed we calcualte ETC like in the previous formula, but we have
#   to sum and calculate ETC for both of the vertecies that comprise a preprocessed graph
#   ( a preprocessed graph has another vertex appended to it )
def calculateRealETC(vertex, processor):
    pathStr = path.abspath(sys.modules['__main__'].__file__)
    if pathStr[-26::] == "Test_ProcessorFunctions.py":
        return calculateETC(vertex.weight, processor)
    if vertex.preprocessed == True:
        ETCvalue = 0
        for val in vertex.appendedVertexList:
            ETCvalue = ETCvalue + ETC[((round(float(val[1::])-1))*3 + round(float(val[1::]))-1)]
        return ETCvalue
    vertexVal = vertex.val.split('.')[0]
    return(ETC[((round(float(vertexVal[1::])-1))*3 + round(float(processor.val[1::]))-1)])

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
# Issues:
#   processor.capacity needs to be defined with VmBaseSpeed in mind
def vmCost(vertex, processor):
    return vmBasePrice*exp(processor.capacity)



# Input args:
#   Processor
# output args:
#   No output args
# Description: 
#   Adds an element of type slot in processor.taskList to denote processor 
#   idle-time if no tasks are being processed
def addSlot(G):
    for processor in G.P.processorList:
        L = processor.taskList[:] #pravim kopiju liste da mogu da je menjam
        c = 1 #iterator broja dodatih slotova da kopija prati original
        for i in range(0,len(L)-1):
            if L[i].finishTime != L[i+1].startTime:
                processor.taskList.insert(i+c,Slot(L[i].finishTime,L[i+1].startTime))
                c = c + 1
        addNoCostSlot(processor)

# Input args:
#   Processor
# output args:
#   No output args
# Description: 
#   Adds an element of type slot with no cost if the start time of
#   processor.taskList isn't 0 to denote free processor space which
#   isn't charged, needed for duplication of tasks
def addNoCostSlot(processor):
    if len(processor.taskList) == 0:
        return
    if not (processor.taskList[0].startTime == 0):
        processor.taskList.insert(0, Slot(0, processor.taskList[0].startTime, noCost=True, val="NoCostSlot"))

# Input args:
#   Processor, Vertex
# output args:
#   No output args
# Description: 
#   Calculates the total cost of task execution on processor. In case of idle
#   time it just multiplies the price per unit of time with the idle time
def cost(processor, vertex):
    if not isinstance(vertex,Slot):
        return vmCost(vertex, processor)*calculateRealETC(vertex, processor)
    if vertex.noCost == True:
        return 0
    return vmCost(vertex, processor)*(vertex.finishTime - vertex.startTime)

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

# Input args:
#   Graph
# output args:
#   No output args
# Description: 
#    Updates all necessary info for Processor if changes are made to vertex
#    processor assignment
def updateProcessorInfo(G):
    setTimeToNone(G)
    updateProcessorTaskList(G)
    updateStartTime(G)
    updateFinishTime(G)
    addSlot(G)
    addLastWeightCost(G)

# Input args:
#   Graph
# output args:
#   No output args
# Description: 
#    Adds a Slot to processor after the last task in taskList with duration of max successor
#    weight of the last task 
def addLastWeightCost(G):
    for processor in G.P.processorList:
        if len(processor.taskList) > 0:
            if not isinstance(processor.taskList[-1], Slot):        
                finishTime = processor.taskList[-1].startTime + getHighestEdgeWeight(G, processor.taskList[-1])
                if finishTime == processor.taskList[-1].startTime:
                    continue
                processor.taskList.append(Slot(processor.taskList[-1].startTime, finishTime))
            else:
                print("Before: ")
                print(processor.taskList[-1].val)
                del processor.taskList[-1]
                if isinstance(processor.taskList[-1], Slot):
                    exit(2) 
                print("After: ")
                print(processor.taskList[-1].val)
                finishTime = processor.taskList[-1].startTime + getHighestEdgeWeight(G, processor.taskList[-1])
                if finishTime == processor.taskList[-1].startTime:
                    continue
                processor.taskList.append(Slot(processor.taskList[-1].startTime, finishTime))

# Input args:
#   Graph, Vertex(task)
# output args:
#   int
# Description: 
#    Returns max weight of all successor edges of task
def getHighestEdgeWeight(G, task):
    highestWeight = 0
    for edge in G.E:
        if edge.first == task:
            edgeWeight = getWeight(G, edge.first, edge.second)
            if highestWeight < edgeWeight:
                highestWeight = edgeWeight
    return highestWeight

# Input args:
#   Graph
# output args:
#   No output
# Description: 
#    Sets start and finish time of all vertecies inside a graph to None
def setTimeToNone(G):
    for vertex in G.V:
        vertex.startTime = None
        vertex.finishTime = None