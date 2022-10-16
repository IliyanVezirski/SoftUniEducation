number = int(input())
range_glasses = number * 5
side_glasses = (range_glasses - number) // 2
print('*' * side_glasses + ' ' * number + '*' * side_glasses)
for i in range(1, number - 1):
    if number % 2 == 1:
        if i == (number - 1) / 2:
            print('*' + '/' * (side_glasses - 2) + '*' + '|' * number + '*' + '/' * (side_glasses - 2) + '*')
        else:
            print('*' + '/' * (side_glasses - 2) + '*' + ' ' * number + '*' + '/' * (side_glasses - 2) + '*')
    else:
        if i == number / 2 - 1:
            print('*' + '/' * (side_glasses - 2) + '*' + '|' * number + '*' + '/' * (side_glasses - 2) + '*')
        else:
            print('*' + '/' * (side_glasses - 2) + '*' + ' ' * number + '*' + '/' * (side_glasses - 2) + '*')
print('*' * side_glasses + ' ' * number + '*' * side_glasses)