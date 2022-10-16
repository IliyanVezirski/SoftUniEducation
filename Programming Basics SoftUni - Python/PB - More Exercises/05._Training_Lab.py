waist = float(input())
height = float(input())
working_per_waist = waist // 1.2
working_per_height = (height - 1) // 0.7
working_places = working_per_waist * working_per_height - 3
print (int(working_places))