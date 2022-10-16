n = int(input())
sum_number = 0
for i in range(1, n + 1):
    number = int(input())
    sum_number += number
average_number = (sum_number / n)
print(f'{average_number:.2f}')