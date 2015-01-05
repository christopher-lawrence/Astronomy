import blueSock, threading, json

class blueServer(threading.Thread):
    def __init__(self, blueSock):
        threading.Thread.__init__(self)
        self.blueSock = blueSock
        self.Ra = 0x0
        self.Dec = 0x0
        self.NewRa = 0x0
        self.NewDec = 0x0
        self.alive = True
        self.coordsLocked = False
    
    def run(self):
        print "Starting Blue Server..."
        try:
            while (self.alive and self.blueSock.alive):
                if (self.Ra != self.NewRa or self.Dec != self.NewDec):
                    self.sendCoords()
        except Exception as e:
            print "Blue server exception ", e.message
        
        self.stop()
        
    def updateCoords(self, Ra, Dec):
        if(not self.coordsLocked):
            self.coordsLocked = True
            self.NewRa = Ra
            self.NewDec = Dec
            self.coordsLocked = False
            return True
        return False
            
    def sendCoords(self):
        if (not self.coordsLocked):
            self.coordsLocked = True
            data = json.dumps({'code':3, 'NewRa':self.NewRa, 'NewDec':self.NewDec})
            self.blueSock.sendData(data)
            self.Ra = self.NewRa
            self.Dec = self.NewDec
            self.coordsLocked = False
            
    def stop(self):
        self.alive = False
        self.blueSock.close()
