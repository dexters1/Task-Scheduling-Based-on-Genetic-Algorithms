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
