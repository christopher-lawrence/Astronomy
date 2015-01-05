# HMC5888L Magnetometer (Digital Compass) wrapper class
# Based on https://bitbucket.org/thinkbowl/i2clibraries/src/14683feb0f96,
# but uses smbus rather than quick2wire and sets some different init
# params.

import smbus
import math
import time
import sys

class hmc5883l:

    __scales = {
        0.88: [0, 0.73],
        1.30: [1, 0.92],
        1.90: [2, 1.22],
        2.50: [3, 1.52],
        4.00: [4, 2.27],
        4.70: [5, 2.56],
        5.60: [6, 3.03],
        8.10: [7, 4.35],
    }

    def __init__(self, port=1, address=0x1E, gauss=1.3, declination=(0,0)):
        self.bus = smbus.SMBus(port)
        self.address = address

        (degrees, minutes) = declination
        self.__declDegrees = degrees
        self.__declMinutes = minutes
        self.__declination = (degrees + minutes / 60) * math.pi / 180

        (reg, self.__scale) = self.__scales[gauss]
        self.bus.write_byte_data(self.address, 0x00, 0x70) # 8 Average, 15 Hz, normal measurement
        self.bus.write_byte_data(self.address, 0x01, reg << 5) # Scale
        self.bus.write_byte_data(self.address, 0x02, 0x00) # Continuous measurement

    def declination(self):
        return (self.__declDegrees, self.__declMinutes)

    def twos_complement(self, val, len):
        # Convert twos compliment to integer
        if (val & (1 << len - 1)):
            val = val - (1<<len)
        return val

    def __convert(self, data, offset):
        val = self.twos_complement(data[offset] << 8 | data[offset+1], 16)
        if val == -4096: return None
        return round(val * self.__scale, 4)

    def axes(self):
        data = self.bus.read_i2c_block_data(self.address, 0x00)
        #print map(hex, data)
        #x = (self.__convert(data, 3))
        x = -(self.__convert(data, 3))
        y = self.__convert(data, 7)
        #z = (self.__convert(data, 5))
        z = -(self.__convert(data, 5))
        print "X: ", x
        print "Y: ", y
        print "Z: ", z
        return (x,y,z)

    def heading(self):
        (x, y, z) = self.axes()
        headingRad = math.atan2(y, x)
        headingRadYZ = math.atan2(y, z)
        # Not sure if this is needed....
        #headingRadXZ = math.atan2(x, z) + (32 * math.pi/180)
        headingRadXZ = math.atan2(x, z)
        #test = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        #headingRadXZ = math.atan2(z, test)
        #headingRad = math.atan2(y, z)
        headingRad += self.__declination
        headingRadYZ += self.__declination
        headingRadXZ += self.__declination

        #atanZ = math.asin(z)
        hypOP = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z,2))
        hypON = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        atanZ = math.acos(hypON/hypOP)
        if(atanZ < 0):
            atanZ += 2 * math.pi
        elif atanZ > 2 * math.pi:
            atanZ -= 2 * math.pi
        # Correct for reversed heading
        if headingRad < 0:
            headingRad += 2 * math.pi
        # Check for wrap and compensate
        elif headingRad > 2 * math.pi:
            headingRad -= 2 * math.pi

        if headingRadYZ < 0:
            headingRadYZ += 2 * math.pi
        elif headingRadYZ > 2 * math.pi:
            headingRadYZ -= 2 * math.pi
 
        if headingRadXZ < 0:
            headingRadXZ += 2 * math.pi
        elif headingRadXZ > 2 * math.pi:
            headingRadXZ -= 2 * math.pi
        # Convert to degrees from radians
        headingDeg = headingRad * 180 / math.pi
        headingDegYZ = headingRadYZ * 180 / math.pi
        headingDegXZ = headingRadXZ * 180 / math.pi
        atanZ = atanZ * 180 / math.pi
        return (headingDeg, headingDegYZ, headingDegXZ, atanZ)

    def degrees(self, headingDeg):
        degrees = math.floor(headingDeg)
        minutes = round((headingDeg - degrees) * 60)
        return (degrees, minutes)

    def __str__(self):
        (x, y, z) = self.axes()
        return "Axis X: " + str(x) + "\n" \
               "Axis Y: " + str(y) + "\n" \
               "Axis Z: " + str(z) + "\n" \
               #"Declination: " + self.degrees(self.declination()) + "\n" \
               #"Heading: " + self.degrees(self.heading()) + "\n"

if __name__ == "__main__":
    # http://magnetic-declination.com/Great%20Britain%20(UK)/Harrogate#
    #compass = hmc5883l(gauss = 4.7, declination = (9,11))
    compass = hmc5883l(gauss = 5.6, declination = (9,11))
    while True:
        #sys.stdout.write("\rHeading: " + str(compass.degrees(compass.heading())) + "     ")
        (headingYX, headingYZ, headingXZ, atanZ) = compass.heading()
        sys.stdout.write("\rHeadingYX: " + str(compass.degrees(headingYX)) + "\n\rHeadingYZ: " + str(compass.degrees(headingYZ)) + "\n\rHeadingXZ: " + str(compass.degrees(headingXZ)) + "\n\ratanZ: " + str(compass.degrees(atanZ)))
        #sys.stdout.write("\rHeading: " + str(compass.degrees(compass.heading())) + "     ")
#        sys.stdout.write(str(compass))
        sys.stdout.flush()
        time.sleep(0.5)

