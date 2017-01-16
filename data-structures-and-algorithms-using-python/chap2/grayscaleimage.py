from myarray import Array2D

class GrayscaleImage:
    def __init__( self, nrows, ncols ):
        self._grid = Array2D( nrows, ncols )

    def width( self ):
        return self._grid.numCols()

    def height( self ):
        return self._grid.numRows()

    def clear( self, val ):
        self._grid.clear( val )

    def __getitem__( self, row, col ):
        return self._grid[ row, col ]

    def __setitem__( self, row, col, val ):
        self._grid[ row, col ] = val
