
string = input()
counter = int(input())

def repeat_string(string, counter):
    repeated_string = ''
    for i in range(counter):
        repeated_string += string
    return repeated_string

print(repeat_string(string, counter))