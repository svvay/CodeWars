# Description:
# Encrypt this!
# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

secret_library = {
    'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71,
    'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78,
    'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85,
    'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90,

    'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103,
    'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110,
    'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117,
    'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122,
}

text = "Say the must be have nice dishes"

def encrypt_this(text):
    encript_text = []
    for i in text.split():
        lenght = len(i)
        if lenght == 1:
            numb = str(secret_library[i[0]])
            encript_text.append(numb)
        elif lenght == 2:
            numb = str(secret_library[i[0]]) + i[1]
            encript_text.append(numb)
        else:
            numb = str(secret_library[i[0]]) + i[-1] + i[2:-1] + i[1]
            encript_text.append(numb)
    return ' '.join(map(str, encript_text))

print(encrypt_this(text))


# CODE WARS
# #
# def process_word(word):
#     return str(ord(word[0])) + ((word[-1] + word[2:-1] + word[1]) if len(word) > 2 else word[1:])
#
# def encrypt_this(text):
#     return " ".join(map(process_word, text.split()))