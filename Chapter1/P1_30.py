'''
P-1.30: Write a Python program that can take a positive integer greater than
2 as input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.

#Pseudo-code
Write a function that takes a value:
    check if the number is greater than 2
    Use the while loop to check the answer is > 2:
        Use the counter to count the loops
    return the count number

'''


def numberDivision(num):
    if num < 2:
        print "The number is less than 2"
    answer = num
    count = 0
    while answer > 2:
        answer = answer / 2.
        count += 1
    return count

print numberDivision(150)
