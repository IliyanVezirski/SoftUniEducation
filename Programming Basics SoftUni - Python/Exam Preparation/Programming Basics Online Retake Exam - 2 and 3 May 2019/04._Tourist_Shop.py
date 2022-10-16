budget = float(input())
product_count = 0
total = 0
all_bought = True

while True:
    product = input()
    if product == 'Stop':
        break
    price_per_product = float(input())
    product_count += 1
    if product_count % 3 == 0:
        price_per_product *= 0.50
    total += price_per_product
    if total > budget:
        all_bought = False
        print(f"You don't have enough money!")
        break
diff = abs(total - budget)
if all_bought:
    print(f'You bought {product_count} products for {total:.2f} leva.')
else:
    print(f'You need {diff:.2f} leva!')