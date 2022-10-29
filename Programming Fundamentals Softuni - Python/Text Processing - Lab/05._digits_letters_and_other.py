code = input()

digits = ''
alpha = ''
other = ''

for letter in code:
    if letter.isalpha():
        alpha += letter
    elif letter.isdigit():
        digits += letter
    else:
        other += letter

print(digits, alpha, other, sep="\n")
