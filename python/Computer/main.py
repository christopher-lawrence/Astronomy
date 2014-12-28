import stellariumServer, stellariumClient, socks, time, socket, blueSock, blueServer

if __name__ == '__main__':
    serverSock = socks.socks('', 10002)
    serverSock.listen()
    
    # Create a bluetooth socket
    blueSock = blueSock.blueSock()
    blueSock.connect()
    
    stellariumServer = stellariumServer.stellariumServer(serverSock)
    stellariumServer.daemon = True
    stellariumServer.start()
    
    stellariumClient = stellariumClient.stellariumClient(blueSock, serverSock)
    stellariumClient.daemon = True
    stellariumClient.start()    
    
    # Start the 'send coords' service
    blueServer = blueServer.blueServer()
    blueServer.daemon = True
    bluesServer.start()
    
    # Start the 'receive coords' service
    
    
    try:
        while (stellariumServer.isAlive() and stellariumClient.isAlive()):
            pass
    except Exception, e:
        print "Exception encountered: %s. Stopping server..." % e
        stellariumServer.stop()
        stellariumClient.stop()
        
    stellariumServer.stop()
    stellariumClient.stop()
    print "Done."