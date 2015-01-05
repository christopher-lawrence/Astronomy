import hmc5883l, sys, time

if __name__ == '__main__':
    compass = hmc5883l.HMC5883L()
    while True:
        (x,y,z) = compass.getHeading()
        convertX = -compass.convert_twos_compliment(x)
        convertY = compass.convert_twos_compliment(y)
        convertZ = -compass.convert_twos_compliment(z)
        if (x == -4096):
            print "X: failed!"
        else:
            print "X: %d - %d"  %(x, convertX)
        if (y == -4096):
            print "Y: failed!"
        else:
            print "Y: %d - %d" %(y, convertY)
        if (z == -4096):
            print "Z: failed!"
        else:
            print "Z: %d - %d" %(z, convertZ)
        print "XY: ", compass.headingCoords(convertX, convertY)
        print "YZ: ", compass.headingCoords(convertY, convertZ)
        print "XZ: ", compass.headingCoords(convertX, convertZ)
        #sys.stdout.flush()
        time.sleep(0.5)
