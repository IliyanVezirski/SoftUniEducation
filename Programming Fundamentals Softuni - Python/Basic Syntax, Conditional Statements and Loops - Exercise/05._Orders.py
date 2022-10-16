orders = int(input())
total = 0
for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    price_for_order = price_per_capsule * capsules_needed_per_day * days
    total += price_per_capsule * capsules_needed_per_day * days
    price_for_order = price_per_capsule * capsules_needed_per_day * days
    print(f'The price for the coffee is: ${price_for_order:.2f}')

print(f'Total: ${total:.2f}')