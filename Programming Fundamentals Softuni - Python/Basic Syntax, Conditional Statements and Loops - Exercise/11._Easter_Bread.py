budget = float(input())
price_of_1_kg_flour = float(input())
price_of_1_pack_eggs = price_of_1_kg_flour * 0.75
price_of_1_liter_milk = price_of_1_kg_flour * 1.25
loaf_needed_budget = price_of_1_liter_milk / 4 + price_of_1_kg_flour + price_of_1_pack_eggs
colored_eggs = 0
loaf = 0
total = budget
spent_money = 0
money_left = 0
money_cost = 0
while True:
    spent_money += loaf_needed_budget
    if spent_money > budget:
        break
    money_cost += loaf_needed_budget
    colored_eggs += 3
    loaf += 1
    if loaf % 3 == 0:
        colored_eggs -= loaf - 2
money_left = budget - spent_money
print(f'You made {loaf} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget - money_cost:.2f}BGN left.')

