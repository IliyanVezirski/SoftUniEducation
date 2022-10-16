train = int(input())
wagon_len = [0] * train
command = input()
while command != "End":
    data = command.split()
    if data[0] == "add":
        wagon_len[-1] += int(data[1])
    elif data[0] == "insert":
        wagon_len[int(data[1])] += int(int(data[2]))
    else:
        wagon_len[int(data[1])] -= int(int(data[2]))
    command = input()
print(wagon_len)