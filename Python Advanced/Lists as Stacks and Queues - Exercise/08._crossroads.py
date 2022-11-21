from collections import deque

duration_of_green_line = int(input())
free_window = int(input())
queue = deque()
lights = deque()
passed_cars = 0
command = input()
crash = False
while command != "END":
    if command == "green":
        current_green = duration_of_green_line
        current_free_window = free_window
        while current_green > 0:
            if not queue:
                break
            current_car = queue.popleft()
            len_of_current_car = len(current_car)

            current_green -= len_of_current_car
            if current_green < 0:
                left_parts = current_green * -1
                if left_parts > current_free_window:
                    print(f"A crash happened!")
                    print(f"{current_car} was hit at {current_car[(current_green * -1)-1]}.")
                    crash = True
                    break
                else:
                    passed_cars += 1

        if crash:
            break

        passed_cars += 1
    else:
        queue.append(command)
    command = input()
if not crash:
    print(f"Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
