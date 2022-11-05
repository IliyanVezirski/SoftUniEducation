import re

string = input()
word = input()

pattern = fr'\b{word}\b'

count = len(re.findall(pattern, string, flags=re.IGNORECASE))

print(count)
