import json, blueSock, time

sock = blueSock.blueSock()
sock.address = '10:40:F3:7C:8D:95'
sock.channel = 1
sock.connect()

data = json.dumps({'code':1, 'coords':"Some coords"})

time.sleep(10)
sock.sendData(data)

sock.close()
