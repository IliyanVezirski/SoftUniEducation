number = int(input())

number_of_percentage = number // 10
number_of_dots = 10 - number_of_percentage


if number == 100:
    print(f'100% Complete!')
    print(f'[' + number_of_percentage * '%' + number_of_dots * '.' + ']')
else:
    print(f'{number}% [' + number_of_percentage * '%' + number_of_dots * '.' + ']')
    print(f'Still loading...')