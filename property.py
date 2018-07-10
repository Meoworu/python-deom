class Num:
    def __init__(self):
        __num = 100
    @property
    def num(self) :
        print('正在获取__num值')
        return self.__num
    @num.setter
    def num(self, num):
        print('正在设置__num值')
        self.__num = num

n = Num()
n.num = 10