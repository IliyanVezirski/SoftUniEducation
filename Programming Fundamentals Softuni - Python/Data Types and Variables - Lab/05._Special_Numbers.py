numbers = int(input())
is_special = False
for i in range(1, numbers + 1):
    sum_of_digits = 0
    number = str(i)
    for n in number:
        sum_of_digits += int(n)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True
    print(f'{i} -> {is_special}')
    is_special = False