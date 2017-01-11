# encoding: utf8
# project 1.8

import math

class Point:
    def __init__( self, x, y ):
        self.xCoord = x
        self.yCoord = y

class LineSegment:
    def __init__( self, ptA, ptB ):
        self._ptA = ptA
        self._ptB = ptB

    def endPointA( self ):
        return self._ptA

    def endPointB( self ):
        return self._ptB

    def __len__( self ):
       math.sqrt( math.pow( self._ptA.xCoord - self._ptB.xCoord, 2 ) + \
            math.pow( self._ptA.yCoord - self._ptB.yCoord, 2 ) )

    def __str__( self ):
        return "(%.2f, %.2f)#(%.2f, %.2f)" % ( self._ptA.xCoord, self._ptA.yCoord, self._ptB.xCoord, self._ptB.yCoord )

    def isVertical( self ):
        return self._ptA.xCoord == self._ptB.xCoord

    def isHorizontal( self ):
        return self._ptA.yCoord == self._ptB.yCoord

    # 判断斜率相等
    def isParallel( self, otherLine ):
        r1 = ( self._ptA.xCoord - self._ptB.xCoord ) / ( self._ptA.yCoord - self._ptB.yCoord )
        r2 = ( otherLine._ptA.xCoord - otherLine._ptB.xCoord ) / ( otherLine._ptA.yCoord - otherLine._ptB.yCoord )
        return r1 == r2

    def isPerpendicular( self, otherLine ):
        if self._ptA.yCoord == self._ptB.yCoord and otherLine._ptA.xCoord == otherLine._ptB.xCoord:
            return True

        if self._ptA.xCoord == self._ptB.xCoord and otherLine._ptA.yCoord == otherLine._ptB.yCoord:
            return True

        r1 = ( self._ptA.xCoord - self._ptB.xCoord ) / ( self._ptA.yCoord - self._ptB.yCoord )
        r2 = ( otherLine._ptA.xCoord - otherLine._ptB.xCoord ) / ( otherLine._ptA.yCoord - otherLine._ptB.yCoord )

        if r1 * r2 == -1:
            return True

        return False

    def intersects( self, otherLine ):
        return !self.isParallel(otherLine)


    def shift(self, xInc, yInc):
        self._ptA.xCoord += xInc
        self._ptA.yCoord += yInc
        self._ptB.xCoord += xInc
        self._ptB.yCoord += yInc

    def midpoint(self):
        x = (self._ptA.xCoord + self._ptB.xCoord)/2.0
        y = (self._ptA.yCoord + self._ptB.yCoord)/2.0
        return Point(x, y)
