#full pyramid
for i in range(20):
    print " "*(20 - i - 1) + "*"*(2 * i +1)
    
for j in range(30):
    print " "*(30 - j - 1) + "*"*(2 * j + 1)

#left pyramid  
for k in range(20):
    print " "*(20 - k - 1) + "*"*(1 * k + 1)
    
for l in range(30):
    print " "*(30 - l - 1) + "*"*(1 * l + 1)
    
#right pyramid

for m in range(20):
    print "*"*(1 * m + 1)
    
for n in range(30):
    print "*"*(1 * n + 1)