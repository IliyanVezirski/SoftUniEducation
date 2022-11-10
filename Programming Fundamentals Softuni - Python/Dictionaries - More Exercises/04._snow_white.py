dwarfs = {
    'names': [],
    'hat': [],
    'physics': []
}

data = input()
while data != "Once upon a time":
    data = data.split(" <:> ")
    name = data[0]
    hat_color = data[1]
    physics = int(data[2])
    if name not in dwarfs['names']:
        dwarfs['names'].append(name)
        dwarfs['hat'].append(hat_color)
        dwarfs['physics'].append(physics)
    elif name in dwarfs['names']:
        index_for_current_dwarf = dwarfs['names'].index(name)
        if dwarfs['hat'][index_for_current_dwarf] != hat_color:
            dwarfs['names'].append(name)
            dwarfs['hat'].append(hat_color)
            dwarfs['physics'].append(physics)
        else:
            if physics > dwarfs['physics'][index_for_current_dwarf]:
                dwarfs['physics'][index_for_current_dwarf] = physics
    data = input()
index_dict = {}
for i, v in enumerate(dwarfs['names']):
    index_dict[i] = v
dwarfs['physics'] = sorted(dwarfs['physics'], key=lambda x: -x)
print(index_dict)
print(dwarfs)
