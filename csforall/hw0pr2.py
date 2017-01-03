# coding: utf-8
#
# hw0pr2.py

# A rock, paper, scissors program

"""
Notes on this rps function:

"""

import random        # a random library

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game ...)
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    user = input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    print()

    print('the user (you) chose', user)
    print('the comp (I)   chose', comp)
    print()

    if user == 'rock':
        print('Ha! I really chose paper -- I WIN!')

    print("Better luck next time...")
