import sys

class ProcessorList:
    def __init__(self, processorList=[] ):
        self.processorList = processorList

class Processor:
    def __init__(self, taskList=[], capacity=0):
        self.taskList = taskList
        self.capacity = capacity
