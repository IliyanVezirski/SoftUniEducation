days = int(input())
hours_per_day = int(input())
total = 0
total_for_all_days = 0
for day in range(1, days + 1):
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 == 1:
            price = 2.5
            total += 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            price = 1.25
            total += price
        else:
            price = 1
            total += price
    print(f'Day: {day} - {total:.2f} leva')
    total_for_all_days += total
    total = 0
print(f'Total: {total_for_all_days:.2f} leva')