import blueSock, threading, json, select

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
        self.handshake()
        try:
            while (self.alive and self.blueSock.alive):
                if (self.Ra != self.NewRa or self.Dec != self.NewDec):
                    self.sendCoords()
        except Exception as e:
            print "RPi Blue server exception ", e.message
        
    def handshake(self):
        print "Starting handshake"
        code = -1
        while code != 10:
            data = json.dumps({'code':10})
            self.blueSock.sendData(data)
            response = None
            (response,write,ex) = select.select([self.blueSock.socket.fileno()], [], [], 5)
            if (not response):
                continue 
            decode = json.loads(response)
            code = decode['code']
            if (code == 10):
                print "Handshake successful"

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
