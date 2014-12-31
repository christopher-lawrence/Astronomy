import stellariumServer, stellariumClient, socks, blueSock, blueServer, blueClient

if __name__ == '__main__':

    serverSock = socks.socks('', 10002)
    serverSock.listen()
    
    # Create a bluetooth socket
    blueSock = blueSock.blueSock()
    blueSock.connect('RPi Bluetooth')
    
    # Start the 'send coords' service
    blueServer = blueServer.blueServer(blueSock)
    blueServer.daemon = True
    blueServer.start()
    
    # Start the stellarium client (receive coords)
    stellariumClient = stellariumClient.stellariumClient(blueServer, serverSock)
    stellariumClient.daemon = True
    stellariumClient.start()    
    
    # Start the stellarium server (send coords)
    stellariumServer = stellariumServer.stellariumServer(serverSock)
    stellariumServer.daemon = True
    stellariumServer.start()
    
    # Start the 'receive coords' service
    blueClient = blueClient.blueClient(blueSock, stellariumServer)
    blueClient.daemon = True
    blueClient.start()
    
    try:
        while (stellariumServer.isAlive() and stellariumClient.isAlive() and blueServer.isAlive() and blueClient.alive):
            pass
    except Exception, e:
        print "Exception encountered: %s. Stopping server..." % e
    finally:
    	blueServer.stop()
    	blueClient.stop()
    	stellariumServer.stop()
    	stellariumClient.stop()
    	print "Done."
