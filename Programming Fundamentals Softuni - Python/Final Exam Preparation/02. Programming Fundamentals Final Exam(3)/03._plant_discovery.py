def rate_plant(current_plants: dict, plant: str, rating: int):
    if plant not in current_plants:
        print(f"error")
    else:
        current_plants[plant]['rating'].append(rating)
    return current_plants


def update_plant(current_plants: dict, plant: str, rarity: str):
    if plant not in current_plants:
        print(f"error")
    else:
        current_plants[plant]['rarity'] = rarity
    return current_plants


def reset_plant(current_plants: dict, plant: str):
    if plant not in current_plants:
        print(f"error")
    else:
        current_plants[plant]["rating"] = []
    return current_plants


plant_info = {}

number_of_plants = int(input())

for _ in range(number_of_plants):
    plant, rarity = input().split('<->')
    plant_info[plant] = {'rarity': int(rarity), 'rating': []}

command = input()

while command != "Exhibition":
    command = command.split(" - ")
    current_command = command[0].split(": ")
    if current_command[0] == "Rate":
        plant_info = rate_plant(plant_info, current_command[1], int(command[1]))
    elif current_command[0] == "Update":
        plant_info = update_plant(plant_info, current_command[1], command[1])
    elif current_command[0] == "Reset":
        plant_info = reset_plant(plant_info, current_command[1])
    command = input()
print(f"Plants for the exhibition:")
for plant, stats in plant_info.items():
    if stats['rating']:
        print(f"- {plant}; Rarity: {stats['rarity']}; Rating: {sum(stats['rating']) / len(stats['rating']):.2f}")
    else:
        print(f"- {plant}; Rarity: {stats['rarity']}; Rating: 0.00")
