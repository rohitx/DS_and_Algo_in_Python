'''
C-1.14: Write a short Python function that takes a sequence of integer values and determines
if there is a distinct pair of numbers in the sequence whose product is odd.

#Pseudo code
The basic thing to know here is that if a and b are odd, then ab is odd.
Look for odd numbers in the sequence
Find the first pair that is odd
return their product

'''


def getOddProducts(seq):
    odd = []
    for num in seq:
        if num % 2:
            odd.append(num)
    if len(odd) > 0:
        for i in range(len(odd)):
            print odd[i], odd[i+1]
        return ""


print getOddProducts([1, 2, 3, 4, 5, 6, 7, 8, 9])