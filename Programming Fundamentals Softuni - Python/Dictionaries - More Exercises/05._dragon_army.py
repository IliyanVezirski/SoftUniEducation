number_of_dragons = int(input())
dragons = {}
default_armor = 10
default_health = 250
default_damage = 45

for _ in range(number_of_dragons):
    dragon = input()
    type, name, damage, health, armor = dragon.split()
    if type not in dragons:
        dragons[type] = {name: [damage, health, armor]}
    else:
        dragons[type][name] = [damage, health, armor]

for type, dragon in dragons.items():
    for name, stats in dragon.items():
        if stats[0] == "null":
            dragons[type][name][0] = default_damage
        if stats[1] == "null":
            dragons[type][name][1] = default_health
        if stats[2] == "null":
            dragons[type][name][2] = default_armor
        dragons[type][name][0] = int(dragons[type][name][0])
        dragons[type][name][1] = int(dragons[type][name][1])
        dragons[type][name][2] = int(dragons[type][name][2])
for sort, dragon in dragons.items():
    dragons[sort] = dict(sorted(dragon.items(), key=lambda kvp: kvp[0]))

for type, dragon in dragons.items():
    average_damage = 0
    average_health = 0
    average_armor = 0
    for name, stats in dragon.items():
        average_damage += stats[0]
        average_health += stats[1]
        average_armor += stats[2]
    average_damage /= len(dragon)
    average_health /= len(dragon)
    average_armor /= len(dragon)
    print(f"{type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for name, stats in dragon.items():
        print(f"-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
