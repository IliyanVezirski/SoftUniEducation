string = input()
open_brackets_link = []
for index in range(len(string)):
    if string[index] == "(":
        open_brackets_link.append(index)
    elif string[index] == ")":
        print(string[open_brackets_link.pop():index+1])
