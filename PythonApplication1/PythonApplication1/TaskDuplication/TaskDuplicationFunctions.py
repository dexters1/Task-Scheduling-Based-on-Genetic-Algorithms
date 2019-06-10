from GeneticAlgorithm.GeneticAlgorithmClasses import *
from Processor.ProcessorFunctions import *
from Graph.PriorityDefinition import getWeight
import copy
from math import pow

k = pow((Omega/(1 - Omega)),2)
maxPrice = 0

# Input:
#   Graph
# Output:
#   No output
# Description:
#   Goes through all tasks in processors in Graph.Processors and considers task duplication
#   when there is enough time in Slot for a predecessor of a task to be duplicated
#   onto another processor. taskDuplication only duplicates desirable tasks that meet criteria: 
#       1. totalTime of Graph will be improved
#       2. costCriteria is satisfied
#       3. there is enough time for taskDuplication
#   if the criteria is not met task won't be duplicated.
#   There is a loop of range (0,maximumDepthOfGraph) for duplication in case duplicated tasks
#   could also benefit from further duplication
def taskDuplication(G):
    maxPrice = G.cost
    for depth in range(0,G.V[-1].depth):
        for processor in G.P.processorList:
            taskIterator = -1
            taskListCopy = processor.taskList[:]
            for task in processor.taskList[:-1]:
                taskIterator = taskIterator + 1
                if isinstance(task, Slot):
                        vertex = taskListCopy[taskIterator+1]
                        vertexStartTime = vertex.startTime
                        vertexPredecessors = sortPredecessorsByArrivalTime(G, vertex)
                        for predecessor in vertexPredecessors:
                            if predecessor.processor == vertex.processor:
                                continue
                            timeOnNewProcessor = calculateRealETC(predecessor,processor)
                            finishTimeOnNewProcessor = startTimeOnNewProcessor(G, predecessor, processor) + timeOnNewProcessor
                            if (task.finishTime - task.startTime) >= timeOnNewProcessor and finishTimeOnNewProcessor < vertexStartTime:
                                print("duplication of: " + str(predecessor.val) + " on: " + str(vertex.val))
                                vertexStartTime = duplicateTask(G, predecessor, vertex)
                                task.finishTime = vertexStartTime
        updateGraph(G)

# Input:
#   Graph, Vertex
# Output:
#   List(predecessorsSortedByArrivalTime)
# Description:
#   Makes and returns a new list (L) in which it sorts predecessors of a vertex
#   by arrivalTime from latest arrivalTime to earliest
def sortPredecessorsByArrivalTime(G, vertex):
    L = []
    for predecessor in vertex.predecessors:
        predecessor.arrivalTime = predecessor.finishTime + getWeight(G, predecessor, vertex)
        L.append(predecessor)   
    L.sort(key=lambda x: x.arrivalTime, reverse=True)
    print ([x.arrivalTime for x in L])
    return L

# Input:
#   Graph, Vertex(taskToBeDuplicated), Vertex(successorOfTaskToBeDuplicated)
# Output:
#   int(finishTimeForSlot)
# Description:
#   Makes a deep copy of predecessor and assigns all relevant values from predecessor
#   to duplicatedTask, assigns new relevant edges for duplicatedTask and removes them
#   from predecessor. Checks if duplication meets all criteria of a desirable duplication
#   if not return Graph to previous state and return that there has been no change to 
#   slot finish time. If the duplication is desirable make permanent changes to the Graph
#   and calculate and return the latest start time of the duplicatedTask to signal that the
#   Slot finish time ends earlier now
def duplicateTask(G, predecessor, vertex):
    duplicatedTask = copy.deepcopy(predecessor)
    duplicatedTaskAssignment(G, duplicatedTask, vertex, predecessor)
    
    #Stores information about the state of Graph before duplication
    vertexCopyOfGraph = G.V[:]
    edgeCopyOfGraph = G.E[:]
    oldCost = totalCost(G.P)
    oldTime = totalTime(G)

    #Checks if the oldCost has higher value than the maxPrice of previous valid Graphs
    #if it does assign it as the new maxPrice
    global maxPrice
    if maxPrice < oldCost:
        maxPrice = oldCost

    predecessorCheck(G, duplicatedTask)

    #Duplicates relevant Edges of predecessor for duplicatedTask
    duplicateEdges(G, predecessor, vertex, duplicatedTask)
    #Removes all edges from predecessor.successors that are now
    #a part of the duplicatedTask
    for successor in predecessor.successors:
        if successor.processor == vertex.processor:
            removeEdge(G, predecessor, successor)

    G.V.append(duplicatedTask)
    updatePredecessors(G)
    updateSuccessors(G)

    if checkIfAllCriteriaIsSatisfied(G, duplicatedTask, edgeCopyOfGraph, vertexCopyOfGraph, oldCost, oldTime):
        return duplicatedTask.startTime
    else:
        return vertex.startTime
    

# Input:
#   Graph, Vertex(predecessor), Vertex(vertex), Vertex(duplicatedTask)
# Output:
#   No output
# Description:
#   Duplicates the edges for all predecessors for the duplicatedTask
#   checks to see if there are successors for the duplicatedTask that are
#   on the same processor if there are connect them to the new duplicatedTask
#   they will be disconnected from the original task in another function
def duplicateEdges(G, predecessor, vertex, duplicatedTask):
    for successor in predecessor.successors:
        if successor.processor == vertex.processor: 
            G.E.append(Edge(duplicatedTask, successor, getEdgeWeight(G,predecessor,successor)))
    for predecess in predecessor.predecessors:
        G.E.append(Edge(predecess, duplicatedTask, getEdgeWeight(G, predecess, predecessor)))

# Input:
#   Graph, Vertex, Processor
# Output:
#   int(startTimeOnNewProcessor)
# Description:
#   Calculates earliest startTime for vertex in case
#   the processor is changed
def startTimeOnNewProcessor(G, vertex, processor): 
    L = []
    copyProcessor = vertex.processor
    vertex.processor = processor
    for predecessor in vertex.predecessors:
        L.append(predecessor.finishTime + getWeight(G, predecessor, vertex))
    vertex.processor = copyProcessor
    if len(L) == 0:
        return 0
    return max(L)

# Input:
#   Graph, Vertex(duplicatedTasK)
# Output:
#   No output
# Description:
#   Checks to see if there is a predecessor that was already duplicated 
#   to the same processor and if there is it becomes the new predecessor
def predecessorCheck(G, duplicatedTask):
    for i in range(0, len(duplicatedTask.predecessors)):
        for vertex in G.V:
            split = vertex.val.split('.')[0]
            if duplicatedTask.predecessors[i].val == split:
                if vertex.processor == duplicatedTask.processor: 
                    duplicatedTask.predecessors[i] = vertex
                    print( "predecessor Check: "+ vertex.val)

# Input:
#   Graph, Vertex(duplicatedTasK), List(ofEdges), List(ofGraphVertices), 
#   double(oldCostOfGraph), double(oldTotalTimeOfGraph)
# Output:
#   Boolean
# Description:
#   Checks if arrivalTime on newProcessor is after duplicatedTask.startTime,
#   if there is an improvement in the totalTime and if the costCriteria is satisfied.
#   if any of the above are true return that criteriaIsNotSatisfied and restore Graph to 
#   pre-duplication state, else return that the duplication is worth it and that the
#   criteria is satisfied
def checkIfAllCriteriaIsSatisfied(G, duplicatedTask, edgeCopyOfGraph, vertexCopyOfGraph, oldCost, oldTime):
    arrivalTimeList = sortPredecessorsByArrivalTime(G, duplicatedTask)
    if len(arrivalTimeList) >= 1:
        arrivalTime = arrivalTimeList[0].arrivalTime
    else:
        arrivalTime = 0

    if arrivalTime > duplicatedTask.startTime:
        print("Task can't be duplicated due to arrivalTime being after latest startTime")
        G.E = edgeCopyOfGraph
        G.V = vertexCopyOfGraph
        updateGraph(G)
        return False

    updateGraph(G)
    newCost = totalCost(G.P)
    newTime = totalTime(G)

    #check for improvement in Time
    if not(newTime == oldTime):
        #costCriteria
        if not (-((newCost-oldCost)/(newTime - oldTime)) < k*maxPrice): #izgleda da nisam dobro razumeo formulu
            print("not worth it")
            G.E = edgeCopyOfGraph
            G.V = vertexCopyOfGraph
            updateGraph(G)
            return False
        if newCost > oldCost and newTime > oldTime:
            print("not worth it at all")
            G.E = edgeCopyOfGraph
            G.V = vertexCopyOfGraph
            updateGraph(G)
            return False
    else:
        print("Same time")
        G.E = edgeCopyOfGraph
        G.V = vertexCopyOfGraph
        updateGraph(G)
        return False

    return True

# Input:
#   Graph, Vertex(duplicatedTasK), Vertex(vertex), Vertex(predecessor)
# Output:
#   No output
# Description:
#   Assings necessary information to duplicatedTask from predecessor and vertex
def duplicatedTaskAssignment(G, duplicatedTask, vertex, predecessor):
    duplicatedTask.val = predecessor.val + "." + vertex.processor.val[1::]
    duplicatedTask.weight = predecessor.weight
    duplicatedTask.processor = vertex.processor

    duplicatedTask.predecessors = predecessor.predecessors
    successorList = []
    successorList.append(vertex)
    duplicatedTask.successors = successorList

    duplicatedTask.finishTime = vertex.startTime
    #define last possible startTime, true startTime will be defined later with ProcessorFunctions
    duplicatedTask.startTime = duplicatedTask.finishTime - calculateRealETC(predecessor, duplicatedTask.processor)