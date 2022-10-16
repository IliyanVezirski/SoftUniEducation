numbers = int(input())
n = numbers * 2
sum_left = 0
sum_right = 0
for i in range(1, n + 1):
    number = int(input())
    if i <= numbers:
        sum_left = sum_left + number
    else:
        sum_right = sum_right + number
diff = abs(sum_left - sum_right)
if sum_left == sum_right:
    print(f'Yes, sum = {sum_left}')
else:
    print(f'No, diff = {diff}')