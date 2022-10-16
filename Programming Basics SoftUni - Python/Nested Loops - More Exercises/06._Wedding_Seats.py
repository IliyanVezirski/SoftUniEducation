last_sector = input()
row_numbers_for_first_sector = int(input())
places_for_odd_row = int(input())
place = 'a'
place_count = 0
for sectors in range(ord('A'), ord(last_sector)+ 1):
    for row in range(1, row_numbers_for_first_sector + 1):
        if row % 2 == 1:
            for places in range(1, places_for_odd_row + 1):
                place = ord(place)
                print(f'{chr(sectors)}{row}{chr(place)}')
                place += 1
                place = chr(place)
                place_count += 1
        else:
            for places in range(1,places_for_odd_row + 3):
                place = ord(place)
                print(f'{chr(sectors)}{row}{chr(place)}')
                place += 1
                place = chr(place)
                place_count +=1
        place = 'a'
    row_numbers_for_first_sector += 1
print(place_count)