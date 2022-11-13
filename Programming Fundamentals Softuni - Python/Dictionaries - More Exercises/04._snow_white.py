dwarfs = {}

counter_1 = 0
data = input()
while data != "Once upon a time":
    data = data.split(" <:> ")
    name = data[0]
    hat_color = data[1]
    physics = int(data[2])
    counter_1 += 1
    founded_dwarf = False
    for counter, dwarf in dwarfs.items():
        if dwarfs[counter][0] == name and dwarfs[counter][1] == hat_color:
            founded_dwarf = True
            dwarfs[counter] = [name, hat_color, physics]
    if not founded_dwarf:
        dwarfs[counter_1] = [name, hat_color, physics]
    data = input()

dwarfs = dict(sorted(dwarfs.items(), key=lambda kvp: (-kvp[1][2], dwarfs[1].count(kvp[1][1]))))
[print(f"({dwarf[1]}) {dwarf[0]} <-> {dwarf[2]}") for count, dwarf in dwarfs.items()]
