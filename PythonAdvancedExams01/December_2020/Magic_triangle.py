def is_valid(r, c, size):
    return 0 <= r < size and 0 <= c < size


def get_magic_triangle(n):
    triangle = [[0 for _ in range(row)] for row in range(1, n + 1)]

    for row in range(n):
        for col in range(len(triangle[row])):
            if is_valid(row - 1, col - 1, n):
                try:
                    triangle[row][col] += triangle[row - 1][col]
                    triangle[row][col] += triangle[row - 1][col - 1]
                except IndexError:
                    triangle[row][col] = 1
            else:
                triangle[row][col] = 1

    return triangle


print(get_magic_triangle(5))
