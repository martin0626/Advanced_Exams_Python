from math import floor


size = int(input())

field = [input().split() for row in range(size)]
path = []
is_lose = False
coin_collected = 0


def p_found():
    global field, size
    for r in range(size):
        for c in range(size):
            if field[r][c] == 'P':
                return [r, c]


def move(size_matrix, r_move, c_move, current_r, current_c):
    global field, path, is_lose, coin_collected
    if 0 <= r_move < size_matrix and 0 <= c_move < size_matrix:
        try:
            coin_collected += int(field[r_move][c_move])
            field[current_r][current_c] = '0'
            field[r_move][c_move] = 'P'
            path.append([r_move, c_move])

        except ValueError:
            is_lose = True

    else:
        is_lose = True


while True:
    command = input()
    current_row, current_col = p_found()

    if command == 'up':
        move(size, current_row - 1, current_col, current_row, current_col)

    elif command == 'down':
        move(size, current_row + 1, current_col, current_row, current_col)

    elif command == 'left':
        move(size, current_row, current_col - 1, current_row, current_col)

    elif command == 'right':
        move(size, current_row, current_col + 1, current_row, current_col)

    else:
        pass

    if coin_collected >= 100:
        print(f"You won! You've collected {coin_collected} coins.")
        break

    if is_lose:
        print(f"Game over! You've collected {floor(coin_collected/2)} coins.")
        break

print('Your path:')
[print(p) for p in path]
