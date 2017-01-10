import random

class CountingBag:
    def __init__(self):
        self._theItems = dict()

    def __len__(self):
        return sum(self._theItems.values())

    def __contains__(self, item):
        return item in self._theItems

    def add(self, item):
        self._theItems[item] = self._theItems.get(item, 0) + 1

    def numOf(self, item):
        return self._theItems.get(item, 0)

    def remove(self, item):
        assert item in self._theItems, "item must be in the bag."
        c = self._theItems[item] - 1
        if c > 0:
            self._theItems[item] = c
        else:
            del self._theItems[item]

    def __iter__(self):
        return _CountingGenerator(self._theItems)

def _CountingGenerator(theItems):
    for k in theItems:
        for counter in xrange(theItems[k]):
            yield k

if __name__ == '__main__':
    b = CountingBag()
    for i in xrange(10):
        b.add(i)
    print( "Num of 1 : %d" % b.numOf( 1 ) )
    print( "Length: %d" % len(b) )
    for i in xrange(10):
        b.add(i)
    print( "Num of 1 : %d" % b.numOf( 1 ) )
    print( "Length: %d" % len(b) )

    for i in xrange(5, 15):
        if i in b:
            print( "%d in bag" % i )
        else:
            print( "%d not in bag" % i )

    for i in xrange(5, 10):
        b.remove(i)

    print( "Iterate bag:" )
    for i in b:
        print i,
    print
