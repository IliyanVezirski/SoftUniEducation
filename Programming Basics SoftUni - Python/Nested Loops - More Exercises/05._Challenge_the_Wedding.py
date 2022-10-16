man_clients = int(input())
women_clients = int(input())
tables_max = int(input())
table_count = 0
for man in range(1, man_clients + 1):
    if table_count >= tables_max:
        break
    for women in range(1, women_clients + 1):
        print(f'({man} <-> {women})', end=' ')
        table_count += 1
        if table_count >= tables_max:
            break
