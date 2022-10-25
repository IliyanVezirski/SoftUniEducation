command = input()

users_side = {}
user_found = False
user_side = ''
old_side_to_change = ""
while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        user = command[1]
        side = command[0]
        for key, value in users_side.items():
            for v in value:
                if value == user:
                    user_found = True
        if not user_found and side not in users_side.keys():
            users_side[side] = [user]
        elif user_found:
            users_side[side].append(user)
            user_found = False
        else:
            user_found = False


    else:
        command = command.split(" -> ")
        user = command[0]
        side = command[1]
        user_side = ''
        for key, value in users_side.items():
            for v in value:
                if v == user:
                    user_found = True
                    user_side = key
        if user_found:
            users_side[user_side].pop()
            users_side[side].append(user)
        elif not user_found and side in users_side.keys():
            users_side[side].append(user)
        else:
            users_side[side] = [user]
        print(f"{user} joins the {side} side!")
    command = input()
for key, value in users_side.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for v in value:
            print(f"! {v}")
