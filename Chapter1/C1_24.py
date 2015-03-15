'''
C-1.24: Write a short Python function that counts the number of vowels in a
given character string.

#Pseudo-code:
Create a list with vowels
Get the length of the string
loop through the string characters and for every character check if
the character is in the list of vowels

'''
import random

vowels = ["a", "e", "i", "o", "u"]


def vowelsChecker(myList):
    n = len(myList)
    count = 0
    for i in range(n):
        if myList[i] in vowels:
            count += 1
    return count

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]

word = ""
for i in range(10):
    index = random.randint(0, 25)
    word += letters[index]
print word

print vowelsChecker(word)
print vowelsChecker("sequoiab")