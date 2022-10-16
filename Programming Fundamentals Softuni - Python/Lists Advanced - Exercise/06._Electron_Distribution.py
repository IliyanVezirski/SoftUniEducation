electrons_limit = int(input())
electrons = []
layer = 1
while electrons_limit > 0:
    limit = 2 * pow(layer, 2)

    if electrons_limit >= limit:
        electrons.append(limit)
    else:
        electrons.append(electrons_limit)
    electrons_limit -= limit
    layer += 1
print(f'{electrons}')