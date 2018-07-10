from threading import Thread
import time

class ThreadClass(Thread):
    def run(self, num):
        for i in range(5):
            print('我是第%s个线程'%i)
            time.sleep(1)

t = ThreadClass()
t.start()