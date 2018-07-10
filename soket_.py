from socket import *

udpScoket = socket(AF_INET, SOCK_DGRAM)
# sendAddr = ('10.216.96.217', 5240)
# upScoket.sendto(b'haha', sendAddr)
# upScoket.close()
udpScoket.bind(('', 8080))
recvData = udpScoket.recvfrom(1024)
print(recvData)