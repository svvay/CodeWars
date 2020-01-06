# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.
#
# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
source_array = [5, 3, 2, 8, 1, 4]
print(sorted(source_array))
def sort_array(source_array):
    return sorted([ascending for ascending in source_array if ascending % 2 != 0])

print(sort_array(source_array))
