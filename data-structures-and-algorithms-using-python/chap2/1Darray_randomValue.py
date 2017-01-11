from myarray import Array
import random

valueList = Array( 100 )

for i in range( len( valueList ) ):
    valueList[ i ] = random.random()

for val in valueList:
    print val
