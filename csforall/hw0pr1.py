# CS5 Gold/Black: Lab 0
# Filename: hw0pr1.py
# Name:
# Problem description: The four fours challenge!

# add several more lines similar to this one so
# that you compute 16 of the 21 values from 0 through 20 using exactly four
# fours. You should use Python's arithmetic operations:
#    +    addition
#    -    subtraction or negation
#    *    multiplication
#    /    division
#    (   )    parentheses for grouping
#    **    power
#    You may also use 44 or 4.4, which count as two fours,
#    or .4, which counts as one four.
#    See below for two more allowable operations, sqrt and factorial, both in
#    the math library
#    The 16 out of 21 is so that you can choose a few to skip!
#    Here are what the results, but not the source code, will look like. 
#    Remember you need only 16 of the 21:
#    Zero is 0
#    One is 1
#    Two is 2
#    Three is 3
#    Four is 4
#    Five is 5
#    Six is 6
#    Seven is 7
#    Eight is 8
#    Nine is 9
#    Ten is 10
#    Eleven is 11
#    Twelve is 12
#    Thirteen is 13
#    Fourteen is 14
#    Fifteen is 15
#    Sixteen is 16
#    Seventeen is 17
#    Eighteen is 18
#    Nineteen is 19
#    Twenty is 20

from math import *

print("Zero is", 4+4-4-4)
print("One is", 4-4+4//4)
print("Two is", 4//4+4//4)
print("Three is", sqrt(4)+sqrt(4)-4//4)
print("Four is", sqrt(4)+sqrt(4)+4-4)
print("Five is", factorial(4)//4-4//4)
print("Six is", factorial(4)//4+4-4)
print("Seven is", 4+4-4//4)
print("Eight is", 4+4+4-4)
print("Nine is", 4+4+4//4)
print("Ten is",'xx')
print("Eleven is",'xx')
print("Twelve is",sqrt(4)+sqrt(4)+4+4)
print("Thirteen is",44//4+sqrt(4))
print("Fourteen is",factorial(4)//4+4+4)
print("Fifteen is",4*4-4//4)
print("Sixteen is",4+4+4+4)
print("Seventeen is",'xx')
print("Eighteen is",'xx')
print("Nineteen is",factorial(4)-4-4//4)
print("Twenty is",factorial(4)-4+4-4)
