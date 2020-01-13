fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]

moves = ['left']*8
# print(moves)
# print(len(moves))
initial_position = 0.0


def street_fighter_selection(fighters, initial_position, moves):

    step = []
    x = 0
    y = 0

    for move in moves:

        if y == 5:
            y = -1
        if y == -6:
            y = 0

        if move == 'up':
            x = 0
            step.append(fighters[x][y])

        elif move == 'right' and x == 0:
            y += 1
            step.append(fighters[x][y])

        elif move == 'left' and x == 0:
            y -= 1
            step.append(fighters[x][y])

        elif move == 'down':
            x = 1
            step.append(fighters[x][y])

        elif move == 'right' and x == 1:
            y += 1
            step.append(fighters[x][y])

        elif move == 'left' and x == 1:
            y -= 1
            step.append(fighters[x][y])
        else:
            pass

    return step

print(street_fighter_selection(fighters, initial_position, moves))
