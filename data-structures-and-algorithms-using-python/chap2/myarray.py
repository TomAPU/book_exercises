import ctypes

class Array:
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear( None )

    def __len__( self ):
        return self._size

    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    def __setitem__( self, index, val ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = val

    def clear( self, val ):
        for i in range( self._size ):
            self._elements[ i ] = val

    def __iter__( self ):
        return _ArrayGenerator( self._elements, self._size )

def _ArrayGenerator( elements, size ):
    for i in range( size ):
        yield elements[i]

class Array2D:
    def __init__( self, nrows, ncols ):
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array( nrows )

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range( nrows ):
            self._theRows[i] = Array( ncols )

    def numRows( self ):
        return len( self._theRows )

    def numCols( self ):
        return len( self._theRows[0] )

    # Clears the array by setting every element to the given value.
    def clear( self, val ):
        for row in range( self.numRows() ):
            self._theRows[row].clear( val )

    def __getitem__( self, xy ):
        assert len( xy ) == 2, "Invalid number of array subscripts."
        row = xy[0]
        col = xy[1]
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1arr = self._theRows[row]
        return the1arr[col]

    def __setitem__( self, xy, val ):
        assert len( xy ) == 2, "Invalid number of array subscripts."
        row = xy[0]
        col = xy[1]
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1arr = self._theRows[row]
        the1arr[col] = val


class Vector:
    def __init__( self ):
        self._capacity = 2
        self._len = 0
        PyArrayType = ctypes.py_object * self._capacity
        self._elements = PyArrayType()

    def __len__( self ):
        return self._len

    def __contains__( self, item ):
        ndx = self.indexOf( item )
        return ndx != -1 
        
    def __getitem__( self, ndx ):
        assert ndx >= 0 and ndx < len(self), "Array subscript out of range"
        return self._elements[ ndx ]

    def __setitem__( self, ndx, val ):
        assert ndx >= 0 and ndx < len(self), "Array subscript out of range"
        self._elements[ ndx ] = val

    def append( self, val ):
        self._len += 1
        if self._len * 2 > self._capacity:
            self._capacity = self._len * 2
            PyArrayType = ctypes.py_object * self._capacity
            old = self._elements
            self._elements = PyArrayType()
            for i in range( self._len - 1 ):
                self._elements[i] = old[i]
        self._elements[ self._len - 1 ] = val

    def insert( self, ndx, val ):
        self._len += 1
        old = self._elements
        if self._len * 2 > self._capacity:
            self._capacity = self._len * 2
            PyArrayType = ctypes.py_object * self._capacity
            old = self._elements
            self._elements = PyArrayType()
            for i in range( ndx ):
                self._elements[i] = old[i]

        self._elements[ ndx ] = val
        for i in range( ndx + 1, self._len ):
            self._elements[ i ] = old[ i - 1 ]

    def remove( self, ndx ):
        assert ndx >= 0 and ndx < self._len, "Array subscript out of range"
        self._len -= 1

        if self._len * 2 < self._capacity:
            self._capacity = self._len * 2
            PyArrayType = ctypes.py_object * self._capacity
            old = self._elements
            self._elements = PyArrayType()
            for i in range( 0, ndx ):
                self._elements[i] = old[i]
            for i in range( ndx, self._len ):
                self._elements[ i ] = old[ i + 1 ]
        else:
            for i in range( ndx, self._len ):
                self._elements[ i ] = self._elements[ i + 1 ]

    def indexOf(self, item ):
        for i in range( self._len ):
            if self._elements[ i ] == item:
                return i
        return -1

    def extend( self, otherVector ):
        total_len = self._len + otherVector._len
        if total_len * 2 > self._capacity:
            self._capacity = total_len * 2
            PyArrayType = ctypes.py_object * self._capacity
            old = self._elements
            self._elements = PyArrayType()
            for i in range( self._len ):
                self._elements[i] = old[i]

        for i in range( otherVector._len ):
            self._elements[ self._len + i ] = otherVector._elements[i]
        self._len += otherVector._len

        
    def subVector( self, fromNdx, toNdx ):
        assert fromNdx >= 0 and fromNdx < len(self), "From index out of range"
        assert toNdx >= 0 and toNdx < len(self), "To index out of range"
        
        newVector = Vector()
        for i in range( fromNdx, toNdx + 1 ):
            newVector.append( self[ i ] )
        return newVector

    def __iter__( self ):
        return _VectorGenerator( self._elements, self._len )

def _VectorGenerator( elements, length ):
    for i in range( length ):
        yield elements[ i ]

class MultiArray:
    def __init__( self, *dimensions ):
        assert len( dimensions ) > 0, "The array must have 2 or more dimensions."
        self._dims = dimensions
        size = 1
        for d in dimensions:
            assert d > 0, "Dimension must be > 0."
            size *= d

        self._elements = Array( size )
        # Create a 1-D array to store the equation factors.
        self._factors = Array ( len( self._dims ) )
        self._computeFactors()

    def _computeFactors( self ):
        # index4 (i1, i2, i3, i4) = i1 * (d2 * d3 * d4 ) + i2 * (d3 * d4) + i3 * d4 + i4
        # index( i1, i2, ..., in) = i1 * f1 + i2 * f2 + ... + in-1 * fu-1 + in*1
        factor = 1
        self._factors[ len( self._dims ) - 1 ] = factor

        for d in range( len( self._dims ) - 2, 1, -1 ):
            factor *= self._dims[ d ]
            self._factors[ d ] = factor

    def numDims( self ):
        return len( self._dims )

    def length( self, dim ):
        assert dim > 1 and dim <= len( self._dims ), \
            "Dimension component out of range."
        return self._dims[dim-1]

    def clear( self, value ):
        self._elements.clear( value )

    def __getitem__( self, ndxTupe ):
        assert len( ndxTupe ) == len( self._dims ), "Invalid array subscripts."
        idx = self._computeIndex( ndxTupe )
        assert idx is not None, "Array subscript out of range."
        return self._elements[ idx ]

    def __setitem__( self, ndxTupe, value ):
        assert len( ndxTupe ) == len( self._dims ), "Invalid array subscripts."
        idx = self._computeIndex( ndxTupe )
        assert idx is not None, "Array subscript out of range."
        self._elements[ idx ] = value

    # Computes the 1-D array offset for element (i_1, i_2, ... i_n)
    # using the equation i_1 * f_1 + i_2 * f_2 + ... + i_n * f_n
    def _computeIndex( self, ndxTupe ):
        offset = 0
        for j in range( len( ndxTupe ) ):
            if ndxTupe[j] < 0 or ndxTupe >= self._dims[j]:
                return None
            else:
                offset += ndxTupe[j] * self._factors[j]
        return offset



if __name__ == '__main__':
    print "Create an empty Vector"
    v = Vector()
    print "Len: ", len( v ), 'capacity:', v._capacity
    for i in range( 10 ):
        v.append( i )
    print "Len: ", len( v ), 'capacity:', v._capacity
    print "1 in vector? " , 1 in v
    print "v[1] = ", v[1]
    print "set v[0] = 'a'"
    v[1] = 'a'
    v.insert(0, 'holl')
    v.remove(9)
    print 'indexOf("holl")=', v.indexOf('holl')
    v2 = Vector()
    for i in range( 10, 15 ):
        v2.append( i )

    v.extend( v2 )
    print "Len: ", len( v ), 'capacity:', v._capacity
    subV = v.subVector( 10, 14 )
    for i in subV:
        print i,

    print
    for i in v:
        print i,
    for i in range( 10 ):
        v.remove( 0 )
    print "Len: ", len( v ), 'capacity:', v._capacity
    for i in v:
        print i,
