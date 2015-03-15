'''
C-1.22: Write a short Python program that takes two arrays a and b of length
n storing int values, and returns the dot product of a and b. That is, it
returns an array c of length n such that c[i] = a[i] dot b[i], for i = 0,n-1

#Pseudo code:
I will show to ways of doing this:
(1) Create arrays a and b using list comprehension
    create a blank list
    iterate through each element and do the dot product
    append the product to the blank list
    return the list
(1a) Could use generator to save two lines but generators are little weird
(2) Import numpy
    create numpy arrays
    simply multiply those arrays

'''
import numpy
import random
# Method 1:


def dotProduct(a, b):
    if len(a) != len(b):
        print "A and B don't have the same length"
    elif len(a) == len(b) == 1:
        return a[0] * b[0]
    else:
        product = []
        for i in range(len(a)):
            product.append(a[i] * b[i])
    return product

# Method 2:


def dotNumProduct(a, b):
    if a != 0 and b != 0:
        return a * b


a = [random.randint(0, 10) for i in range(5)]
b = [random.randint(0, 10) for i in range(5)]
print "This is a: ", a
print "This is b: ", b
print "This is product: ", dotProduct(a, b)
