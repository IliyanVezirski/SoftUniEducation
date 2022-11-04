"""
You have just bought the latest and greatest computer game – Need for Seed III. Pick your favorite cars and drive them
all you want! We know that you can't wait to start playing.
On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain. On the
next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the following
format:
"{car}|{mileage}|{fuel}"
Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
•	"Drive : {car} : {distance} : {fuel}":
o	You need to drive the given distance, and you will need the given fuel to do that. If the car doesn't have enough fuel,
 print: "Not enough fuel to make that ride"
o	If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel
with the given fuel, and print:
"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
o	You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print:
"Time to sell the {car}!"
•	"Refuel : {car} : {fuel}":
o	Refill the tank of your car.
o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank,
take only what is required to fill it up.
o	Print a message in the following format: "{car} refueled with {fuel} liters"
•	"Revert : {car} : {kilometers}":
o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with
 in the following format:
"{car} mileage decreased by {amount reverted} kilometers"
o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
DO NOT print anything.
Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
Input/Constraints
•	The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
•	The fuel and distance amounts in the commands will never be negative.
•	The car names in the commands will always be valid cars in your possession.
Output
•	All the output messages with the appropriate formats are described in the problem description.

"""


def drive(garage: dict, car: str, distance: int, needed_fuel: int):
    garage[car][0] += distance
    if garage[car][1] < needed_fuel:
        garage[car][0] -= distance
        print(f"Not enough fuel to make that ride")
    else:
        garage[car][1] -= needed_fuel
        print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
    if garage[car][0] >= 100000:
        garage.pop(car)
        print(f"Time to sell the {car}!")
    return garage

def refuel(garage: dict, car: str, fuel):
    if garage[car][1] + fuel > 75:
        needed_fuel = 75 - garage[car][1]
        garage[car][1] = 75
        print(f"{car} refueled with {needed_fuel} liters")
        return garage
    else:
        garage[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
        return garage


def revert(garage: dict, car: str, kilometers: int):
    if garage[car][0] - kilometers < 10000:
        garage[car][0] = 10000
        return garage
    else:
        garage[car][0] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
        return garage


cars = {}
number_of_cars = int(input())
for i in range(number_of_cars):
    car = input().split('|')
    car_of_usage = car[0]
    fuel = int(car[2])
    mileage = int(car[1])
    cars[car_of_usage] = [mileage, fuel]

command = input()

while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        garage = drive(cars, command[1], int(command[2]), int(command[3]))
    elif command[0] == "Refuel":
        garage = refuel(cars, command[1], int(command[2]))
    elif command[0] == "Revert":
        garage = revert(cars, command[1], int(command[2]))
    command = input()
for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
