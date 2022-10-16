number = float(input())
if number <= 100 and number >= 1:
    print(f'The number {number} is between 1 and 100')
else:
    while number < 1 or number > 100:
        number = float(input())
        if number <= 100 and number >= 1:
            print(f'The number {number} is between 1 and 100')
            break
