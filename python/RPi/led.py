import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led = 23

GPIO.setup(led, GPIO.OUT)

try:
	while(True):
		GPIO.output(led, 1)
		print(GPIO.input(led))
		time.sleep(.01)
		GPIO.output(led, 0)
		print(GPIO.input(led))
		time.sleep(.1)
except KeyboardInterrupt:
	GPIO.cleanup()
