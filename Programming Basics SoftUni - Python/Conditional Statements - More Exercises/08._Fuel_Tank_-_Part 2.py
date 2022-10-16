fuel_type = input()
fuel = float(input())
club_cart = input()
club_cart = str.lower(club_cart)
fuel_type = str.lower(fuel_type)
gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
if club_cart == 'yes' and fuel_type == 'diesel':
    diesel_price = 2.33 - 0.12
elif club_cart == 'yes' and fuel_type == 'gasoline':
    gasoline_price = 2.22 - 0.18
elif club_cart == 'yes' and fuel_type == 'gas':
    gas_price = 0.93 - 0.08
if fuel_type == 'diesel':
    price = diesel_price * fuel
elif fuel_type == 'gasoline':
    price = gasoline_price * fuel
elif fuel_type == 'gas':
    price = gas_price * fuel
if 20 <= fuel <= 25:
    price = price * 0.92
elif fuel > 25:
    price = price * 0.90
else:
    price = price
print(f'{price: .2f} lv.')