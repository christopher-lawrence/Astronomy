import socks, threading, server

class client(threading.Thread):
	def __init__(self, server, sock)
		self.server = server
		self.sock = sock
		thead.Threading.__init__(self)
	
	def run(self)
		# TODO
	
	def receiveCoords(self, timeout)
		incomingData = self.receiveStellariumData(timeout)
        if (incomingData != None) and (len(incomingData) != 0):
        #if (len(incomingData) != 0):
            print ("Incoming data[%d]: ", (len(incomingData),incomingData))
            data = struct.unpack("3iIi", incomingData)
            print("Unpacked data: Length:%d Type:%d Time:%d RA: %d Dec: %d" % (data[0], data[1], data[2], data[3], data[4]))
            [Ra,Dec] = self.stellariumToAngle(data[3], data[4])
            
            return [Ra,Dec]
        else:
            return [False,False]