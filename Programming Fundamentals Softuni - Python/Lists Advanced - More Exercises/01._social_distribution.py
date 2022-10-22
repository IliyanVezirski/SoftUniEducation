import math
population = [int(i) for i in input().split(', ')]
min_wealth = int(input())
difference = 0
is_ok = True
for i in range(len(population)):
    if population[i] < min_wealth:
        difference = min_wealth - population[i]
        max_population = max(population)
        max_population_index = population.index(max_population)
        population[max_population_index] -= difference
        if population[max_population_index] < min_wealth:
            print(f"No equal distribution possible")
            is_ok = False
            break
        population[i] = min_wealth
        difference = 0
if is_ok:
    print(population)
