"""
You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic.
You want to play it all day long! So cancel all other arrangements and create your party!
On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for your party.
 On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a single space
 in the following format:
"{hero name} {HP} {MP}"
-	HP stands for hit points and MP for mana points
-	a hero can have a maximum of 100 HP and 200 MP
After you have successfully picked your heroes, you can start playing the game. You will be receiving different commands,
each on a new line, separated by " – ", until the "End" command is given.
There are several actions that the heroes can perform:
"CastSpell – {hero name} – {MP needed} – {spell name}"
•	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
•	If the hero is unable to cast the spell print:
o	"{hero name} does not have enough MP to cast {spell name}!"
"TakeDamage – {hero name} – {damage} – {attacker}"
•	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
•	If the hero has died, remove him from your party and print:
o	"{hero name} has been killed by {attacker}!"
"Recharge – {hero name} – {amount}"
•	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200.
(the MP can't go over the maximum value).
•	 Print the following message:
o	"{hero name} recharged for {amount recovered} MP!"
"Heal – {hero name} – {amount}"
•	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100),
 HP is increased to 100 (the HP can't go over the maximum value).
•	 Print the following message:
o	"{hero name} healed for {amount recovered} HP!"

"""


def cast_spell(current_heroes: dict, hero_name: str, mana_needed: int, spell_name: str):
    if current_heroes[hero_name][1] - mana_needed < 0:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        return current_heroes
    else:
        current_heroes[hero_name][1] -= mana_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {current_heroes[hero_name][1]} MP!")
        return current_heroes


def damage(current_heroes: dict, hero_name: str, damage: int, attacker: str):
    current_heroes[hero_name][0] -= damage
    if current_heroes[hero_name][0] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_heroes[hero_name][0]} HP left!")
        return current_heroes
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del current_heroes[hero_name]
        return current_heroes


def recharge(current_heroes: dict, hero_name: str, amount: int):
    if current_heroes[hero_name][1] + amount >= 200:
        gained_mana = 200 - current_heroes[hero_name][1]
        print(f"{hero_name} recharged for {gained_mana} MP!")
        current_heroes[hero_name][1] = 200
        return current_heroes
    else:
        current_heroes[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")
        return current_heroes


def heal(current_heroes: dict, hero_name: str, amount: int):
    if current_heroes[hero_name][0] + amount >= 100:
        gained_hp = 100 - current_heroes[hero_name][0]
        current_heroes[hero_name][0] = 100
        print(f"{hero_name} healed for {gained_hp} HP!")
        return current_heroes
    else:
        current_heroes[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")
        return current_heroes


heroes = {}
heroes_number = int(input())
for status in range(heroes_number):
    hero = input()
    hero_stats = hero.split()
    heroes[hero_stats[0]] = [int(hero_stats[1]), int(hero_stats[2])]

command = input()

while command != "End":
    command = command.split(' - ')
    if command[0] == "CastSpell":
        heroes = cast_spell(heroes, command[1], int(command[2]), command[3])
    elif command[0] == "TakeDamage":
        heroes = damage(heroes, command[1], int(command[2]), command[3])
    elif command[0] == "Recharge":
        heroes = recharge(heroes, command[1], int(command[2]))
    elif command[0] == "Heal":
        heroes = heal(heroes, command[1], int(command[2]))
    command = input()

for hero, stats in heroes.items():
    print(hero)
    print(f"  HP: {stats[0]}")
    print(f"  MP: {stats[1]}")