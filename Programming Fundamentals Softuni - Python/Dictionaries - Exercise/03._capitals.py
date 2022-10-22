country = input().split(', ')
capitals = input().split(', ')
countries_capitals = dict(zip(country,capitals))
for k, v in countries_capitals.items():
    print(f"{k} -> {v}")