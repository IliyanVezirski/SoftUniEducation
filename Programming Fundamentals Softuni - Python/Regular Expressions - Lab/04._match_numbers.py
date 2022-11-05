import re

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

numbers = input()

numbers_to_print = re.finditer(pattern, numbers)

print(' '.join([i.group() for i in numbers_to_print]))