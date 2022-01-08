def numbers_searching(*args):
    duplicate_nums = []
    for n in args:
        if args.count(n) > 1 and n not in duplicate_nums:
            duplicate_nums.append(n)

    missing_nums = []
    for n in range(min(args), max(args)):
        if n not in args:
            missing_nums.append(n)
    return [max(missing_nums), sorted(duplicate_nums)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
