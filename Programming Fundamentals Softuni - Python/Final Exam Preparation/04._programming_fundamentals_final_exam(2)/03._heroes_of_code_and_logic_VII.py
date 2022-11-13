heroes = {}


def cast_spell(current_heroes: dict, name: str, mana_needed: int, spell: str):
    if mana_needed > current_heroes[name][1]:
        print(f"{name} does not have enough MP to cast {spell}!")
    else:
        current_heroes[name][1] -= mana_needed
        print(f"{name} has successfully cast {spell} and now has {current_heroes[name][1]} MP!")
    return current_heroes


def take_damage(current_heroes: dict, name: str, damage: int, attacker: str):
    if current_heroes[name][0] - damage <= 0:
        del current_heroes[name]
        print(f"{name} has been killed by {attacker}!")
    else:
        current_heroes[name][0] -= damage
        print(f"{name} was hit for {damage} HP by {attacker} and now has {current_heroes[name][0]} HP left!")
    return current_heroes


def recharge(current_heroes: dict, name: str, amount: int):
    if current_heroes[name][1] + amount > 200:
        gained_mana = 200 - current_heroes[name][1]
        current_heroes[name][1] = 200
        print(f"{name} recharged for {gained_mana} MP!")
    else:
        current_heroes[name][1] += amount
        print(f"{name} recharged for {amount} MP!")
    return current_heroes


def heal(current_heroes: dict, name: str, amount: int):
    if current_heroes[name][0] + amount > 100:
        gained_hp = 100 - current_heroes[name][0]
        current_heroes[name][0] = 100
        print(f"{name} healed for {gained_hp} HP!")
    else:
        current_heroes[name][0] += amount
        print(f"{name} healed for {amount} HP!")
    return current_heroes

number_of_heroes = int(input())
for _ in range(number_of_heroes):
    hero = input()
    hero = hero.split()
    heroes[hero[0]] = [int(hero[1]), int(hero[2])]

command = input()

while command != "End":
    command = command.split(" - ")
    if command[0] == "Heal":
        heroes = heal(heroes, command[1], int(command[2]))
    elif command[0] == "Recharge":
        heroes = recharge(heroes, command[1], int(command[2]))
    elif command[0] == "TakeDamage":
        heroes = take_damage(heroes, command[1], int(command[2]), command[3])
    elif command[0] == "CastSpell":
        heroes = cast_spell(heroes, command[1], int(command[2]), command[3])
    command = input()
for hero, stats in heroes.items():
    print(f"{hero}")
    print(f"  HP: {stats[0]}")
    print(f"  MP: {stats[1]}")