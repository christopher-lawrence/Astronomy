import math

MAX_RA_VALUE = 0x80000000
MAX_DEC_VALUE = 0x40000000

def degreesToDecimal(degrees, minutes = 0, seconds = 0):
    total = 0.0
    secondsAbs = abs(seconds)
    minutesAbs = abs(minutes)
    degreesAbs = abs(degrees)
    if (secondsAbs > 0):
        total += secondsAbs/60.0
    if (minutesAbs > 0):
       total = ((minutesAbs + total)/60.0)
    total += degreesAbs
    if (degrees < 0 or minutes < 0 or seconds < 0):
        return total * -1
    return total

def decimalToDegrees(decimal):
    total = abs(decimal) * 3600
    seconds = round((total % float(60)), 2)
    # If we round up to 60, add to the total seconds
    if (seconds == 60):
        seconds = 0
        total += 1
    minutes = math.trunc(total/float(60)) % 60 
    degrees = math.trunc(total/3600)
    if (decimal < 0):
        return degrees * -1, minutes, seconds
    return degrees, minutes, seconds

def hoursToDegrees(hours):
    conversion = hours*15
    hour = math.trunc(conversion)
    # Take the fraction portion * 60
    mins = math.modf(conversion)[0] * 60
    secs = round((math.modf(mins)[0] * 60), 2)
    mins = math.trunc(mins)
    if (secs == 60.0):
	mins += 1
	secs = 0
    degrees = math.trunc(conversion) 
    if (mins == 60):
	degrees += 1
	mins = 0
    return degrees, mins, secs    

def degreesToHours(degrees, mins, secs):
    total = float(degrees)
    total += float(mins) / 60.0 
    total += float(secs) / 60.0 /60.0
    return total / 15

def stellariumToPiRa(value):
    conversion = value * (12.0/MAX_RA_VALUE)
    return hoursToDegrees(conversion)

def piToStellariumRa(degrees, mins, secs):
    conversion = degreesToHours(degrees, mins, secs)
    conversion = conversion*MAX_RA_VALUE
    return math.trunc(conversion/12)
    
def stellariumToPiDec(value):
    conversion = value * (90.0/MAX_DEC_VALUE)
    return decimalToDegrees(conversion)
    
def piToStellariumDec(degrees, mins, secs):
    conversion = degreesToDecimal(degrees, mins, secs)
    conversion = conversion*MAX_DEC_VALUE
    return math.trunc(conversion/90)

def convertTwosCompliment(self, val):
    if (val & (1<<(16 - 1)) != 0):
        val = val - (1<<16)
    if val == -4096: return val
    return round(val * self.gain)
