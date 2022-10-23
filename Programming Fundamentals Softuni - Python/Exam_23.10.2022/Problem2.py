route = input().split("||")

fuel = int(input())
ammunition = int(input())


for way in route:
    way = way.split()
    command = way[0]
    if command == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        break
    distance = int(way[1])
    if command == "Travel":
        if distance <= fuel:
            fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print(f"Mission failed.")
            break
    elif command == "Enemy":
        if distance <= ammunition:
            ammunition -= distance
            print(f"An enemy with {distance} armour is defeated.")
        else:
            distance *= 2
            if distance <= fuel:
                fuel -= distance
                print(f"An enemy with {distance // 2} armour is outmaneuvered.")
            else:
                print(f"Mission failed.")
                break
    elif command == "Repair":
        fuel += distance
        ammunition += distance * 2
        print(f"Ammunitions added: {distance * 2}.")
        print(f"Fuel added: {distance}.")