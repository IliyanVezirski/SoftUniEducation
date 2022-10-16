cake_width = int(input())
cake_len = int(input())
cake_pieaces = cake_width * cake_len
cakes = ''
while cake_pieaces >= 0:
    cakes = input()
    if cakes == 'STOP':
        break
    cakes = int(cakes)
    cake_pieaces -= cakes


if cake_pieaces >= 0:
    print(f'{cake_pieaces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieaces)} pieces more.')
