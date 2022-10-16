height_house = float(input())
lenght_house = float(input())
triangal_height = float(input())
side_area = lenght_house * height_house
window_area = 1.5 * 1.5
side_areas = (side_area * 2) - (window_area * 2)
front_and_back_areas = (height_house * height_house) * 2 - 1.2 * 2
side_and_front_area = side_areas + front_and_back_areas
green_paint = side_and_front_area / 3.4
roof_sides = 2 * (height_house * lenght_house)
triangal_area = 2 * (height_house * triangal_height / 2)
roof_area = roof_sides + triangal_area
red_paint = roof_area / 4.3
print("%.2f" % green_paint)
print("%.2f" % red_paint)