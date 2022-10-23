phones = input().split(', ')


def add(phones: list, phone_to_add: str):
    if phone_to_add in phones:
        return phones
    else:
        phones.append(phone_to_add)
        return phones


def remove(phones: list, phone_to_remove: str):
    if phone_to_remove in phones:
        phones.remove(phone_to_remove)
        return phones
    else:
        return phones


def bonus_phone(phones: list, old_phone: str, new_phone: str):
    if old_phone in phones:
        index = phones.index(old_phone)
        index_to_add = index + 1
        phones.insert(index_to_add, new_phone)
        return phones
    else:
        return phones


def last(phones: list, phone: str):
    if phone in phones:
        phones.remove(phone)
        phones.append(phone)
        return phones
    else:
        return phones


command = input()
while command != "End":
    command = command.split(' - ')
    if command[0] == "Add":
        add(phones, command[1])
    elif command[0] == "Remove":
        remove(phones, command[1])
    elif command[0] == "Bonus phone":
        bonus_phones = command[1].split(":")
        old_phone = bonus_phones[0]
        new_phone = bonus_phones[1]
        bonus_phone(phones, old_phone, new_phone)
    elif command[0] == "Last":
        last(phones, command[1])
    command = input()

print(*phones, sep=', ')
