def drive(garage: dict, car: str, distance: int, fuel: int):
    if garage[car]['fuel'] - fuel < 0:
        print(f"Not enough fuel to make that ride")
        return garage
    else:
        garage[car]['fuel'] -= fuel
        garage[car]['mileage'] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if garage[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del garage[car]
        return garage


def refuel(garage: dict, car: str, fuel):
    if garage[car]['fuel'] + fuel > 75:
        filled_fuel = 75 - garage[car]['fuel']
        garage[car]['fuel'] = 75
        print(f"{car} refueled with {filled_fuel} liters")
    else:
        garage[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")
    return garage


def revert(garage: dict, car: str, distance: int):
    if garage[car]['mileage'] - distance < 10000:
        garage[car]['mileage'] = 10000
    else:
        garage[car]['mileage'] -= distance
        print(f"{car} mileage decreased by {distance} kilometers")
    return garage


garage = {}

number_of_cars = int(input())

for _ in range(number_of_cars):
    car = input()
    car = car.split("|")

    garage[car[0]] = {'mileage': int(car[1]), 'fuel': int(car[2])}

command = input()

while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        garage = drive(garage, command[1], int(command[2]), int(command[3]))
    elif command[0] == "Refuel":
        garage = refuel(garage, command[1], int(command[2]))
    elif command[0] == "Revert":
        garage = revert(garage, command[1], int(command[2]))
    command = input()
for car, stats in garage.items():
    print(f"{car} -> Mileage: {stats['mileage']} kms, Fuel in the tank: {stats['fuel']} lt.")