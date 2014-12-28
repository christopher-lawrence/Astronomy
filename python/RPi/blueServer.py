from lightblue import *
import json

s = socket()
s.bind(("",7))
s.listen(1)
advertise("RPi Bluetooth", s,RFCOMM)

print "Listening on %s port %s" % (s.getsockname()[0], s.getsockname()[1])

conn, addr = s.accept()
print "Connected by", addr
#result = conn.recv(1024)
[result,write,ex] = select.select([conn], [], [], timeout)
conn.send('WTF?!?')

decoded = json.loads(result)

print "Result: ", decoded['code'] 
conn.close()
s.close()

