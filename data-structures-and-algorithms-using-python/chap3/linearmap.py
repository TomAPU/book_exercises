# Implementation of Map ADT using a single list.
class _MapEntry:
    def __init__(self, key, val):
        self.key = key
        self.value = val

class Map:
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    # Helper method used to find the index position of a category. If the
    # key is not found, None is returned.
    def _findPosition(self, key):
        for e, ndx in enumerate(self._entryList):
            if e.key == key:
                return ndx
        return None

    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    # Adds a new entry to the map if the key does exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add(self, key, val):
        ndx = self._findPosition(self, key)
        if ndx is not None:
            self._entryList[ndx].value = val
            return False
        else:
            self._entryList.append(_MapEntry( key, val) )
            return True

    def valueOf(self, key):
        ndx = self._findPosition(self, key)
        assert ndx is not None, "Invalid map key."
        return self._entryList[ndx].value

    def remove(self, key):
        ndx = self._findPosition(self, key)
        assert ndx is not None, "Invalid map key."
        self._entryList.pop(ndx)

    def keyArray(self):
        keys = list()
        for e in self._entryList:
            keys.append(e.key
        return keys

    def __iter__(self):
        return _MapGenerator(self._entryList)

    __setitem__ = add
    __getitem__ = valueOf

def _MapGenerator(entryList):
    for e in entryList:
        yield e
