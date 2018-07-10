from multiprocessing import Process
import time

def test():
    print('----2----')
    time.sleep(1)

p = Process(target=test)
p.start()

def test2():
    print('-------1-----')
    time.sleep(1)

test2()

print('hello world')