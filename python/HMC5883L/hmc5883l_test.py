import hmc5883l, sys, time, conversions, math

if __name__ == '__main__':
    compass = hmc5883l.HMC5883L()
    while True:
        (x,y,z) = compass.GetHeading()
        print 'x, y, z', (x, y, z)
        (Ra, Dec) = compass.ObtainRaDec(x, y, z)
        #print 'Ra: ', conversions.decimalDegreesToHMS(math.degrees(Ra))
        print 'Ra: ', conversions.decimalToDegrees(math.degrees(Ra))
        print 'Dec: ', conversions.decimalToDegrees(math.degrees(Dec))
        time.sleep(0.5)
