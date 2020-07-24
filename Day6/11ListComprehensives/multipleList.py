a = [['bangalore', 'chennai', 'pune'], ['hyd', 'delhi', 'rajasthan']]

b = []
for i in a:
    for j in i:
        b.append(j)


print(b)

print([j for i in a for j in i])