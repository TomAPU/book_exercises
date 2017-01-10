import random

class GrabBag:
    def __init__(self):
        self._theItems = list()

    def __len__(self):
        return len(self._theItems)

    def __contains__(self, item):
        return item in self._theItems

    def add(self, item):
        self._theItems.append(item)

    def grabItem(self):
        assert len(self._theItems) > 0, "The bag should not be empty."
        ndx = random.randint(0, len( self._theItems )-1)
        return self._theItems.pop(ndx)

    def __iter__(self):
        return _BagIterator(self._theItems)

class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._currItem = 0

    def __iter__(self):
        return self

    def next( self ):
        if self._currItem < len( self._bagItems ):
            item =  self._bagItems[ self._currItem ]
            self._currItem += 1
            return item
        else:
            raise StopIteration

if __name__ == '__main__':
    b = GrabBag()
    for i in xrange(10):
        b.add(i)
    for i in xrange(5, 15):
        if i in b:
            print( "%d in bag" % i )
        else:
            print( "%d not in bag" % i )

    print( "Iterate bag:" )
    for i in b:
        print i,
    print

    print( "GrabItem test:" )
    while len(b):
        print b.grabItem(), 
