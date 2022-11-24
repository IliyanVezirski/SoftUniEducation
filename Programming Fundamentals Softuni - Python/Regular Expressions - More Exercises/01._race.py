import re

racers_dict = {}
racers = input().split(', ')
for race in racers:
    if race not in racers_dict:
        racers_dict[race] = 0

pattern_for_name = r'(?P<name_ch>[A-Za-z])'
pattern_for_distance = r'(?P<distance>\d)'

command = input()

while command != "end of race":
    match_for_name = re.finditer(pattern_for_name, command)
    match_for_distance = re.finditer(pattern_for_distance, command)
    current_name = ''
    current_distance = 0
    for match in match_for_name:
        match = match.groupdict()
        current_name += match['name_ch']
    for match in match_for_distance:
        match = match.groupdict()
        current_distance += int(match['distance'])
    if current_name in racers_dict:
        racers_dict[current_name] += current_distance

    command = input()

racers_dict = dict(sorted(racers_dict.items(), key=lambda kvp: -kvp[1]))
count = 0
for racer, points in racers_dict.items():
    count += 1
    if count == 1:
        print(f"{count}st place: {racer}")
    elif count == 2:
        print(f"{count}nd place: {racer}")
    elif count == 3:
        print(f"{count}rd place: {racer}")
    if count == 3:
        break
