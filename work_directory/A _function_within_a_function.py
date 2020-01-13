# Given an input n, write a function always that returns a function which returns n. Ruby should return a lambda or a proc.
#
# three = always(3)
# three() /* returns 3 */

x = 3

def always(x):
    return lambda y=0: y + x

print(always(x))


# COdewars
# def always(n=0):
#     return lambda: n