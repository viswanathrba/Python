name = "anjan"

def add(a, b):
    global c, d
    c = "kumar"
    d = a
    return a+b, name
print(add(4, 5))


print(c)
print(d)