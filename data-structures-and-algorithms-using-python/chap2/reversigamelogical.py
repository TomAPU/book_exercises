import itertools

from myarray import Array2D

GRID_NROWS = 8
GRID_NCOLS = 8

class ReversiGameLogic:
    PLAYER1 = 1 # black
    PLAYER2 = 2 # white
    PLAYER1_CHAR = '#'
    PLAYER2_CHAR = 'O'

    # Creates a new instance of the Reversi game logic with the initial conf.
    def __init__( self ):
        self._grid = Array2D(GRID_NROWS, GRID_NCOLS)
        self._grid.clear( 0 )

        self._curr_turn = ReversiGameLogic.PLAYER1

        self._grid[ 3, 4 ] = ReversiGameLogic.PLAYER1
        self._grid[ 4, 3 ] = ReversiGameLogic.PLAYER1
        self._grid[ 3, 3 ] = ReversiGameLogic.PLAYER2
        self._grid[ 4, 4 ] = ReversiGameLogic.PLAYER2

        self._finished = False

    # Returns the player number(1 or 2) for the current player or 0 if no
    # player can move
    def whoseTurn( self ):
        player = self._curr_turn

        for r in range( self._grid.numRows() ):
            for c in range( self._grid.numCols() ):
                if self._isLegalMoveFor( r, c, player ):
                    return player

        # current player can not move
        other_player = player % 2 + 1
        for r in range( self._grid.numRows() ):
            for c in range( self._grid.numCols() ):
                if self._isLegalMoveFor(r, c, other_player):
                    self._curr_turn = other_player
                    return other_player

        self._finished = True
        return 0

    # returns the num of chips on the board belonging to the indicated player.
    # The value of player must be 1 or 2.
    def numChips( self, player):
        assert player == ReversiGameLogic.PLAYER1 or \
                player == ReversiGameLogic.PLAYER2, "player must be 1 or 2"
        n = 0
        for r in range( self._grid.numRows() ):
            for c in range( self._grid.numCols() ):
                if self._grid[r, c] == player:
                    n += 1
        return n

    # Returns the number of squares still open and available for play
    def numOpenSquares( self ):
        n = 0
        for r in range( self._grid.numRows() ):
            for c in range( self._grid.numCols() ):
                if self.isLegalMove(r, c):
                    n += 1
        return n

    # Returns the player number (1 or 2) for the player who has
    # won the game or 0 if the game if not finished.
    def getWinner( self ):
        if not self._finished:
            return 0

        numP1 = self.numChips( ReversiGameLogic.PLAYER1 )
        numP2 = self.numChips( ReversiGameLogic.PLAYER2 )

        if numP1 >= numP2:
            return ReversiGameLogic.PLAYER1
        else:
            return ReversiGameLogic.PLAYER2

    # Returns True or False to indicate if the current player
    # can place their chip in the square at position (row, col)
    def isLegalMove( self, row, col ):
        player = self._curr_turn
        return self._isLegalMoveFor( row, col, player )


    def _playerLeagalMoveByDirection(self, row, col, player, direction):
        name = 'top'
        iters = itertools.izip(range(row-1-1, -1, -1),
                itertools.repeat(col))
        iters = itertools.izip(range(row-1-1, -1, -1),
                itertools.repeat(col))
        if self._squareData(row-1, col) == other_player:
            for r in range(row-2, -1, -1):
                if self._squareData(r, col) == other_player:
                    continue
                elif self._squareData(r, col) == player:
                    ret.append(('top', r, col))
                    break
    # The players take turns placing chips on the board with their color facing up. A
    # chip can only be played in a square that is adjacent to a chip of the other player
    # and that forms a straight line of attack 
    # direction:
    #   top, top right, right, bottom right, bottom, bottom left, left, top left
    def _legalMoveFor( self, row, col, player, direction):
        if 0 <= row < GRID_NROWS and 0 <= col < GRID_NCOLS:
            other_player = player % 2 + 1
            if self._grid[ row, col ] == 0: # is open
                iters = []
                if direction == 'top':
                    next_cell = (row-1, col)
                    iters = itertools.izip(range(row-1-1, -1, -1),
                            itertools.repeat(col))

                elif direction == 'top right':
                    next_cell = (row-1, col+1)
                    iters = itertools.izip(range(row-1-1, -1, -1),
                            range(col+1+1, GRID_NCOLS, 1))

                elif direction == 'right':
                    next_cell = (row, col+1)
                    iters = itertools.izip(itertools.repeat(row),
                            range(col+1+1, GRID_NCOLS, 1))

                elif direction == 'bottom right':
                    next_cell = (row+1, col+1)
                    iters = itertools.izip(range(row+1+1, GRID_NROWS, 1),
                            range(col+1+1, GRID_NCOLS, 1))

                elif direction == 'bottom':
                    next_cell = (row+1, col)
                    iters = itertools.izip(range(row+1+1, GRID_NROWS, 1),
                            itertools.repeat(col))

                elif direction == 'bottom left':
                    next_cell = (row-1, col-1)
                    iters = itertools.izip(range(row-1-1, -1, -1),
                            range(col-1-1, -1, -1))

                elif direction == 'left':
                    next_cell = (row, col-1)
                    iters = itertools.izip(itertools.repeat(row),
                            range(col-1-1, -1, -1))

                elif direction == 'top left':
                    next_cell = (row-1, col-1)
                    iters = itertools.izip(range(row-1-1, -1, -1),
                            range(col-1-1, -1, -1))

                if self._squareData(row-1, col+1) == other_player:
                    for r, c in iters:
                        if self._squareData(r, c) == other_player:
                            continue
                        elif self._squareData(r, c) == player:
                            return direction, r, c
        return None

                if self._grid[
                for r in range(max(row-1,0), min(row+2, GRID_NROWS)):
                    for c in range(max(col-1, 0), min(col+1, GRID_NCOLS)):
                        if r == row and c == col:
                            break
                        if self._grid[r, c] == other_player:
                            return True

        # horizontal left,   -->x.....x
        for c in range( col ):
            if self._grid[row, c] == player:
                for c2 in range( c+1, col ):
                    self._grid[ row, c2 ] = player
                break

        # horizontal right, x...x<---
        for c in range( self._grid.numCols() - 1, col, -1 ):
            if self._grid[row, c] == player:
                for c2 in range( col+1, c ):
                    self._grid[ row, c2 ] = player
                break

        # vertical top
        #  |
        #  |
        #  v
        #  x
        #  .
        #  .
        #  .
        #  x
        for r in range( row ):
            if self._grid[ r, col ] == player:
                for r2 in range( r+1, row ):
                    self._grid[ r2, col ] = player
                break

        # vertical bottom
        #  x
        #  .
        #  .
        #  .
        #  x
        #  ^
        #  |
        #  |
        for r in range( self._grid.numRows() - 1, row, -1 ):
            if self._grid[ r, col ] == player:
                for r2 in range( row+1, r ):
                    self._grid[ r2, col ] = player
                break


        # diagonal top left
        # row up, col up
        # \
        #  \
        #   v
        #    x
        #     .
        #      .
        #       .
        #        x
        if row >= col:
            start_row = row-col
            for c in range(col):
                if self._grid[start_row+c, c] == player:
                    for c2 in range(c+1, col):
                        self._grid[start_row+c2, c2] = player
                    break
        else:
            start_col = col-row
            for r in range(row):
                if self._grid[r, start_col+r] == player:
                    for r2 in range(r+1, row):
                        self._grid[r2, start_col+r2] = player
                    break

        # diagonal  bottom right
        # 
        # x
        #  .
        #   .
        #    .
        #     x
        #      ^
        #       \
        #        \
        if row >= col:
            for r in range(self._grid.numRows()-1, row, -1):
                if self._grid[r, col+(r-row)] == player:
                    for r2 in range(row+1, r):
                        self._grid[r2, col+(r2-row)] = player
                    break
        else:
            for c in range(self._grid.numCols()-1, col, -1):
                if self._grid[row+(c-col), c] == player:
                    for c2 in range(col+1, c):
                        self._grid[row+(c2-col), c2] = player
                    break

        # diagonal  bottom left
        # col-> +, row -> -
        #        x
        #       .
        #      .
        #    .
        #   x
        #  ^
        if self._grid.numCols()-col >= row:
            for r in range(row):
                if self._grid[r, col+(r-row)] == player:
                    for r2 in range(r-1, row, -1):
                        self._grid[r2, col+(r2-row)] = player
                    break
        else:
            for c in range(col):
                if self._grid[row+(col-c), c] == player:
                    for c2 in range(c+1, col):
                        self._grid[row+(col-c2), c2] = player
                    break

        # diagonal  top right
        # col-> up, row -> down
        if self._grid.numCols()-col >= row:
            for r in range(0, row-1):
                if self._grid[r, col+(r-row)] == player:
                    for r2 in range(row-1, r, -1):
                        self._grid[r2, col+(r2-row)] = player
                    break
        else:
            for c in range(self._grid.numCols()-1, col, -1):
                if self._grid[row+(col-c), c] == player:
                    for c2 in range(col+1, c):
                        self._grid[row+(col-c2), c2] = player
                    break


        return False

    def _squareData( self, row, col ):
        if 0 <= row < GRID_NROWS and \
                0 <= col < GRID_NCOLS:
            return self._grid[ row, col ]
        return -1

    # Which player has a chip in the given square?
    # Returns the player number (1 or 2) or 0 if the square is empty.
    def occupiedBy( self, row, col ):
        return _squareData(row, col)

    # The current player places one of his chips in the
    # square at pos (row, col). All chips on the board that
    # should be flipped based on the rules of Reversi are flipped.
    def makeMove( self, row, col ):
        player = self.whoseTurn()
        assert self._isLegalMoveFor( row, col, player), "Play %d move to [%d, %d] is illegal." % ( player, row, col )

        other_player = player % 2 + 1

        # horizontal left,   -->x.....x
        for c in range( col ):
            if self._grid[row, c] == player:
                for c2 in range( c+1, col ):
                    self._grid[ row, c2 ] = player
                break

        # horizontal right, x...x<---
        for c in range( self._grid.numCols() - 1, col, -1 ):
            if self._grid[row, c] == player:
                for c2 in range( col+1, c ):
                    self._grid[ row, c2 ] = player
                break

        # vertical top
        #  |
        #  |
        #  v
        #  x
        #  .
        #  .
        #  .
        #  x
        for r in range( row ):
            if self._grid[ r, col ] == player:
                for r2 in range( r+1, row ):
                    self._grid[ r2, col ] = player
                break

        # vertical bottom
        #  x
        #  .
        #  .
        #  .
        #  x
        #  ^
        #  |
        #  |
        for r in range( self._grid.numRows() - 1, row, -1 ):
            if self._grid[ r, col ] == player:
                for r2 in range( row+1, r ):
                    self._grid[ r2, col ] = player
                break


        # diagonal top left
        # row up, col up
        # \
        #  \
        #   v
        #    x
        #     .
        #      .
        #       .
        #        x
        if row >= col:
            start_row = row-col
            for c in range(col):
                if self._grid[start_row+c, c] == player:
                    for c2 in range(c+1, col):
                        self._grid[start_row+c2, c2] = player
                    break
        else:
            start_col = col-row
            for r in range(row):
                if self._grid[r, start_col+r] == player:
                    for r2 in range(r+1, row):
                        self._grid[r2, start_col+r2] = player
                    break

        # diagonal  bottom right
        # 
        # x
        #  .
        #   .
        #    .
        #     x
        #      ^
        #       \
        #        \
        if row >= col:
            for r in range(self._grid.numRows()-1, row, -1):
                if self._grid[r, col+(r-row)] == player:
                    for r2 in range(row+1, r):
                        self._grid[r2, col+(r2-row)] = player
                    break
        else:
            for c in range(self._grid.numCols()-1, col, -1):
                if self._grid[row+(c-col), c] == player:
                    for c2 in range(col+1, c):
                        self._grid[row+(c2-col), c2] = player
                    break

        # diagonal  bottom left
        # col-> +, row -> -
        #        x
        #       .
        #      .
        #    .
        #   x
        #  ^
        if self._grid.numCols()-col >= row:
            for r in range(row):
                if self._grid[r, col+(r-row)] == player:
                    for r2 in range(r-1, row, -1):
                        self._grid[r2, col+(r2-row)] = player
                    break
        else:
            for c in range(col):
                if self._grid[row+(col-c), c] == player:
                    for c2 in range(c+1, col):
                        self._grid[row+(col-c2), c2] = player
                    break

        # diagonal  top right
        # col-> up, row -> down
        if self._grid.numCols()-col >= row:
            for r in range(0, row-1):
                if self._grid[r, col+(r-row)] == player:
                    for r2 in range(row-1, r, -1):
                        self._grid[r2, col+(r2-row)] = player
                    break
        else:
            for c in range(self._grid.numCols()-1, col, -1):
                if self._grid[row+(col-c), c] == player:
                    for c2 in range(col+1, c):
                        self._grid[row+(col-c2), c2] = player
                    break

        self._grid[row, col] = player
        self._curr_turn = other_player

    def draw( self ):
        for c in range( self._grid.numCols()+1 ):
            print c,
        print
        for r in range( self._grid.numRows() ):
            print r+1,
            for c in range( self._grid.numCols() ):
                if self._grid[r, c] == ReversiGameLogic.PLAYER1:
                    print ReversiGameLogic.PLAYER1_CHAR,
                elif self._grid[r, c] == ReversiGameLogic.PLAYER2:
                    print ReversiGameLogic.PLAYER2_CHAR,
                else:
                    print '-',
            print
        print


if __name__ == '__main__':
    gl = ReversiGameLogic()
    turn = gl.whoseTurn()
    assert turn == ReversiGameLogic.PLAYER1, "assert turn == ReversiGameLogic.PLAYER1"

    """
    while True:
        gl.draw()

        turn = gl.whoseTurn()
        if turn == 0:
            win = gl.getWinner()
            print 'Winner is Player %d' % win+1
            break

        if turn == ReversiGameLogic.PLAYER1:
            play = '#'
        else:
            play = '@'

        row_col = raw_input( "Player %c place at(Enter to exit, example row,col): " % play)
        if not row_col:
            exit(0)
        row_col = row_col.split(',')
        # 1 based
        row = int( row_col[0] )-1
        col = int( row_col[1] )-1
        if gl.isLegalMove( row, col ):
            gl.makeMove( row, col )
        else:
            print 'Move illegal, try again'

    """
