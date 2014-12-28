import blueSocks, json

blueSock = blueSocks.blueSocks()
blueSock.connect()

data = json.dumps({'code':1, 'coords':"some coords"})

blueSock.sendData(data)

data  = blueSock.receiveData()

print "Data received: ", data
