def shot_sum(current_r, current_c):
    global size, players, field
    sides = [[current_r, 0], [current_r, size - 1], [size - 1, current_c], [0, current_c]]
    sum_points = 0
    for side in sides:
        r = side[0]
        c = side[1]
        sum_points += int(field[r][c])
    return sum_points


size = 7

players = [[p, 501, 0] for p in input().split(', ')]

field = [input().split() for line in range(size)]
current_index = 0

while True:

    name = players[current_index][0]
    players[current_index][2] += 1

    coordinates = input()[1:-1].split(', ')
    row = int(coordinates[0])
    col = int(coordinates[1])

    if not (0 <= row < size and 0 <= col < size):
        pass

    elif field[row][col] == 'D':
        points_decrease = shot_sum(row, col) * 2
        players[current_index][1] -= points_decrease

    elif field[row][col] == 'T':
        points_decrease = shot_sum(row, col) * 3
        players[current_index][1] -= points_decrease

    elif field[row][col] == 'B':
        print(f'{name} won the game with {players[current_index][2]} throws!')
        break

    else:
        players[current_index][1] -= int(field[row][col])

    if players[current_index][1] <= 0:
        print(f'{name} won the game with {players[current_index][2]} throws!')
        break

    current_index += 1
    if current_index == len(players):
        current_index = 0