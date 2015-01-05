import conversions

if __name__ == '__main__':
    print 'degreesToDecimal(182, 31, 27)'
    value1 = conversions.degreesToDecimal(182, 31, 27)
    print 'value: ', value1

    print 'degreesToDecimal(-182, 32, 27)'
    value2 = conversions.degreesToDecimal(-182, 31, 27)
    print 'value: ', value2
    
    print "\ndecimalToDegrees(182.5241667)"
    value3 = conversions.decimalToDegrees(182.5241667)
    print 'value: ', value3

    print "\ndecimalToDegrees(-182.5241667)"
    value4 = conversions.decimalToDegrees(-182.5241667)
    print 'value: ', value4
