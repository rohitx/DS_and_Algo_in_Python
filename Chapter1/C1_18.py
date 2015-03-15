'''
C-1.18:Demonstrate how to use Python's list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

#Pseudo-code:

We look at this in the following way:
(1) [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
(2) [0, 1, 2, 3,   4,  5,  6,  7,  8,  9]
(3) [0, 2, 3, 4,   5,  6   7,  8,  9,  10]

So we would produce (2) with range(10) with iterator i
we would produce the second one with i+1 such that
result = i * (i+1)

'''

result = [i * (i+1) for i in range(10)]
print result
