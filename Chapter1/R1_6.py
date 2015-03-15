'''
R-1.4: Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the odd positive integers smaller than n.

#Pseudo Code:

Similar to R-1.4, just that the range return
odd values
'''


def SumPositive(n):
    total = 0
    for i in range(1, n, 2):
        total += i**2
    return total

print SumPositive(5)
