'''
R-1.12: Python's random module includes a function choice(data) that returns a random element
from a non-empty sequence. The random module includes a more basic function randrange, with
parameterization similar to the built-in range function, that return a random choice from the
given range. Using only the randrange function, implement your own version of the choice function.


# Pseudo Code

Take in the list
Get the length of the list
use randrange as index
return the value from the list

'''
import random


def myChoice(seq):
    n = len(seq)
    if n == 0:
        print "Sequence has no values"
    value = seq[random.randrange(n)]
    return value

sequence = [1, 4, 3, 7, 8, 10]
print myChoice(sequence)
