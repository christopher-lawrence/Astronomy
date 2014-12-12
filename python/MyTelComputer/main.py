import stellariumConnect as stellariumConnect
from blueClient import blueClient
import threading, time
#from configParser import configParser

class stellariumReceive(threading.Thread):
    def __init__(self,stelCom):
        self.stelCom = stelCom
        #self.stelMod = stelMod
        threading.Thread.__init__(self)
        self.alive = True
        self.target = None
        self.hasTarget = False
        
    def run(self):
        print("Starting receiver...")
        self.alive = True
        try:
            while self.alive:
                targ = self.stelCom.receiveStellariumCoords(5)
                if targ[0]!= False:
                    self.newTarget(targ)
                    self.getTargetString()
                    #self.stelCom.sendStellariumCoords(targ[0],targ[1])
                #else:
                #    print ("No coordinates received")
                #    sleep(1)
                
        except IOError as e:
            print ("Error in receiving coordinates from Stellarium: %s" % e.message)
                    
        
    def newTarget(self,targ):
        self.target = targ
        self.hasTarget = True
        
    def getTargetString(self):
        tString = "%02f:%02f" % (self.target[0].r,self.target[1].r)
        print("Target string: %s\n" % tString)
        return tString
        
    def targetReceived(self):
        self.hasTarget = False   
        
    def endThread(self):
        self.alive = False  

if __name__ == '__main__':
    host = "localhost"
    port = 10002
    #while(True):
    print ("** Here we go...")
    #theClient = sockClient()
    stelCom = stellariumConnect.stellariumConnect(host, port)
    stelCom.handshakeStellarium()
    #theClient.stellariumMode(stelCom)
    stelReceiver = stellariumReceive(stelCom)
    stelReceiver.start()
    try:
        while(True):
            sleep(1)
    except:
        print ("Done.")
        
 
    