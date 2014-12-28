from lightblue import *

class blueSock(object):
	def __init__(self, isServer = False):
		self.socket = socket()
        self.alive = True
        self.connection = -1
        self.clientAddress = None
		
    def startService(self, port="", channel=0):
        print "Starting service 'RPi Bluetooth'..."
        self.socket.bind((port,channel))
        s.socket.listen(1)
        advertise("RPi Bluetooth", s,RFCOMM)
        self.connection, self.clientAddress = s.accept()
        print "Connected by ", self.clientAddress
    
	def connect(self):
		print "Connecting..."
		self.findService()
		self.socket.connect((self.address, self.channel))
		
	def findService(self):
		print "Finding service..."
		while True:
			services = findservices(name="RPi Bluetooth")
			if (len(services) > 0):
				self.address = services[0][0]
				self.channel = services[0][1]
				print "Service found"
				break;
		
	def sendData(self, data):
		print "Sending data ", data
		self.socket.send(data)
	
	def receiveData(self):
		return self.socket.recv(1024)
    
    def close(self):
        self.alive = False
        if (self.connection != -1):
            self.connection.close()