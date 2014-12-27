from lightblue import *

class cBlueServer(object):
	def __init__(self):
		self.socket = socket()
		self.connected = False
		
	def connect(self):
		self.socket.bind(("",0))
		self.socket.listen(1)
		advertise("RPi Bluetooth", self.socket,RFCOMM)
		print "Listening on %s port %s" % (self.socket.getsockname()[0], self.socket.getsockname()[1])
		self.connection, self.clientAddress = self.socket.accept()
		print "Connect to ", self.clientAddress
		self.connected = True
	
	def close(self):
		self.connection.close()
		self.socket.close()
		
if __name__ == '__main__':
	server = cBlueServer()
	while not server.connected:
		server.connect()
	server.close()