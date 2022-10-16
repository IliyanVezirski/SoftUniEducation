eggs_availability = int(input())
command = ''
eggs = 0
enough_eggs = True
buyed_eggs = 0
while True:
    command = input()
    if command == 'Close':
        break
    eggs = int(input())
    if command == 'Buy':
        if eggs_availability < eggs:
            enough_eggs = False
            break
        buyed_eggs += eggs
        eggs_availability -= eggs
    elif command == 'Fill':
        eggs_availability += eggs
if enough_eggs:
    print(f'Store is closed!')
    print(f'{buyed_eggs} eggs sold.')
else:
    print(f'Not enough eggs in store!')
    print(f'You can buy only {eggs_availability}.')