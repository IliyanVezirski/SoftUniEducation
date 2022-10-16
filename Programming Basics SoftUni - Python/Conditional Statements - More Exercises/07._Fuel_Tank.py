fuel_type = input()
fuel = int(input())
fuel_type = str.lower(fuel_type)
if fuel < 25 and fuel_type == 'diesel':
    print(f'Fill your tank with {fuel_type}!')
elif fuel < 25 and fuel_type == 'gasoline':
    print(f'Fill your tank with {fuel_type}!')
elif fuel < 25 and fuel_type == 'gas':
    print(f'Fill your tank with {fuel_type}!')
elif fuel >= 25 and fuel_type == 'diesel':
    print(f'You have enough {fuel_type}.')
elif fuel >= 25 and fuel_type == 'gasoline':
    print(f'You have enough {fuel_type}.')
elif fuel >= 25 and fuel_type == 'gas':
    print(f'You have enough {fuel_type}.')
else:
    print('Invalid fuel!')