# Your job is to write a function which increments a string, to create a new string.
#
#     If the string already ends with a number, the number should be incremented by 1.
#     If the string does not end with a number. the number 1 should be appended to the new string.
#
# Attention: If the number has leading zeros the amount of digits should be considered.

strng = "(FWMi%Y899o060330413866183WP#I593446567866L|Kv.8872568[d}Pr~Qn002527239"
print(strng.rstrip("0123456789"))

def increment_string(s):
    if s and s[-1].isdigit():
        num = s[len(s.rstrip("0123456789")):]
        return s[:-len(num)] + str(int(num) + 1).zfill(len(num))

    return s + "1"
print(increment_string(strng))


# def increment_string(strng):
#     zero = 0
#     numb = '0987654321'
#     numbs = ''
#     if strng.isalpha() == True:
#         return (strng + '1')
#     elif len(strng) == 0:
#         return '1'
#     else:
#         for string in strng:
#             if string in numb:
#                 numbs += string
#
#         lenght = len(numbs)
#         numbs = (int(numbs)) + 1
#         if lenght > len(str(numbs)):
#             multiply = lenght - len(str(numbs))
#             return (strng[:-lenght] + ('0'*multiply) + str(numbs))
#         else:
#             return (strng[:-lenght] + str(numbs))
#
# print(increment_string(strng))