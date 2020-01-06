# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b.
a = [2, 1, 2, 1]
b = [1]

def array_diff(a, b):
    return [l for l in a if l not in b]

print(array_diff(a, b))
