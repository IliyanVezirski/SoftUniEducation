number_of_cars = int(input())
parking_lot = set()

for _ in range(number_of_cars):
    current_car = tuple(input().split(', '))
    if current_car[0] == "IN":
        parking_lot.add(current_car[1])
    elif current_car[0] == "OUT":
        parking_lot.remove(current_car[1])

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print("Parking Lot is Empty")