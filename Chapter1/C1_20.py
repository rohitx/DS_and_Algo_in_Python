'''
C-1.20: Python's random module includes a function shuffle(data) that accepts
a list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a more basic
function randint(a,b) that returns a uniformly random integer from a to b,
including both endpoints. Using only the randint function, implement your
own version of the shuffle function.

#Pseudo-code:
We use randint() function as indices for the list such that we can
index the list and return a random array. We do this the number of times
equal to length of the list so every element is shuffled at least once.

'''
import random


def myShuffle(myList):
    n = len(myList)
    for i in range(n):
        index_1 = random.randint(1, n-1)
        index_2 = random.randint(1, n-1)
        myList[index_1], myList[index_2] = myList[index_2], myList[index_1]
    return myList

myList = [random.randint(0, 10) for i in range(10)]
print "Orignal List:  ", myList
shuf_list = myShuffle(myList)
print "Shuffled List: ", shuf_list
