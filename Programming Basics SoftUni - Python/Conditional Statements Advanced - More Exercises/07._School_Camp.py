season = input()
group = input()
student_num = int(input())
nights = int(input())
price = 0
vacation = ''
if group == 'boys':
    if season == 'Winter':
        price = student_num * 9.60 * nights
        vacation = 'Judo'
    elif season == 'Spring':
        price = student_num * 7.20 * nights
        vacation = 'Tennis'
    elif season == 'Summer':
        price = student_num * 15 * nights
        vacation = 'Football'
elif group == 'girls':
    if season == 'Winter':
        price = student_num * 9.60 * nights
        vacation = 'Gymnastics'
    elif season == 'Spring':
        price = student_num * 7.20 * nights
        vacation = 'Athletics'
    elif season == 'Summer':
        price = student_num * 15 * nights
        vacation = 'Volleyball'
else:
    if season == 'Winter':
        price = student_num * 10 * nights
        vacation = 'Ski'
    elif season == 'Spring':
        price = student_num * 9.50 * nights
        vacation = 'Cycling'
    elif season == 'Summer':
        price = student_num * 20 * nights
        vacation = 'Swimming'
if 10 <= student_num < 20:
    price *= 0.95
elif 20 <= student_num < 50:
    price *= 0.85
elif student_num >= 50:
    price *= 0.50
print(f'{vacation} {price:.2f} lv.')