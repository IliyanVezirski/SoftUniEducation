def even_odd_filter(**kwargs):
    for key, items in kwargs.items():
        if key == 'odd':
            kwargs[key] = kwargs['odd'] = list(filter(lambda x: x if x % 2 == 1 else None, kwargs.get('odd')))
        elif key == 'even':
            kwargs[key] = list(filter(lambda x: x if x % 2 == 0 else None, kwargs.get('even')))
    kwargs = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
    return kwargs

