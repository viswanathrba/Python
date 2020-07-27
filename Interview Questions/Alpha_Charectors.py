#How to convert Swapcase alternate charectors
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = ''
for i,j in enumerate(a):
    print i,j
    if i%2 == 0:
        b += j.upper()
    else:
        b += j.lower()
print b

print 0%2 == 0
print 1%2 == 0
print 2%2 == 0
print 3%2 == 0
print 4%2 == 0
print 5%2 == 0
print 6%2 == 0
print 7%2 == 0
print 8%2 == 0
print 9%2 == 0
print 10%2 == 0
print 11%2 == 0
print 12%2 == 0
print 13%2 == 0

c = 2
d = 3
c += d
print c