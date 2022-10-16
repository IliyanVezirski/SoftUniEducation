notes = [0] * 10
command = input()
while command != 'End':
    index, to_do = command.split('-')
    index = int(index) - 1
    notes[index] = to_do
    command = input()
notes = [i for i in notes if i != 0]
print(notes)