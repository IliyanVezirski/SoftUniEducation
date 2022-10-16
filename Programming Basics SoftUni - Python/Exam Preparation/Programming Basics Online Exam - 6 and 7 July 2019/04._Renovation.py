height = int(input())
width = int(input())
percentage_without_paint = int(input())
paint = input()
area = height * width * 4
clean_area = area - (area * percentage_without_paint / 100)
painted_area = 0
left_area = clean_area
total_paints = 0
is_painted = False
while paint != 'Tired!':
    paint = int(paint)
    total_paints += paint
    if left_area < paint:
        is_painted = True
        diff = abs(clean_area - total_paints)
        print(f"All walls are painted and you have {int(diff)} l paint left!")
        break
    elif left_area == paint:
        is_painted = True
        print(f'All walls are painted! Great job, Pesho!')
        break
    left_area -= paint
    paint = input()
if not is_painted:
    print(f'{int(left_area)} quadratic m left.')