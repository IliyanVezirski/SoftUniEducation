start_letter = input()
end_letter = input()
miss_letter = input()
count = 0
for i in range(ord(start_letter),ord(end_letter) + 1):
    if i != ord(miss_letter):
        for n in range(ord(start_letter), ord(end_letter)+ 1):
            if n != ord(miss_letter):
                for v in range(ord(start_letter), ord(end_letter)+1):
                    if v != ord(miss_letter):
                        count += 1
                        print(f'{chr(i)}{chr(n)}{chr(v)}', end=" ")
print(count)

