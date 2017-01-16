from myarray import Array2D

class LifeGrid:
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__( self, nrows, ncols ):
        self._grid = Array2D( nrows, ncols )
        self.configure( list() )

    def numRows( self ):
        return self._grid.numRows()

    def numCols( self ):
        return self._grid.numCols()

    def configure( self, coordList ):
        for i in range( self.numRows() ):
            for j in range( self.numCols() ):
                self.clearCell(i, j)

        for coord in coordList:
            self.setCell( coord[0], coord[1] )

    def isLiveCell( self, row, col ):
        return self._grid[ row, col ] == LifeGrid.LIVE_CELL

    def clearCell( self, row, col ):
        self._grid[ row, col ] = LifeGrid.DEAD_CELL

    def setCell( self, row, col ):
        self._grid[ row, col ] = LifeGrid.LIVE_CELL

    def numLiveNeighbors( self, row, col ):
        nrows = self.numRows()
        ncols = self.numCols()

        liveNum = 0
        for i in range( row-1, row+2 ):
            for j in range( col-1, col+2 ):
               if ( 0 <= i < nrows ) and ( 0 <= j < ncols ):
                   liveNum += self._grid[i, j]
        liveNum -= self._grid[ row, col ]

        return liveNum
