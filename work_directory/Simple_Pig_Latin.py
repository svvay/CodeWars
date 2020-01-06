# Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.

text = 'Aaa ! Hallo a A world ?'
def pig_it(text):
    pig_text = []
    for latin in text.split():
        if latin.isalpha():
            pig_text.append(latin[1:] + latin[0] + 'ay')
        else:
            pig_text.append(latin)
    return ' '.join(pig_text)
print(pig_it(text))


# CODEWARS
# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])