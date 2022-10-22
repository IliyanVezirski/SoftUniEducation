

words =[i.lower() for i in input().split()]
dictionary = {}
for word in words:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1

for k, v in dictionary.items():
    if v % 2 == 1:
        print(k, end=" ")

