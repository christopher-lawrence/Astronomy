import blueSock, threading, json

class blueRpiServer(threading.Thread):
    def __init__(self, blueSock):
        self.blueSock = blueSock
        self.Ra = 0.0
        self.Dec = 0.0
        self.NewRa = 0.0
        self.NewDec = 0.0
        self.alive = True
        self.coordsLocked = False
        threading.Thread.__init__(self)
    
    def run(self):
        print "Starting Rpi Blue Server..."
        try:
            while (self.alive and self.blueSock.alive):
                if (self.Ra != self.NewRa or self.Dec != self.NewDec):
                    self.sendCoords()
        except Exception as e:
            print "RPi Blue server exception ", e.message
        
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
            data = json.dumps({'code':3, 'Ra':self.NewRa, 'Dec':self.NewDec})
            self.blueSock.sendData(data)
            self.Ra = self.NewRa
            self.Dec = self.NewDec
            self.coordsLocked = False
            
    def close(self):
        self.alive = False
        self.blueSock.close()
