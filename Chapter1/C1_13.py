'''
C-1.13: Write a pseudo-code description of a function that reverses a list of
n integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function for
doing the same thing.

#Pseudo-code:
write a function that takes in a list:
    create an empty list, myList
    iterate over each value such that:
        append.myList(list[-1-i])
    return myList

'''
import random


def reverseList(myList):
    if len(myList) == 0:
        print 'There is no list to reverse'
    elif len(myList) == 1:
        return myList
    else:
        revList = []
        for i in range(len(myList)):
            revList.append(myList[-1-i])
    return revList

myList = [random.randint(1,100) for i in range(10)]
print myList
print reverseList(myList)