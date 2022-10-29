usernames = input().split(', ')
for username in usernames:
    is_valid = True
    if not 3 <= len(username) <= 16:
        is_valid = False
        continue
    for ch in username:
        if ch.isdigit():
            continue
        elif ch.isalpha():
            continue
        elif ch == "-":
            continue
        elif ch == "_":
            continue
        else:
            is_valid = False
    if is_valid:
        print(username)