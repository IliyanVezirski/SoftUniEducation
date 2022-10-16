searched_book = input()
book = input()
counter = 0
while book != 'No More Books':
    if book == searched_book:
        print(f'You checked {counter} books and found it.')
        break
    book = input()
    counter +=1
if book == 'No More Books':
    print(f'The book you search is not here!')
    print(f'You checked {counter} books.')