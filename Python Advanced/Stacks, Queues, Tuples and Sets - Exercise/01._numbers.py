def add_first(first_set: set, set_to_add: list):
    [first_set.add(int(i)) for i in set_to_add]
    return first_set


def add_second(second_set: set, set_to_add: list):
    [second_set.add(int(i)) for i in set_to_add]
    return second_set


def remove_first(first_set: set, set_to_remove: list):
    [first_set.discard(int(i)) for i in set_to_remove]
    return first_set


def remove_second(second_set: set, set_to_remove: list):
    [second_set.discard(int(i)) for i in set_to_remove]
    return second_set


def check_subset(first_set: set, second_set: set):
    if first_set.issubset(second_set) or second_set.issubset(first_set):
        return True
    return False


first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))

number_of_command = int(input())

for _ in range(number_of_command):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            add_first(first_sequence, command[2:])
        else:
            add_second(second_sequence, command[2:])
    elif command[0] == "Remove":
        if command[1] == "First":
            remove_first(first_sequence, command[2:])
        else:
            remove_second(second_sequence, command[2:])
    elif command[0] == "Check":
        print(check_subset(first_sequence, second_sequence))
print(*list(sorted(first_sequence, key=lambda x: x)), sep=', ')
print(*list(sorted(second_sequence, key=lambda x: x)), sep=', ')
