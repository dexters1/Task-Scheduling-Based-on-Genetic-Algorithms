import sys

class ProcessorList:
    def __init__(self, processorList=[] ):
        self.processorList = processorList

class Slot:
    def __init__(self,startTime,finishTime, noCost=False, val="Slot"):
        self.startTime = startTime
        self.finishTime = finishTime
        self.noCost = noCost
        self.val = val

class Processor:
    def __init__(self, taskList=[], capacity=0, val="None"):
        self.taskList = taskList
        self.capacity = capacity
        self.val = val

ETC = [14, 16, 9,
       13, 19, 18,
       11, 13, 19,
       13, 8, 7,
       12, 13, 10,
       13, 16, 9,
       7, 15, 11, 
       5, 11, 14,
       18, 12, 20,
       21, 7, 16]
