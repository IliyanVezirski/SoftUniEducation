register = {}

register_number = int(input())

for i in range(register_number):
    command = input().split()
    name = command[1]
    if command[0] == "register":
        number_of_car = command[2]
        if name not in register:
            register[name] = number_of_car
            print(f"{name} registered {number_of_car} successfully")
        else:
            print(f"ERROR: already registered with plate number {number_of_car}")
    elif command[0] == "unregister":
        if name not in register:
            print(f"ERROR: user {name} not found")
        else:
            register.pop(name)
            print(f"{name} unregistered successfully")
for k, v in register.items():
    print(f"{k} => {v}")