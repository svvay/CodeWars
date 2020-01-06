# You need to write regex that will validate a password to make sure it meets the following criteria:
#
#     At least six characters long
#     contains a lowercase letter
#     contains an uppercase letter
#     contains a number
#
# Valid passwords will only be alphanumeric characters.

regex = 'DSJKHD23f'
def validator(regex):
    ahtung = '!/\|^&*()$%#@,. _-?;:'
    up, lo, di = 0, 0, 0
    if len(regex) >= 6:
        for val in regex:
            if val.isupper():
                up += 1
            if val.islower():
                lo += 1
            if val.isdigit():
                di += 1
            if val in ahtung:
                return False
        if up and lo and di != 0:
            return True
        else:
            return False

print(validator(regex))


#CODEWARS
# regex = (
#     '^'            # start line
#     '(?=.*\d)'     # must contain one digit from 0-9
#     '(?=.*[a-z])'  # must contain one lowercase characters
#     '(?=.*[A-Z])'  # must contain one uppercase characters
#     '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
#     '{6,}'         # length at least 6 chars
#     '$'            # end line
# )