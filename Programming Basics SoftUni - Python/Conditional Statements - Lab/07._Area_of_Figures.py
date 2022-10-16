import math
type_figure = str(input())
if type_figure == 'square':
    a = float(input())
    area_square = a * a
    print("%.3f" % area_square)
elif type_figure == 'rectangle':
    a = float(input())
    b = float(input())
    area_rectangle = a * b
    print('%.3f' % area_rectangle)
elif type_figure == 'circle':
    h = float(input())
    area_circle = math.pi * (h * h)
    print('%.3f' % area_circle)
elif type_figure == 'triangle':
    a = float(input())
    h = float(input())
    area_triangle = (a / 2) * h
    print('%.3f' % area_triangle)