x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
status = ''
if x1 < x < x2 and y1 < y < y2:
    status = 'Inside / Outside'
elif x1 == x < x2 and y1 < y < y2:
    status = 'Border'
elif x1 <= x == x2 and y1 <= y <= y2:
    status = 'Border'
elif x1 <= x <= x2 and y1 == y <= y2:
    status = 'Border'
elif x1 <= x <= x2 and y1 <= y == y2:
    status = 'Border'
else:
    status = 'Inside / Outside'
print(status)
