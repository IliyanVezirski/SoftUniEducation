import sys
number = int(input())
max_number = -sys.maxsize
sum_number = 0
for i in range(1, number+1):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_number += num
if max_number == sum_number - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    sum_other = sum_number - max_number
    print(f'Diff = {abs(max_number - sum_other)}')