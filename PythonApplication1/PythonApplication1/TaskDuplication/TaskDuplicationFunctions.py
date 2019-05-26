from GeneticAlgorithm.GeneticAlgorithmClasses import *
from Processor.ProcessorFunctions import *
from Graph.PriorityDefinition import getWeight
import copy
from math import pow

k = pow((Omega/(1 - Omega)),2)
maxPrice = 0

def taskDuplication(G):
    for depth in range(0,G.V[-1].depth):
        for processor in G.P.processorList:
            taskIterator = -1
            taskListCopy = processor.taskList[:]
            for task in processor.taskList:
                taskIterator = taskIterator + 1
                if isinstance(task, Slot):
                        vertex = taskListCopy[taskIterator+1] #pazi na ovo sranje
                        vertexStartTime = vertex.startTime
                        vertexPredecessors = sortPredecessorsByArrivalTime(G, vertex)
                        for predecessor in vertexPredecessors:
                            if predecessor.processor == vertex.processor:
                                continue
                            timeOnNewProcessor = calculateRealETC(predecessor,processor)
                            finishTimeOnNewProcessor = startTimeOnNewProcessor(G, predecessor, processor) + timeOnNewProcessor #OVDE OBRATI PAZNJU DA MOZDA POCETNO VREME IZVRSAVANJA SE MENJA JER JE NA DRUGOM PROCESORU OD PRETHODNIKA
                            #I dalje nije sredjeno btw
                            if (task.finishTime - task.startTime) >= timeOnNewProcessor and finishTimeOnNewProcessor < vertexStartTime:
                                print ("Ovde bi kopirao: " + predecessor.val + " kao predecessor na task: " + vertex.val)
                                vertexStartTime = duplicateTask(G, predecessor, vertex) #valjda ce zalepiti samo vertexu vrednost nove adrese a ne menjati staru adresu na novu vrednost
                                task.finishTime = vertexStartTime
                            
                                #Kada dodam  nova kopiranja moram ih racunati zarad daljeg obzira i uvazavanja za dalje kopiranje
                            #znaci slot bi mi se smanjio u trajanju i vertex.startTime tj vertex treba da postane kopirani task
        updateGraph(G)

def sortPredecessorsByArrivalTime(G, vertex):
    L = []
    for predecessor in vertex.predecessors:
        predecessor.arrivalTime = predecessor.finishTime + getWeight(G, predecessor, vertex)
        L.append(predecessor)   
    L.sort(key=lambda x: x.arrivalTime, reverse=True)
    print ([x.arrivalTime for x in L])
    return L

def duplicateTask(G, predecessor, vertex):
    duplicatedTask = copy.deepcopy(predecessor)
    duplicatedTask.val = predecessor.val + "." + vertex.processor.val[1::]
    duplicatedTask.weight = predecessor.weight
    duplicatedTask.processor = vertex.processor

    duplicatedTask.predecessors = predecessor.predecessors
    successorList = []
    successorList.append(vertex)
    duplicatedTask.successors = successorList

    duplicatedTask.finishTime = vertex.startTime
    duplicatedTask.startTime = duplicatedTask.finishTime - calculateRealETC(predecessor, duplicatedTask.processor)#za ovo nisam siguran msm da moram pogledati njegove predecessore za to

    vertexCopyOfGraph = G.V[:]
    edgeCopyOfGraph = G.E[:]
    oldCost = totalCost(G.P)#P ili P.processorList?
    oldTime = totalTime(G)
    print(oldCost)
    print(oldTime)

    global maxPrice
    if maxPrice < oldCost:
        maxPrice = oldCost

    predecessorCheck(G, duplicatedTask)

    duplicateEdges(G, predecessor, vertex, duplicatedTask)
    for successor in predecessor.successors:
        if successor.processor == vertex.processor:
            removeEdge(G, predecessor, successor)

    G.V.append(duplicatedTask)
    updatePredecessors(G)
    updateSuccessors(G)

    arrivalTimeList = sortPredecessorsByArrivalTime(G, duplicatedTask)
    if len(arrivalTimeList) >= 1:
        arrivalTime = arrivalTimeList[0].arrivalTime
    else:
        arrivalTime = 0

    if arrivalTime > duplicatedTask.startTime:
        print("Unhandled issue! Task can't be duplicated")
    #Proveri kriterijum za cenu ako je zadovoljen samo zavrsi normalo, ako nije vrati stanje kao sto je bilo pre promena
    updateGraph(G)
    newCost = totalCost(G.P)#P ili P.processorList?
    newTime = totalTime(G)
    print(newCost)
    print(newTime)
    if not(newTime == oldTime):
        if not (-((newCost-oldCost)/(newTime - oldTime)) < k*maxPrice):
            print("not worth it")
            G.E = edgeCopyOfGraph
            G.V = vertexCopyOfGraph
            updateGraph(G)
    else:
        print("not worth it")
        G.E = edgeCopyOfGraph
        G.V = vertexCopyOfGraph
        updateGraph(G)

    return duplicatedTask.startTime

    #Moram da napravim deep kopiju predecessora da skinem veze originala sa trenutnim vertexom 
    #i napravim vezu kopije sa trenutnim vertexom


def duplicateEdges(G, predecessor, vertex, duplicatedTask):
    for successor in predecessor.successors:#debug novo
        if successor.processor == vertex.processor: #debug
            #G.E.append(Edge(duplicatedTask, vertex, getEdgeWeight(G,predecessor,vertex)))
            G.E.append(Edge(duplicatedTask, successor, getEdgeWeight(G,predecessor,successor)))
    for predecess in predecessor.predecessors:
        G.E.append(Edge(predecess, duplicatedTask, getEdgeWeight(G, predecess, predecessor)))

def startTimeOnNewProcessor(G, vertex, processor): #Treba videti da li mozes srediti da pocne kasnije ako je moguce samo ne znam kako jer se updejtuje start Time na kraju sam
    #ako ne sredim to onda startTime nece biti optimizovan za redosled i potencijalno ne mogu 2 taska da ubacim u dupliciranje gde bih mogao da sam ih stisnuo po vremenu izvrsavanja
    #mogu napraviti funkciju startTime optimize za taskove dodate dupliciranjem potencijalno gde zgusne taskove da idu jedan za drugim i odvoji prostora za jos dupliciranja
    L = []
    copyProcessor = vertex.processor
    vertex.processor = processor
    for predecessor in vertex.predecessors:
        L.append(predecessor.finishTime + getWeight(G, predecessor, vertex))
    vertex.processor = copyProcessor
    if len(L) == 0:
        return 0
    return max(L)

def predecessorCheck(G, duplicatedTask):
    for i in range(0, len(duplicatedTask.predecessors)):
        for vertex in G.V:
            split = vertex.val.split('.')[0]
            if duplicatedTask.predecessors[i].val == split:
                if vertex.processor == duplicatedTask.processor: 
                    duplicatedTask.predecessors[i] = vertex
                    print( "predecessor Check: "+ vertex.val)