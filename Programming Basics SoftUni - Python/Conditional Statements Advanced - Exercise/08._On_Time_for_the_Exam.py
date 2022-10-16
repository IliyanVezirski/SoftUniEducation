hour_exam = int(input())
minutes_exam = int(input())
hour_come = int(input())
minutes_come = int(input())
total_minutes_exam = hour_exam * 60 + minutes_exam
total_minutes_come = hour_come * 60 + minutes_come
difference = abs(total_minutes_exam - total_minutes_come)
status = ''
if total_minutes_exam < total_minutes_come:
    status = 'Late'
    print("Late")
elif total_minutes_exam - 30 > total_minutes_come:
    status = 'Early'
    print("Early")
else:
    status = 'On time'
    print("On time")
difference_hour = difference // 60
difference_minute = difference % 60
if status == 'Late':
    if difference_hour != 0:
        print(f"{difference_hour}:{difference_minute:0>2d} hours after the start" )
    else:
        print(f'{difference_minute} minutes after the start')
elif status == 'Early':
    if difference_hour != 0:
        print(f"{difference_hour}:{difference_minute:0>2d} hours before the start" )
    else:
        print(f'{difference_minute} minutes before the start')
elif status == 'On time' and total_minutes_exam > total_minutes_come - 30:
    print(f'{difference_minute} minutes before the start')