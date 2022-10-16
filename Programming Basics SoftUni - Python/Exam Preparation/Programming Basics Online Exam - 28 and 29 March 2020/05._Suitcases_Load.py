capacity = float(input())
count_package = 0
all_packages = True
capacity_in_cm = int(capacity * 100)
while True:
    package_volume = input()
    if package_volume == 'End':
        break
    package_volume = float(package_volume)
    package_volume = int(package_volume * 100)
    if package_volume >= capacity_in_cm:
        all_packages = False
        break
    count_package += 1
    if count_package % 3 == 0:
        package_volume *= 1.10
    capacity_in_cm -= package_volume
if all_packages:
    print(f'Congratulations! All suitcases are loaded!')
else:
    print(f'No more space!')
print(f'Statistic: {count_package} suitcases loaded.')