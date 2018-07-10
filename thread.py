from threading import Thread
import time

def fn(num):
    print('我是第%s个线程'%num)
    time.sleep(1)

for i in range(5):
    thread = Thread(target=fn, args=(i,))
    thread.start()