a = 'bangalore'

# for i in a:
    # print(i)


c = iter(a)

first_iter = next(c)
second_iter = next(c)
third_iter = next(c)

print(first_iter)
print(second_iter)
print(third_iter)