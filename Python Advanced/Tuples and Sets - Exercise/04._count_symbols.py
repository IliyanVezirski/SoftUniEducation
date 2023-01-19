text = input()
letters = set()
text_list = []
for letter in text:
    letters.add(letter)
    text_list.append(letter)
sorted_letters = tuple(sorted(letters, key=lambda x: x))
for letter in sorted_letters:

    print(f"{letter}: {text_list.count(letter)} time/s")
