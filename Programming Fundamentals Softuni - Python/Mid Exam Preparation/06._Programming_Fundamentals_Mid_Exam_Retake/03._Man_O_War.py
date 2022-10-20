"""Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line, you will receive the status of the pirate ship, which is a string representing integer sections separated by ">". On the second line, you will receive the same type of status, but for the warship:
"{section1}>{section2}>{section3}… {sectionn}"
On the third line, you will receive the maximum health capacity a section of the ship can reach.
The following lines represent commands until "Retire":
•	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section. Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks, print the following and stop the program: "You won! The enemy ship has sunken."
•	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not, skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."
•	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if the index is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity.
•	"Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."
In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in the following format:
"Pirate ship status: {pirateShipSum}
Warship status: {warshipSum}"
Input
•	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
•	On the 2nd line, you are going to receive the status of the warship
•	On the 3rd line, you will receive the maximum health a section of a ship can reach.
•	On the following lines, until "Retire", you will be receiving commands.
Output
•	Print the output in the format described above.
Constraints
•	The section numbers will be integers in the range [1….1000]
•	The indexes will be integers [-200….200]
•	The damage will be an integer in the range [1….1000]
•	The health will be an integer in the range [1….1000]
"""

pirate_ship = [int(i) for i in input().split(">")]
warship = [int(i) for i in input().split(">")]
health_capacity = int(input())


def fire(warship: list, index: int, dmg: int):
    warship[index] -= dmg
    if warship[index] <= 0:
        print(f"You won! The enemy ship has sunken.")
        exit()
    return warship


def defend(pirate_ship: list, start_point: int, end_point: int, dmg: int):
    for index in range(start_point, end_point + 1):
        pirate_ship[index] -= dmg
        if pirate_ship[index] <= 0:
            print(f"You lost! The pirate ship has sunken.")
            exit()
    return pirate_ship


def repair(pirate_ship: list, index: int, health: int):
    pirate_ship[index] += health
    if pirate_ship[index] > health_capacity:
        pirate_ship[index] = health_capacity
    return pirate_ship


def status(pirate_ship: list):
    section_count = 0
    for i in pirate_ship:
        if i < health_capacity * 0.2:
            section_count += 1
    print(f"{section_count} sections need repair.")


command = input()

while command != "Retire":
    command = command.split()
    shot = command[0]
    if shot == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index in range(len(warship)):
            fire(warship, index, damage)
    elif shot == "Defend":
        index_1 = int(command[1])
        index_2 = int(command[2])
        damage = int(command[3])
        if index_1 in range(len(pirate_ship)) and index_2 in range(len(pirate_ship)):
            defend(pirate_ship, index_1, index_2, damage)
    elif shot == "Status":
        status(pirate_ship)
    elif shot == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index in range(len(pirate_ship)):
            repair(pirate_ship, index, health)
    command = input()
print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")