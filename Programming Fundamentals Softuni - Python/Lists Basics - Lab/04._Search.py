number = int(input())
word = input()
all_word = []
matched_word = []


for i in range(number):
    current_word = input()
    all_word.append(current_word)
    if word in current_word:
        matched_word.append(current_word)

print(all_word)
print(matched_word)