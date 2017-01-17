# Implementation of the Set ADT container using a Python list.
class Set:
    def __init__( self, *initElements ):
        self._theElements = list()

        if initElements:
            for e in initElements:
                self.add( e )

    def __len__( self ):
        return len( self._theElements )

    def __contains__( self, item ):
        return item in self._theElements

    def add( self, item ):
        if item not in self._theElements:
            self._theElements.append( item )

    def remove( self, item ):
        assert item in self, "The element must be in the set."
        self._theElements.remove( item )

    def __eq__( self, setB ):
        if len( self ) != len( setB ):
            return False
        else:
            return self.isSubsetOf( setB )

    def isSubsetOf( self, setB ):
        for i in self._theElements:
            if i not in setB._theElements:
                return False
        return True

    def isProperSubset( self, setB ):
        if len( self ) >= len( setB ):
            return False
        return self.isSubsetOf( setB )

    def union( self, setB ):
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for i in setB._theElements:
            if i not in self:
                newSet._theElements.append( i )

        return newSet

    def intersect( self, setB ):
        newSet = Set()
        for i in self._theElements:
            if i in setB:
                newSet._theElements.append( i )

        return newSet

    def difference( self, setB ):
        newSet = Set()
        for i in self._theElements:
            if i not in setB:
                newSet._theElements.append( i )

        return newSet

    __add__ = union
    __mul__ = intersect
    __sub__ = difference
    __lt__ = isSubsetOf

    def __str__( self ):
        print '(',
        for e in self._theElements:
            print e, ',',
        print ')',

    def __iter__( self ):
        return _SetGenerator( self._theElements )

def _SetGenerator( elements ):
    for i in elements:
        yield i


if __name__ == '__main__':
    smith = Set()
    smith.add( "CSCI-112" )
    smith.add( "MATH-121" )
    smith.add( "HIST-340" )
    smith.add( "ECON-101" )

    roberts = Set()
    roberts.add( "POL-101" )
    roberts.add( "ANTH-230" )
    roberts.add( "CSCI-112" )
    roberts.add( "ECON-101" )

    if smith == roberts :
        print( "Smith and Roberts are taking the same courses." )
    else :
        sameCourses = smith.intersect( roberts )
    if len(sameCourses) == 0:
        print( "Smith and Roberts are not taking any of "\
            + "the same courses." )
    else :
        print( "Smith and Roberts are taking some of the "\
            + "same courses:" )
        for course in sameCourses :
            print( course ), 
