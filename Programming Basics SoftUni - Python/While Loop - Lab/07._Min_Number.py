import sys
n = input()
number = int(n)
min_number = sys.maxsize
while n != "Stop":
    number = int(n)
    if min_number > number:
        min_number = number
    n = input()

print(min_number)