command = input()

users_side = {}
user_found = False
user_side = ''
old_side_to_change = ""
while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(' | ')
        side = command[0]
        user = command[1]
        for key, value in users_side.items():
            if user in value:
                user_found = True
                user_side = key
        if side not in users_side.keys():
            users_side[side] = [user]
        elif user_found:
            continue
        else:
            new_users = users_side[side]
            new_users = new_users.append(user)
            users_side[side] = new_users
    elif "->" in command:
        command = command.split(" -> ")
        user = command[0]
        side = command[1]
        old_side = ''
        for key, value in users_side.items():
            if user in value:
                user_found = True
                user_side = key
                break
        if user_found and users_side != side:
            remove_user = users_side[user_side]
            remove_user.remove(user)
            users_side[user_side] = remove_user
            new_side = users_side[side]
            new_side.append(user)
            users_side[side] = new_side
            print(f"{user} joins the {side} side!")
        elif side in users_side.keys():
            old_side = users_side[side]
            old_side.append(user)
            users_side[side] = old_side
            print(f"{user} joins the {side} side!")
        else:
            users_side[side] = user
            print(f"{user} joins the {side} side!")
    command = input()
    user_found = False
    user_side = ''
    old_side_to_change = ""
dict_to_print = {}
for k, v in users_side.items():
    if len(v) > 0:
        dict_to_print[k] = v
for key, value in dict_to_print.items():
    print(f"Side: {key}, Members: {len(value)}")
    for users in value:
        print(f"! {users}")
