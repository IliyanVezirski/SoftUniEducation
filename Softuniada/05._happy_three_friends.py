number_of_checkout = int(input())
counter_of_found = 0
elements_to_remove = []
for _ in range(number_of_checkout):
    current_checkout = [int(i) for i in input().split()]
    if sum(current_checkout) / 3 != sum(current_checkout) // 3:
        print("No")
        continue

    else:
        counter = 0
        for el in current_checkout:
            target = sum(current_checkout) // 3 - el
            elements_to_remove.append(el)
            for check in current_checkout:
                if current_checkout.index(el) != current_checkout.index(check):
                    current_check = el + check
                    elements_to_remove.append(check)

                    if current_check == target:
                        for number in elements_to_remove:
                            current_checkout.remove(number)
                        elements_to_remove = []
                        counter += 1

                        break
