"""
You have now returned from your world tour. On your way, you have discovered some new plants, and you want
 to gather some information about them and create an exhibition to see which plant is highest rated.
On the first line, you will receive a number n. On the next n lines, you will be given some information about
 the plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will
  need it later. If you receive a plant more than once, update its rarity.
After that, until you receive the command "Exhibition", you will be given some of these commands:
•	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
•	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
•	"Reset: {plant}" – remove all the ratings of the given plant
Note: If any given plant name is invalid, print "error"
After the command "Exhibition", print the information that you have about the plants in the following format:
"Plants for the exhibition:
- {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
- {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
…
- {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
The average rating should be formatted to the second decimal place.
Input / Constraints
•	You will receive the input as described above
•	JavaScript: you will receive a list of strings
Output
•	Print the information about all plants as described above

"""

number_of_plants = int(input())
plants = {}

for plant in range(number_of_plants):
    data = input()
    data = data.split("<->")
    plants[data[0]] = {'rarity': int(data[1]), 'rating': []}


def rate(current_plants: dict, current_plant: str, new_rating: int):
    if current_plant not in current_plants:
        print(f"error")
        return current_plants
    current_plants[current_plant]['rating'].append(new_rating)
    return current_plants


def update(current_plants: dict, current_plant: str, rarity: int):
    if current_plant not in current_plants:
        print(f"error")
        return current_plants
    current_plants[current_plant]['rarity'] = rarity
    return current_plants


def reset(current_plants: dict, current_plant: str):
    if current_plant not in current_plants:
        print(f"error")
        return current_plants
    current_plants[current_plant]['rating'] = []
    return current_plants


data = input()

while data != "Exhibition":
    command = data.split(' - ')
    current_command = command[0].split(": ")
    plant = current_command[1]
    if current_command[0] == "Rate":
        plant = current_command[1]
        rating = int(command[1])
        plants = rate(plants, plant, rating)
    elif current_command[0] == "Update":
        plant = current_command[1]
        new_rarity = int(command[1])
        plants = update(plants, plant, new_rarity)
    elif current_command[0] == "Reset":
        plant = current_command[1]
        plants = reset(plants, plant)
    data = input()

print(f"Plants for the exhibition:")
for plant, stats in plants.items():
    if stats['rating']:
        print(f"- {plant}; Rarity: {stats['rarity']}; Rating: {sum(stats['rating']) / len(stats['rating']):.2f}")
    else:
        print(f"- {plant}; Rarity: {stats['rarity']}; Rating: 0.00")
