start = int(input())
end = int(input())
magic_number = int(input())
combination = 0
right_combination = False
n2 = 0
n1 = 0
for n1 in range(start, end + 1):
    for n2 in range(start, end + 1):
        if right_combination:
            break
        combination += 1
        if n1 + n2 == magic_number:
            right_combination = True
            print(f'Combination N:{combination} ({n1} + {n2} = {magic_number})')
            break
if not right_combination:
    print(f'{combination} combinations - neither equals {magic_number}')