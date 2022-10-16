days = int(input())
hours_for_day = int(input())
total = 0
for i in range(1, days + 1):
    price = 0
    day = i
    for n in range (1, hours_for_day + 1):
        if day % 2 == 0 and n % 2 == 1:
            price += 2.5
        elif day % 2 == 1 and n % 2 == 0:
            price += 1.25
        else:
            price += 1
    total += price
    print(f'Day: {day} - {price:.2f} leva')
print(f'Total: {total:.2f} leva')