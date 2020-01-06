# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.
#
# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
arr = [5, 3, 2, 8, 1, 4]
# print(sorted(source_array))
# [1, 3, 5, 11, 2, 8, 4] should equal [1, 3, 2, 8, 5, 4, 11]
# [5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


# def sort_odds(lst):
#     sorted_odds = sorted([n for n in lst if n%2])
#     print(sorted_odds)
#     new_list = []
#     for n in lst:
#         if n%2:
#             new_list.append(sorted_odds.pop(0))
#         else:
#             new_list.append(n)
#     return list(new_list)
# print(sort_odds(source_array))


# CODE WARS
def sort_array(arr):
  odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
  print(odds)
  return [x if x % 2 == 0 else odds.pop() for x in arr]
print(sort_array(arr))