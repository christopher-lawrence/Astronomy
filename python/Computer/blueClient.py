import blueSock, threading, stellariumServer, json, select

class blueClient(threading.Thread):
    def __init__(self, blueSock, stellariumServer):
        threading.Thread.__init__(self)
        self.blueSock = blueSock
        self.stellariumServer = stellariumServer
        self.alive = True

    def run(self):
        print "Starting Blue Client service..."
        try:
            while (self.alive and self.blueSock.alive and self.stellariumServer.alive):
                [Ra,Dec] = self.receiveCoords(10000)
                if (Ra != None):
                    self.stellariumServer.updateCoords(Ra, Dec)
        except Exception, e:
            print "Blue Client exception ", e.message
        finally:
            self.stop()
        
    def receiveCoords(self,timeout):
        try:
            incomingData = None
            [read,write,ex] = select.select([self.blueSock.connection.fileno()], [], [], timeout)
            if not read:
                return incomingData
            incomingData = self.blueSock.receiveData()
            decoded = json.loads(incomingData)
            if (decoded['code'] == 3):
                return (decoded['Ra'], decoded['Dec'])

            print "Invalid or empty code sent: ", decoded['code']
            return None
        except Exception, e:
            print "Failed to receive data from {0}: {1}".format(self.blueSock.address, e)
            
    def stop(self):
        self.alive = False
        self.blueSock.close()
