from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
url = ('10.216.96.217',8080)
str1 = '吴志祥是好人'
udpSocket.sendto(str1.encode('utf-8'),url)
udpSocket.close()