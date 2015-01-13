import hmc5883l, sys, time, conversions

if __name__ == '__main__':
    compass = hmc5883l.HMC5883L()
    while True:
        (x,y,z) = compass.GetHeading()
        #convertX = -compass.ConvertTwosCompliment(x)
        #convertY = compass.ConvertTwosCompliment(y)
        #convertZ = -compass.ConvertTwosCompliment(z)
        #if (x == -4096):
        #    print "X: failed!"
        #else:
        #    print "X: %d - %d"  %(x, convertX)
        #if (y == -4096):
        #    print "Y: failed!"
        #else:
        #    print "Y: %d - %d" %(y, convertY)
        #if (z == -4096):
        #    print "Z: failed!"
        #else:
        #    print "Z: %d - %d" %(z, convertZ)
        #print "XY: ", conversions.decimalToDegrees(compass.headingCoords(convertX, convertY))
        #print "YZ: ", conversions.decimalToDegrees(compass.headingCoords(convertY, convertZ))
        #print "XZ: ", conversions.decimalToDegrees(compass.headingCoords(convertX, convertZ))
        #sys.stdout.flush()
        (ra, dec) = compass.GetCoordinatesDecimal()
        print 'x, y, z', (x, y, z)
        print 'Ra: ', ra
        print 'Dec: ', dec
        #print 'Ra: ', conversions.decimalToDegrees(ra)
        #print 'Dec: ', conversions.decimalToDegrees(dec)
        time.sleep(0.5)
