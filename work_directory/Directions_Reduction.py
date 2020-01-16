# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions
# were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
#
# Going to one direction and coming back the opposite direction right away is a
# needless effort. Since this is the wild west, with dreadfull weather and not much water,
# it's important to save yourself some energy, otherwise you might die of thirst!
#
# How I crossed a mountain desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):
import re

plan = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan

print(dirReduc(plan))
