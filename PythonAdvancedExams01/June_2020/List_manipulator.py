from collections import deque


def list_manipulator(list_manipulate, command, place, *args):
    list_manipulate = deque(list_manipulate)
    if command == 'add':
        if place == 'beginning':
            list_manipulate.extendleft(reversed(args))

        elif place == 'end':
            list_manipulate.extend(args)

    elif command == 'remove':
        if place == 'beginning':
            if args:
                for _ in range(args[0]):
                    list_manipulate.popleft()

            elif not args:
                list_manipulate.popleft()

        elif place == 'end':
            if args:
                for _ in range(args[0]):
                    list_manipulate.pop()

            elif not args:
                list_manipulate.pop()

    return list(list_manipulate)