def is_valid(s, r, c):
    return 0 <= r < s and 0 <= c < s


def up_move(matrix, r, c, n, f):
    is_out = False

    if is_valid(n, (r - 1), c):
        matrix[r][c] = '.'
        if matrix[r - 1][c] == '*':
            f += 1
            matrix[r - 1][c] = 'S'

        elif matrix[r - 1][c] == 'B':
            matrix[r - 1][c] = '.'
            row_teleport, col_teleport = current_pos(matrix, n, 'B')
            matrix[row_teleport][col_teleport] = 'S'

        else:
            matrix[r - 1][c] = 'S'

        return matrix, is_out, f

    is_out = True
    matrix[r][c] = '.'
    return matrix, is_out, f


def down_move(matrix, r, c, n, f):
    is_out = False

    if is_valid(n, (r + 1), c):
        matrix[r][c] = '.'
        if matrix[r + 1][c] == '*':
            f += 1
            matrix[r + 1][c] = 'S'

        elif matrix[r + 1][c] == 'B':
            matrix[r + 1][c] = '.'
            row_teleport, col_teleport = current_pos(matrix, n, 'B')
            matrix[row_teleport][col_teleport] = 'S'

        else:
            matrix[r + 1][c] = 'S'

        return matrix, is_out, f

    is_out = True
    matrix[r][c] = '.'
    return matrix, is_out, f


def left_move(matrix, r, c, n, f):
    is_out = False

    if is_valid(n, r, (c - 1)):
        matrix[r][c] = '.'
        if matrix[r][c - 1] == '*':
            f += 1
            matrix[r][c - 1] = 'S'

        elif matrix[r][c - 1] == 'B':
            matrix[r][c - 1] = '.'
            row_teleport, col_teleport = current_pos(matrix, n, 'B')
            matrix[row_teleport][col_teleport] = 'S'
        else:
            matrix[r][c - 1] = 'S'

        return matrix, is_out, f

    is_out = True
    matrix[r][c] = '.'
    return matrix, is_out, f


def right_move(matrix, r, c, n, f):
    is_out = False

    if is_valid(n, r, (c + 1)):
        matrix[r][c] = '.'
        if matrix[r][c + 1] == '*':
            f += 1
            matrix[r][c + 1] = 'S'

        elif matrix[r][c + 1] == 'B':
            matrix[r][c + 1] = '.'
            row_teleport, col_teleport = current_pos(matrix, n, 'B')
            matrix[row_teleport][col_teleport] = 'S'

        else:
            matrix[r][c + 1] = 'S'

        return matrix, is_out, f

    is_out = True
    matrix[r][c] = '.'
    return matrix, is_out, f


def current_pos(matrix, n, to_find):
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == to_find:
                return [r, c]


size = int(input())

field = [[c for c in input()] for r in range(size)]

food = 0
is_outside = False

while True:
    command = input()
    snake_row, snake_col = current_pos(field, size, 'S')

    if command == 'up':
        field, is_outside, food = up_move(field, snake_row, snake_col, size, food)

    elif command == 'down':
        field, is_outside, food = down_move(field, snake_row, snake_col, size, food)

    elif command == 'left':
        field, is_outside, food = left_move(field, snake_row, snake_col, size, food)

    elif command == 'right':
        field, is_outside, food = right_move(field, snake_row, snake_col, size, food)

    if is_outside:
        print('Game over!')
        break

    if food >= 10:
        print('You won! You fed the snake.')
        break

print(f'Food eaten: {food}')
[print(''.join(line)) for line in field]
