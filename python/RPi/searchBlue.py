from lightblue import *

devices = finddevices(getnames=True, length=10)

for dev in devices:
    print "Found: ", dev
