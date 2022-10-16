kilometer = int(input())
day_or_night = input()
taxi_day = 0.70 + (kilometer * 0.79)
taxi_night = 0.70 + (kilometer * 0.90)
bus = kilometer * 0.09 #минимум 20 км
train = kilometer * 0.06 #минимум 100 км
if kilometer < 20 and day_or_night == 'day':
    print('%.2f' % taxi_day)
elif kilometer < 20 and day_or_night == 'night':
    print('%.2f' % taxi_night)
if 20 <= kilometer < 100:
    print('%.2f' % bus)
elif kilometer >= 100:
    print('%.2f' % train)