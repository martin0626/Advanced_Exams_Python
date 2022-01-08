from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    k = args[1]
    best_rotation = {'rotation': 0, 'sum': -1000}

    for r in range(k + 1):
        current_sum = 0
        for i, x in enumerate(numbers):
            current_sum += x * i

        if current_sum > best_rotation['sum']:
            best_rotation['sum'] = current_sum
            best_rotation['rotation'] = r
        numbers.rotate(1)

    return f'Best pureness {best_rotation["sum"]} after {best_rotation["rotation"]} rotations'
