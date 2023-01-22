from collections import deque
import math
string = deque(input().split())

substring = string[0] + string[-1]
main_colors = []
secondary_colors = []
indexes_of_secondary_colors = []


def pop_from_string(string: deque):
    if len(string) > 1:
        first = string.pop()
        second = string.popleft()
    else:
        string.pop()


def color_append(substring):
    if substring in "redyellowblue":
        main_colors.append(substring)
        pop_from_string(string)
        return True
    elif substring in "orangepurplegreen":
        if substring == "orange":
            if 'red' in main_colors and 'yellow' in main_colors:
                main_colors.append(substring)
                pop_from_string(string)
                return True
            else:
                secondary_colors.append(substring)
                indexes_of_secondary_colors.append(len(main_colors))
                pop_from_string(string)
                return True
        elif substring == "purple":
            if 'red' in main_colors and 'blue' in main_colors:
                main_colors.append(substring)
                pop_from_string(string)
                return True
            else:
                secondary_colors.append(substring)
                indexes_of_secondary_colors.append(len(main_colors))
                pop_from_string(string)
                return True
        elif substring == "green":
            if 'yellow' in main_colors and 'blue' in main_colors:
                main_colors.append(substring)
                pop_from_string(string)
                return True
            else:
                secondary_colors.append(substring)
                indexes_of_secondary_colors.append(len(main_colors))
                pop_from_string(string)
                return True
        else:
            pop_from_string(string)
            return True
    else:
        return False


while string:
    if len(string) > 1:
        substring = string[-1] + string[0]
        substring2 = string[0] + string[-1]
    else:
        substring = string[0]
        substring2 = substring
    if color_append(substring):
        continue
    elif color_append(substring2):
        continue
    else:
        if len(string) > 1:
            first = string.pop()
            first = first[:len(first) - 1]
            second = string.popleft()
            second = second[:len(second) - 1]
            string.insert(int(math.ceil(len(string) / 2)), first)
            string.insert(int(math.ceil(len(string) / 2)), second)
            string = deque(i for i in string if i)
        else:
            color_append(string[0])
            break
for index in range(len(secondary_colors)):
    if secondary_colors[index] == "orange":
        if 'red' in main_colors and 'yellow' in main_colors:
            main_colors.insert(indexes_of_secondary_colors[index], secondary_colors[index])
    elif secondary_colors[index] == "purple":
        if 'red' in main_colors and 'blue' in main_colors:
            main_colors.insert(indexes_of_secondary_colors[index], secondary_colors[index])
    elif secondary_colors[index] == 'green':
        if 'yellow' in main_colors and 'blue' in main_colors:
            main_colors.insert(indexes_of_secondary_colors[index], secondary_colors[index])
print(main_colors)
