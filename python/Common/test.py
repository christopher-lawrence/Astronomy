import conversions

if __name__ == '__main__':
    print 'degreesToDecimal(182, 31, 27)'
    value1 = conversions.degreesToDecimal(182, 31, 27)
    print 'value: ', value1
    print 'Pass: ',  round(value1, 6) == round(182.524166667, 6)

    print '\ndegreesToDecimal(-182, 32, 27)'
    value2 = conversions.degreesToDecimal(-182, 31, 27)
    print 'value: ', value2
    print 'Pass: ', round(value2, 6) == round(-182.524166667, 6)
    
    print "\ndecimalToDegrees(182.5241667)"
    value3 = conversions.decimalToDegrees(182.5241667)
    print 'value: ', value3
    print 'Pass: ', value3 == (182, 31, 27.0)

    print "\ndecimalToDegrees(-182.5241667)"
    value4 = conversions.decimalToDegrees(-182.5241667)
    print 'value: ', value4
    print 'Pass: ', value4 == (-182, 31, 27.0)

    print '\nstellariumToPiRa(3960111917)'
    value5 = conversions.stellariumToPiRa(3960111917)
    print 'value: ', value5
    print 'Pass: ', value5 == (331, 55, 57.89)

    print '\npiToStellariumRa(331, 55, 57.89)'
    value6 = conversions.piToStellariumRa(331, 55, 57.89)
    print 'value: ', value6
    print 'Pass: ', value6 == 3960111927

    # 11930464 == 1 degree
    print '\nstellariumToPiRa(11930464)'
    value7 = conversions.stellariumToPiRa(11930464)
    print 'value: ', value7
    print 'Pass: ', value7 == (1, 0, 0)

    print '\nstellariumToPiRa(11930464*180)'
    value8 = conversions.stellariumToPiRa(11930464*180)
    print 'value: ', value8
    print 'Passs: ', value8 == (179, 59, 59.96)

    print '\nstellariumToPiDec(-199494690)'
    value9 = conversions.stellariumToPiDec(-199494690)
    print 'value: ', value9
    print 'Pass: ', value9 == (-16, 43, 17.23) 
    
    print '\npiToStellariumDec(-16, 43, 17.23)'
    value10 = conversions.piToStellariumDec(-16, 43, 17.23)
    print 'value: ', value10
    print 'Pass: ', value10 == -199494702
    
    # This is similar to test 9 -- checking to see what would happen if the number 
    # is only off by a few
    print '\nstellariumToPiDec(-199494702)'
    value11 = conversions.stellariumToPiDec(-199494702)
    print 'value: ', value11
    print 'Pass: ', value11 == (-16, 43, 17.23)

    print '\ndecimalDegreesToHMS(degrees)'
    value12 = conversions.decimalDegreesToHMS(144.0425)
    print 'value: ', value12
    print 'Pass: ', value12 == (9, 36, 10.2)
