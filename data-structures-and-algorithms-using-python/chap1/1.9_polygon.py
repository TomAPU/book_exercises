import math

class Point:
    def __init__( self, x, y ):
        self.xCoord = x
        self.yCoord = y

class Polygon:
    def __init__( self, *vertices):
        assert len(vertices)>=3, "should not less than 3 vertices"
        self.vertices = vertices
