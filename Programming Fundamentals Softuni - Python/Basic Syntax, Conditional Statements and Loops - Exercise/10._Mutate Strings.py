string1 = input()
string2 = input()
string1_list = []
string2_list = []
word1_list = []
word2_list = []
word = ''
j = 0
for i in range(len(string1)):
    string1_list.append(string1[i])
    string2_list.append(string2[i])
    word1_list.append(string1[i])
    word2_list.append(string2[i])
for j in range(len(string1_list)):
    string1_list[j] = string2_list[j]
    for m in range(len(string1_list)):
        word += string1_list[m]
    letter1 = word1_list[j]
    letter2 = word2_list[j]
    if letter1 != letter2:
        print(word)
    word = ''