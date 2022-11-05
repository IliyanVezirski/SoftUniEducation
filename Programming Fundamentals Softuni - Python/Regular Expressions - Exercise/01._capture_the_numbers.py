import re

numbers = r'\d+'
text = input()


while True:
    if text:
        numbers_to_print = re.findall(numbers, text)
        if numbers_to_print:
            print(' '.join(numbers_to_print), end=' ')
    else:
        break

    text = input()