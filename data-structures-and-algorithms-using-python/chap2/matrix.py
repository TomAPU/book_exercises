from myarray import Array2D

class Matrix:
    def __init__( self, nrow, ncols ):
        self._theGrid = Array2D( nrow, ncols )
        self._theGrid.clear( 0 )

    def numRows( self ):
        return self._theGrid.numRows()

    def numCols( self ):
        return self._theGrid.numCols()

    def __getitem__( self, xy ):
        return self._theGrid[ xy[0], xy[1] ]

    def __setitem__( self, xy, scalar ):
        self._theGrid[ xy[0], xy[1] ] = scalar

    def scaleBy( self, scalar ):
        for r in xrange( self.numRows() ):
            for c in xrange( self.numCols() ):
                self[r, c] *= scalar

    def transpose( self ):
        newMatrix = Matrix( self.numCols(), self.numRows() )
        for r in xrange( self.numRows() ):
            for c in xrange( self.numCols() ):
                newMatrix[c, r] = self[r, c]
        return newMatrix

    def add( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not compatible for the add operation."

        newMatrix = Matrix( self.numRows(), self.numCols() )
        for r in xrange( self.numRows() ):
            for c in xrange( self.numCols() ):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]

        return newMatrix

    def subtract( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not compatible for the add operation."

        newMatrix = Matrix( self.numRows(), self.numCols() )
        for r in xrange( self.numRows() ):
            for c in xrange( self.numCols() ):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]

        return newMatrix

    def multiple( self, rhsMatrix ):
        assert self.numRows() == rhsMatrix.numCols() and \
            self.numCols() == rhsMatrix.numRows(), \
            "Matrix sizes not compatible for the multiple operation."

        newMatrix = Matrix( self.numRows(), rhsMatrix.numCols() )

        for r in xrange( self.numRows() ):
            for rhsC in xrange ( rhsMatrix.numCols() ):
                tmp = 0
                for c in xrange( self.numCols() ):
                    tmp += self[r, c] * rhsMatrix[c, r]
                newMatrix[r, rhsC] = tmp

        return newMatrix
