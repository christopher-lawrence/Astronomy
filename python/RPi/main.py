import blueRpiServer, blueRpiClient, blueSock, time

if __name__ == '__main__':    
    # Create a bluetooth server socket
    blueSock = blueSock.blueSock()
    blueSock.startService('RPi Bluetooth', "", 7)
    
    # Connect to computer bluetooth sever
    blueSockClient = blueSock.blueSock()
    blueSockClient.connect('Computer Bluetooth')
    
    # Start the 'send coords' service
    blueRpiServer = blueRpiServer.blueRpiServer(blueSockClient)
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
        
    blueRpiServer.close()
    blueRpiClient.close()
    print "Done."
