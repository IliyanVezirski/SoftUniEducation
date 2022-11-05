import re

string = input()

matched_pattern = r"\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b"

string_to_print = re.findall(matched_pattern, string)


print(*string_to_print)
