import re

string = input()

pattern = r"\b_([A-Za-z0-9]+)\b"

text_to_print = re.findall(pattern, string)
print(*text_to_print, sep=',')