word = input()
word_list = []
letters = []
count = 0
for letter in word:
    word_list += letter
for ss in word_list:
    if ss.isupper():
        letters += [count]
    count += 1
print(letters)