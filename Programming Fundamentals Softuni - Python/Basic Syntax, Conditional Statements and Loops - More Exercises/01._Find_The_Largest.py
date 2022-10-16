number = str(input())
number_list = []
word = ''
for i in range(len(number)):
    m = int(i)
    number_list.append(number[m])
number_list.sort(reverse=True)
for j in number_list:
    word += str(j)
print(word)