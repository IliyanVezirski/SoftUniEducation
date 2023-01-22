def sorting_cheeses(**kwargs):
    result = ''
    for name, date in kwargs.items():
        result += name + '\n'
        for n in date:
            result += str(n) + '\n'
    return result