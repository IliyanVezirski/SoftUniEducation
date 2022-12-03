def driving_car(current_garage: dict, current_car: str, distance_to_drive: int, fuel_needed: int):
    if current_garage[current_car]['fuel'] - fuel_needed < 0:
        print(f'Not enough fuel to make that ride')
    else:
        current_garage[current_car]['fuel'] -= fuel_needed
        current_garage[current_car]['mileage'] += distance_to_drive
        print(f"{current_car} driven for {distance_to_drive} kilometers. {fuel_needed} liters of fuel consumed.")
        if current_garage[current_car]['mileage'] >= 100000:
            print(f"Time to sell the {current_car}!")
            del current_garage[current_car]
    return current_garage


def refuel_car(current_garage: dict, current_car: str, fuel: int):
    if current_garage[current_car]['fuel'] + fuel > 75:
        fuel = 75 - current_garage[current_car]['fuel']
        current_garage[current_car]['fuel'] = 75
        print(f"{current_car} refueled with {fuel} liters")
    else:
        current_garage[current_car]['fuel'] += fuel
        print(f"{current_car} refueled with {fuel} liters")
    return current_garage


def revert_cat(current_garage: dict, current_car: str, distance: int):
    if current_garage[current_car]['mileage'] - distance < 10000:
        current_garage[current_car]['mileage'] = 10000
    else:
        print(f'{current_car} mileage decreased by {distance} kilometers')
        current_garage[current_car]['mileage'] -= distance
    return current_garage


number_of_cars = int(input())
garage = {}
for _ in range(number_of_cars):
    car, distance, fuel = input().split('|')
    garage[car] = {'mileage': int(distance), 'fuel': int(fuel)}

command = input()

while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        garage = driving_car(garage, command[1], int(command[2]), int(command[3]))
    elif command[0] == "Refuel":
        garage = refuel_car(garage, command[1], int(command[2]))
    elif command[0] == "Revert":
        garage = revert_cat(garage, command[1], int(command[2]))
    command = input()
[print(f"{car} -> Mileage: {stats['mileage']} kms, Fuel in the tank: {stats['fuel']} lt.") for car, stats in
 garage.items()]
