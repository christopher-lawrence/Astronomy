import server, socks, time

if __name__ == '__main__':
    sock = socks.socks("localhost", 10002)
    sock.listen()
    
    server = server.server(sock)
    server.start()
    
    try:
        while (server.alive):
            time.sleep(1)
    except Exception, e:
        print "Exception encountered: %s. Stopping server..." % e
        server.stop()
        print "Done."