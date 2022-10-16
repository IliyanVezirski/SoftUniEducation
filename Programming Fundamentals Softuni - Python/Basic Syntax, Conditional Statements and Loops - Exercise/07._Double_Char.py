string = input()
word = ''
while string != "End":
    for i in range(len(string)):
        word += string[i] * 2
    if string != 'SoftUni':
        print(word)
    string = input()
    word = ''