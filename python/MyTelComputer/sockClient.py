import stellariumConnect as stellariumConnect
import socket

class sockClient(object)
    def __init__(self,host,port)
        self.serverAddress=(host,port)
        # Create a TCP/IP socket
        self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.connect()
    
    def connect(self):
        try:
            # Create the client socket
            self.clientSock.connect((host, port))
            
            ##HandShake
            try:
                while True:
                    self.clientSock.send("iTelRaspberry I presume")
                    data = self.clientSock.recv(1024)
                    if len(data) == 0: 
                        pass
                    elif data=="iTelComputer I presume":
                        print ( "Connected to iTelRaspberryServer")
                        self.connected = True
                        break            
            except IOError as e:
                print ( "Handshake failed, %s" % e.message)
        except IOError as e:
                print ( "Connection failed %s" % e.message)
            
    def stellariumMode(self,stelCom):
        stellariumMode(self.clientSock,stelCom)

class stellariumMode(object):
    def __init__(self,clientSock,stelCom):
        self.clientSock = clientSock.connection
        self.stelCom = stelCom
        self.theQuitCall = quitter.quitter("The Stellarium server")
        self.theQuitCall.start()
        try:
            self.stelReceiver = stellariumReceive(stelCom)
            self.stelReceiver.start()
            
            while self.theQuitCall.alive:
                self.reportingLoop()
                self.clientSock.send("0")
                completion = self.clientSock.recv(1024)
                if completion != "reportingComplete":
                    print ( "Error: the iTelRaspberry server did not confirm completion of reporting mode")
                
                if self.stelReceiver.hasTarget:
                    self.sendTarget()
                else:
                    break
            
            self.stelReceiver.endThread()              
            self.stelCom.closeConnection() 
            
        except IOError as e:
            self.clientSock.send("0")
            self.stelReceiver.endThread() 
            self.stelCom.closeConnection()
            print ( "Sending time failed, check connection %s" % e.message)
    
    def reportingLoop(self):
        self.clientSock.send("report")
        while self.theQuitCall.alive:
                reading = self.clientSock.recv(1024)
                radecS  = reading.split(":")
                Ra = angles.Angle(r=float(radecS[0]))
                Dec = angles.Angle(r=float(radecS[1]))
                self.stelCom.sendStellariumCoords(Ra,Dec)
                
                if(self.stelReceiver.hasTarget):
                    break
                else:
                    self.clientSock.send("1")      
    
    def sendTarget(self):
        target = self.stelReceiver.getTargetString()
        try:
            self.clientSock.send("goTo")
            answer = self.clientSock.recv(1024)
            if answer == "receivingTarget":
                self.clientSock.send(target)
                self.stelReceiver.targetReceived()
                completion = self.clientSock.recv(1024)
                if completion != "targetReceived":
                    print ( "Error: the iTelRaspberry server did not confirm receipt of the target star")
            else:
                print ( "Error: the iTelRaspberry server did not want to receive the target star")
        except IOError as e:
            print ( "Sending time failed, check connection %s" % e.message)