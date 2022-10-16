country = input()
device = input()
points = 0
if country == 'Russia':
    if device == 'ribbon':
        points = 9.1 + 9.4
    elif device == 'hoop':
        points = 9.3 + 9.8
    elif device == 'rope':
        points = 9.6 + 9
elif country == 'Bulgaria':
    if device == 'ribbon':
        points = 9.6 + 9.4
    elif device == 'hoop':
        points = 9.55 + 9.75
    elif device == 'rope':
        points = 9.5 + 9.4
elif country == 'Italy':
    if device == 'ribbon':
        points = 9.2 + 9.5
    elif device == 'hoop':
        points = 9.45 + 9.35
    elif device == 'rope':
        points = 9.7 + 9.15
percentage = ('%.2f' % ((20 - points) / 20 * 100))
print(f'The team of {country} get {points:.3f} on {device}.')
print(f'{percentage}%')
