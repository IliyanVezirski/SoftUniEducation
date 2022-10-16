steps = ''
sum_steps = 0
diff = 0

while steps != 'Going home':
    steps = input()
    if steps == 'Going home':
        steps = input()
        steps_i = int(steps)
        sum_steps += steps_i
        if sum_steps >= 10000:
            diff = abs(sum_steps - 10000)
            print(f'Goal reached! Good job!')
            print(f'{diff} steps over the goal!')
            break
        else:
            diff = abs(sum_steps - 10000)
            print(f'{diff} more steps to reach goal.')
        break
    steps_i = int(steps)
    sum_steps += steps_i
    if sum_steps >= 10000:
        diff = abs(sum_steps - 10000)
        print(f'Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
        break