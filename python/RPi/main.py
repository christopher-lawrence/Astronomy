import blueRpiServer, blueRpiClient, blueSock, time, select, json

if __name__ == '__main__':    

    blueSockServer = blueSock.blueSock()
    blueSockServer.startService('RPi Bluetooth', "", 7)
    
    # Start the 'send coords' service
    blueRpiServer = blueRpiServer.blueRpiServer(blueSockServer)
    blueRpiServer.daemon = True
    blueRpiServer.start()
    
    # Start the 'receive coords' service
    blueRpiClient = blueRpiClient.blueRpiClient(blueSockServer, blueRpiServer)
    blueRpiClient.daemon = True
    blueRpiClient.start()
    
    try:
        while (blueRpiServer.isAlive() and blueRpiClient.isAlive()):
            pass
    except Exception, e:
        print "Exception encountered: %s. Stopping server..." % e
        blueRpiServer.stop()
        blueRpiClient.stop()
        
    blueRpiServer.close()
    blueRpiClient.close()
    print "Done."
