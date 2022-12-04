import re

pattern = r'(?P<sep>[!])(?P<command>[A-Z][a-z]{2,})(?P=sep):\[(?P<word>[A-Za-z]+)\]'

number = int(input())

for _ in range(number):
    string = input()
    matches = re.findall(pattern, string)
    if matches:
        for match in matches:
            word_to_translate = match[2]
            command = match[1]
            translated_word = []
        translated_word = [str(ord(letter)) for letter in word_to_translate]
        print(f"{command}: {' '.join(translated_word)}")
    else:
        print("The message is invalid")
