import blueSock, threading

class blueReceiveCoords(threading.Thread):
    def __init(self, blueSock, stellariumServer):
        self.blueSock = blueSock
        self.stellariumServer = stellariumServer
        self.alive = True 
        threading.Thread.__init__(self)
        
   def run(self):
        print "Starting Blue RPi Client service..."
        try:
            while (self.alive and self.sock.alive and self.stellariumServer.alive):
                [Ra,Dec] = self.receiveCoords(10000)
                if (Ra == False):
                	pass;
                self.stellariumServer.updateCoords(Ra, Dec)
                #time.sleep(1)
        except Exception, e:
            print "Client exception ", e.message
        
        self.stop()
        
    def receiveCoords(self,timeout):
        try:
            incomingData = None
            #print "Waiting for data from {0}...".format(self.sock.host)
            [read,write,ex] = select.select([self.blueSock.connection], [], [], timeout)
            if not read:
                return incomingData
            incomingData = self.blueSock.recieveData()
            return incomingData
        except Exception, e:
            print "Failed to receive data from {0}: {1}".format(self.blueSock.address, e)