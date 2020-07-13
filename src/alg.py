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

    isVisit = [0 for _ in range(0, len(nodeList))]
    visit = 0
    dist = [-1 for _ in range(0, len(nodeList))]

    isVisit[start] = 1
    visit += 1
    dist[start] = 0
    startNode.addToPath(startNode)
    for edgeIdx in startNode.getAdjNodesIdx():

        curEdge = startNode.edges[edgeIdx]
        res = transResourses(0, curEdge.length(), cfg)
        curEdge.updateRes(res)  # 更新资源
        curEdge.updateReling(cfg.RESW, cfg.KEYW, startNode)  # 更新可靠率

        inNode = nodeList[curEdge.end]

        inNode.updateRes(startNode, curEdge)
        dist[curEdge.end] = inNode.reling

        inNode.addToPath(startNode)

        heapq.heappush(pQueue, curEdge)



    while True:
        minIdx = -1
        minVal = -1
        for idx, val in enumerate(dist):
            if isVisit[idx] == 0 and val != -1:
                if minVal == -1 or minVal > val:
                    minVal = val
                    minIdx = idx
        if minVal == -1:
            break
            
        curNode = nodeList[minIdx]
        isVisit[minIdx] = 1

        

        for edgeIdx in curNode.getAdjEdge():
            curEdge = curNode.edges[edgeIdx]
            inNodeIdx = curEdge.end
            inNode = nodeList[inNodeIdx]
            
            if isVisit[inNodeIdx] == 1:
                continue
    
            curJump = curNode.jumps + 1

            if maxJump < curJump:
                continue

            res = transResourses(curJump, curEdge.length(), cfg)
            curEdge.updateRes(res)  # 更新资源
            curEdge.updateReling(cfg.RESW, cfg.KEYW, curNode)  # 更新可靠率
            if minIdx == 4 and inNodeIdx == 11:
                print(dist[11])
            if dist[inNodeIdx] == -1 or dist[inNodeIdx] > curEdge.res + curNode.res:
                inNode.updateRes(curNode, curEdge)
                dist[inNodeIdx] = inNode.res
                inNode.updateJump(curNode)
                inNode.addToPath(curNode)
    return endNode
