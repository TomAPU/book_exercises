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

    def other_player(self, curr_player):
        return curr_player % 2 + 1

    # Returns the player number(1 or 2) for the current player or 0 if no
    # player can move
    def whoseTurn( self ):
        player = self._curr_turn
        other_player = self.other_player(player)

        for p in (player, other_player,):
            for r in range( self._grid.numRows() ):
                for c in range( self._grid.numCols() ):
                    if self._legalMoveAttackEndpointsForPlayer(r, c, p,
                            return_immediately=True):
                        return p

        # no player can move
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
        player = self._curr_turn
        other_player = self.other_player(player)
        for r in range( self._grid.numRows() ):
            for c in range( self._grid.numCols() ):
                if self._legalMoveAttackEndpointsForPlayer(r, c, player) or \
                        self._legalMoveAttackEndpointsForPlayer(r, c, other_player):
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
        return self._legalMoveAttackEndpointsForPlayer(row, col, player)


    def _legalMoveAttackEndpointsForPlayer(self, row, col, player, return_immediately=True):
        ret = []
        for direction in ('top', 'top right', 'right', 'bottom right',
                'bottom', 'bottom left', 'left', 'top left'):
            endpoint = self._legalMoveAttactEndpointForPlayerByDirection(row, col, player, direction)
            if endpoint:
                if return_immediately:
                    return [endpoint,]
                else:
                    ret.append(endpoint)
        return ret

    # The players take turns placing chips on the board with their color facing up. A
    # chip can only be played in a square that is adjacent to a chip of the other player
    # and that forms a straight line of attack 
    # direction:
    #   top, top right, right, bottom right, bottom, bottom left, left, top left
    def _legalMoveAttactEndpointForPlayerByDirection(self, row, col, player, direction):
        if 0 <= row < GRID_NROWS and 0 <= col < GRID_NCOLS:
            other_player = self.other_player(player)
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
                    next_cell = (row+1, col-1)
                    iters = itertools.izip(range(row+1+1, GRID_NROWS, 1),
                            range(col-1-1, -1, -1))

                elif direction == 'left':
                    next_cell = (row, col-1)
                    iters = itertools.izip(itertools.repeat(row),
                            range(col-1-1, -1, -1))

                elif direction == 'top left':
                    next_cell = (row-1, col-1)
                    iters = itertools.izip(range(row-1-1, -1, -1),
                            range(col-1-1, -1, -1))

                if self._squareData(*next_cell) == other_player:
                    for r, c in iters:
                        if self._squareData(r, c) == other_player:
                            continue
                        elif self._squareData(r, c) == player:
                            return direction, r, c
        return None

    def _squareData( self, row, col ):
        if 0 <= row < GRID_NROWS and \
                0 <= col < GRID_NCOLS:
            return self._grid[row, col]
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

        if player == 0:
            print '\nNo player can move, finished'

        attackEndpoints = self._legalMoveAttackEndpointsForPlayer(row, col, player,
                return_immediately=False)

        for direction, end_row, end_col in attackEndpoints:
            if direction == 'top':
                iters = itertools.izip(range(row-1, end_row, -1),
                        itertools.repeat(col))

            elif direction == 'top right':
                iters = itertools.izip(range(row-1, end_row, -1),
                        range(col+1, end_col, 1))

            elif direction == 'right':
                iters = itertools.izip(itertools.repeat(row),
                        range(col+1, end_col, 1))

            elif direction == 'bottom right':
                iters = itertools.izip(range(row+1, end_row, 1),
                        range(col+1, end_col, 1))

            elif direction == 'bottom':
                iters = itertools.izip(range(row+1, end_row, 1),
                        itertools.repeat(col))

            elif direction == 'bottom left':
                iters = itertools.izip(range(row+1, end_row, 1),
                        range(col-1, end_col, -1))

            elif direction == 'left':
                iters = itertools.izip(itertools.repeat(row),
                        range(col-1, end_col, -1))

            elif direction == 'top left':
                iters = itertools.izip(range(row-1, end_row, -1),
                        range(col-1, end_col, -1))

            for r, c in iters:
                self._grid[r, c] = player

        self._grid[row, col] = player
        other_player = self.other_player(self._curr_turn)
        self._curr_turn = other_player
        return

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
    0 1 2 3 4 5 6 7 8
    1 # # # # # # # #
    2 # # O O # O # #
    3 # # O # O # # #
    4 # # # # # # # #
    5 # # O # # # # #
    6 # # O # O O # #
    7 O # O O O # O #
    8 # # O O O O O -


    for r in range(8):
        for c in range(8):
            gl._grid[r,c]=1
    for r,c in (
        (1,2),(1,3),(1,5),(2,2),(2,4),(4,2),(5,2),(5,4),(5,5),(6,0),(6,2),(6,3),(6,4),(6,6),(7,2),(7,3),(7,4),(7,5),(7,6)):
        gl._grid[r,c]=2

    gl._grid[7,7]=0
    """

    while True:
        gl.draw()

        turn = gl.whoseTurn()
        if turn == 0:
            win = gl.getWinner()
            print 'Winner is Player%d' % win
            print 'Winner chips: %d' % gl.numChips(win)
            print 'Other Player chips: %d' % gl.numChips(gl.other_player(win))
            break

        if turn == ReversiGameLogic.PLAYER1:
            play = ReversiGameLogic.PLAYER1_CHAR
        else:
            play = ReversiGameLogic.PLAYER2_CHAR

        row_col = raw_input( "Player %s place at(Enter to exit, example row,col): " % play)
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
