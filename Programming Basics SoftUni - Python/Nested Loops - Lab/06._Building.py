floors = int(input())
number_apartments_or_offices = int(input())
number = 0
for last_floor in range(0, number_apartments_or_offices):
    if last_floor == number_apartments_or_offices - 1:
        print(f'L{floors}{last_floor}', end="\n")
    else:
        print(f'L{floors}{last_floor}', end=" ")
for floor_number in range(floors - 1, 0, -1):
    if floor_number % 2 != 0:
        for apartments in range(0, number_apartments_or_offices):
            if apartments == number_apartments_or_offices - 1:
                print(f'A{floor_number}{apartments}', end="\n")
            else:
                print(f'A{floor_number}{apartments}', end=" ")
    else:
        for offices in range(0,number_apartments_or_offices):
            if offices == number_apartments_or_offices - 1:
                print(f'O{floor_number}{offices}', end="\n")
            else:
                print(f'O{floor_number}{offices}', end=" ")