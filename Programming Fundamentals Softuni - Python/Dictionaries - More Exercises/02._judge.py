judge = {}
individual_standing = {}
command = input()

while command != "no more time":
    command = command.split(" -> ")
    username = command[0]
    contest = command[1]
    points = int(command[2])
    if contest in judge:
        for user in judge.values():
            if username in user:
                if user[username] <= points:
                    user[username] = points
            else:
                judge[contest][username] = points
    else:
        judge[contest] = {username: points}
    command = input()

for key, value in judge.items():
    new_key = dict(sorted(value.items(), key=lambda v: (-v[1], v[0])))
    judge[key] = new_key
for key, value in judge.items():
    for k, v in value.items():
        if k in individual_standing:
            individual_standing[k] += v
        else:
            individual_standing[k] = v
individual_standing = dict(sorted(individual_standing.items(), key=lambda v: (-v[1], v[0])))

for key, value in judge.items():
    print(f"{key}: {len(value)} participants")
    counter = 0
    for k, v in value.items():
        counter += 1
        print(f"{counter}. {k} <::> {v}")
print(f"Individual standings:")
counter = 0
for key, value in individual_standing.items():
    counter += 1
    print(f"{counter}. {key} -> {value}")
