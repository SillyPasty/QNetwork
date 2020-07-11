

class Config():
    '''设置类，存放参数'''
    def __init__(self, ext=40, perLen=1):
        self.prob = 0.99    # 成功概率
        self.maxJumps = 30  # 最大跳数内搜索
        self.keyW = 0.05    # X1
        self.resW = -5      # X2
        self.extraKey = ext  # 每跳额外消耗密钥量
        self.keyPerLen = perLen  # 单位长度消耗密钥量

    
    @property
    def MAXJUMPS(self):
        return self.maxJumps

    @property
    def KEYW(self):
        return self.keyW

    @property
    def RESW(self):
        return self.resW