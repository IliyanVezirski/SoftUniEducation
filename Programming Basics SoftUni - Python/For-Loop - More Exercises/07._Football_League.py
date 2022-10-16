capacity = int(input())
fens = int(input())
fens_in_a = 0
fens_in_b = 0
fens_in_v = 0
fens_in_g = 0
for i in range(1, fens + 1):
    sector = input()
    if sector == 'A':
        fens_in_a += 1
    elif sector == 'B':
        fens_in_b += 1
    elif sector == 'V':
        fens_in_v += 1
    elif sector == 'G':
        fens_in_g += 1
fens_in_a_percentage = ('%.2f' % (fens_in_a / fens * 100))
fens_in_b_percentage = ('%.2f' % (fens_in_b / fens * 100))
fens_in_v_percentage = ('%.2f' % (fens_in_v / fens * 100))
fens_in_g_percentage = ('%.2f' % (fens_in_g / fens * 100))
fens_percentage = ('%.2f' % (fens / capacity * 100))
print(f'{fens_in_a_percentage}%')
print(f'{fens_in_b_percentage}%')
print(f'{fens_in_v_percentage}%')
print(f'{fens_in_g_percentage}%')
print(f'{fens_percentage}%')