destination = input()
while destination != 'End':
    budget = float(input())
    current_income = 0
    while current_income < budget:
        income = float(input())
        current_income += income
    print(f'Going to {destination}!')
    destination = input()