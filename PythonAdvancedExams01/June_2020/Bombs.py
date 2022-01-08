from collections import deque


def is_fulfill(bombs_num):
    return bombs_num['smoke'] >= 3 and bombs_num['datura'] >= 3 and bombs_num['cherry'] >= 3


bomb_effect = deque([int(n) for n in input().split(', ')])
bomb_casing = deque([int(n) for n in input().split(', ')])

bombs = {'cherry': 0, 'datura': 0, 'smoke': 0}

while bomb_casing and bomb_effect:
    effect = bomb_effect.popleft()
    case = bomb_casing.pop()

    if effect + case == 40:
        bombs['datura'] += 1

    elif effect + case == 60:
        bombs['cherry'] += 1

    elif effect + case == 120:
        bombs['smoke'] += 1

    else:
        if effect >= 0:
            bomb_effect.appendleft(effect)

        case -= 5
        if case >= 0:
            bomb_casing.append(case)

    if is_fulfill(bombs):
        print(f'Bene! You have successfully filled the bomb pouch!')
        break


if not is_fulfill(bombs):
    print(f"You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print(f'Bomb Effects: empty')

else:
    print(f'Bomb Effects: {", ".join([str(n) for n in bomb_effect])}')

if not bomb_casing:
    print('Bomb Casings: empty')

else:
    print(f'Bomb Casings: {", ".join([str(n) for n in bomb_casing])}')

print(f'Cherry Bombs: {bombs["cherry"]}\nDatura Bombs: {bombs["datura"]}\nSmoke Decoy Bombs: {bombs["smoke"]}')
