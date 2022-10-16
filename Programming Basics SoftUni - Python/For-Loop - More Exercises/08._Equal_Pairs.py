number = int(input())
sum_value = 0
old_value = 0
diff = 0
for i in range(1, number + 1):
    number_1 = int(input())
    number_2 = int(input())
    old_value = sum_value
    sum_value = number_1 + number_2
    if old_value == sum_value:
        sum_value = sum_value
    else:
        diff = abs(sum_value - old_value)
if number == 1:
    if number_1 - number_2 != 0:
        diff = abs(number_1 - number_2)
        print(f'No, maxdiff={diff}')
    else:
        print(f'Yes, value={sum_value}')
else:
    if old_value == sum_value:
        print(f'Yes, value={sum_value}')
    else:
        print(f'No, maxdiff={diff}')