from lightblue import *
import blueSock

class blueRpiClient(object):
    def __init__(self, blueSock, blueRpiServer):
        self.blueSock = blueSock
        self.blueRpiServer = blueRpiServer
        self.alive = True 
        threading.Thread.__init__(self)
    
    def run(self):
        print "Starting Blue RPi Client service..."
        try:
            while (self.alive and self.sock.alive and self.blueServer.alive):
                [Ra,Dec] = self.receiveCoords(10000)
                if (Ra != None):
                    self.blueRpiServer.updateCoords(Ra, Dec)
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
            decoded = json.loads(incomingData)
            if (decoded['code'] == 3
                return (decoded['NewRa'], decoded['NewDec'])
            
            print "Invalid or empty code sent: ", decoded['3']
            return None
        except Exception, e:
            print "Failed to receive data from {0}: {1}".format(self.blueSock.clientAddress, e)