import blueRpiServer, blueRpiClient, blueSock, time, select, json

if __name__ == '__main__':    
    # Create a bluetooth server socket
    blueSockServer = blueSock.blueSock()
    blueSockServer.startService('RPi Bluetooth', "", 7)

    # Receive the computer's service info
    while True:
        [read,write,ex] = select.select([blueSockServer.connection], [], [], 10000)
        if not read:
            pass
        data = blueSockServer.receiveData()
        decoded = json.loads(data)
        if (decoded['code'] != 4):
            pass
        address = decoded['message']['address']
        channel = decoded['message']['channel']
        break

    # Connect to computer bluetooth server
    #blueSockClient = blueSock.blueSock()
    #blueSockClient.connect("Computer Bluetooth")
    blueSockClient = blueSock.blueSock(address=address, channel=channel)
    blueSockClient.connect()
    
    # Start the 'send coords' service
    blueRpiServer = blueRpiServer.blueRpiServer(blueSockClient)
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
