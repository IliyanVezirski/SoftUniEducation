from collections import deque

petrol_pumps = int(input())
distance = deque()
petrol_filled = deque()

for i in range(petrol_pumps):
    pump = input()
    pump = [int(i) for i in pump.split()]
    petrol_filled.append(pump[0])
    distance.append(pump[1])
index = 0
while True:
    current_petrol = petrol_filled.popleft()
    current_distance = distance.popleft()
    if current_petrol > current_distance:
        break
    index += 1
print(index)
