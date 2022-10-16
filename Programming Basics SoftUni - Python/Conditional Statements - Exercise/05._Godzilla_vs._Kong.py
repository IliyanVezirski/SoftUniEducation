budget = float(input())
statist_number = int(input())
price_for_statist = float(input())
decor_price = budget * 0.10
total_price_for_statis = statist_number * price_for_statist
if statist_number > 150:
    total_price_for_statis = total_price_for_statis * 0.90
total = total_price_for_statis + decor_price
if budget < total:
    budget = abs(budget - total)
    print('Not enough money!')
    print(f"Wingard needs{budget: .2f} leva more.")
else:
    budget = abs(budget - total)
    print("Action!")
    print(f"Wingard starts filming with{budget: .2f} leva left.")
