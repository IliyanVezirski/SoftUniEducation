from collections import deque

food_portions = [int(i) for i in input().split(', ')]
stamina = deque(int(i) for i in input().split(', '))
conquered_peaks = []
destinations = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70
}
days = 0
all_climbed = True
while True:
    days += 1
    if days > 7:
        break
    current_portion = food_portions.pop()
    current_stamina = stamina.popleft()
    test_sum = current_stamina + current_portion
    for destination_to_check, points in destinations.items():
        if destination_to_check not in conquered_peaks:
            if test_sum >= points:
                conquered_peaks.append(destination_to_check)
            break
for destination, points in destinations.items():
    if destination in conquered_peaks:
        pass
    else:
        all_climbed = False
        break

if all_climbed:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print(f'Conquered peaks:')
    print('\n'.join(conquered_peaks))
