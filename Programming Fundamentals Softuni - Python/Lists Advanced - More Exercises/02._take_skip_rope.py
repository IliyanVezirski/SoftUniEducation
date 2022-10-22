string = [i for i in input()]
not_alphabetic_list = []
alphabetic_list = []
take_list = []
skip_list = []
result = []
for letter in string:
    if letter.isdigit():
        not_alphabetic_list.append(letter)
    else:
        alphabetic_list.append(letter)
for index in range(len(not_alphabetic_list)):
    if index % 2 == 0:
        take_list.append(int(not_alphabetic_list[index]))
    else:
        skip_list.append(int(not_alphabetic_list[index]))
test_list = alphabetic_list.copy()
while alphabetic_list != []:
    for i in range(len(take_list)):
        if alphabetic_list == []:
            break
        taked_letters = alphabetic_list[:take_list[i]]
        result += taked_letters
        del alphabetic_list[0:take_list[i]]
        del alphabetic_list[0:skip_list[i]]


print(*result, sep='')
