from SocketServer import *
from socket import *
HOST=''
PORT=33331
ADDR=(HOST,PORT)

class TcpReqHandler(StreamRequestHandler):
    def handle(self):
        print 'connect...'
        conn=self.request
        while 1:
            msg=conn.recv(1024)
            if not msg:
                conn.close()
                print self.client_address,' disconnected!'
                break
            print self.client_address, msg
            if msg=='exit':
                conn.send('bye')

class UserList():
    def __init__(self,ulist):
        self.userList=ulist


    def userCheck(self,id):
        self.id=id
        if self.id in self.userList:
            print 'user name exist!'
        else:
            self.userList.append(self.id)

    def userDel(self):
        self.userList.remove(self.id)
    def printUser(self):
        print self.userList
class SendMsg():
    userList={}

    def userAdd(self,ip,conn):
        self.userList[ip]=conn

    def sendMSG(self,ip,msg):
        if len(self.userList)<=1:
            self.userList[ip].send('more user needed!')
            return
        for i in self.userList.keys():
            if i!=ip:
                self.userList[i].send(msg)

    def userDel(self,ip):
        self.userList.pop(ip)
class TCPChatHandler(StreamRequestHandler):
    users=SendMsg()
    #def handle(self):
    #    print 'connect!....'
    #    self.id=raw_input('type your id:')
    #    x.userCheck(self.id)
    #    conn=self.request
    #    while 1:
    def handle(self):
        print 'conenct!...'
        conn=self.request
        ip=self.client_address[0]
        self.users.userAdd(ip,conn)
        while 1:
            msg=conn.recv(1024)
            if not msg:
                self.users.userDel(self.client_address[0])
                conn.close()
                print self.client_address,' disconnected!'
                break
            self.users.sendMSG(ip,msg)

















if __name__=='__main__':
    #ThreadingTCPServer.allow_reuse_address=True
    #server=ThreadingTCPServer(ADDR,TcpReqHandler)
    #print 'listening on port ',PORT
    #server.serve_forever()
    ThreadingTCPServer.allow_reuse_address=True
    server=ThreadingTCPServer(ADDR,TCPChatHandler)
    print 'listening on port ',PORT
    server.serve_forever()


