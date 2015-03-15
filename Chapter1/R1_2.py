'''
R-1.2: Write a short Python function is_even(k), that takes an integer value
and return True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, division operators.


#Pseudo Code

Take in a value.
store the value in a variable called result
create a loop with a range to that value
    At every time in the loop,
        subtract that result by 2
            if the result is zero
                return True
            else if the result is negative:
                return False
wrap the whole thing in a loop
'''


def is_even(n):
    result = n
    for i in range(n):
        result = result - 2
        if (result == 0):
            return True
        elif (result < 0):
            return False

print is_even(31)