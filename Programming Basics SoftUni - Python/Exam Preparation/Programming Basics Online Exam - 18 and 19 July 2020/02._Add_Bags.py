price_for_package_for_20kg = float(input())
package_kg = float(input())
days_from_trip = int(input())
number_package = int(input())
price = 0
if package_kg < 10:
    price = price_for_package_for_20kg * 0.20
elif 10 <= package_kg <= 20:
    price = price_for_package_for_20kg * 0.50
else:
    price = price_for_package_for_20kg
if days_from_trip > 30:
    price *= 1.10
elif 7 <= days_from_trip <= 30:
    price *= 1.15
elif days_from_trip < 7:
    price *= 1.40
total = price * number_package
print(f'The total price of bags is: {total:.2f} lv.')