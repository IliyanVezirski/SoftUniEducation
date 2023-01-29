def even_odd(*args):
    args = list(args)
    command = args.pop()
    numbers = [int(i) for i in args]
    if command == "even":
        return [i for i in numbers if i % 2 == 0]
    else:
        return [i for i in numbers if i % 2 == 1]


