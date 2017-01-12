from life import LifeGrid

INIT_CONFIG = [ (0, 0), (0, 1), (1, 0), (1, 2), (3, 2), (3, 4), (5, 4), (5, 6), (7, 6), (7, 8), (9, 8), (9, 10), (11, 10), (11, 12), (12, 11), (12, 12)]

GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations
NUM_GENS = 8

def main():
    GRID_WIDTH = int( raw_input( "Grid width:" ) )
    GRID_HEIGHT = int( raw_input( "Grid height:" ) )
    NUM_GENS = int( raw_input( "Nbr of generations to evolve:" ) )
    grid = LifeGrid( GRID_WIDTH, GRID_HEIGHT )
    grid.configure( INIT_CONFIG )

    draw( grid )
    for i in xrange( NUM_GENS ):
        evolve( grid )
        draw( grid )

def evolve( grid ):
    liveCells = list()

    for i in xrange( grid.numRows() ):
        for j in xrange( grid.numCols() ):
            neighbors = grid.numLiveNeighbors( i, j )

            # 1. If a cell is alive and has either two or three live neighbors, the cell remains alive in the next generation. 
            # The neighbors are the eight cells immediately surrounding a cell: vertically, horizontally, and diagonally.  
            # 2. A living cell that has no live neighbors or a single live neighbor dies from isolation in the next generation.
            # 3. A living cell that has four or more live neighbors dies from overpopulation in the next generation.
            # 4. A dead cell with exactly three live neighbors results in a birth and becomes alive in the next generation.
            # All other dead cells remain dead in the next generation.

            if (neighbors == 2 and grid.isLiveCell( i, j )) or \
                (neighbors == 3):
                    liveCells.append( (i, j) )

    grid.configure( liveCells )

def draw( grid ):
    print 
    for i in xrange( grid.numRows() ):
        for j in xrange( grid.numCols() ):
            if grid.isLiveCell( i, j):
                print '@',
            else:
                print '.',
        print

main()
