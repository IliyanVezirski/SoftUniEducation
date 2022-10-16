n = int(input())
number_under_200 = 0
number_200_399 = 0
number_400_599 = 0
number_600_799 = 0
number_800 = 0
for i in range(1, n+ 1):
    number = int(input())
    if number < 200:
        number_under_200 += 1
    elif 200 <= number <= 399:
        number_200_399 += 1
    elif 400 <= number <= 599:
        number_400_599 += 1
    elif 600 <= number <= 799:
        number_600_799 += 1
    elif number >= 800:
        number_800 += 1
n1_percentage = ('%.2f' % ((number_under_200 / n) * 100))
n2_percentage = ('%.2f' % ((number_200_399 / n) * 100))
n3_percentage = ('%.2f' % ((number_400_599 / n) * 100))
n4_percentage = ('%.2f' % ((number_600_799 / n) * 100))
n5_percentage = ('%.2f' % ((number_800 / n) * 100))
print(f'{n1_percentage}%')
print(f'{n2_percentage}%')
print(f'{n3_percentage}%')
print(f'{n4_percentage}%')
print(f'{n5_percentage}%')
