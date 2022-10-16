number = int(input())
for i in range(1, 10):
    for z in range(1, 10):
        for d in range(1, 10):
            for m in range(1, 10):
                if i + z == d + m and number % (i + z) == 0:
                    print(f'{i}{z}{d}{m}', end=' ')