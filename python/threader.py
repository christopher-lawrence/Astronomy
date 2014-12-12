import threading

class threader(threading.Thread):
	def __init__(self):
		self.Count = 0
		self.Changed = False
		self.Alive = True
		threading.Thread.__init__(self)
		
	def run(self):
		print "Count: ", self.Count
		print
		try:
			while self.Alive:
				if (self.Changed):
					print "Count: ", self.Count
					print
					self.Changed = False
		except Exception as e:
			print("Exception: ", e.message)
			
	def increment(self):
		self.Count = self.Count + 1
		self.Changed = True
		
	def decrement(self):
		if (self.Count > 0):
			self.Count = self.Count - 1
		self.Changed = True			
			
	def quit(self):
		print("Killing thread")
		self.Alive = False
			
if __name__ == '__main__':
	try:
		thread = threader()
		thread.start()
	
		input = None
		while (input != 'q'):
			if (input == 'w'):
				thread.increment()
			elif (input == 's'):
				thread.decrement()
			else:
				pass
			input = raw_input("'w' to incriment, 's' to decriment, 'q' to quit: ")
		thread.quit()
	except:
		if (thread != None):
			thread.quit()
		
		