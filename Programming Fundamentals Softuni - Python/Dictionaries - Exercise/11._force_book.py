command = input()
users = {}


def no_side(dictionary: dict, side: str, user: str):
    dictionary[side] = [user]
    return dictionary


def no_user(dictionary: dict, side: str, user: str):
    dictionary[side] = [user]
    return dictionary


while command != "Lumpawaroo":

    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        if force_side in users.keys():
            for key, value in users.items():
                if force_user in value:
                    user_in = True
            if user_in:
                user_in = False
                command = input()
                continue
    else:
        command = command.split(" -> ")
        force_side = command[1]
        force_user = command[0]
        print(f"{force_user} joins the {force_side} side!")

    if force_side in users.keys():
        for key, value in users.items():
            if force_user in value:
                value.remove(force_user)
        users[force_side].append(force_user)

    else:
        no_user(users, force_side, force_user)
    command = input()
for key, value in users.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for v in value:
            print(f"! {v}")
