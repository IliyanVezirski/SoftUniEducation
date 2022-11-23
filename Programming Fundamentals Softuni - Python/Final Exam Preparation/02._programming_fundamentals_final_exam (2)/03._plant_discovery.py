def rat(plants: dict, plant: str, rating: int):
    if plant in plants.keys():
        plants[plant]['rating'].append(rating)
    else:
        print(f"error")
    return plants


def update(plants: dict, plant: str, new_rarity: int):
    if plant in plants.keys():
        plants[plant]['rarity'] = new_rarity
    else:
        print(f"error")
    return plants


def reset(plants: dict, plant):
    if plant in plants.keys():
        plants[plant]['rating'] = []
    else:
        print(f"error")
    return plants


number_of_plants = int(input())
plants_information = {}

for _ in range(number_of_plants):
    data = input()
    data = data.split("<->")
    plants_information[data[0]] = {"rarity": int(data[1]), "rating": []}

command = input()

while command != "Exhibition":
    command = command.split(' - ')
    current_command = command[0].split(": ")
    plant = current_command[1]
    if current_command[0] == "Rate":
        rating = int(command[1])
        plants_information = rat(plants_information, plant, rating)
    elif current_command[0] == "Update":
        new_rarity = int(command[1])
        plants_information = update(plants_information, plant, new_rarity)
    elif current_command[0] == "Reset":
        plants_information = reset(plants_information, plant)
    command = input()
print("Plants for the exhibition:")

for plant, stats in plants_information.items():
    if stats['rating']:
        print(f"- {plant}; Rarity: {stats['rarity']}; Rating: {sum(stats['rating']) / len(stats['rating']):.2f}")
    else:
        print(f"- {plant}; Rarity: {stats['rarity']}; Rating: 0.00")
