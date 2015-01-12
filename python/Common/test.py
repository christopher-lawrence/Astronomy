import conversions

if __name__ == '__main__':
    print 'degreesToDecimal(182, 31, 27)'
    value1 = conversions.degreesToDecimal(182, 31, 27)
    print 'value: ', value1

    print '\ndegreesToDecimal(-182, 32, 27)'
    value2 = conversions.degreesToDecimal(-182, 31, 27)
    print 'value: ', value2
    
    print "\ndecimalToDegrees(182.5241667)"
    value3 = conversions.decimalToDegrees(182.5241667)
    print 'value: ', value3

    print "\ndecimalToDegrees(-182.5241667)"
    value4 = conversions.decimalToDegrees(-182.5241667)
    print 'value: ', value4

    print '\nstellariumToPiRa(3960111917)'
    value5 = conversions.stellariumToPiRa(3960111917)
    print 'value: ', value5

    print '\npiToStellariumRa(331, 55, 57.89)'
    value6 = conversions.piToStellariumRa(331, 55, 57.89)
    print 'value: ', value6

    # 11930464 == 1 degree
    print '\nstellariumToPiRa(11930464)'
    value7 = conversions.stellariumToPiRa(11930464)
    print 'value: ', value7

    print '\nstellariumToPiRa(11930464*180)'
    value8 = conversions.stellariumToPiRa(11930464*180)
    print 'value: ', value8
