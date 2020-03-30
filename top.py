class Node():
    
    def __init__(self, nodeId):
        self.nodeId = nodeId
        self.__adjNodeIdx = []
        self.edges = {}

        self.jumps = 0
        self.res = 0
        self.path = []


    def getAdjNodesIdx(self):
        return self.__adjNodeIdx
    
    def getAdjEdge(self):
        return self.edges
    
    def con(self, node, length):
        self.__adjNodeIdx.append(node.nodeId)
        edge = Edge(self.nodeId, node.nodeId, length)
        self.edges[node.nodeId] = edge
    
    def addToPath(self, other):
        self.path = other.path[:]
        self.path.append(self.nodeId)

class Edge():

    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.__length = length
        self.__keys = 0

        self.weight = length
    
    def addKeys(self, keys):
        self.__keys += keys
        return self.__keys

    def useKeys(self, keys):
        if self.__keys < keys:
            return -1
        self.__keys -= keys
        return self.__keys

    def getKeys(self):
        return self.__keys

    def length(self):
        return self.__length

    def weight(self):
        return self.weight

    def __lt__(self, other):
        return self.weight < other.weight


class Task():
    def __init__(self, startIdx, endIdx, res):
        self.startIdx = startIdx
        self.endIdx = endIdx
        self.res = res
