start_number = int(input())
end_number = int(input())
for i in range(start_number, end_number + 1):
        for n in range(start_number, end_number + 1):
            for z in range(start_number, end_number + 1):
                for m in range(start_number, end_number + 1):
                    if i > m and i % 2 == 0 and m % 2 == 1 and (z + n) % 2 == 0:
                        print(f'{i}{n}{z}{m}', end=' ')
                    elif i > m and i % 2 == 1 and m % 2 == 0 and (z + n) % 2 == 0:
                        print(f'{i}{n}{z}{m}', end=' ')