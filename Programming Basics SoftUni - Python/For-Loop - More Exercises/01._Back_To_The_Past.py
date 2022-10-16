inherited_money = float(input())
age_to_live = int(input())
spended_money_for_even = 0
spended_money_for_odd = 0
age = 17
for i in range(1800, age_to_live + 1):
    age += + 1
    if i % 2 == 0:
        spended_money_for_even += 12000
    else:
        spended_money_for_odd += 12000 + (age* 50)

diff = abs(spended_money_for_even + spended_money_for_odd - inherited_money)
if inherited_money < spended_money_for_odd + spended_money_for_even:
    print(f'He will need {diff:.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')