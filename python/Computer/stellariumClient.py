import socks, threading, blueServer, angles, struct, select, time

class stellariumClient(threading.Thread):
    def __init__(self, blueServer, sock):
        self.blueServer = blueServer
        self.sock = sock
        threading.Thread.__init__(self)
        self.alive = True
    
    def run(self):
        print "Starting Stellarium Client..."
        try:
            while (self.alive and self.sock.alive and self.blueServer.alive):
                [Ra,Dec] = self.receiveCoords(10000)
                if (Ra == False):
                	pass;
                # TODO: Change this to the blueServer
                self.blueServer.updateCoords(Ra, Dec)
                #time.sleep(1)
        except Exception, e:
            print "Client exception ", e.message
        
        self.stop()
        
    def receiveCoords(self, timeout):
        incomingData = self.receiveStellariumData(timeout)
        if (incomingData != None) and (len(incomingData) != 0):
            #print ("Incoming data: ", (len(incomingData),incomingData))
            data = struct.unpack("3iIi", incomingData)
            #print("Unpacked data: Length:%d Type:%d Time:%d RA: %d Dec: %d" % (data[0], data[1], data[2], data[3], data[4]))
            [Ra,Dec] = self.stellariumToAngle(data[3], data[4])
            
            #print "Sending update to server: Ra={0:02f}, Dec={1:02f}".format(Ra.r, Dec.r)
            return [Ra.r,Dec.r]
        else:
            return [False,False]
            
    def receiveStellariumData(self,timeout):
        try:
            incomingData = None
            #print "Waiting for data from {0}...".format(self.sock.host)
            [read,write,ex] = select.select([self.sock.connection], [], [], timeout)
            if not read:
                return incomingData
            incomingData = self.sock.recieveData()
            return incomingData
        except Exception, e:
            print "Failed to receive data from Stellarium: {0}".format(e)
            
    def stellariumToAngle(self,RaInt,DecInt):
        Ra = angles.Angle(h=(RaInt*12.0/2147483648))
        Dec = angles.Angle(d=(DecInt*90.0/1073741824))
        return [Ra, Dec]
        
    def stop(self):
        self.alive = False
        self.sock.close()