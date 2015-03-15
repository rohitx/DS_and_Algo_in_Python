'''
R-1.1: Write a short Python function, is_multiply(n, m), that takes two
integer values and returns True if n is a multiple of m, that is, n = mi
for some integer i, and False otherwise

# Pseudo Code
get two values, n and m
check if n % m is 0
    if it is
        then return True
    else return
        return False

wrap the whole thing into a function

'''


def is_multiply(n, m):
    if (n < m):
        n, m = m, n
    if (n % m == 0):
        return True
    else:
        return False

print is_multiply(2, 4)
print is_multiply(4, 2)
