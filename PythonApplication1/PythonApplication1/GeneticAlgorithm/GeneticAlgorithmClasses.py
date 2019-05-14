from math import inf

Omega = 0.25

class Population:
    def __init__(self, population):
        self.individualList = population
        self.maxTime = 0
        self.minTime = inf
        self.maxCost = 0
        self.minCost = inf