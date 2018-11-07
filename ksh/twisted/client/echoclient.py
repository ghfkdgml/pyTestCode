from twisted.internet import reactor,protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("hello world")
    def dataReceived(self,data):
        print "Server said:",data
        print self.transport.getPeer()
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self,addr):
        return EchoClient()

    def clientConnectionFailed(self,connector,reason):
        print "Connection failed!"
        reactor.stop()

    def clientConnectionLost(self,connector,reason):
        print "Connection Lost!"
        reactor.stop()

reactor.connectTCP("127.0.0.1",8000,EchoFactory())
reactor.run()
