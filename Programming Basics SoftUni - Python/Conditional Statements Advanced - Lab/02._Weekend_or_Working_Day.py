day = input()
day_is = ''
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    day_is = 'Working day'
elif day == 'Saturday' or day == 'Sunday':
    day_is = 'Weekend'
else:
    day_is = 'Error'
print(day_is)