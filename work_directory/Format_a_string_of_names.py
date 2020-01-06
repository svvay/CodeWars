# Given: an array containing hashes of names
#
# Return: a string formatted as a list of names separated by
# commas except for the last two names, which should be separated by an ampersand.

names = [
    {'name': 'Bart'},
    {'name': 'Lisa'},
    {'name': 'Maggie'},
    {'name': 'Oggi'},
    ]

def namelist(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
print(namelist(names))