from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('',8080))
while True:
    recvData = udpSocket.recvfrom(1024)[0]
    print(recvData)
    
