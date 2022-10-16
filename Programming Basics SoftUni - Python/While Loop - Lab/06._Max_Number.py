import sys
n = input()
number = int(n)
max_number = -sys.maxsize
while n != 'Stop':
    number = int(n)
    if number > max_number:
        max_number = number
    n = input()
print(f'{max_number}')