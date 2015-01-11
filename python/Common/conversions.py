import math

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

def ConvertTwosCompliment(self, val):
    if (val & (1<<(16 - 1)) != 0):
        val = val - (1<<16)
    if val == -4096: return val
    return round(val * self.gain)
