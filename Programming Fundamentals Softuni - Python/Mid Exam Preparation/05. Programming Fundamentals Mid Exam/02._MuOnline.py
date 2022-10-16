""""You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms.
 Each room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space. The command can be:
•	"potion"
o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
o	First print: "You healed for {amount} hp."
o	After that, print your current health: "Current health: {health} hp."
•	"chest"
o	You've found some bitcoins, the number in the second part.
o	Print: "You found {amount} bitcoins."
•	In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of the monster.
 You should remove the monster's attack from your health.
o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
o	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage to reach:
"Best room: {room}"
If you managed to go through all the rooms in the dungeon, print on the following three lines:
"You've made it!"
"Bitcoins: {bitcoins}"
"Health: {health}"
Input / Constraints
You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
Output
Print the corresponding messages described above.
"""
health = 100
coins = 0

dungeon_rooms = input().split("|")


def potion(health: int, healing: int):
    health += healing
    if health > 100:
        print(f"You healed for {abs(health-100 - healing)} hp.")
        health = 100
        print(f"Current health: {health} hp.")
        return health
    else:
        print(f"You healed for {healing} hp.")
        print(f"Current health: {health} hp.")
        return health

def chest(coins: int, founded_coins: int):
    coins += founded_coins
    print(f"You found {founded_coins} bitcoins.")
    return coins

won_game = True
rooms_counter = 0
for i in range(0, len(dungeon_rooms)):

    rooms = dungeon_rooms[i].split()
    room = rooms[0]
    points = rooms[1]
    rooms_counter += 1
    if room == "potion":
        health = potion(health, int(points))
    elif room == "chest":
        coins = chest(coins, int(points))
    else:
        health -= int(points)
        if health <= 0:
            print(f"You died! Killed by {room}.")
            print(f"Best room: {rooms_counter}")
            won_game = False
            break
        else:
            print(f"You slayed {room}.")
if won_game:
    print(f"You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")