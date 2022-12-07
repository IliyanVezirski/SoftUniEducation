size_of_cup = int(input())
name_of_cup = input().upper()
size = 3 * size_of_cup + 6 - 1
place_for_name = size_of_cup // 2
for _ in range(size_of_cup):
    space_number = size_of_cup - 1
    print(" " * space_number + " ~" * 3)
for upper_of_cup in range(1, size_of_cup - 1):
    size_of_empty_part = size - 2 - len(name_of_cup) - 2 * size_of_cup
    if upper_of_cup == 1:
        print("=" * size)
    if upper_of_cup == place_for_name:
        print("|" + "~" * size_of_cup + name_of_cup + "~" * size_of_cup + "|" + " " * size_of_empty_part + "|")
    else:
        print(
            "|" + "~" * size_of_cup + "~" * len(name_of_cup) + "~" * size_of_cup + "|" + " " * size_of_empty_part + "|")
print("=" * size)
size_to_remove = 0
for down_part in range(size_of_cup):
    new_size = size_of_cup - size_to_remove
    print(" " * size_to_remove + "\\" + "@" * new_size + "@" * len(
        name_of_cup) + "@" * new_size + "/" + " " * size_to_remove)
    size_to_remove += 1
print("-" * size)
