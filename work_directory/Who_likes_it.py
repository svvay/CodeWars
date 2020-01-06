# You probably know the "like" system from Facebook and other pages. People can "like"
# blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#
# Implement a function likes :: [String] -> String, which must take in input array,
# containing the names of people who like an item. It must return the display text as shown in the examples:

names = ['Peter', 'arsi', 'Alsu', 'Sergiy', 'Sasha']
print(len(names))

def likes(names):
    lenght = len(names)
    if lenght == 0:
        return "no one likes this"
    elif lenght == 1:
        return f'{names[0]} likes this'
    elif lenght == 2:
        return f'{names[0]} and {names[1]} like this'
    elif lenght == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {lenght - 2} others like this'

print(likes(names))


# CODEWARS
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)
# print(likes(names))