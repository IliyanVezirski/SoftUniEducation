words = input().split()

repeated_words = ''

for word in words:
    repeated_words += word * len(word)

print(repeated_words)