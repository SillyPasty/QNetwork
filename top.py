import math

class Node():
    """ 节点类 """
    def __init__(self, nodeId):
        """初始化节点

        Args:
            nodeId (int): 节点的编号

        """
        self.nodeId = nodeId
        self.__adjNodeIdx = []  # 本节点邻接节点编号
        self.edges = {}  # 邻接节点编号对应的边

        self.jumps = 0  # 当前跳数
        self.res = 0    # 到本节点所需资源
        self.reling = 0 # 到本节点可靠率
        self.path = []  # 初始点到本节点路径


    def getAdjNodesIdx(self):
        """ 得到本节点邻接节点编号
        
        Returns:
            list: 本节点邻接节点列表

        """
        return self.__adjNodeIdx

    def getAdjEdge(self):
        """ 得到本节点出边编号
        
        Returns:
            dictionary: 本节点出边字典，按照邻接节点id访问

        """
        return self.edges


    def con(self, node, length):
        """ 连接两节点

        本节点为初始点
        
        Args：
            node (class Node): 终点节点
            length (double): 节点长度

        """
        self.__adjNodeIdx.append(node.nodeId)
        edge = Edge(self.nodeId, node.nodeId, length)
        self.edges[node.nodeId] = edge


    def updateJump(self, prevNode):
        """ 更新跳数
        更新当前节点跳数，并返回跳数

        Args:
            prevNode (class Node): 前一节点
        
        Returns:
            int: 当前节点跳数
         """
        
        self.jumps = prevNode.jumps + 1
        return self.jumps

    def addToPath(self, other):
        """ 将本节点加入路径
        
        Args:
            other (class Node): 上一个节点
        """
        self.path = other.path[:]
        self.path.append(self.nodeId + 1)

    def updateRes(self, prevNode, edge):
        """ 更新本节点资源和可靠率

        Args:
            prevNode (class Node): 初始节点
            res (double): 新增消耗资源
        """
        self.res = prevNode.res + edge.res
        self.reling = edge.reling


class Edge():

    def __init__(self, start, end, length):
        """ 初始化一条边

        Args:
            start (int): 初始点编号
            end (int): 中止点编号
            length (double): 边长度

        """
        self.start = start
        self.end = end
        self.__length = length
        self.__keys = 0       # 当前边的密钥量

        self.res = 0  # 边消耗资源

        self.reling = 0
    
    def addKeys(self, keys):
        """ 添加密钥

        向本边分配密钥

        Args:
            keys (int): 新增密钥量

        Returns:
            int: 当前剩余密钥量
        
        """
        self.__keys += keys
        return self.__keys

    def useKeys(self, keys):
        """ 使用密钥

        判断当前剩余密钥量是否足够，并消耗密钥

        Args:
            keys (int): 消耗密钥量

        Returns:
            int: 当前剩余密钥量 若当前密钥量不足，返回-1

        """
        if self.__keys < keys:
            return -1
        self.__keys -= keys
        return self.__keys

    def getKeys(self):
        """ 获得当前密钥量

        Returns:
            int: 返回当前密钥量
        """
        return self.__keys

    def length(self):
        """ 获得边长度

        Returns:
            int: 返回边长度
        """
        return self.__length
    
    def updateRes(self, res):
        """ 更新边消耗资源

        Args:
            res (double): 边消耗资源
        """
        self.res = res

    def updateReling(self, resW, keyW, prevNode):
        """ 更新可靠率
        
        Args:
            resW (double): 消耗资源权重
            keyW (double): 当前密钥量权重
            prevNode (class Node): 初始节点
        """
        rel = resW * self.res # + keyW * self.__keys
        self.reling = prevNode.reling + rel


    def __lt__(self, other):
        return self.reling > other.reling


class Task():
    def __init__(self, startIdx, endIdx, res):
        self.startIdx = startIdx
        self.endIdx = endIdx
        self.res = res
