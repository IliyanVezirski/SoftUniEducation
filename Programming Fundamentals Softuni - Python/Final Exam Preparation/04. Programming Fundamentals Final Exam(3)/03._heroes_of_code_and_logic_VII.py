def cast_spell(current_heroes: dict, hero_name: str, mana_needed: int, spell_name: str):
    if current_heroes[hero_name]['mp'] - mana_needed < 0:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    else:
        current_heroes[hero_name]['mp'] -= mana_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {current_heroes[hero_name]['mp']} MP!")
    return current_heroes


def take_dmg(current_heroes: dict, hero_name: str, damage: int, attacker: str):
    current_heroes[hero_name]['hp'] -= damage
    if current_heroes[hero_name]['hp'] <= 0:
        print(f'{hero_name} has been killed by {attacker}!')
        del current_heroes[hero_name]
    else:
        print(
            f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_heroes[hero_name]['hp']} HP left!")
    return current_heroes


def recharge(current_heroes: dict, hero_name: str, amount: int):
    if current_heroes[hero_name]['mp'] + amount > 200:
        amount = 200 - current_heroes[hero_name]['mp']
    current_heroes[hero_name]['mp'] += amount
    print(f"{hero_name} recharged for {amount} MP!")
    return current_heroes


def heal(current_heroes: dict, hero_name: str, amount: int):
    if current_heroes[hero_name]['hp'] + amount > 100:
        amount = 100 - current_heroes[hero_name]['hp']
    current_heroes[hero_name]['hp'] += amount
    print(f"{hero_name} healed for {amount} HP!")
    return current_heroes


number_of_heroes = int(input())
heroes_stats = {}
for _ in range(number_of_heroes):
    hero, hp, mp = input().split()
    heroes_stats[hero] = {"hp": int(hp), "mp": int(mp)}

command = input()

while command != "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        heroes_stats = cast_spell(heroes_stats, command[1], int(command[2]), command[3])
    elif command[0] == "TakeDamage":
        heroes_stats = take_dmg(heroes_stats, command[1], int(command[2]), command[3])
    elif command[0] == "Recharge":
        heroes_stats = recharge(heroes_stats, command[1], int(command[2]))
    elif command[0] == "Heal":
        heroes_stats = heal(heroes_stats, command[1], int(command[2]))
    command = input()
[print(f"{hero}\n  HP: {stats['hp']}\n  MP: {stats['mp']}") for hero, stats in heroes_stats.items()]
