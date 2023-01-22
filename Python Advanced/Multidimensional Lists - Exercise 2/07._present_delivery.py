number_of_presents = int(input())
size_of_neighborhood = int(input())
neighborhood = []
santa_position = ()
naughty_kids_places = []
nice_kids_places = []
cookies_places = []
for r in range(size_of_neighborhood):
    neighborhood.append(input().split())
    for c in range(size_of_neighborhood):
        if neighborhood[r][c] == "S":
            santa_position = (r, c)
        elif neighborhood[r][c] == 'X':
            naughty_kids_places.append((r, c))
        elif neighborhood[r][c] == "V":
            nice_kids_places.append((r, c))
        elif neighborhood[r][c] == "C":
            cookies_places.append((r, c))
print(nice_kids_places)
print(cookies_places)
print(naughty_kids_places)
print(santa_position)
