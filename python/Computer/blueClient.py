import blueSock, threading, stellariumServer, json, select

class blueClient(threading.Thread):
    def __init__(self, blueSock, stellariumServer):
        self.blueSock = blueSock
        self.stellariumServer = stellariumServer
        self.alive = True 
        threading.Thread.__init__(self)

	def run(self):
		print "Starting Blue Client service..."
		try:
			while (self.alive and self.blueSock.alive and self.stellariumServer.alive):
				[Ra,Dec] = self.receiveCoords(10000)
				if (Ra != None):
					self.stellariumServer.updateCoords(Ra, Dec)
                #time.sleep(1)
		except Exception, e:
			print "Blue Client exception ", e.message
		
		self.stop()
		
	def receiveCoords(self,timeout):
		try:
			incomingData = None
			#print "Waiting for data from {0}...".format(self.sock.host)
			[read,write,ex] = select.select([self.blueSock.socket], [], [], timeout)
			if not read:
				return incomingData
			incomingData = self.blueSock.receiveData()
			decoded = json.loads(incomingData)
			if (decoded['code'] == 3):
				return (decoded['NewRa'], decoded['NewDec'])

			print "Invalid or empty code sent: ", decoded['3']
			return None
		except Exception, e:
			print "Failed to receive data from {0}: {1}".format(self.blueSock.address, e)
			
	def stop(self):
		self.alive = False
		self.blueSock.close()