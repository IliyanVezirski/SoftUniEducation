games = int(input())
points_from_0_9 = 0
points_from_9_19 = 0
points_from_19_29 = 0
points_from_29_39 = 0
points_from_39_49 = 0
sum_points = 0
other_points = 0
count_0_9 = 0
count_9_19 = 0
count_19_29 = 0
count_29_39 = 0
count_39_49 = 0
count_other = 0
for i in range(1, games+1):
    number = int(input())
    if 0 <= number <=9:
        count_0_9 += 1
        points_from_0_9 = number * 0.20
        sum_points += points_from_0_9
    elif 9 < number <=19:
        count_9_19 += 1
        points_from_9_19 = number * 0.30
        sum_points += points_from_9_19
    elif 19 < number <= 29:
        count_19_29 += 1
        points_from_19_29 = number * 0.40
        sum_points += points_from_19_29
    elif 29 < number <= 39:
        points_from_29_39 = 50
        count_29_39 += 1
        sum_points += points_from_29_39
    elif 39 < number <= 50:
        count_39_49 += 1
        points_from_39_49 = 100
        sum_points += points_from_39_49
    else:
        count_other += 1
        other_points += other_points
        sum_points = sum_points / 2
total_points = sum_points
from_0_9_percentage =('%.2f' % (count_0_9 / games * 100))
from_9_19_percentage = ('%.2f' % (count_9_19 / games * 100))
from_19_29_percentage = ('%.2f' % (count_19_29 / games * 100))
from_29_39_percentage = ('%.2f'% (count_29_39 / games * 100))
from_39_49_percentage = ('%.2f' % (count_39_49 / games * 100))
from_other_percentage = ('%.2f' % (count_other / games * 100))
print('% .2f' % total_points)
print(f'From 0 to 9: {from_0_9_percentage}%')
print(f'From 10 to 19: {from_9_19_percentage}%')
print(f'From 20 to 29: {from_19_29_percentage}%')
print(f'From 30 to 39: {from_29_39_percentage}%')
print(f'From 40 to 50: {from_39_49_percentage}%')
print(f'Invalid numbers: {from_other_percentage}%')