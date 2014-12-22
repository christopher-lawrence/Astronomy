import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

input = 11
output = 23

GPIO.setup(input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(output, GPIO.OUT)
GPIO.output(output, GPIO.LOW)

try:
	while True:
		print(GPIO.input(input))
		GPIO.output(output, GPIO.input(input))

except KeyboardInterrupt:
	GPIO.cleanup()

