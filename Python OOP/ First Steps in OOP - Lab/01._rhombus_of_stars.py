number = int(input())


def print_current_side(i):
    spaces = number - i
    stars = number - spaces
    print(' ' * spaces + "* " * stars)


def upper_side(n):
    for i in range(1, n + 1):
        print_current_side(i)


def down_side(n):
    for i in range(n-1, 0, -1):
        print_current_side(i)


upper_side(number)
down_side(number)
