number = int(input())
n = 1
for rows in range(1, number + 1):
    for col in range(1, rows + 1):
        print(f'{n}', end=" ")

        n += 1
        if n > number:
            break
    if n > number:
        break
    print()