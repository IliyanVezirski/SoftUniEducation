start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination_count = 0
is_found = False
for first in range(start_number, end_number + 1):
    if is_found:
        break
    for second in range(start_number, end_number + 1):
        combination_count += 1
        if first + second == magic_number:
            is_found = True
            print(f'Combination N:{combination_count}', end=' ')
            print(f'({first} + {second} = {magic_number})')
if not is_found:
    print(f'{combination_count} combinations - neither equals {magic_number}')