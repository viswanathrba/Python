#How to get maximum integer from list use of function (or) normal
a = [1, 2, 4, 8, 9, -1, 0, -999, 666, -55, 666]
print max(a)
print min(a)

Maximum = a[0]
for i in a:
    if i > Maximum:
        Maximum = i
print Maximum

Minimum = a[0]
for j in a:
    if j < Minimum:
        Minimum = j
print Minimum