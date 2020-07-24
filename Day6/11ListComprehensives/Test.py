a = ['bangalore', 'chennai', 'pune']

b = []
for i in a:
    #if 
    b.append(i)

print(b)

c = [i for i in a if i.endswith('e')]
print(c)


