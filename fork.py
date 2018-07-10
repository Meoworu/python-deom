import os
import time

ret = os.fork()
print(ret)
if ret == 0:
    while True:
        time.sleep(1)
else:
    while True:
        time.sleep(1)