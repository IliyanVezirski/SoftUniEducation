version = [int(i) for i in input().split('.')]
for number in range(len(version) -1 , 0-1, -1):
    version[number] += 1
    if version[number] > 9:
        version[number] = 0
        continue
    break

print(* version, sep='.')