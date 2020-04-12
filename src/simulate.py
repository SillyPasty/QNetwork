import random
import dataInit
import alg

def simulate(times, size):
    for i in range(0, times):
        start = random.randint(0, size)
        end = start
        while end == start:
            end = random.randint(0, size)
        # do algorithm
        
def simulateManual(path):
    """ 手动模拟
    根据路径读取excel内网络拓扑信息
    手动输入起点和中点
    打印路径

    Args:
        path (str): 文件路径
    """
    print('初始化...')
    nodeList = dataInit.readExcelInput(path)
    dataInit.printTop(nodeList)
    print('----------测试算法----------')
    while 1:
        print('...开始测试，输入-1退出...')
        start = int(input('起点编号:'))
        if start == -1:
            break
        end = int(input('终点编号:'))
        node = alg.getBestPath(nodeList, start - 1, end - 1)
        path = node.path
        if node:
            print(path)
        else:
            print('无路径')

        dataInit.recover(nodeList)


def main():
    FILEPATH = r'D:\Programme\Python\fz\矩阵数据.xlsx'
    simulateManual(FILEPATH)

main()