from myarray import Array

theCounters = Array( 127 )
theCounters.clear( 0 )

theFile = open( 'atextfile.txt', 'r' )
for line in theFile:
    for letter in line:
        code = ord( letter )
        theCounters[code] += 1

theFile.close()

#Print the results. The uppercase letters have ASCII values in the
# range 65..90 and the lowercase letters are in the range 97..122.
for i in range( 26 ):
    print("%c - %4d     %c - %4d" % (chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]))
