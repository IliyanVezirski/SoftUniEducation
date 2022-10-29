string = input()
reversed_string = ""
while string != "end":
    reversed_string = [i for i in string[::-1]]
    print(f"{string} = {''.join(reversed_string)}")
    string = input()

