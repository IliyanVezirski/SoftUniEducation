import re

barcodes = int(input())
pattern = r'(?P<sep>[@][#]+)(?P<barcode>[A-Z][A-Za-z\d]{4,}[A-Z])(?P<second_sep>[@][#]+)'
digits = ''
letters = ''
for _ in range(barcodes):
    current_barcode = input()
    matched_barcodes = re.findall(pattern, current_barcode)
    if matched_barcodes:
        for match in matched_barcodes:
            for letter in match[1]:
                if letter.isdigit():
                    digits += letter
            if digits:
                print(f'Product group: {digits}')
            else:
                print(f'Product group: 00')
            digits = ''
    else:
        print("Invalid barcode")
