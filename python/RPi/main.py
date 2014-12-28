import blueRpiServer, blueRpiClient, blueSock, time

if __name__ == '__main__':    
    # Create a bluetooth socket
    blueSock = blueSock.blueSock()
    blueSock.connect()
    
    # Start the 'send coords' service
    blueRpiServer = blueRpiServer.blueRpiServer(blueSock)
    blueRpiServer.daemon = True
    blueRpiServer.start()
    
    # Start the 'receive coords' service
    blueRpiClient = blueRpiClient.blueRpiClient(blueSock, blueRpiServer)
    blueRpiClient.daemon = True
    blueRpiClient.start()
    
    try:
        while (blueRpiServer.isAlive() and blueRpiClient.isAlive()):
            pass
    except Exception, e:
        print "Exception encountered: %s. Stopping server..." % e
        blueRpiServer.stop()
        blueRpiClient.stop()
        
    blueRpiServer.stop()
    blueRpiClient.stop()
    print "Done."