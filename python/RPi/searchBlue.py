#from lightblue import *
import bluetooth

#devices = finddevices(getnames=True, length=10)
devices = bluetooth.discover_devices(lookup_names=True)

for dev in devices:
    print "Found: ", dev
