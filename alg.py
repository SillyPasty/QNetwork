from top import Node, Edge
from key import KeyPool
from cfgs import Config
import heapq


def initTop():
    nodeList = []
    size = int(input('Input the number of the nodes:'))

    for i in range(0, size):
        node = Node(i)
        nodeList.append(node)

    for outNode in range(0, size):
        row = input('Input the %d row:' % (outNode + 1))
        lens = row.split(' ')
        for inNode, length in enumerate(lens):
            length = int(length)
            if length and inNode != outNode:
                nodeList[outNode].con(nodeList[inNode], length)
    
    return nodeList


def getExtraR(jump):
    return jump

def getBestPath(nodeList, start, end):  
    cfg = Config()
    startNode = nodeList[start]
    endNode = nodeList[end]
    maxJump = cfg.MAXJUMPS
    pQueue = []

    for edgeIdx in startNode.getAdjNodesIdx():
        heapq.heappush(pQueue, startNode.edges[edgeIdx])
    
    startNode.addToPath(startNode)

    while pQueue:
        print(pQueue)
        tpEdge = heapq.heappop(pQueue)
        print(pQueue)
        outIdx = tpEdge.start
        inIdx = tpEdge.end

        print('outIdx=' + str(outIdx) + ' inIdx=' + str(inIdx))
        outNode = nodeList[outIdx]
        inNode = nodeList[inIdx]
        # add jump
        inNode.jumps = outNode.jumps + 1
        curJump = inNode.jumps
        # upload path
        inNode.addToPath(outNode)

        if inNode == endNode:
            return inNode.path

        if maxJump < inNode.jumps:
            continue

        for edgeIdx in inNode.getAdjNodesIdx():
            # add to heap
            newEdge = inNode.edges[edgeIdx]
            newEdge.weight = newEdge.length() + getExtraR(curJump)  # calculate weight by jump times
            heapq.heappush(pQueue, newEdge)

    return None

def printTop(nodeList):
    for node in nodeList:
        print('Node id %d ' % (node.nodeId + 1))
        adjNodesIdx = node.getAdjNodesIdx()
        for idx in adjNodesIdx:
            edges = node.getAdjEdge()[idx]
            print('node:%d length:%d' % ((idx + 1), edges.length()), end=',')
        print()

def main():
    print('----------输入网络----------')
    nodeList = initTop()
    printTop(nodeList)
    for node in nodeList:
        print(node.path)

    print('----------测试算法----------')
    while 1:
        print('...开始测试，输入-1退出...')
        start = int(input('起点编号:'))
        if start == -1:
            break
        end = int(input('终点编号:'))
        bestPath = getBestPath(nodeList, start - 1, end - 1)
        if bestPath:
            print(bestPath)
        else:
            print('无路径')
    
main()



'''

0 100 1
0 0 0
0 1 0

'''