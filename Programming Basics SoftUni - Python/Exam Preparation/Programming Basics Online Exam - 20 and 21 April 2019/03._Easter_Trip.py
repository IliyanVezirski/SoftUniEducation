destination = input()
reservation_day = input()
nights = int(input())
price = 0
if destination == 'France':
    if reservation_day == '21-23':
        price = 30
    elif reservation_day == '24-27':
        price = 35
    elif reservation_day == '28-31':
        price = 40
elif destination == 'Italy':
    if reservation_day == '21-23':
        price = 28
    elif reservation_day == '24-27':
        price = 32
    elif reservation_day == '28-31':
        price = 39
elif destination == 'Germany':
    if reservation_day == '21-23':
        price = 32
    elif reservation_day == '24-27':
        price = 37
    elif reservation_day == '28-31':
        price = 43
total = price * nights
print(f'Easter trip to {destination} : {total:.2f} leva.')