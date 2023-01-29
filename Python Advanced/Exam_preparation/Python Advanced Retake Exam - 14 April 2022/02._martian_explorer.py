"""
Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:
•	One rover - marked with the letter "E"
•	Water deposit (one or many) - marked with the letter "W"
•	Metal deposit (one or many) - marked with the letter "M"
•	Concrete deposit (one or many) - marked with the letter "C"
•	Rock (one or many) - marked with the letter "R"
•	Empty positions will be marked with "-"
After that, you will be given the commands for the rover's movement on one line separated by a comma and a space
(", "). Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of the given types
of deposit or a rock:
•	When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and
increase its value by 1.
•	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown
 below, and the program ends.
•	If the rover goes out of the field, it should continue from the opposite side in the same direction.
 Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be
 placed at position (3, 5).
The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
Stop the program if you run out of commands or the rover gets broken.
Input
•	On the first 6 lines, you will receive the matrix.
•	On the following line, you will receive the commands for the rover separated by a comma and a space.
Output
•	For each deposit found while you go through the commands, print out on the console: "{Water, Metal or
Concrete} deposit found at ({row}, {col})"
•	If the rover hits a rock, print the coordinates where it got broken in the format: "Rover got broken
at ({row}, {col})"
After you go through all the commands or the rover gets broken, print out on the console:
•	If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
•	Otherwise, print on the console: "Area not suitable to start the colony."
See examples for more clarification.

"""


def in_range_of_field(size: int, current_position: list, direction: str):
    directions = {
        'right': (0, +1),
        'left': (0, -1),
        'down': (+1, 0),
        'up': (-1, 0)
    }
    current_position = [directions[direction][0] + current_position[0], directions[direction][1] + current_position[1]]
    if current_position[0] < 0:
        current_position[0] = size + current_position[0]
    if current_position[1] < 0:
        current_position[1] = size + current_position[1]
    if current_position[0] >= size:
        current_position[0] = size - current_position[0]
    if current_position[1] >= size:
        current_position[1] = size - current_position[1]
    return tuple(current_position)


field_size = 6
resources = {
    "Water": 0,
    "Metal": 0,
    "Concrete": 0,
}
water_deposit = []
metal_deposit = []
concrete_deposit = []
field = []
rover_position = tuple()
for r in range(field_size):
    field.append(input().split())
    for c in range(field_size):
        if field[r][c] == "E":
            rover_position = (r, c)
            break
current_direction = input().split(', ')
for direction in current_direction:
    new_position = in_range_of_field(field_size, list(rover_position), direction)
    if field[new_position[0]][new_position[1]] == 'W':
        print(f"Water deposit found at ({', '.join(list(map(str, new_position)))})")
        resources["Water"] += 1
    elif field[new_position[0]][new_position[1]] == "M":
        print(f"Metal deposit found at ({', '.join(list(map(str, new_position)))})")
        resources["Metal"] += 1
    elif field[new_position[0]][new_position[1]] == "C":
        print(f"Concrete deposit found at ({', '.join(list(map(str, new_position)))})")
        resources["Concrete"] += 1
    rover_position = new_position
    if field[rover_position[0]][rover_position[1]] == 'R':
        print(f"Rover got broken at ({', '.join(list(map(str, new_position)))})")
        break
won = True
for component in resources:
    if resources[component] == 0:
        won = False
        break
if won:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
