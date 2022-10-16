a1 = int(input())
a2 = int(input())
n = int(input())
for first in range(a1, a2):
    for second in range(1, n):
        for third in range(1, int(n / 2)):
            if first % 2 == 1 and (second + third + first) % 2 == 1:
                print(f'{chr(first)}-{second}{third}{first}')