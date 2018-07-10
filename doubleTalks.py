from socket import *
from threading import Thread,Lock

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('',8080))
url = ('10.216.96.217', 8080)
mutex = Lock()
mutex1 = Lock()
def listion():
    while True:
        mutex1.acquire()
        data = udpSocket.recvfrom(1024)
        print(data[0][1:])
        mutex.release()
def sendData():
    while True:
        mutex.acquire()
        data = input('请输入要发送的内容:')
        udpSocket.sendto(data.encode('utf-8'),url)
        mutex1.release()

if __name__ == '__main__':
    tl = Thread(target=listion)
    ts = Thread(target=sendData)


    ts.start()
    tl.start()