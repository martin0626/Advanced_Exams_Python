def flights(*args):
    result = {}
    for i in range(len(args)):
        if args[i] == 'Finish':
            break

        elif isinstance(args[i], int):
            result[args[i - 1]] += args[i]

        else:
            if args[i] not in result:
                result[args[i]] = 0

    return result
