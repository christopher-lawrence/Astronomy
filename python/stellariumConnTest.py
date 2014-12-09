import socket

class stellariumConnect(object):
    def __init__(self,host,port):
        self.serverAddress=(host,port)
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.serverAddress)
        self.sock.settimeout(600)
        self.sock.listen(1)
        self.connected = False

    def handshakeStellarium(self):
        try:
            while True:
                self.connection, self.clientAddress = self.sock.accept()
                if self.connection != None:
                    self.connected = True
                    break
        except Exception:
            print "Failed handshake with Stellarium: %s" % (Exception.message)

