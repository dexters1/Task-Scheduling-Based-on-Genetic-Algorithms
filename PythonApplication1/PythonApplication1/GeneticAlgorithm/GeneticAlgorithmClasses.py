from math import inf

Omega = 0.25
NIND = 10
mPN = 2
k1 = 0.6
k2 = 0.8
k3 = 0.1
k4 = 0.05

class Population:
    def __init__(self, population):
        self.individualList = population
        self.maxTime = 0
        self.minTime = inf
        self.maxCost = 0
        self.minCost = inf
        self.fitnessSum = None
        self.fitnessAverage = None