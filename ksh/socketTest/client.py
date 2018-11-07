import socket,sys
from threading import Thread


HOST='127.0.0.1'
ADDR=(HOST,33331)

def rcvMsg(sock):
    while 1:
        try:
            msg=sock.recv(1024)
            if not msg:
                break
            print msg
        except:
            pass


clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    clientSocket.connect(ADDR)
except:
    print ' connect failed!'
    sys.exit()
t=Thread(target=rcvMsg,args=(clientSocket,))
t.daemon=True
t.start()


while True:
    msg=raw_input()
    clientSocket.send(msg.encode('utf-8'))
    print 'msg send!'

    #if msg=='exit':
    #    m=clientSocket.recv(1024)
    #    if m=='bye':
    #        print 'Done!'
    #        #sys.exit()
    #        clientSocket.close()

clientSocket.close()
