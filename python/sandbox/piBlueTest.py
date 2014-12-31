import blueSock, time, select, json, threading

class blueRpiClient(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock 
        self.alive = True
    
    def run(self):
        while(self.alive and self.sock.alive):
            self.handshake()

    def handshake(self):
        print 'Starting handshake'
        code = -1
        while code != 10:
            data = json.dumps({'code':10})
            self.sock.sendData(data)
            [read,write,ex] = select.select([self.sock.connection.fileno()], [],[], 5)
            if (not read):
                continue
            data = self.sock.receiveData()
            decode = json.loads(data)
            code = decode['code']
            if (code == 10):
                print "Handshake successful"
    
    def close(self):
        self.alive = False
        self.sock.close()
        

if __name__ == '__main__':    
    # Create a bluetooth server socket
    blueSockServer = blueSock.blueSock()
    blueSockServer.startService('RPi Bluetooth', "", 7)

    # Receive the computer's service info
#    while True:
#        [read,write,ex] = select.select([blueSockServer.connection], [], [], 10000)
#        if not read:
#            pass
#        data = blueSockServer.receiveData()
#        decoded = json.loads(data)
#        if (decoded['code'] != 4):
#            pass
#        address = decoded['message']['address']
#        channel = decoded['message']['channel']
#        break

    # Connect to computer bluetooth server
    #blueSockClient = blueSock.blueSock()
    #blueSockClient.connect("Computer Bluetooth")
#    blueSockClient = blueSock.blueSock(address=address, channel=channel)
#    blueSockClient.connect()
    
    # Start the 'send coords' service
    #blueRpiServer = blueRpiServer.blueRpiServer(blueSockClient)
    #blueRpiServer.daemon = True
    #blueRpiServer.start()
    
    # Start the 'receive coords' service
    blueRpiClient = blueRpiClient(blueSockServer)
    blueRpiClient.daemon = True
    blueRpiClient.start()
    
    try:
        #while (blueRpiServer.isAlive() and blueRpiClient.isAlive()):
        while (blueRpiClient.isAlive()):
            pass
    except Exception, e:
        print "Exception encountered: %s. Stopping server..." % e
        #blueRpiServer.stop()
        blueRpiClient.stop()
        
    #blueRpiServer.close()
    blueRpiClient.close()
    print "Done."
