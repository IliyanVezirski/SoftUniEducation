def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for name, date in sorted_dict:
        sorted_date = list(sorted(date, reverse=True))
        result += name + '\n' + '\n'.join(list(map(str, sorted_date))) + '\n'
    return result
