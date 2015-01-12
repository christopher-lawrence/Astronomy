import math

MAX_INT_VALUE = 0x7FFFFFFF+1

def degreesToDecimal(degrees, minutes = 0, seconds = 0):
    total = 0.0
    secondsAbs = abs(seconds)
    minutesAbs = abs(minutes)
    degreesAbs = abs(degrees)
    if (secondsAbs > 0):
        total = secondsAbs/float(60)
    if (minutesAbs > 0):
       total = ((minutesAbs + total)/float(60))
    total += abs(degreesAbs)
    if (degrees < 0 or minutes < 0 or seconds < 0):
        return -total
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
    secs = math.modf(mins)[0] * 60
    degrees = math.trunc(conversion) 
    return degrees, math.trunc(mins), round(secs, 2)    

def degreesToHours(degrees, mins, secs):
    total = float(degrees)
    total += float(mins) / 60.0 
    total += float(secs) / 60.0 /60.0
    return total / 15

def stellariumToPiRa(value):
    conversion = value * (12.0/MAX_INT_VALUE)
    return hoursToDegrees(conversion)

def piToStellariumRa(degrees, mins, secs):
    conversion = degreesToHours(degrees, mins, secs)
    conversion = conversion*MAX_INT_VALUE
    return math.trunc(conversion/12)

def convertTwosCompliment(self, val):
    if (val & (1<<(16 - 1)) != 0):
        val = val - (1<<16)
    if val == -4096: return val
    return round(val * self.gain)
