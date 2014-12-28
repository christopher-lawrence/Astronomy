from lightblue import *

class blueSock(object):
	def __init__(self):
		self.socket = socket()
		self.alive = True
		self.clientAddress = None
		self.connection = -1
		self.isServer = False

	def startService(self, port = "", channel = 0):
		print "Starting service 'RPi Bluetooth'..."
		self.isServer = True
		self.socket.bind((port,channel))
		self.socket.listen(1)
		advertise("RPi Bluetooth", self.socket,RFCOMM)
		self.connection, self.clientAddress = self.socket.accept()
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
		print "(blue)Sending data ", data
		if (self.isServer):
			self.connection.send(data)
		else:
			self.socket.send(data)

	def receiveData(self):
		print "(blue)Receiving data..."
		if (self.isServer):
			return self.connection.recv(1024)
		return self.socket.recv(1024)

	def close(self):
		self.alive = False
		if (self.connection != -1):
			self.connection.close()
		self.socket.close()
