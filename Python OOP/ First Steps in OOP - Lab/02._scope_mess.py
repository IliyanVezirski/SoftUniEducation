x = "global"


def outer(x):
    x = "local"

    def inner(x):
        x = "nonlocal"
        print("inner:", x)
        return x

    def change_global(x):
        x = "global: changed!"
        return x

    print("outer:", x)
    x = inner(x)
    print("outer:", x)
    x = change_global(x)
    return x


print(x)
x = outer(x)
print(x)
