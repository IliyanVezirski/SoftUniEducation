"""
You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the first line,
 you will receive a sequence of targets with their integer values,
 split by a single space. Then, you will start receiving commands for manipulating the targets until the "End" command.
  The commands are the following:
•	"Shoot {index} {power}"
o	Shoot the target at the index if it exists by reducing its value by the given power (integer value).
o	Remove the target if it is shot. A target is considered shot when its value reaches 0.
•	"Add {index} {value}"
o	Insert a target with the received value at the received index if it exists.
o	If not, print: "Invalid placement!"
•	"Strike {index} {radius}"
o	Remove the target at the given index and the ones before and after it depending on the radius.
o	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
 Example:  "Strike 2 2"
	{radius}	{radius}	{strikeIndex}	{radius}	{radius}

•	"End"
o	Print the sequence with targets in the following format and end the program:
"{target1}|{target2}…|{targetn}"
Input / Constraints
•	On the first line, you will receive the sequence of targets – integer values [1-10000].
•	On the following lines, until the "End" will be receiving the command described above – strings.
•	There will never be a case when the "Strike" command would empty the whole sequence.
Output
•	Print the appropriate message in case of any command if necessary.
•	In the end, print the sequence of targets in the format described above.
"""

targets = [int(i) for i in input().split()]


def shoot(numbers: list, index: int, damage: int):
    if 0 <= index < len(numbers):
        numbers[index] -= damage
        if numbers[index] <= 0:
            numbers.pop(index)
        return numbers
    else:
        return numbers



def add(numbers: list, index: int, value: int):
    if 0 <= index < len(numbers):
        numbers.insert(index,value)
        return numbers
    else:
        print("Invalid placement!")
        return numbers


def strike(numbers: list, index: int, index_radius: int):
    left_radius = index - index_radius
    right_radius = index + index_radius
    if 0 <= left_radius < len(numbers) and 0 <= right_radius < len(numbers):
        del numbers[left_radius:right_radius + 1]
        return numbers
    else:
        print(f'Strike missed!')
        return numbers


command = input()

while command != "End":
    command = command.split()
    if command[0] == "Shoot":
        index = int(command[1])
        damage = int(command[2])
        shoot(targets, index, damage)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        add(targets,index,value)
    elif command[0] =="Strike":
        index = int(command[1])
        radius = int(command[2])
        strike(targets, index, radius)

    command = input()
targets = [str(i) for i in targets]
print('|'.join(targets))