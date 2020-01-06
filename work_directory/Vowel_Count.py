# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, and u as vowels for this Kata.
#
# The input string will only consist of lower case letters and/or spaces.

inputStr = 'sdfghjkwertyuimnbvc'

def getCount(inputStr):
    num_vowels = 0
    vowels = 'aeiou'
    for string in inputStr:
        if string in vowels:
            num_vowels += 1
    return num_vowels

print(getCount(inputStr))

# CODEWARS
# def getCount(s):
#     return sum(c in 'aeiou' for c in s)