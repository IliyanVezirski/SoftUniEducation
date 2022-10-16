number = float(input())
if number < 0:
    print('Negative number!')
while number >= 0:
    print(f' Result:{(number * 2): .2f}')
    number = float(input())
    if number < 0:
        print('Negative number!')