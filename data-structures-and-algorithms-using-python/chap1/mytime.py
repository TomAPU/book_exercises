# Project 1.6

class Time:
    def __init__( self, hours, minutes, seconds ):
        assert 0 <= hours <= 23, "Hour: [0~23]"
        assert 0 <= minutes <= 59, "Minute: [0~59]"
        assert 0 <= seconds <= 59, "Second: [0~59]"
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def hours( self ):
        return self._hours

    def minutes( self ):
        return self._minutes

    def seconds( self ):
        return self._seconds

    def _totalSeconds( self ):
        return self._hours * 60 * 60 + self._minutes * 60 + self._seconds

    def numSeconds( self, otherTime ):
        r = self._totalSeconds() - otherTime._totalSeconds()
        if r < 0:
            return -r
        return r

    def isAM( self ):
        if self._hours < 12:
            return True
        return False

    def isPM( self ):
        if self._hours >= 12:
            return True

        return False

    def __eq__( self, otherTime ):
        return self._totalSeconds() == otherTime._totalSeconds()

    def __gt__( self, otherTime ):
        return self._totalSeconds() > otherTime._totalSeconds()

    def __str__( self ):
        return "%02d:%02d:%02d" % ( self._hours, self._minutes, self._seconds )

if __name__ == '__main__':
    try:
        t = Time(42, 23, 4)
    except AssertionError as e:
        print ('AssertionError: ', e)

    t = Time(15, 23, 4)
    print( "Hours: ", t.hours())
    print( "Minutes: ", t.minutes())
    print( "Seconds: ", t.seconds())

    ot = Time( 16, 23, 4)
    print( "NumSeconds: ", t.numSeconds( ot ))
    print( "isAM: ", t.isAM())
    print( "isPM: ", t.isPM())
    print( 't=', t)

    print( 't==ot', t == ot)
