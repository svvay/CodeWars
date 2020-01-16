# Your task is to sort a given string. Each word in the string will contain a single
# number. This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input
# String will only contain valid consecutive numbers.

sentence = "is2 Thi1s T4est 3a"


def order(sentence):
	return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))


# CODE WARS
# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
