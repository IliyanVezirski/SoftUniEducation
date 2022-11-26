def plunder(current_towns: dict, town: str, people: int, gold: int):
    current_towns[town]['population'] -= people
    current_towns[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if current_towns[town]['population'] == 0 or current_towns[town]['gold'] == 0:
        print(f"{town} has been wiped off the map!")
        del current_towns[town]
    return current_towns


def prosper(current_towns: dict, town: str, gold: int):
    if gold <= 0:
        print(f'Gold added cannot be a negative number!')
    else:
        current_towns[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {current_towns[town]['gold']} gold.")
    return current_towns


towns_info = {}

stats = input()
while stats != "Sail":
    city, population, gold = stats.split('||')
    if city not in towns_info:
        towns_info[city] = {"population": int(population), "gold": int(gold)}
    else:
        towns_info[city]['population'] += int(population)
        towns_info[city]['gold'] += int(gold)
    stats = input()

command = input()

while command != "End":
    command = command.split("=>")
    if command[0] == "Plunder":
        towns_info = plunder(towns_info, command[1], int(command[2]), int(command[3]))
    elif command[0] == "Prosper":
        towns_info = prosper(towns_info, command[1], int(command[2]))
    command = input()
if towns_info:
    print(f"Ahoy, Captain! There are {len(towns_info)} wealthy settlements to go to:")
    [print(f"{town} -> Population: {stats['population']} citizens, Gold: {stats['gold']} kg") for town, stats in
     towns_info.items()]
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
