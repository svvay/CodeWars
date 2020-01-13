# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

letters = 'abcdefghijklmnopqrstuvwxyz'
text = "The sunset sets at twelve o'clock."

def alphabet_position(text):
    numb = []
    for letter in text.lower():
        if letter in letters:
           numb.append(letters.index(letter) + 1)
    return ' '.join(map(str, numb))


print(alphabet_position(text))



# CODEWARS
# def alphabet_position(text):
#   al = 'abcdefghijklmnopqrstuvwxyz'
#   return " ".join(filter(lambda a: a != '0', [str(al.find(c) + 1) for c in text.lower()]))