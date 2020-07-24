def my_gen(n, m):
    yield n
    yield m
    print(m)

    n += 1
    yield n

    n += 1
    yield n
    
    n += 10
    yield n

b = iter(my_gen(1, 20))
print(next(b))
print(next(b))
print(next(b))
# Using for loop
# for item in my_gen(1, 20):
    # print(item)
