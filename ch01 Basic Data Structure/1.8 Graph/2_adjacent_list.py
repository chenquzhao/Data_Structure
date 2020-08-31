class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class UnDirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []  # should be consistent in both direction
