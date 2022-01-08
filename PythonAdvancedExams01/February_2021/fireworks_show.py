from collections import deque


firework_effects = deque([int(num) for num in input().split(', ')])
explosive_power = [int(num) for num in input().split(', ')]

palm = 0
willow = 0
crossette = 0

while firework_effects and explosive_power:

    effect = firework_effects.popleft()
    power = explosive_power.pop()

    if effect <= 0:
        explosive_power.append(power)
        continue

    if power <= 0:
        firework_effects.appendleft(effect)
        continue

    sum_check = effect + power

    if sum_check % 3 == 0 and sum_check % 5 == 0:
        crossette += 1

    elif sum_check % 3 == 0:
        palm += 1

    elif sum_check % 5 == 0:
        willow += 1

    else:
        explosive_power.append(power)
        effect -= 1
        firework_effects.append(effect)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        print('Congrats! You made the perfect firework show!')
        break

if palm < 3 or willow < 3 or crossette < 3:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f'Firework Effects left: {", ".join([str(x) for x in firework_effects])}')

if explosive_power:
    print(f'Explosive Power left: {", ".join([str(x) for x in explosive_power])}')

print(f'Palm Fireworks: {palm}\nWillow Fireworks: {willow}\nCrossette Fireworks: {crossette}')