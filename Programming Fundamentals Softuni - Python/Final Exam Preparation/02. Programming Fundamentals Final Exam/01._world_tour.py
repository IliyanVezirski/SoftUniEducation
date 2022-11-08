"""
You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything first.
To start with, you would like to plan out all of your stops where you will have a break.
On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel",
you will be given some commands to manipulate that initial string. The commands can be:
•	"Add Stop:{index}:{string}":
o	Insert the given string at that index only if the index is validx
•	"Remove Stop:{start_index}:{end_index}":
o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
•	"Switch:{old_string}:{new_string}":
o	If the old string is in the initial string, replace it with the new one (all occurrences)
Note: After each command, print the current state of the string if it is valid!
After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
Input / Constraints
•	JavaScript: you will receive a list of strings
•	An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
Output
•	Print the proper output messages in the proper cases as described in the problem description

"""


def add(current_stops: str, index_to_add: int, string_to_add: str):
    if index_to_add in range(len(current_stops)):
        first_part = current_stops[:index_to_add]
        second_part = current_stops[index_to_add:]
        current_stops = first_part + string_to_add + second_part
    print(current_stops)
    return current_stops


def remove(current_stops: str, start_index: int, end_index: int):
    if start_index in range(len(current_stops)) and end_index in range(len(current_stops)):
        first_part = current_stops[:start_index]
        second_part = current_stops[end_index+1:]
        current_stops = first_part + second_part
    print(current_stops)
    return current_stops


def switch(current_stops: str, old_string: str, new_string: str):
    if old_string in current_stops:
        current_stops = current_stops.replace(old_string, new_string)
    print(current_stops)
    return current_stops


stops = input()

command = input()

while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        stops = add(stops, int(command[1]), command[2])
    elif command[0] == "Remove Stop":
        stops = remove(stops,int(command[1]), int(command[2]))
    elif command[0] == "Switch":
        stops = switch(stops, command[1], command[2])
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")