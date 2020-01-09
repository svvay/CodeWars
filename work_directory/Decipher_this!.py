secret_library = {
    65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G',
    72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N',
    79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U',
    86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z',

    97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g',
    104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n',
    111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u',
    118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z',
}

string = '121qXvKIv 109KdzPEjU 66ulNzOBy 81ZTzp 74MqtlJSIuY 66UcdkEPbU 66JiXNVeJzZ'

my_try = 'NewaxaNHKaEM'

dep = my_try[0] + my_try[-1] + my_try[2:-1] + my_try[1]
print('lenDEP', len(dep), 'lenTRY', len(my_try))
print('Dep', dep)



def decipher_this(string):
    translate = ''[:-1]
    for word in string.split():
        words = str(word.strip('1234567890'))

        lenght = len(word) - len(words)

        code = int(word[:lenght])
        first_letter = secret_library[code]

        if len(str(word.strip('1234567890'))) >= 4:
            upgrade1 = first_letter + words
            upgrade2 = first_letter + upgrade1[-1] + upgrade1[2:-1] + upgrade1[1]
            translate += upgrade2 + ' '

        elif len(words) == len(word):
            translate += first_letter + ' '

        else:
            translate += (first_letter + words[::-1] + ' ')


    return translate[:-1]


print(decipher_this(string))


#CODEWARS

# def decipher_this(string):
#     words = []
#     for word in string.split():
#         code = ''.join(char for char in word if char.isdigit())
#         new_word = chr(int(code))+''.join(char for char in word if not char.isdigit())
#         words.append(new_word[:1]+new_word[-1]+new_word[2:-1]+new_word[1] if len(new_word)>2 else new_word)
#     return ' '.join(words)