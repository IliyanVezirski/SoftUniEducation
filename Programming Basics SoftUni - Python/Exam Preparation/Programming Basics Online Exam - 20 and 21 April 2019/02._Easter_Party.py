guests_count = int(input())
price_per_menu = float(input())
budget = float(input())

if 10 <= guests_count <=15:
    price_per_menu *= 0.85
elif 15 < guests_count <= 20:
    price_per_menu *= 0.80
elif guests_count > 20:
    price_per_menu *= 0.75
cake_price = budget * 0.10
total = cake_price + (guests_count * price_per_menu)
diff = abs(total - budget)
if total <= budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {diff:.2f} leva needed.')