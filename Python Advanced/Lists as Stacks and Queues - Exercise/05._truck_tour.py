from collections import deque

queue = deque()
number_of_gas_station = int(input())

for i in range(number_of_gas_station):
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])

for index_gas in range(len(queue)):
    fuel = 0
    current_pump_ok = True
    for gas_stats in queue:
        current_fuel, current_distance = gas_stats[0], gas_stats[1]
        fuel += current_fuel
        if fuel >= current_distance:
            fuel -= current_distance
        else:
            current_pump_ok = False
            break
    if current_pump_ok:
        print(index_gas)
        break
    queue.rotate(-1)
