from collections import deque

litres = int(input())
queue = deque()
name = input()

while name != "Start":
    queue.append(name)
    name = input()
command = input()

while command != "End":
    if "refill" in command:
        command = command.split()
        litres += int(command[-1])
    else:
        if litres >= int(command):
            print(f"{queue.popleft()} got water")
            litres -= int(command)
        else:
            print(f"{queue.popleft()} must wait")
    command = input()
print(f"{litres} liters left")