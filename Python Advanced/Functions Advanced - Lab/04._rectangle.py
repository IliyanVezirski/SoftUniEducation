def area(length: int, width: int):
    return length * width


def perimeter(length: int, width: int):
    return length + length + width + width


def rectangle(length: int, width: int):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"
    else:
        return f'Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}'


print(rectangle(2, 10))


print(rectangle('2', 10))