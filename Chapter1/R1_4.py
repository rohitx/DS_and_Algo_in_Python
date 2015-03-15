'''
R-1.4: Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the positive integers smaller than n.

#Pseudo Code:

Take in the integer n
Set a variable called total to zero
Use the range to get positive values
Square them and add them to total
'''


def SumPositive(n):
    total = 0
    for i in range(1, n):
        total += i**2
    return total

print SumPositive(3)
