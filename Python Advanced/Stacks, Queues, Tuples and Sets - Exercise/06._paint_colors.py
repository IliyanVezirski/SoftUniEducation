from collections import deque

string = deque(input().split())

colors = []
MAIN_COLORS = ["red", "yellow", "blue"]
SECONDARY_COLORS = ["orange", "purple", "green"]

while string:
    if len(string) > 1:
        first_substring = string[-1] + string[0]
        second_substring = string[0] + string[-1]
        if first_substring in MAIN_COLORS or first_substring in SECONDARY_COLORS:
            colors.append(first_substring)
            string.pop()
            string.popleft()
        elif second_substring in MAIN_COLORS or second_substring in SECONDARY_COLORS:
            colors.append(second_substring)
            string.pop()
            string.popleft()
        else:
            first_substring = string[0][:-1]
            second_substring = string[-1][:-1]
            string.pop()
            string.popleft()
            if first_substring:
                string.insert(len(string) // 2, first_substring)
            if second_substring:
                string.insert(len(string) // 2, second_substring)

    else:
        substring = string[0]
        if substring in MAIN_COLORS or substring in SECONDARY_COLORS:
            colors.append(substring)
            string.pop()
        else:
            string.pop()
for color in colors:
    if color == "orange":
        if "red" in colors and "yellow" in colors:
            continue
        else:
            colors.remove(color)
    if color == "purple":
        if 'red' in colors and 'blue' in colors:
            continue
        else:
            colors.remove(color)
    if color == "green":
        if 'yellow' in colors and 'blue' in colors:
            continue
        else:
            colors.remove(color)
print(colors)