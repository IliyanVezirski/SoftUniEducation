import re

pattern = r'(?P<sep>[@][#]+)(?P<word>[A-Z][A-Za-z0-9]{4,}[A-Z])([@][#]+)'

count_of_barcodes = int(input())

for _ in range(count_of_barcodes):
    barcode = input()
    barcode = re.findall(pattern, barcode)
    if not barcode:
        print(f"Invalid barcode")
        continue
    barcode = barcode[0][1]
    digits = ''
    for digit in barcode:
        if digit.isdigit():
            digits += digit
    if digits != "":
        print(f"Product group: {digits}")
    else:
        print(f"Product group: 00")
