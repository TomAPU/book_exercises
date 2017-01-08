# Implements the Bag ADT container using a Python list.
# bag is a container that stores a collection in which duplicate values are allowed. The items, each of which is individually stored, have no particular order but they must be comparable.
# + Bag(): Creates a bag that is initially empty.
# + length(): Returns the number of items stored in the bag. Accessed using the len() function.
# + contains ( item ): Determines if the given target item is stored in the bag and returns the appropriate boolean value. Accessed using the in operator.
# + add( item ): Adds the given item to the bag.
# + remove(item): Removes and returns an occurrence of item from the bag. An exception is raised if the element is not in the bag.
# + iterator (): Creates and returns an iterator that can be used to iterate over the collection of items.

# An iterator for the Bag ADT implemented as a Python list.
class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration

class Bag:
    # Constructs an empty bag.
    def __init__(self):
        self._theItems = list()

    # Returns the number of items in the bag.
    def __len__(self):
        return len(self._theItems)

    # Determines if an item is contained in the bag.
    def __contains__(self, item):
        return item in self._theItems

    # Adds a new item to the bag
    def add(self, item):
        self._theItems.append(item)

    # Removes and returns an instance of the item from the bag.
    def remove(self, item):
        assert item in self._theItems, "The item must be in the bag."
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)

    # Returns an iterator for traversing the list of items.
    def __iter__(self, item):
        return _BagIterator(self._theItems)
