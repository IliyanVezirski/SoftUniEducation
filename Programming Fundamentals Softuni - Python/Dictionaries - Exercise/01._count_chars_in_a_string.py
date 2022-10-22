word = input()
dictionary = {}
for i in word:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

for k, v in dictionary.items():
    if k != " ":
        print(f"{k} -> {v}")
