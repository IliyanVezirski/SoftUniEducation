exam = {}
command = input()
submissions = {}
while command != "exam finished":
    command = command.split("-")
    username = command[0]
    language = command[1]
    if language == "banned":
        for key, value in exam.items():
            if username in value.keys():
                exam[key][username] = None
    else:
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
        points = command[2]
        if language not in exam:
            exam[language] = {username: points}
        elif username not in exam[language].keys():
            exam[language][username] = points
        else:
            for key, value in exam[language].items():
                if key == username:
                    if value < points:
                        exam[language][username] = points

    command = input()

print(f"Results:")
for key, value in exam.items():
    for k, v in value.items():
        if v:
            print(f"{k} | {v}")
print(f"Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")