first_number = int(input())
second_number = int(input())
third_number = int(input())
prime = None
for i in range(1, first_number + 1):
    if i % 2 == 0:
        for n in range(1, second_number + 1):
            if n == 1:
                prime = False
            elif n == 2:
                prime = True
            else:
                for x in range(2, n):
                    if n % x == 0:
                        prime = False
                        break
                    else:
                        prime = True
            if prime:
                for v in range(1, third_number + 1):
                    if v % 2 == 0:
                        print(f'{i} {n} {v}')