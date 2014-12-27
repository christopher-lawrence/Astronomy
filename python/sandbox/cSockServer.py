import socks, sys, threading
    	
class server(threading.Thread):
	def __init__(self, sock):
		self.sock = sock
		threading.Thread.__init__(self)
		
	def run(self):
		print "Starting client..."
        try:
            while True:
                data = self.receiveData(10000)
                if (data == None):
                	pass;
                print("Data: ", data)
                #time.sleep(1)
        except Exception, e:
            print "Client exception ", e.message

	def receiveData(self, timeout):
		try:
            #print "Waiting for data from {0}...".format(self.sock.host)
			[read,write,ex] = select.select([self.sock.connection], [], [], timeout)
			if not read:
				return None
			incomingData = self.sock.recieveData()
			return incomingData
		except Exception, e:
			print "Failed to receive data: {0}".format(e)
			
	def stop(self):
		self.sock.stop()
    	
if __name__ == '__main__':
	serverSock = socks.socks('', 10002)
	serverSock.listen()
	
	server = server(serverSock)
	server.daemon = True
	server.start()
	