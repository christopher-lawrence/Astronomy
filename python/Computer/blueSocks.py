from lightblue import *

class blueSock(object):
	def __init__(self):
		self.socket = socket()
        self.connected = False
		
	def connect(self):
		print "Connecting..."
		self.findService()
		self.socket.connect((self.address, self.channel))
        self.connected = True
		
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