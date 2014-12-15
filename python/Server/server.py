import socks, threading, angles, time, struct

class server(threading.Thread):
    def __init__(self, sock):
        self.sock = sock
        self.Ra = 0.0
        self.Dec = 0.0
        self.alive = True
        self.coordsLocked = False
        threading.Thread.__init__(self)
        
    def run(self):        
        while(self.alive and self.sock.alive):
            try:
                self.sendCoords()
                time.sleep(1)
            except Exception as e:
                self.alive = False
                print "Server exception ", e.message
        self.stop()
    
    def updateCoords(self, Ra, Dec):
        if(not self.coordsLocked):
            self.coordsLocked = True
            self.Ra = Ra
            self.Dec = Dec
            self.coordsLocked = False
    
    def sendCoords(self):
        if (not self.coordsLocked):
            self.coordsLocked = True
            Ra = angles.Angle(r=float(self.Ra))
            print "Ra: ", Ra
            Dec = angles.Angle(r=float(self.Dec))
            print "Dec: ", Dec
            [RaInt,DecInt] = self.angleToStellarium(Ra, Dec)
            print "RaInt: %d, DecInt: %d" % (RaInt, DecInt)
            # Ok to unlock now
            self.coordsLocked = False
            data = struct.pack("3iIi", 20, 0, int(time.time()), RaInt, DecInt)
            self.sock.sendData(data)
        
    def angleToStellarium(self,Ra,Dec):
        return [int(Ra.h*(2147483648/12.0)), int(Dec.d*(1073741824/90.0))]
        
    def stop(self):
        self.alive = False
        self.sock.close()
        
    