# (a): Derive an equation that computes the total number of elements in the
# lower triangular table for a table of size m × n.

# N = min(m, n)
# LEN = 1+2+3+N = N(N+1)/2

# (b) Derive an index equation that maps an element of the lower triangular
# table onto a one-dimensional array stored in row-major order

# 1-D array size: LEN
# table_location(i, j) = 1+2+...+i +j
# example: table_location(0,0)=0, table_location(1,1)=2
