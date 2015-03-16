'''
P-1.34: Write a Python program that inputs a document and then outputs a
bar-chart plot of the frequencies of each alphabet character that appears
in that document

#Pseudo-Code
Write a function:
    Get the document path
    read it in with a Python function readline() which recreates a long string
    get the length of the string
    create an empty dictionary called "characters"
    use the loop to read in each character:
        if the character is not an empty string:
            if the character is in the dictionary:
                add +1 to it
           if not:
                create a new character in the dictionary
                and assign +1 to it
    return dictionary
'''
