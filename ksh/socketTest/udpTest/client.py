import os
from socket import *

HOST=''
PORT=40000

ADDR=(HOST,PORT)

s=socket(AF_INET,SOCK_DGRAM)
s.bind(ADDR)

s.sendto('test msg to server',ADDR)
msg,addr=s.recvfrom(1024)

print msg,addr


