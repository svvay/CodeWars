# A pangram is a sentence that contains every single letter of the alphabet
# at least once. For example, the sentence "The quick brown fox jumps over the lazy dog"
# is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
# Ignore numbers and punctuation.
import string

alphabet = 'qwertyuiopasdfghjklzxcvbnm'
s = "The quick brown fox jumps over the lazy dog"

def is_pangram(s):
    numb = 0
    if len(s) >= 26:
        for string in alphabet:
            if (s.lower()).count(string):
                numb += 1
    if numb == 26:
        return True
    else:
        return False
print(is_pangram(s))


# CODEWARS
# import string
#
# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())
