import socket, sys

class socks(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.alive = True
        #self.connection = -1
    
    def listen(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.settimeout(600)#Throws a timeout exception if connections are idle for 10 minutes
        self.sock.listen(1)#set the socket to listen, now it's a server!
        self.connected = False
        
        try:
            while True:
                # Wait for a connection
                self.connection, self.clientAddress = self.sock.accept() 
                if self.connection != None:
                    print "Connected to ", self.clientAddress
                    self.connected = True
                    break
        except:
            e = sys.exc_info()[1]
            print ("Failed handshake with Stellarium: %s" % e)
            self.sock.close()
    
    def sendData(self, data):
        print "Incoming data[%d]: ", (len(data),data)
        try:
            self.connection.send(data)
        except Exception, e:
            print "Send error: %s" % e
            self.alive = False
    def recieveData(self):
        print "Receiving data: "
        return self.connection.recv(1024)
        
    def close(self):
        self.alive = False
        self.connection.close()
        self.sock.close()
        