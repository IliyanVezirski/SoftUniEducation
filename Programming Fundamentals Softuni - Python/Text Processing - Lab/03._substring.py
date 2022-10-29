key_word = input()

words = input()

while key_word in words:
    words = words.replace(key_word,"")

print(words)
