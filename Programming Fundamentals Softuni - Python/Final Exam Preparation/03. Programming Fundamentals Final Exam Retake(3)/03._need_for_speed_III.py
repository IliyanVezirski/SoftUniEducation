def drive_car(current_garage: dict, car_to_drive: str, distance_to_drive: int, fuel_needed: int):
    if current_garage[car_to_drive]['fuel'] - fuel_needed < 0:
        print(f"Not enough fuel to make that ride")
    else:
        current_garage[car_to_drive]['fuel'] -= fuel_needed
        current_garage[car_to_drive]['mileage'] += distance_to_drive
        print(f'{car_to_drive} driven for {distance_to_drive} kilometers. {fuel_needed} liters of fuel consumed.')
        if current_garage[car_to_drive]['mileage'] >= 100000:
            print(f'Time to sell the {car_to_drive}!')
            del current_garage[car_to_drive]
    return current_garage


def refuel_car(current_garage: dict, car_refill: str, fuel_to_refill: int):
    if current_garage[car_refill]['fuel'] + fuel_to_refill > 75:
        fuel_to_refill = 75 - current_garage[car_refill]['fuel']
    current_garage[car_refill]['fuel'] += fuel_to_refill
    print(f'{car_refill} refueled with {fuel_to_refill} liters')
    return current_garage


def revert_car(current_garage: dict, car_to_decrease_km: str, km_to_decrese):
    if current_garage[car_to_decrease_km]['mileage'] - km_to_decrese < 10000:
        current_garage[car_to_decrease_km]['mileage'] = 10000
    else:
        current_garage[car_to_decrease_km]['mileage'] -= km_to_decrese
        print(f'{car_to_decrease_km} mileage decreased by {km_to_decrese} kilometers')
    return current_garage


garage = {}
number_of_cars = int(input())
for _ in range(number_of_cars):
    current_car, mileage, fuel = input().split("|")
    garage[current_car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()

while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        garage = drive_car(garage, command[1], int(command[2]), int(command[3]))
    elif command[0] == "Refuel":
        garage = refuel_car(garage, command[1], int(command[2]))
    elif command[0] == "Revert":
        garage = revert_car(garage, command[1], int(command[2]))
    command = input()

[print(f"{car} -> Mileage: {stats['mileage']} kms, Fuel in the tank: {stats['fuel']} lt.") for car, stats in
 garage.items()]
