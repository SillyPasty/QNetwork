

class Config():
    '''设置类，存放参数'''
    def __init__(self):
        self.prob = 0.99  #  成功概率
        self.maxJumps = 30  #  最大跳数内搜索
    
    @property
    def MAXJUMPS(self):
        return self.maxJumps