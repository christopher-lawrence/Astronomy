import server, client, socks, time, socket

if __name__ == '__main__':
    serverSock = socks.socks('', 10002)
    serverSock.listen()
    
    server = server.server(serverSock)
    server.daemon = True
    server.start()
    
    client = client.client(server, serverSock)
    client.daemon = True
    client.start()
    
    try:
        while (server.isAlive() and client.isAlive()):
            pass
    except Exception, e:
        print "Exception encountered: %s. Stopping server..." % e
        server.stop()
        client.stop()
        
    server.stop()
    client.stop()
    print "Done."