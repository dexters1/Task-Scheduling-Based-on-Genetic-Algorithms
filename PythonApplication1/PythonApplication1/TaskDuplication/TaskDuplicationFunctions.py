from GeneticAlgorithm.GeneticAlgorithmClasses import *
from Processor.ProcessorFunctions import *
from Graph.PriorityDefinition import getWeight
import copy

#k = (Omega/(1 - Omega))^2

def taskDuplication(G):
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

    

    duplicateEdges(G, predecessor, vertex, duplicatedTask)
    removeEdge(G, predecessor, vertex)
    G.V.append(duplicatedTask)

    return duplicatedTask.startTime

    #Moram da napravim deep kopiju predecessora da skinem veze originala sa trenutnim vertexom 
    #i napravim vezu kopije sa trenutnim vertexom


def duplicateEdges(G, predecessor, vertex, duplicatedTask):
    G.E.append(Edge(duplicatedTask, vertex, getEdgeWeight(G,predecessor,vertex)))
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