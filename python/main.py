import stellariumConnect as stellariumConnect

if __name__ == '__main__':
    host = "localhost"
    port = 10002
    while(True):
        print "** Here we go..."
        stelConn = stellariumConnect.stellariumConnect(host, port)
        stelConn.handshakeStellarium()