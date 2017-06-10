# Develop the index equation that computes the location within a 1-D array for
# element (i,j) of a 2-D array stored in column-major order

# 2-D array size: 
N_ROWS = 8
N_COLS = 9

# 1-D array size:
LEN = N_ROWS * N_COLS
def location(i, j):
    return j*N_COLS + i
