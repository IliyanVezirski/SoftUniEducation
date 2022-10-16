day = int(input())
day_name = ''
if day == 1:
    day_name = 'Monday'
elif day == 2:
    day_name = 'Tuesday'
elif day == 3:
    day_name = 'Wednesday'
elif day == 4:
    day_name = 'Thursday'
elif day == 5:
    day_name = 'Friday'
elif day == 6:
    day_name = 'Saturday'
elif day == 7:
    day_name = 'Sunday'
else:
    day_name = 'Error'
print(day_name)