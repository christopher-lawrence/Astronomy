"""
Shows how to send "Hello world" over a RFCOMM client socket.
"""
import lightblue

# ask user to choose the device to connect to
#hostaddr = lightblue.selectdevice()[0]        

#print "Using address ", hostaddr

# find the EchoService advertised by the simple_server.py example
#hostaddr, serviceport, servicename = lightblue.selectservice()
#echoservice = lightblue.findservices(addr=hostaddr, name="RPi Service")[0]
#serviceport = echoservice[1]

#print "Connecting to address %s : %s" % (hostaddr, serviceport)

s = lightblue.socket()
s.connect(("00:1A:7D:DA:71:13", 7))
s.send("Hello world!")
print "Sent data, waiting for echo..."
data = ''
data = s.recv(1024)
print "Got data:", data
s.close()


# Note:
# Instead of calling selectdevice() and findservices(), you could do:
#       hostaddr, serviceport, servicename = lightblue.selectservice()
# to ask the user to choose a service (instead of just choosing the device).
