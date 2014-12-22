from lightblue import *

s = socket()
s.bind(("",7))
s.listen(1)
advertise("RPi Service", s,RFCOMM)

print "Listening on %s port %s" % (s.getsockname()[0], s.getsockname()[1])

conn, addr = s.accept()
print "Connected by", addr
result = conn.recv(1024)
conn.send('WTF?!?')
print "Result: ", result
conn.close()
s.close()

