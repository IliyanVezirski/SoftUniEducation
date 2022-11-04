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

travel_route = input()


def add(travel: str, index: int, stop: str):
    if index in range(len(travel)):
        travel_list = []
        for el in travel:
            travel_list.append(el)
        travel_list.insert(index, stop)
        travel = ''.join(travel_list)
        print(travel)
    return travel


def remove(travel: str, start_index: int, end_index: int):

    if start_index in range(len(travel)) and end_index in range(len(travel)):
        deleted_item = travel[start_index:end_index+1]
        travel = travel.replace(deleted_item, "")
        print(travel)
    return travel


def switch(travel: str, old_destination: str, new_destination: str):
    if old_destination in travel:
        travel = travel.replace(old_destination, new_destination)
        print(travel)
    else:
        print(travel)
    return travel


command = input()

while command != "Travel":
    command = command.split(":")

    if command[0] == "Add Stop":
        travel_route = add(travel_route, int(command[1]), command[2])
    elif command[0] == "Remove Stop":
        travel_route = remove(travel_route, int(command[1]), int(command[2]))
    elif command[0] == "Switch":
        travel_route = switch(travel_route, command[1], command[2])
    command = input()

print(f"Ready for world tour! Planned stops: {travel_route}")
