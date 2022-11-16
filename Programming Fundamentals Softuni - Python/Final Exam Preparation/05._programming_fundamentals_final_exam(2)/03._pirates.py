def plunder(towns: dict, town_name: str, people: int, gold: int):
    if towns[town_name][0] - people <= 0 or towns[town_name][1] - gold <= 0:
        del towns[town_name]
        print(f"{town_name} plundered! {gold} gold stolen, {people} citizens killed.")
        print(f"{town_name} has been wiped off the map!")
    else:
        towns[town_name][0] -= people
        towns[town_name][1] -= gold
        print(f"{town_name} plundered! {gold} gold stolen, {people} citizens killed.")
    return towns


def prosper(towns: dict, town_name: str, gold: int):
    if gold <= 0:
        print(f"Gold added cannot be a negative number!")
    else:
        towns[town_name][1] += gold
        print(f"{gold} gold added to the city treasury. {town_name} now has {towns[town_name][1]} gold.")
    return towns


city = input()
towns = {}
while city != "Sail":
    city = city.split("||")
    if city[0] not in towns:
        towns[city[0]] = [0, 0]
    towns[city[0]][0] += int(city[1])
    towns[city[0]][1] += int(city[2])
    city = input()
command = input()

while command != "End":
    command = command.split('=>')
    if command[0] == "Plunder":
        towns = plunder(towns, command[1], int(command[2]), int(command[3]))
    elif command[0] == "Prosper":
        towns = prosper(towns, command[1], int(command[2]))
    command = input()
if towns:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    [print(f"{town} -> Population: {towns[town][0]} citizens, Gold: {towns[town][1]} kg") for town in towns]
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
