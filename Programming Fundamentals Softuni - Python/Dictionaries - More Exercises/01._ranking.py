command = input()
contest = {}
submissions = {}
sorted_dictionary = {}
best_candidate = ""
points_of_best_candidate = 0
while command != "end of contests":
    command = command.split(":")
    contest_user = command[0]
    password = command[1]
    if contest_user not in contest:
        contest[contest_user] = password
    command = input()

command = input()

while command != "end of submissions":
    command = command.split("=>")
    contest_user = command[0]
    password = command[1]
    username = command[2]
    points = int(command[3])
    if contest_user in contest:
        if password == contest[contest_user]:
            if username not in submissions.keys():
                submissions[username] = {contest_user: points}
            else:
                if contest_user not in submissions[username].keys():
                    submissions[username][contest_user] = points
                else:
                    if int(points) > submissions[username][contest_user]:
                        submissions[username][contest_user] = points
    command = input()
for kye, value in submissions.items():
    best = sum(value.values())
    if best > points_of_best_candidate:
        best_candidate = kye
        points_of_best_candidate = best
print(f"Best candidate is {best_candidate} with total {points_of_best_candidate} points.")
print(f"Ranking:")
for key, value in submissions.items():
    sorted_dict = submissions[key]
    sorted_dict = dict(sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True))
    submissions[key] = sorted_dict
for key, value in submissions.items():
    for v in value.values():
        if key not in sorted_dictionary:
            sorted_dictionary[key] = v
        sorted_dictionary[key] += v
sorted_dictionary = dict(sorted(sorted_dictionary.items(), key=lambda x: x[0]))

for key in sorted_dictionary.keys():
    for k, v in submissions.items():
        if k == key:
            print(f"{k}")
            for key1, value in v.items():
                print(f"#  {key1} -> {value}")

# for kye, value in submissions.items():
#     if kye != best_candidate:
#         print(kye)
#         for k, v in value.items():
#             print(f"#  {k} -> {v}")
# for key, value in submissions.items():
#     if key == best_candidate:
#         print(key)
#         for k, v in value.items():
#             print(f"#  {k} -> {v}")
