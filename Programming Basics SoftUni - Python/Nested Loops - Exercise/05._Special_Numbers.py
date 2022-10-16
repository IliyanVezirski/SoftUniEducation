magic_number = int(input())
for first in range(1,10):
    for second in range(1,10):
        for third in range(1,10):
            for forth in range(1,10):
                if magic_number / first == magic_number // first and magic_number / second == magic_number // second and magic_number / third == magic_number // third and magic_number / forth == magic_number // forth:
                    print(f'{first}{second}{third}{forth}', end=' ')