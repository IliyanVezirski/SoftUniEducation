word = input()
word_lower = word.lower()
count = 0
while 'water' in word_lower or 'sun' in word_lower or 'sand' in word_lower or 'fish' in word_lower:
    count += 1
    if 'water' in word_lower:
        word_lower = word_lower.replace('water', '', 1)
    elif 'sun' in word_lower:
        word_lower = word_lower.replace('sun', '', 1)
    elif 'sand' in word_lower:
        word_lower = word_lower.replace('sand', '', 1)
    elif 'fish' in word_lower:
        word_lower = word_lower.replace('fish', '', 1)



print(count)