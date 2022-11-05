import re

first_case = r'(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})\b'

text = input()

numbers_to_print = re.finditer(first_case, text)
matches = [i.group() for i in numbers_to_print]

print(*matches, sep=', ')