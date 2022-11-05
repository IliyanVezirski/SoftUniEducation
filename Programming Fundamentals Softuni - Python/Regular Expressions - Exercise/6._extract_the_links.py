import re

text = input()
pattern = r"[w]{3}.[A-Za-z0-9-]+\.[a-z\.]+"
while True:
    if text:
        word = re.findall(pattern, text)
        if word:
            print(*word)
    else:
        break
    text = input()