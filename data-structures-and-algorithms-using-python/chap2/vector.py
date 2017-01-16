import ctypes

from myarray import Array

# Implement the Vector ADT using the Array class
# implemented in the chapter. Your implementation should produce a mutable
# sequence type that works like Python's list structure. When the underlying
# array needs to be expanded, the new array should double the size of the original.
class Vector:
    def __init__(self):
        # Creates a new empty vector with an initial capacity of two elements.
        self._array = Array(2)
        self._len = 0

    def __len__(self):
        # Returns the number of items contained in the vector.
        return self._len

    def __contains__(self, item):
        # Determines if the given item is contained in the vector.
        for i in range(self._len):
            if self._array[i] == item:
                return True
        return False

    def __getitem__(self, ndx):
        # Returns the item stored in the ndx element of the list.
        # The value of ndx must be within the valid range.

        if isinstance(ndx, slice):
            assert 0 <= ndx.start <= self._len, "index out of range"
            assert 0 <= ndx.stop < self._len, "index out of range"
            v = Vector()
            for i in range(ndx.start, ndx.stop, ndx.step):
                v.append(self._array[i])
            return v
        else:
            assert 0 <= ndx <= self._len, "index out of range"
            return self._array[ndx]

    def setitem(self, ndx, item):
        # Sets the element at position ndx to contain the given item.
        # The value of ndx must be within the valid range, which includes the first position past the last item.
        assert 0 <= ndx <= self._len, "index out of range"
        self._array[ndx] = item

    def _doublesize(self):
        a = Array(2*len(self._array))
        for i in range(self._len):
            a[i] = self._array[i]
        self._array = a

    def append(self, item):
        # Adds the given item to the end of the list.
        if self._len + 1 > len(self._array):
            self._doublesize()

        self._array[self._len] = item
        self._len += 1

    def insert(self, ndx, item):
        # Inserts the given item in the element at position ndx.
        # The items in the elements at and following the given position are
        # shifted down to make room for the new item. 
        # ndx must be within the valid range.
        assert 0 <= ndx <= self._len, "index out of range"

        if self._len + 1 > len(self._array):
            self._doublesize()

        for i in range(self._len, ndx, -1):
            self._array[i] = self._array[i-1]

        self._array[ndx] = item
        self._len += 1

    def remove(self, ndx):
        # Removes and returns the item from the element from the given ndx position.
        # The items in the elements at and following the given position are shifted up to close the gap created by the removed item.
        # ndx must be within the valid range.
        assert 0 <= ndx <= self._len, "index out of range"

        if (self._len -1)*2 < len(self._array):
            a = Array(len(self._array)/2)
            for i in range(0, ndx):
                a[i] = self._array[i]
            for i in range(ndx, self._len-1):
                a[i] = self._array[i+1]
            self._array = a
        else:
            for i in range(ndx, self._len-1):
                self._array[i] = self._array[i+1]
        self._len -= 1


    def indexOf(self, item):
        # Returns the index of the vector element containing the given item.
        # The item must be in the list.
        for i in range(self._len):
            if item == self._array[i]:
                return i
        return -1

    def extend(self, otherVector):
        # Extends this vector by appending the entire contents of the otherVector to this vector.
        for i in range(len(otherVector)):
            self.append(otherVector[i])

   # def subVector(self, from_pos, to_pos ):
        # see __slice__ implementation in __getitem__

    def __iter__(self):
        # Creates and returns an iterator that can be used to traverse the elements of the vector
        return _VectoryGenerator( self._array, self._len )

def _VectoryGenerator( elements, size ):
    for i in range( size ):
        yield elements[i]


if __name__ == '__main__':
    v = Vector()

    print("empty vector.")

    print("Insert 1..10:")
    for i in range(11):
        v.append(i)
    print "Now vector:",
    for i in v:
        print i,

    print
