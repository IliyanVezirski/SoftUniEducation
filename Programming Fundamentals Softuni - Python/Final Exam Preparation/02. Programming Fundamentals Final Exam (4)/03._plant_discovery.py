def rate(current_plants: dict, plant: str, rating: int):
    if plant in current_plants:
        current_plants[plant]["rating"].append(rating)
    else:
        print(f"error")
    return current_plants


def update(current_plants: dict, plant: str, rarity: int):
    if plant in current_plants:
        current_plants[plant]["rarity"] = rarity
    else:
        print(f'error')
    return current_plants


def reset(current_plants: dict, plant: str):
    if plant in current_plants:
        current_plants[plant]['rating'] = []
    else:
        print('error')
    return current_plants


plants_info = {}
number_of_plants = int(input())

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    plants_info[plant] = {"rarity": int(rarity), "rating": []}

command = input()
while command != "Exhibition":
    rating = command.split(" - ")
    current_command, plant = rating[0].split(": ")
    if current_command == "Rate":
        plants_info = rate(plants_info, plant, int(rating[1]))
    elif current_command == "Update":
        plants_info = update(plants_info, plant, int(rating[1]))
    elif current_command == "Reset":
        plants_info = reset(plants_info, plant)
    command = input()
print(f"Plants for the exhibition:")
for plant, stats in plants_info.items():
    if stats['rating']:
        print(f"- {plant}; Rarity: {stats['rarity']}; Rating: {sum(stats['rating']) / len(stats['rating']):.2f}")
    else:
        print(f"- {plant}; Rarity: {stats['rarity']}; Rating: 0.00")
