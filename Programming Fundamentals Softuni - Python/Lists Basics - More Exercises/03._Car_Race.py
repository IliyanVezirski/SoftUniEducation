times = [int(n) for n in input().split()]
half = len(times) // 2
left_racer = times[:half]
right_racer = times[half + 1:]
sum_left = 0
sum_right = 0
for time in left_racer:
    sum_left += time
    if time == 0:
        sum_left *= 0.8
for time in right_racer:
    sum_right += time
    if time == 0:
        sum_right *= 0.8
sum_right = round(float(sum_right), 1)
sum_left = round(float(sum_left), 1)

if sum_right > sum_left:
    print(f'The winner is left with total time: {sum_left:.1f}')
else:
    print(f'The winner is right with total time: {sum_right:.1f}')