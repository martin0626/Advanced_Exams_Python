size = int(input())
n = int(input())
field = [[0 for c in range(size)] for r in range(size)]


def is_right(s, r, c):
    return 0 <= r < s and 0 <= c < s


def mine_placer(matrix, row_mine, col_mine, s):
    if is_right(s, row_mine, col_mine):
        matrix[row_mine][col_mine] = '*'
    return matrix


def field_maker(matrix, size_m):
    for curr_row in range(size_m):
        for curr_col in range(size_m):
            if matrix[curr_row][curr_col] == 0:
                matrix[curr_row][curr_col] += mine_detector(matrix, size_m, curr_row, curr_col)
    return matrix


def mine_detector(matrix, size_m, r, c):
    move_rows = [-1, 1, 0, 0, 1, 1, -1, -1]
    move_cols = [0, 0, 1, -1, -1, 1, 1, -1]
    mines = 0
    for i in range(8):
        if is_right(size_m, r + move_rows[i], c + move_cols[i]):
            if matrix[r + move_rows[i]][c + move_cols[i]] == '*':
                mines += 1
    return mines


for _ in range(n):
    row, col = input()[1:-1].split(', ')
    row = int(row)
    col = int(col)
    field = mine_placer(field, row, col, size)

[print(" ".join(str(el) for el in line)) for line in field_maker(field, size)]
