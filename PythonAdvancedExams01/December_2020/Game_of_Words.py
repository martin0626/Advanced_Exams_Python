def p_found(size_field, matrix):
    for r in range(size_field):
        for c in range(size_field):
            if matrix[r][c] == 'P':
                return [r, c]


def move(size_matrix, r_move, c_move, current_r, current_c):
    global field, final_result
    if 0 <= r_move < size_matrix and 0 <= c_move < size_matrix:
        if field[r_move][c_move] != '-':
            final_result += field[r_move][c_move]
            field[r_move][c_move] = 'P'
            field[current_r][current_c] = '-'

        else:
            field[r_move][c_move] = 'P'
            field[current_r][current_c] = '-'

    else:
        final_result = final_result[:-1]


final_result = input()
size = int(input())

field = [list(input()) for _ in range(size)]

commands_num = int(input())


for _ in range(commands_num):
    command = input()
    current_row, current_col = p_found(size, field)

    if command == 'up':
        move(size, current_row - 1, current_col, current_row, current_col)

    elif command == 'down':
        move(size, current_row + 1, current_col, current_row, current_col)

    elif command == 'left':
        move(size, current_row, current_col - 1, current_row, current_col)

    elif command == 'right':
        move(size, current_row, current_col + 1, current_row, current_col)

print(final_result)
[print(''.join(r)) for r in field]
