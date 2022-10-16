n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)
for z in range(1, n):
    print(' ' * (z) + '* ' * (n- z))
