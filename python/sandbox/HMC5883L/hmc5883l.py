import smbus, conversions, math

class HMC5883L(object):
    REGA    = 0x00
    REGB    = 0x01
    MODEREG = 0x02
    DOX     = 0x03
    DOZ     = 0x05
    DOY     = 0x07
    STAT    = 0x09
    IDENTA  = 0x10
    IDENTB  = 0x11
    IDENTC  = 0x12

    ## Register A configs

    # Samples to average per measurement
    SAMPLE_1    = 0x0 # Default
    SAMPLE_2    = 0x1
    SAMPLE_4    = 0x2
    SAMPLE_8    = 0X3
    SAMPLE_OFFSET = 0x5

    # Data output rate (Hz)
    OUTPUT_075  = 0x0
    OUTPUT_1_5  = 0x1
    OUTPUT_3    = 0x2
    OUTPUT_7_5  = 0x3
    OUTPUT_15   = 0x4 # Default
    OUTPUT_30   = 0x5
    OUTPUT_75   = 0x6
    OUTPUT_RES  = 0x7 # Reserved
    OUTPUT_OFFSET = 0x2

    # Measurement mode
    MODE_NORMAL = 0x0 # Default
    MODE_POS_BIAS = 0x1
    MODE_NEG_BIAS = 0x2
    MODE_RESERVED = 0x3 # Reserved
    MODE_OFFSET   = 0x0 

    ## Register B configs

    # Gain
    GAIN_088    = 0x0
    GAIN_1_3    = 0x1
    GAIN_1_9    = 0x2
    GAIN_2_5    = 0x3
    GAIN_4_0    = 0x4
    GAIN_4_7    = 0x5
    GAIN_5_6    = 0x6
    GAIN_8_1    = 0x7
    GAIN_OFFSET = 0x5
    GAIN = {
        GAIN_088: 0.73,
        GAIN_1_3: 0.92,
        GAIN_1_9: 1.22,
        GAIN_2_5: 1.52,
        GAIN_4_0: 2.27,
        GAIN_4_7: 2.56,
        GAIN_5_6: 3.03,
        GAIN_8_1: 4.35}

    ## Mode Register configs

    # High speed I2C mode (3400kHz)
    HIGHSPEED_I2C_ENABLED = 0x1
    HIGHSPEED_I2C_DISABLED = 0x0

    # Operating mode
    OP_CONTINUOUS   = 0x0
    OP_SINGLE       = 0x1
    OP_IDLE1        = 0x2
    OP_IDLE2        = 0x3

    # Misc
    GAUSS_LSB_XY    = 1090.0
    GAUSS_LSB_Z     = 920.0
    SENSORS_GAUSS_TO_MICROTESLA = 100

    def __init__(self, port=1, address=0x1E, declination=(9,12)):
        self.bus = smbus.SMBus(port)
        self.address = address
        (degrees, minutes) = declination
        self.decDegrees = degrees
        self.decMinutes = minutes
        self.declination = conversions.degreesToDecimal(degrees, minutes)
        self.SetConfiguration()

    def SetConfiguration(self, gain=GAIN_1_3, sampleRate=SAMPLE_8, dataRate=OUTPUT_15, mode=MODE_NORMAL, operationMode=OP_CONTINUOUS):
        configA = 0x0
        configA |= sampleRate<<self.SAMPLE_OFFSET
        configA |= dataRate<<self.OUTPUT_OFFSET
        configA |= mode<<self.MODE_OFFSET
        self.bus.write_byte_data(self.address, self.REGA, configA) 
        self.SetGain(gain)
        self.SetMode(operationMode)

    def SetGain(self, gain=GAIN_1_3):
        self.bus.write_byte_data(self.address, self.REGB, (gain<<self.GAIN_OFFSET))  
        self.gain = self.GAIN[gain]
    
    def SetMode(self, mode=MODE_NORMAL):
        self.bus.write_byte_data(self.address, self.MODEREG, (mode<<self.MODE_OFFSET)) 

    def GetHeading(self):
        output = self.__readOutputData()
        rawX = (output[0] << 8 | output[1])
        rawY = (output[4] << 8 | output[5])
        rawZ = (output[2] << 8 | output[3])
        twoX = self.ConvertTwosCompliment(rawX)
        twoY = self.ConvertTwosCompliment(rawY)
        twoZ = self.ConvertTwosCompliment(rawZ)
        print 'rawX, rawY, rawZ', (rawX, rawY, rawZ)
        print 'twoX, twoY, twoZ', (hex(self.ConvertTwosCompliment(rawX)), hex(self.ConvertTwosCompliment(rawY)), hex(self.ConvertTwosCompliment(rawZ)))
        x = (twoX / self.GAUSS_LSB_XY * self.SENSORS_GAUSS_TO_MICROTESLA)
        y = (twoY / self.GAUSS_LSB_XY * self.SENSORS_GAUSS_TO_MICROTESLA)
        z = (twoZ / self.GAUSS_LSB_Z * self.SENSORS_GAUSS_TO_MICROTESLA)
        #x = self.ConvertTwosCompliment((output[0] << 8 | output[1]))  
        #y = self.ConvertTwosCompliment((output[4] << 8 | output[5])) * -1
        #z = self.ConvertTwosCompliment((output[2] << 8 | output[3])) * -1
        return (x, y, z)
        #return (((output[0] << 8) | output[1]), ((output[4] << 8) | output[5]), ((output[2] << 8) | output[3]))

    def GetCoordinatesDecimal(self):
        (x, y, z) = self.GetHeading()
        return (self.HeadingCoords(y, x), self.HeadingCoords(x,z))

    def __readOutputData(self):
        output = []
        i=0
        while i<6:
            result = self.bus.read_byte_data(self.address, self.DOX+i)
            # Give this a try...i have a feeling this is going to mess with the results, however
            #if (result > 127):
            #    print "Subtracting 256 from ", result
            #    result = result - 256
            #print "%d: %s" %(i, hex(result))
            output.append(result)
            i += 1
        return output
    
    def ConvertTwosCompliment(self, val):
        if (val & (1<<(16 - 1)) != 0):
            val = val - (1<<16)
        if val == -4096: return val
        return val
        #return round(val * self.gain)

    def HeadingCoords(self, x, y, isDec = False):
        headingRad = math.atan2(x, y)
        #if not isDec:
        #    headingRad += math.radians(self.declination)
        #    if headingRad > 2*math.pi:
        #        headingRad -= 2*math.pi
        return math.degrees(headingRad) 
