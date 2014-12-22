import serial
import time

while True:
	try:
		ser = serial.Serial("/dev/tty.Bluetooth-Incoming-Port", 9600, timeout = 3)
		ser.write("?\r")
		print ser.readline()
		ser.close()
		time.sleep(10)
	except Exception as e:
		print e