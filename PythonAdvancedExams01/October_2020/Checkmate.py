chess = [input().split() for r in range(8)]
queens_can_catch = []


def up_move(row, col):
    global chess, queens_can_catch
    current_row = row
    while True:
        current_row -= 1
        if 0 <= current_row < 8:

            if chess[current_row][col] == 'K':
                queens_can_catch.append([row, col])
                return

            elif chess[current_row][col] == 'Q':
                return

        else:
            return


def down_move(row, col):
    global chess, queens_can_catch
    current_row = row
    while True:
        current_row += 1
        if 0 <= current_row < 8:

            if chess[current_row][col] == 'K':
                queens_can_catch.append([row, col])
                return

            elif chess[current_row][col] == 'Q':
                return

        else:
            return


def left_move(row, col):
    global chess, queens_can_catch
    current_col = col
    while True:
        current_col -= 1
        if 0 <= current_col < 8:

            if chess[row][current_col] == 'K':
                queens_can_catch.append([row, col])
                return

            elif chess[row][current_col] == 'Q':
                return

        else:
            return


def right_move(row, col):
    global chess, queens_can_catch
    current_col = col
    while True:
        current_col += 1
        if 0 <= current_col < 8:

            if chess[row][current_col] == 'K':
                queens_can_catch.append([row, col])
                return

            elif chess[row][current_col] == 'Q':
                return

        else:
            return


def prime_diagonal_up(row, col):
    global chess, queens_can_catch
    current_row = row
    current_col = col
    while True:
        current_col -= 1
        current_row -= 1
        if 0 <= current_row < 8 and 0 <= current_col < 8:
            if chess[current_row][current_col] == 'K':
                queens_can_catch.append([row, col])
                return

            elif chess[current_row][current_col] == 'Q':
                return

        else:
            return


def prime_diagonal_down(row, col):
    global chess, queens_can_catch
    current_row = row
    current_col = col
    while True:
        current_col += 1
        current_row += 1
        if 0 <= current_row < 8 and 0 <= current_col < 8:
            if chess[current_row][current_col] == 'K':
                queens_can_catch.append([row, col])
                return

            elif chess[current_row][current_col] == 'Q':
                return

        else:
            return


def secondary_diagonal_down(row, col):
    global chess, queens_can_catch
    current_row = row
    current_col = col
    while True:
        current_col -= 1
        current_row += 1
        if 0 <= current_row < 8 and 0 <= current_col < 8:
            if chess[current_row][current_col] == 'K':
                queens_can_catch.append([row, col])
                return

            elif chess[current_row][current_col] == 'Q':
                return

        else:
            return


def secondary_diagonal_up(row, col):
    global chess, queens_can_catch
    current_row = row
    current_col = col
    while True:
        current_col += 1
        current_row -= 1
        if 0 <= current_row < 8 and 0 <= current_col < 8:
            if chess[current_row][current_col] == 'K':
                queens_can_catch.append([row, col])
                return

            elif chess[current_row][current_col] == 'Q':
                return

        else:
            return


def queen_move(current_r, current_c):
    up_move(current_r, current_c)
    down_move(current_r, current_c)
    left_move(current_r, current_c)
    right_move(current_r, current_c)
    prime_diagonal_up(current_r, current_c)
    prime_diagonal_down(current_r, current_c)
    secondary_diagonal_down(current_r, current_c)
    secondary_diagonal_up(current_r, current_c)


for r in range(8):
    for c in range(8):
        if chess[r][c] == 'Q':
            queen_move(r, c)

if queens_can_catch:
    [print(c) for c in queens_can_catch]

else:
    print('The king is safe!')