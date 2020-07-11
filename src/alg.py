from top import Node, Edge
from key import KeyPool
import heapq



def transResourses(jump, length, cfg):
    """ 计算额外资源

    根据跳数和长度计算额外资源
    
    Args: 
        jump (int): 当前跳数
        length (double): 边长度
    
    Returns:
        double: 额外资源

    """
    return (jump * cfg.extraKey + length * cfg.keyPerLen)

def getBestPath(nodeList, start, end, cfg):
    """ 计算额外资源
    
    根据跳数和长度计算额外资源
    
    Args: 
        nodeList (list): 节点列表
        start (int): 起点编号
        end (int): 终点编号
    
    Returns:
        class Node: 终点, 若不存在路径, 返回None

    """  
    startNode = nodeList[start]
    endNode = nodeList[end]
    maxJump = cfg.MAXJUMPS
    pQueue = []
    isVisit = []
    for _ in range(0, len(nodeList)):
        isVisit.append(0)

    for edgeIdx in startNode.getAdjNodesIdx():
        isVisit[start] = 1
        cueEdge = startNode.edges[edgeIdx]
        res = transResourses(0, cueEdge.length(), cfg)
        cueEdge.updateRes(res)  # 更新资源
        cueEdge.updateReling(cfg.RESW, cfg.KEYW, startNode)  # 更新可靠率

        heapq.heappush(pQueue, cueEdge)

    startNode.addToPath(startNode)

    while pQueue:
        curEdge = heapq.heappop(pQueue)
        # print(pQueue)
        outIdx = curEdge.start
        inIdx = curEdge.end
        # print('outIdx=' + str(outIdx) + ' inIdx=' + str(inIdx))
        outNode = nodeList[outIdx]
        inNode = nodeList[inIdx]

        isVisit[inIdx] = 1
        # add jump
        curJump = inNode.updateJump(outNode)

        inNode.updateRes(outNode, curEdge)

        # upload path
        inNode.addToPath(outNode)

        if inNode == endNode:
            return inNode

        if maxJump < curJump:
            continue

        for edgeIdx in inNode.getAdjNodesIdx():
            # add to heap
            newEdge = inNode.edges[edgeIdx]
            if isVisit[newEdge.end]:
                continue
            res = transResourses(curJump, newEdge.length(), cfg)
            newEdge.updateRes(res)
            newEdge.updateReling(cfg.RESW, cfg.KEYW, outNode)  # calculate weight by jump times

            heapq.heappush(pQueue, newEdge)

    return None
