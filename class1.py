class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print('该实例被销毁')
    def brk(self):
        print('-----汪汪叫------')
    def introduce(self):
        print('我叫%s今年%s'%(self.name, self.age))

class Xiaotq(Dog):
    def __init__(self, name, age, heigh):
        super().__init__(name, age)
        self.heigh = heigh

    def brk(self):
        print('-------狂叫--------')

    def introduce(self):
        print('我叫%s今年%s高%s'%(self.name, self.age, self.heigh))

dog = Xiaotq('小王', 18, '180cm')
dog.brk()
dog.introduce()

