health = 100
coins = 0
dungeon_rooms = input().split("|")
won = True
best_room = 0


def potion(health: int, value: int):
    current_health = 100 - health
    health += value
    if health > 100:
        health = 100
        print(f"You healed for {current_health} hp.")
    else:
        print(f"You healed for {value} hp.")
    print(f"Current health: {health} hp.")
    return health


def chest(coin: int, founded_coins: int):
    print(f"You found {founded_coins} bitcoins.")
    coin += founded_coins
    return coin


for room in dungeon_rooms:
    current_room = room.split()
    value = int(current_room[1])
    current_room = current_room[0]
    best_room += 1
    if current_room == "potion":
        potion = potion(health, value)
    elif current_room == "chest":
        coins = chest(coins, value)
    else:
        health -= value
        if health <= 0:
            won = False
            print(f"You died! Killed by {current_room}.")
            print(f"Best room: {best_room}")
            break

        else:
            print(f"You slayed {current_room}.")

if won:
    print(f"You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")
