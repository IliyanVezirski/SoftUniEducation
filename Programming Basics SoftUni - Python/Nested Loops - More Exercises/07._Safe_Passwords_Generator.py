a = int(input())
b = int(input())
passwords_max = int(input())
count_password = 0
first = 34
second = 63
for a in range(1, a + 1):
    if count_password == passwords_max:
        break
    for b in range(1, b + 1):
        if first == 55:
            first = 34
        first += 1
        if second == 96:
            second = 63
        second += 1
        print(f'{chr(first)}{chr(second)}{a}{b}{chr(second)}{chr(first)}', end="|")
        count_password += 1
        if count_password == passwords_max:
            break
