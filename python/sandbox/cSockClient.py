import socks, threading, json

class client(threading.Thread):
	def __init__(self, sock):
		self.sock = sock
		threading.Thread.__init__(self)
		data = json.dumps({'code':1, 'message':"stellarium"})
		
	def run(self):
		print "Starting client..."
        try:
            while(self.alive and self.sock.alive):
                if (self.Ra != self.NewRa and self.Dec != self.NewDec):
                    self.sendData()
                    #time.sleep(1)
        except Exception as e:
            print "Server exception ", e.message
            
    def sendData(self):
    	
    	
# handshake
# {'code':1, 'message':"stellarium"}
# send current declination(??)
# {'code':2, 'message':"declination"}
# send current coords
# {'code':3, 'message':"coords"}
# error
# {'code':100, 'message':"Error"}