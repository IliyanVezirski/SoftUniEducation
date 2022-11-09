judge = {}

data = input()

while data != "no more time":
    data = data.split(' -> ')
    if data[1] not in judge:
        judge[data[1]] = {data[0]: int(data[2])}
    else:
        if data[0] not in judge[data[1]]:
            judge[data[1]][data[0]] = int(data[2])
        else:
            if judge[data[1]][data[0]] < int(data[2]):
                judge[data[1]][data[0]] = int(data[2])

    data = input()
for contest, username in judge.items():
    judge[contest] = dict(sorted(username.items(), key=lambda kvp: (-kvp[1], kvp)))
for contest, username in judge.items():
    print(f"{contest}: {len(username)} participants")
    counter = 1
    for user, points in username.items():
        print(f"{counter}. {user} <::> {points}")
        counter += 1
individual_standings = {}
for contest, username in judge.items():
    for user, points in username.items():
        if user not in individual_standings:
            individual_standings[user] = 0
        individual_standings[user] += points
individual_standings = dict(sorted(individual_standings.items(), key=lambda kvp: (-kvp[1], kvp)))
print(f"Individual standings:")
counter = 1
for user, points in individual_standings.items():
    print(f"{counter}. {user} -> {points}")
    counter += 1
