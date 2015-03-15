'''
R-1.3: Write a short Python function, minmax(data), that takes a sequence
of one or more numbers, and returns the smallest and largest numbers in the
form of a tuple of length two. Do not use the built-in functions min or max
in implementing your solution

#Psuedo-code:

define a function, minmax():
    check to see if it is a list
    iterative over the elements of the list:
        check to see if each element is a numeral
        pick the first element as min value
        compare with the next to see if it is bigger or smaller
        if it is bigger continue with the next one
        if it is smaller chose the next as the current and iterate
        store the smallest value
    repeat the whole loop to look for the max value
    return the max value
    return the tuple.
'''
import collections
import random

def minmax(myList):
    if not isinstance(myList, collections.Iterable):
        raise TypeError("Parameters must be an Iterable type")
    min_value = myList[0]
    max_value = myList[0]
    for i in range(len(myList)):
        if not isinstance(myList[i], (int, float)):
            raise TypeError("Elements must be numeric")
        if myList[i] < min_value:
            min_value = myList[i]
        elif myList[i] > max_value:
            max_value = myList[i]
    return (min_value, max_value)


myList = [random.randint(1,100) for i in range(10)]
print "Random list: ", myList
#print minmax(["A", "C", "Do"])
print minmax(myList)