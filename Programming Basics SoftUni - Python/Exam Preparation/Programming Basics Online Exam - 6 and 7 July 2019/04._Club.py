income_wanted = float(input())
cocktail_name = ''
cocktail_number = 0
cocktail_price = 0
is_income_enough = True
diff = 0
total = 0
while True:
    cocktail_name = input()
    total_for_order = 0
    if cocktail_name == 'Party!':
        is_income_enough = False
        diff = abs(total - income_wanted)
        print(f'We need {diff:.2f} leva more.')
        break
    cocktail_number = int(input())
    cocktail_price = len(cocktail_name)
    total_for_order = cocktail_price * cocktail_number
    if total_for_order % 2 == 1:
        total_for_order *= 0.75
    total += total_for_order
    if total >= income_wanted:
        print(f'Target acquired.')
        break
print(f'Club income - {total:.2f} leva.')