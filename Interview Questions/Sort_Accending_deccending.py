#Sort list with out sort minimum (or) maximum values
s = [-5, -23, 5, 0, -100 , 100, 23, -6, 23, 67]
a = []
for i in range(len(s)):
    b = min(s)
    a.append(b)
    s.remove(b)
print a

#Sort list with out sort minimum (or) maximum values
x = [-5, -23, 5, 0, -100 , 100, 23, -6, 23, 67]
d = []
for j in range(len(x)):
    c = max(x)
    d.append(c)
    x.remove(c)
print d