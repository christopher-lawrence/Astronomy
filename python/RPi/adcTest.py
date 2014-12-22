from Adafruit_ADS1x15 import ADS1x15
from time import sleep

adc = ADS1x15()

while True:
    result = adc.readADCSingleEnded(0)
    print result
    sleep(.5)

