budget = float(input())
nights = int(input())
price_per_night = float(input())
percentage_add_taxes = int(input())
if nights > 7:
    price_per_night *= 0.95
total = nights * price_per_night
total = total + (budget * (percentage_add_taxes / 100))
diff = abs(total - budget)
if total <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')