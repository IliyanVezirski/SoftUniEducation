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


def update(plants_rarity: dict, plant: str, new_rarity: str):
    if plant not in plants_rarity.keys():
        print("error")
        return plants_rating
    plants_rarity[plant] = new_rarity
    return plants_rarity


def rate(plants_rating: dict, plant: str, rating: int, plants: dict):
    if plant not in plants.keys():
        print("error")
        return plants_rating
    if plant in plants_rating:
        plants_rating[plant].append(rating)
    else:
        plants_rating[plant] = [rating]
    return plants_rating


def reset(plants_rating: dict, plant: str, plants: dict):
    if plant not in plants.keys():
        print("error")
        return plants_rating
    plants_rating[plant] = [0]
    return plants_rating


plants = {}
plants_rating = {}
plants_number = int(input())

for i in range(plants_number):
    plants_input = input().split("<->")
    plants[plants_input[0]] = plants_input[1]

plant_rating = input()

while plant_rating != "Exhibition":
    plant_rating = plant_rating.split(' - ')
    plant = plant_rating[0].split(": ")
    command = plant[0]
    plant = plant[1]
    if command == "Rate":
        points = plant_rating[1]
        plant_rating = rate(plants_rating, plant, int(points), plants)
    elif command == "Update":
        points = plant_rating[1]
        plants = update(plants, plant, points)
    elif command == "Reset":
        plants_rating = reset(plants_rating, plant, plants)

    plant_rating = input()
for key, value in plants_rating.items():
    if value == [0]:
        average_value = 0
    else:
        average_value = sum(value) / len(value)
    plants_rating[key] = average_value
print(f"Plants for the exhibition:")
for key, value in plants.items():
    print(f"- {key}; Rarity: {value}; Rating: {plants_rating[key]:.2f}")
