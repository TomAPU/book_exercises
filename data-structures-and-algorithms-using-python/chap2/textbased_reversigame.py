# Not done yet

from reversigamelogical import ReversiGameLogic

gl = ReversiGameLogic()

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
    row_col = row_col.split(',')
    # 1 based
    row = int( row_col[0] )-1
    col = int( row_col[1] )-1
    if gl.isLegalMove( row, col ):
        gl.makeMove( row, col )
    else:
        print 'Move illegal, try again'
