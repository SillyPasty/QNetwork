import random
import dataInit
import alg
from cfgs import Config

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
    k = int(input('本业务传输消耗密钥量:'))
    g = int(input('本网络每跳所额外消耗密钥量:'))
    q = int(input('本网络单位长度消耗密钥量:'))
    
    cfg = Config(g, q)
    # cfg = Config()
    print('----------测试算法----------')
    while 1:
        print('...开始测试，输入-1退出...')
        start = int(input('起点编号:'))
        if start == -1:
            break
        end = int(input('终点编号:'))
        node = alg.getBestPath(nodeList, start - 1, end - 1, cfg)
        path = node.path
        if node:
            print(path)
        else:
            print('无路径')

        dataInit.recover(nodeList)


def test(info):
    a, b, c = info
    print(a, b, c)

def main():
    FILEPATH = r'D:\Programme\Python\fz\矩阵数据.xlsx'

    simulateManual(FILEPATH)
    a = b = c = 1
    info = (a, b, c)
    test(info)

main()