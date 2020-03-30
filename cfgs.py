

class Config():
    '''设置类，存放参数'''
    def __init__(self):
        self.prob = 0.99  #  成功概率
        self.maxJumps = 30  #  最大跳数内搜索
        self.validWeight = 0.05  # X1
        self.resWeight = -5  # X2
        self.extraKey = 40  # g
        self.keyPerLen = 1
    
    @property
    def MAXJUMPS(self):
        return self.maxJumps